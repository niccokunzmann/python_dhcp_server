# Simple DHCP Server

[Download][releases]

This is a purely Python DHCP server that does not require any additional libraries or installs other that Python 3.

It was testet under Ubuntu 14 with Python and Windows 7. It does not use any operating system specific Python functions, so it should work when Python 3 works.

![images/dhcpgui.png](images/dhcpgui.png)  
dhcpgui lists MAC address, IP address and host name.

This DHCP server program will assign IP addresses ten seconds after it received packets from clients. So it can be used in networks that already have a dhcp server running.

This Python DHCP server

- shows clients in the network
- lists IP address, Mac address and host name
- highlights recently refreshed/added clients
- assigns IP addresses 10 seconds later than usual DHCP servers
- remembers addresses in the `hosts.csv` file.
- can be configured to serve all DHCP options using Python

Contributions welcome!

## Windows

You can install this software by downloading the [release][releases] named `python_dhcp_server_standalone_X.Y.zip` file.
Unpack the zip file, you will find an executable `.exe` file inside.

## Linux

Under Linux you can download the [source code][zip] and install Python 3 and Tkinter for Python 3:

```sh
sudo apt-get install python3 python3-tk
```

There are different ways to start:

1. You can use the `python_dhcp_server.desktop` and double-click it.
    If it does not open, please [report it][issues] and try the next one.
2. You can run the following command provided you are in the `server`
    directory.

    ```sh
    sudo python3 ./dhcpgui.pyw
    ```

## Related Work

This program was created to find Raspberry Pis in the network.

- [Adafruit-Pi-Finder](https://github.com/adafruit/Adafruit-Pi-Finder) - finde deinen Raspberry Pi im Netzwerk
- [Angry IP](https://angryip.org/) (Windows)

## Changelog

These are the recent changes.
If a version is not released, yet, it can still show up.
You can view the [realeases on GitHub][releases].

### 1.0.0

- Add QT Release
- Build windows exe automatically
- Publish to PyPI
- Create GitHub Release

### 0.9

- Add icon to exe file and application
- Add flatpak build information

### 0.8

- Make text field expandable
- Show error message if DHCP port cannot be accessed

### 0.7

- Prevent duplicate assignment of IP addresses
- Add sliders to the GUI

### 0.6

- Use a queue
- Run in Linux
- Add install description
- Add ability to bind to a fixed IP address

### 0.5

- Fix issue with delay worker

### 0.4

- Fix issue with delay worker
- Add license

### 0.3

- Also show old values
- Random IP assignment when address space is full

### 0.2

- Add .exe file
- Add width and height

### 0.1

- Mark new entries as yellow
- Initial release

New Releases
------------

When the source code is changed, create a new release.

1. Log the changes: Edit the Changelog Section in
    - `README.md`
    - `python_dhcp_server/flatpak/io.github.niccokunzmann.python_dhcp_server.xml`
    ```
    git log # find changes
    git add README.md
    git commit -m"log changes"
    ```
2. Create a new tag
    ```
    git tag 0.10
    git push origin 0.10
    ```
3. Download the [latest release](https://github.com/niccokunzmann/python_dhcp_server/releases/download/0.9/python_dhcp_server_standalone_0.9.zip).
    ```
    cd ~/Downloads
    wget -c 'https://github.com/niccokunzmann/python_dhcp_server/releases/download/0.9/python_dhcp_server_standalone_0.9.zip'
    ```
4. Unzip it.
    ```
    rm -rf python_dhcp_server_standalone
    unzip python_dhcp_server_standalone_0.9.zip
    ```
5. Replace the `server` directory.
    ```
    cd python_dhcp_server_standalone
    rm -r server
    cp -r ~/python_dhcp_server/server/ .
    rm -r server/__pycache__
    ```
6. Zip the release.
    ```
    cd ..
    zip -9r python_dhcp_server_standalone_0.10.zip python_dhcp_server_standalone
    ```
7. Upload the zip file to the [pushed release][releases].
8. Head over to [the Flathub metadata](https://github.com/niccokunzmann/io.github.niccokunzmann.python_dhcp_server/)
   and create a new release.


[releases]: https://github.com/niccokunzmann/python_dhcp_server/releases
[zip]: https://github.com/niccokunzmann/python_dhcp_server/archive/refs/heads/master.zip
[issues]: https://github.com/niccokunzmann/python_dhcp_server/issues
