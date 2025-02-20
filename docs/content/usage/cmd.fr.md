---
title: "Command Line Usage"
---

The Simple DHCP Server provides several options for executing it, depending on
the install method.

* Get **Help**:

    ```sh
    simple-dhcp-server
    ```

* Tk **User Interface**:

    ```sh
    simple-dhcp-server-tk
    ```

* QT **User Interface**:

    ```sh
    simple-dhcp-server-qt
    ```

* **Command Line** start a server:

    ```sh
    simple-dhcp-server-serve
    ```

* **Command Line** just listening to what is going on:

    ```sh
    simple-dhcp-server-listen
    ```

## Linux (sudo)

On Linux, you need to run the commands with `sudo` to have access to the
network. That is because the DHCP port 67 is below 1024.
