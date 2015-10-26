#!/usr/bin/python3
from dhcp import *
from tkinter import *

root = Tk()
root.title('MAC, IP & Computer')
info_text = Text(root, height = 12, width = 50)
info_text.pack(fill = BOTH, expand = True)

configuration = DHCPServerConfiguration()
configuration.debug = print
#configuration.adjust_if_this_computer_is_a_router()
configuration.load('dhcpgui.conf')
server = DHCPServer(configuration)
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
    global last_time_sorted_hosts
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
