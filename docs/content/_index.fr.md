---
type: "home"
---

This is a purely Python DHCP server that does not require any additional
libraries or installs other that Python 3.

![](/img/windows-tk.png)

- [Install][2]
- [Contribute][1]
- [View the Source][3]

## Compatibility

It was testet under Ubuntu 14 and later with Python and Windows 7 and later. It
does not use any operating system specific Python functions, so it should work
when Python 3 works.

## Features

This DHCP server program will assign IP addresses ten seconds later than
requested. So, it can be used in networks that already have a DHCP server
running.

This Simple DHCP server

- shows clients in the network
- lists IP address, MAC address and host name
- highlights recently refreshed/added clients
- assigns IP addresses 10 seconds later than usual DHCP servers
- remembers addresses in the `hosts.csv` file
- can be configured to serve all DHCP options using Python/Yaml

[Contributions welcome!][1]

## Related Work

This program was created to find Raspberry Pis in the network.

- [Adafruit-Pi-Finder](https://github.com/adafruit/Adafruit-Pi-Finder)
- [Angry IP](https://angryip.org/)

[1]: contribute
[2]: install
[3]: https://github.com/niccokunzmann/simple_dhcp_server/
