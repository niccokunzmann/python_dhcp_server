#!/usr/bin/python3
from .dhcp import *
try:
    from tkinter import *
    from tkinter.messagebox import showerror
except ImportError:
    print("Install tkinter!")
    print("    sudo apt-get install python3-tk")
    input("Press ENTER to exit!")
    exit(1)
import sys
import os

HERE = os.path.dirname(__file__) or "."

THIS_CONFIG = 'simple-dhcp-server-tk.conf'

def main():
    """Create a GUI window and the DHCP server from a possible file."""

    root = Tk()
    root.title('MAC, IP & Computer')
    # use the icon
    # see https://stackoverflow.com/a/75579809
    try:
        root.iconphoto(False, PhotoImage(file=os.path.join(HERE, "icon.png")))
    except AttributeError:
        root.iconbitmap(os.path.join(HERE, "icon.ico"))

    # Horizontal (x) Scroll bar
    xscrollbar = Scrollbar(root, orient=HORIZONTAL)
    xscrollbar.pack(side=BOTTOM, fill=X)

    # Vertical (y) Scroll Bar
    yscrollbar = Scrollbar(root)
    yscrollbar.pack(side=RIGHT, fill=Y)

    # Text Widget
    info_text = Text(root, wrap=NONE, height=12, width=80,
                    xscrollcommand=xscrollbar.set,
                    yscrollcommand=yscrollbar.set)
    info_text.pack(fill=BOTH, expand = True)

    # Configure the scrollbars
    xscrollbar.config(command=info_text.xview)
    yscrollbar.config(command=info_text.yview)

    configuration = DHCPServerConfiguration()
    configuration.debug = print
    #configuration.adjust_if_this_computer_is_a_router()
    config_file = os.path.join(HERE, THIS_CONFIG)
    if not os.path.exists(THIS_CONFIG):
        with open(THIS_CONFIG, "w") as f:
            with open(config_file) as s:
                f.write(s.read())
        print("Created config file:", config_file)
    configuration.load(THIS_CONFIG)
    try:
        server = DHCPServer(configuration)
    except PermissionError:
        showerror("No access to DHCP port", "The network port cannot be accessed. Run this program with sudo.")
        exit(1)
    server.run_in_thread()

    # create pretty tags
    time_tags = []
    for i, yellow in enumerate("0123456789abcdef"):
        tag = 'yellow_{}'.format(i)
        bg = '#ffff{}{}'.format(yellow, yellow)
        info_text.tag_config(tag, background = bg)
        time_tags.append(tag)

    old_tag = 'old'
    info_text.tag_config(old_tag)

    last_time_sorted_hosts = None
    def update_text():
        nonlocal last_time_sorted_hosts
        root.after(100, update_text)
        hosts = server.get_all_hosts()
        current_hosts = server.get_current_hosts()
        time_sorted_hosts = list(reversed(sorted(hosts, key = lambda host: host.last_used)))
        if last_time_sorted_hosts != time_sorted_hosts:
            text = 'MAC'.center(17) + '  ' + 'IP'.center(15) + '  ' + '  HOST' + '\n'
            headerlines = 1
            for host in hosts:
                text += '{}  {}  {}\n'.format(host.mac, host.ip.ljust(15, ' '), host.hostname)
            last_text = text
            info_text.delete('0.0', END)
            info_text.insert(END, text)
            # prettify the text
            for time_i, host in enumerate(time_sorted_hosts):
                text_line = hosts.index(host) + 1 + headerlines
                start = "{}.0".format(text_line)
                stop  = "{}.0".format(text_line + 1)
                if host in current_hosts:
                    tag_index = int(time_i / len(current_hosts) * len(time_tags))
                    info_text.tag_add(time_tags[tag_index], start, stop)
                else:
                    info_text.tag_add(old_tag, start, stop)
            info_text.tag_raise("sel")
        last_time_sorted_hosts = time_sorted_hosts

    update_text()

    root.mainloop()

    server.close()

if __name__ == '__main__':
    main()