"""The Python DHCP server.

You can run these programs:

    python-dhcp-server-tk

        Start the tkinter GUI.

    python-dhcp-server-qt

        Start the QT GUI.

    python-dhcp-server-serve

        Start a dhcp server in the terminal.

    python-dhcp-server-listen

        Listen and print dhcp traffic on the network.

"""

def main():
    """Print the documentation and exit."""
    from .version import version
    print(__name__, version)
    print()
    print(__doc__)
