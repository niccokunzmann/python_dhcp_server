---
title: "Other Sources"
---

Du kannst die Quelldateien direkt installieren. Es gibt mehrere Wege, das zu
machen.

## PyPI

Wenn Du [Python] installiert hast, kannst Du `pip` benutzen, um die Pakete von
[PyPI] zu installieren.

### QT Oberfläche

```sh
pip install simple-dhcp-server[qt]
```

### Tk Frontend

Wenn Du QT nicht installieren kannst, dann kannst du die Tk-Version benutzen:

```sh
pip install simple-dhcp-server
```

### GitHub

Wenn Du [Python] installiert hast, kannst Du `pip` ausführen, um das Paket von
[GitHub] direkt zu installieren.

```sh
pip install git+https://github.com/niccokunzmann/simple_dhcp_server.git
```

## Pipx

[pipx] macht die Installation noch einfacher, weil es die App von anderen
isoliert.

1. Installiere [pipx]
2. Install and start the Simple DHCP Server:

    ```sh
    sudo pipx run --spec simple-dhcp-server[qt] python-dhcp-server-qt  
    ```

## Development Setup

You can also [setup the Simple DHCP Server for development][4].

## Benutzung

Nach der Installation, schau die [Nutzung][3] an.

[Python]: https://www.python.org/
[PyPI]: https://pypi.org/project/simple-dhcp-server/
[GitHub]: https://github.com/niccokunzmann/simple_dhcp_server/
[3]: /usage/cmd.md
[pipx]: https://pipx.pypa.io/stable/installation/
[4]: ../develop
