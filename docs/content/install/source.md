+++
title = "Source"
type = "chapter"
weight = 3
+++

You can install the source files directly.

## PyPI

If you have installed [Python], you can run `pip` to install the package from [PyPI].

### QT Frontend

```sh
pip install simple-dhcp-server[qt]
```

### TK Frontend

If you cannot install QT, you can use the Tk version:

```sh
pip install simple-dhcp-server
```

### GitHub

If you have installed [Python], you can run `pip` to install the package from [GitHub] directly.

```sh
pip install git+https://github.com/niccokunzmann/simple_dhcp_server.git
```

## Pipx

[pipx] makes installation even nicer because it isolates the app.

1. Install [pipx]
2. Install and start:

    ```sh
    sudo pipx run --spec simple-dhcp-server[qt] python-dhcp-server-qt  
    ```

## Usage

After installation, refer to the [usage][3].

[Python]: https://www.python.org/
[PyPI]: https://pypi.org/project/simple-dhcp-server/
[GitHub]: https://github.com/niccokunzmann/simple_dhcp_server/
[3]: /usage/cmd.md
[pipx]: https://pipx.pypa.io/stable/installation/
