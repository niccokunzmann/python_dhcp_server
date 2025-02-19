---
type: "home"
---

Dieser DHCP Server ist in Python geschrieben und benötigt keine anderen
Abhängigkeiten als Python 3.

![](/img/windows-tk.png)

## Kompatibilität

It was testet under Ubuntu 14 and later with Python and Windows 7 and later. It
does not use any operating system specific Python functions, so it should work
when Python 3 works.

## Fähigkeiten

This DHCP server program will assign IP addresses ten seconds later than
requested. So, it can be used in networks that already have a DHCP server
running.

Dieser Einfache DHCP Server

- zeigt andere Geräte im Netzwerk an
- lists IP address, MAC address and host name
- zeigt Veränderungen und Updates an
- vergibt IP-Adressen 10 Sekunden später als herkömmliche DHCP-Server
- remembers addresses in the `hosts.csv` file
- kann so eingerichtet werden, dass alle DHCP-Optionen nutzbar sind

[Mithilfe ist erwünscht!][1]

## Ähnliche Software

Dieses Programm wurde erstellt, um Raspberry-Pis im Netzwerk zu finden.

- [Adafruit-Pi-Finder](https://github.com/adafruit/Adafruit-Pi-Finder)
- [Angry IP](https://angryip.org/)

[1]: /contribute

