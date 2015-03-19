#!/usr/bin/python3
from dhcp import *
from tkinter import *

root = Tk()
root.title('MAC, IP & Computer')
info_text = Text(root)
info_text.pack(fill = BOTH, expand = True)

configuration = DHCPServerConfiguration()
configuration.debug = print
configuration.adjust_if_this_computer_is_a_router()
configuration.load('dhcpgui.conf')
server = DHCPServer(configuration)
server.run_in_thread()

last_text = None
def update_text():
    global last_text
    root.after(100, update_text)
    entries = server.ips.all()
    text = '\n'.join(line for line in ('\t'.join(entry) for entry in entries) if line)
    if text != last_text:
        last_text = text
        info_text.delete('0.0', END)
        info_text.insert(END, text)

update_text()

root.mainloop()
