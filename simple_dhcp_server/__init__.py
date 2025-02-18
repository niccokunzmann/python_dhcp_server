"""The simple DHCP server.

You can run these programs:

    simple-dhcp-server-tk

        Start the tkinter GUI.

    simple-dhcp-server-qt

        Start the QT GUI.

    simple-dhcp-server-serve

        Start a dhcp server in the terminal.

    simple-dhcp-server-listen

        Listen and print dhcp traffic on the network.

"""

def main():
    """Print the documentation and exit."""
    from .version import version
    print(__name__, version)
    print()
    print(__doc__)
