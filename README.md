# Simple DHCP Server

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

Have a look at:

- The [official website][web] for installation and configuration instructions.
- The [source code][source].
- The [project translation on Weblate][weblate].

[web]: https://dhcp.quelltext.eu
[source]: https://github.com/niccokunzmann/simple_dhcp_server/
[weblate]: https://hosted.weblate.org/engage/simple-dhcp-server/
