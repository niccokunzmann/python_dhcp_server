---
title: "Mac OS"
---

![](/img/macos-install.png)

To install the app, download the release `Simple.DHCP.Server.X.Y.Z.dmg` from the [latest release][3].
Open it and move the app into the Applications.

## Configuration and Cache

![](/img/macos-files.png)

Your configuration files are stored in `~/Library/Caches/eu.quelltext.dhcp/`.

Read more about [configuration and usage][2].

## Python Package Installation

You should first setup Python 3 using [brew].

```sh
brew install python-tk
```

Then, you can install the [Python package][1].

[1]: ./source.md
[2]: ../usage
[3]: https://github.com/niccokunzmann/simple_dhcp_server/releases
[brew]: https://brew.sh
