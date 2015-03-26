#!/usr/bin/python3
from dhcp import *
from tkinter import *

root = Tk()
root.title('MAC, IP & Computer')
info_text = Text(root, height = 12, width = 45)
info_text.pack(fill = BOTH, expand = True)

configuration = DHCPServerConfiguration()
configuration.debug = print
#configuration.adjust_if_this_computer_is_a_router()
configuration.load('dhcpgui.conf')
server = DHCPServer(configuration)
server.run_in_thread()

last_time_sorted_entries = None
def update_text():
    global last_time_sorted_entries
    root.after(100, update_text)
    entries = server.get_current_entries()
    time_sorted_entries = list(reversed(sorted(entries, key = lambda entry: entry.last_received)))
    if last_time_sorted_entries != time_sorted_entries:
        text = 'MAC'.center(18) + '\t' + 'IP'.center(13) + '\t' + '  HOST' + '\n'
        headerlines = 1
        for entry in entries:
            text += '{}\t{}\t{}\n'.format(entry.mac, entry.ip, entry.hostname)
        last_text = text
        info_text.delete('0.0', END)
        info_text.insert(END, text)
        # prettify the text
        tags = []
        for time_i, entry in enumerate(time_sorted_entries):
            text_line = entries.index(entry) + 1 + headerlines
            start = "{}.0".format(text_line)
            stop  = "{}.0".format(text_line + 1)
            tag = 'time{}'.format(time_i)
            info_text.tag_add(tag, start, stop)
            tags.append(tag)
        for tag_i, tag in enumerate(tags):
            rank = 100 + int(tag_i * 155 / (len(tags)))
            hexrank = hex((rank >> 4) & 15)[-1] + hex(rank & 15)[-1]
            bg = '#ffff{}'.format(hexrank, hexrank)
            info_text.tag_config(tag, background = bg)
        last_time_sorted_entries = time_sorted_entries
        info_text.tag_raise("sel")
        
update_text()

root.mainloop()

server.close()
