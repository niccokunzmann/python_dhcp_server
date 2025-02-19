---
type: "home"
---

Dieser DHCP Server ist in Python geschrieben und benötigt keine anderen
Abhängigkeiten als Python 3.

![](/img/windows-tk.png)

- [Installieren][2]
- [Beitragen][1]

## Kompatibilität

Die Software wurde unter Ubuntu 14 und späteren Versionen sowie Windows 7 und
späteren Version getestet. Sie benutzt keine spezifischen Funktionen und sollte
funktionieren, wenn Python 3 geht.

## Fähigkeiten

Der DHCP-Server vergibt IP-Adressen zehn Sekunden nach der Anfrage. Damit kann
er in Netzwerken laufen, die schon DHCP-Server laufen haben.

Dieser Einfache DHCP Server

- zeigt andere Geräte im Netzwerk an
- listet IP-Adresse, MAC-Adresse und Gerätename
- zeigt Veränderungen und Updates an
- vergibt IP-Adressen 10 Sekunden später als herkömmliche DHCP-Server
- merkt sich die Adressen in der `hosts.csv` Datei
- kann so eingerichtet werden, dass alle DHCP-Optionen nutzbar sind

[Mithilfe ist erwünscht!][1]

## Ähnliche Software

Dieses Programm wurde erstellt, um Raspberry-Pis im Netzwerk zu finden.

- [Adafruit-Pi-Finder](https://github.com/adafruit/Adafruit-Pi-Finder)
- [Angry IP](https://angryip.org/)

[1]: contribute
[2]: install
