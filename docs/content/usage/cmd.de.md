---
title: "Kommandozeile"
---

Der einfache DHCP Server bietet mehrere Optionen für die Ausführung, je nach
Installationsmethode.

* Bekomm **Hilfe**:

    ```sh
    simple-dhcp-server
    ```

* Tk **Benutzeroberfläche**:

    ```sh
    simple-dhcp-server-tk
    ```

* QT **Benutzeroberfläche**:

    ```sh
    simple-dhcp-server-qt
    ```

* **Command Line** start a server:

    ```sh
    simple-dhcp-server-serve
    ```

* **Kommandozeile** höre nur zu, was passiert:

    ```sh
    simple-dhcp-server-listen
    ```

## Linux (sudo)

Unter Linux musst Du die Kommandos mit `sudo` ausführen, damit sie Zugriff auf
das Netzwerk haben. Das liegt daran, dass der DHCP-Port 67 unter 1024 liegt.
