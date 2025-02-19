---
type: "home"
---

Dieser DHCP Server ist in Python geschrieben und benötigt keine anderen
Abhängigkeiten als Python 3.

![](/img/windows-tk.png)

## Kompatibilität

Diese Software wurde unter Ubuntu 14 mit Python und Windows 7 getestet. Sie
braucht keine speziellen Funktionen und sollte funktionieren, wenn Python 3
installiert wurde.

## Fähigkeiten

Dieser DHCP-Server wird IP-Adressen zehn Sekunden später zuweisen. Damit kann er
in einem Netzwerk laufen, in dem schon andere DHCP server sind.

Dieser Einfache DHCP Server

- zeigt andere Geräte im Netzwerk an
- listet IP-Adresse, MAC, und Gerätename
- zeigt Veränderungen und Updates an
- vergibt IP-Adressen 10 Sekunden später als herkömmliche DHCP-Server
- merkt such Adressen in der `hosts.csv`-Datei.
- kann so eingerichtet werden, dass alle DHCP-Optionen nutzbar sind

[Mithilfe ist erwünscht!][1]

## Ähnliche Software

Dieses Programm wurde erstellt, um Raspberry-Pis im Netzwerk zu finden.

- [Adafruit-Pi-Finder](https://github.com/adafruit/Adafruit-Pi-Finder) - finde
  deinen Raspberry Pi im Netzwerk
- [Angry IP](https://angryip.org/) (Windows)

[1]: /contribute

