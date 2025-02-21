---
title: "Mac OS"
---

![](/img/macos-install.png)

Um die App zu installieren, lade die Datei `Simple.DHCP.Server.X.Y.Z.dmg` der
[neusten Version][3] herunter. Öffne die Datei und schiebe die App in die
Applikationen. Nachdem die App so installiert wurde kannst Du sie ausführen.

## Einstellungen und Cache

![](/img/macos-files.png)

Die Konfigurationsdateien befinden sich in
`~/Library/Caches/eu.quelltext.dhcp/`.

Lies mehr über [Einstellungen und Benutzung][2].

## Installation des Python-Paketes

Eine andere Möglichkeit ist, das Python-Paket zu installieren. Du solltest
zuerst Python 3 mit [brew] installieren.

```sh
brew install python-tk
```

Danach kannst Du das [Python-Paket][1] installieren.

[1]: ./source.md
[2]: ../usage
[3]: https://github.com/niccokunzmann/simple_dhcp_server/releases
[brew]: https://brew.sh
