Python DHCP Server
------------------

[Download][releases]

This is a purely Python DHCP server that does not require any additional libraries or installs other that Python 3.

It was testet under Ubuntu 14 with Python and Windows 7. It does not use any operating system specific Python functions, so it should work when Python 3 works.

![images/dhcpgui.png](images/dhcpgui.png)  
dhcpgui lists MAC address, IP address and host name.

This DHCP server program will assign IP addresses ten seconds after it received packets from clients. So it can be used in networks that already have a dhcp server running.

This Python DHCP server
- shows clients in the network
- lists IP address, Mac address and host name
- highlights recently refreshed/added clients
- assigns IP addresses 10 seconds later than usual DHCP servers
- remembers addresses in the `hosts.csv` file.
- can be configured to serve all DHCP options using Python

Contributions welcome!

Windows
-------

You can install this software by downloading the [release][releases] named `python_dhcp_server_standalone_X.Y.zip`.tible
Unpack the zip file, you will find an executable `.exe` file inside.

Linux
-----

Under Linux you can download the [source code][zip] and install Python 3 and Tkinter for Python 3:

```
sudo apt-get install python3 python3-tk
```

There are different ways to start:
1. You can use the `python_dhcp_server.desktop` and double-click it.
    If it does not open, please [report it][issues] and try the next one.
2. You can run the following command provided you are in the `server`
    directory.
    ```
    python3 ./dhcpgui.pyw
    ```

Related Work
------------

- [Adafruit-Pi-Finder](https://github.com/adafruit/Adafruit-Pi-Finder) - finde deinen Raspberry Pi im Netzwerk


[releases]: https://github.com/niccokunzmann/python_dhcp_server/releases
[zip]: https://github.com/niccokunzmann/python_dhcp_server/archive/refs/heads/master.zip
[issues]: https://github.com/niccokunzmann/python_dhcp_server/issues
