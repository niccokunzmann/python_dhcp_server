---
title: "Autres sources"
---

Vous pouvez installer les fichiers sources directement. Il y a beaucoup de
façons de le faire.

## PyPI

Si vous avez installé [Python], vous pouvez exécuter `pip` pour installer le
paquet depuis [PyPI].

### QT Frontend

```sh
pip install simple-dhcp-server[qt]
```

### Tk Frontend

Si vous ne pouvez pas installer QT, vous pouvez utiliser la version Tk :

```sh
pip install simple-dhcp-server
```

### GitHub

Si vous avez installé [Python], vous pouvez exécuter `pip` pour installer le
paquet directement depuis [GitHub].

```sh
pip install git+https://github.com/niccokunzmann/simple_dhcp_server.git
```

## Pipx

[pipx] makes installation even nicer because it isolates the app.

1. Installer [pipx]
2. Install and start the Simple DHCP Server:

    ```sh
    sudo pipx run --spec simple-dhcp-server[qt] python-dhcp-server-qt  
    ```

## Development Setup

You can also [setup the Simple DHCP Server for development][4].

## Utilisation

Après installation, reportez-vous à l'[utilisation][3].

[Python]: https://www.python.org/
[PyPI]: https://pypi.org/project/simple-dhcp-server/
[GitHub]: https://github.com/niccokunzmann/simple_dhcp_server/
[3]: /usage/cmd.md
[pipx]: https://pipx.pypa.io/stable/installation/
[4]: ../develop
