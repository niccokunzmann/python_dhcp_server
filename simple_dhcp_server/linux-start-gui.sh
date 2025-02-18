#!/bin/sh
#
# Shortcut to start the gui with a terminal and ask for the password.
# 

HERE="`dirname \"$0\"`"

if ! python3 -c "import tkinter"; then
    echo "Install tkinter!"
    echo "    sudo apt-get install python3-tk"
    echo "Press ENTER to exit!"
    read REPLY
    exit 1
fi

python3 "$HERE/dhcpgui.pyw" &


