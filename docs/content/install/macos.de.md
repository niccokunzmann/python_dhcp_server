---
title: "Mac OS"
---

![](/img/macos-install.png)

To install the app, download the release `Simple DHCP Server X.Y.Z.dmg` from the
[latest release][3]. Open it and move the app into the Applications.

## Configuration and Cache

![](/img/macos-files.png)

Your configuration files are stored in `~/Library/Caches/eu.quelltext.dhcp/`.

Read more about [configuration and usage][2].

## Python Package Installation

Zuerst musst Du Python 3 mit [brew] aufsetzen.

```sh
brew install python-tk
```

Danach kannst Du das [Python-Paket][1] installieren.

[1]: ./source.md
[2]: ../usage
[3]: https://github.com/niccokunzmann/simple_dhcp_server/releases
[brew]: https://brew.sh
