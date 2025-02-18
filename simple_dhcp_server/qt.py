"""Run the Python DHCP server with QT."""
import os
import signal
try:
    import PySide6
except ImportError:
    raise ImportError("Install simple_dhcp_server[qt] and run again.")
from PySide6.QtWidgets import QApplication, QMainWindow, QErrorMessage, QTableWidget, QTableWidgetItem
from PySide6.QtGui import QIcon, QFont, QBrush, QColor
from PySide6.QtCore import QTimer

# Only needed for access to command line arguments
import sys

from simple_dhcp_server.dhcp import DHCPServer, DHCPServerConfiguration, Host

HERE = os.path.dirname(__file__)
ICON = os.path.join(HERE, "icon.ico")

THIS_CONFIG = 'simple-dhcp-server-qt.yml'


class HostsTableWidget(QTableWidget):
    def __init__(self, *args):
        QTableWidget.__init__(self, 3, 1, *args)
        self.setColumnCount(3)
        self.last_hosts : list[Host] = []
        
    def bgColor(self, host:Host) -> str:
        """Return the background color for the host."""
        if self.last_hosts is None:
            return "#ffffff"
        try:
            index = self.last_hosts.index(host)
        except IndexError:
            return "#ffffff"
        s = "024579bdf"
        if index >= len(s): return "#ffffff"
        c = s[index]
        color = f"#ffff{c}{c}"
        return color
    
    def bgBrush(self, host:Host) -> QBrush:
        return QBrush(QColor(self.bgColor(host)))
 
    def updateHosts(self, hosts:list[Host]): 
        time_sorted_hosts = list(reversed(sorted(hosts, key = lambda host: host.last_used)))
        self.last_hosts = time_sorted_hosts

        style = ""
        for i, host in enumerate(hosts):
            self.insertRow(i)
            self.setItem(i, 0, self.get_item(host, host.mac))
            self.setItem(i, 1, self.get_item(host, host.ip))
            self.setItem(i, 2, self.get_item(host, host.hostname))
        self.setHorizontalHeaderLabels(["MAC", "IP", "HOST"])
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        self.setRowCount(len(hosts))
        self.setStyleSheet(style)
        
    def get_item(self, host: Host, text: str) -> QTableWidgetItem:
        brush = self.bgBrush(host)
        item = QTableWidgetItem(text)
        item.setBackground(brush)
        return item


def main():
    """Run the Python DHCP server with QT."""

    app = QApplication(sys.argv)

    
    configuration = DHCPServerConfiguration()
    configuration.debug = print
    #configuration.adjust_if_this_computer_is_a_router()
    config_file = os.path.join(HERE, THIS_CONFIG)
    if not os.path.exists(THIS_CONFIG):
        with open(config_file) as s:
            with open(THIS_CONFIG, "w") as f:
                f.write(s.read())
        print("Created config file:", config_file)
    configuration.load_yaml(THIS_CONFIG)
    try:
        server = DHCPServer(configuration)
    except PermissionError:
        # see https://stackoverflow.com/a/40227202
        error_dialog = QErrorMessage()
        error_dialog.showMessage("No access to DHCP port 67.\nThe network port cannot be accessed. Run this program with sudo.")
        app.exec()
        exit(1)
    server.run_in_thread()

    window = QMainWindow()
    window.show()
    window.setWindowTitle('MAC, IP & Computer')
    window.setWindowIcon(QIcon(ICON))
    
    # font 
    # see https://stackoverflow.com/a/1835938
    font = QFont("Monospace")
    font.setStyleHint(QFont.Monospace)
    info = HostsTableWidget()
    # info.setFont(font)
    info.setMinimumWidth(460)
    info.setMinimumHeight(60)
    window.setCentralWidget(info)


    last_time_sorted_hosts = None
    def update_text():
        nonlocal last_time_sorted_hosts
        hosts = server.get_all_hosts()
        info.updateHosts(hosts)
        info.adjustSize()
        window.adjustSize()

    # quit on KeyboardInterrupt
    # see https://stackoverflow.com/a/4939113
    signal.signal(signal.SIGINT, lambda *args: app.quit())

    # see https://stackoverflow.com/a/59094300
    timer = QTimer()
    timer.timeout.connect(update_text)
    timer.setInterval(100)
    timer.start()
    
    info.show()
    update_text()

    app.exec()
    server.close()

if __name__ == '__main__':
    main()

