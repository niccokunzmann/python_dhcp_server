"""Run the Python DHCP server with QT."""
import os
from PySide6.QtWidgets import QApplication, QTextEdit, QMainWindow, QErrorMessage
from PySide6.QtGui import QIcon, QFont
from PySide6.QtCore import QTimer

# Only needed for access to command line arguments
import sys

from dhcp_server.dhcp import DHCPServer, DHCPServerConfiguration

HERE = os.path.dirname(__file__)
ICON = os.path.join(HERE, "icon.ico")

THIS_CONFIG = 'python-dhcp-server-qt.yml'


def main():
    """Run the Python DHCP server with QT."""

    app = QApplication(sys.argv)

    
    configuration = DHCPServerConfiguration()
    configuration.debug = print
    #configuration.adjust_if_this_computer_is_a_router()
    config_file = os.path.join(HERE, THIS_CONFIG)
    if not os.path.exists(THIS_CONFIG):
        with open(THIS_CONFIG, "w") as f:
            with open(config_file) as s:
                f.write(s.read())
        print("Created config file:", THIS_CONFIG)
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
    info_text = QTextEdit()
    info_text.setFont(font)
    info_text.setMinimumWidth(460)
    info_text.setMinimumHeight(60)
    window.setCentralWidget(info_text)


    last_time_sorted_hosts = None
    def update_text():
        nonlocal last_time_sorted_hosts
        # root.after(100, update_text)
        hosts = server.get_all_hosts()
        current_hosts = server.get_current_hosts()
        time_sorted_hosts = list(reversed(sorted(hosts, key = lambda host: host.last_used)))
        if last_time_sorted_hosts != time_sorted_hosts:
            text = 'MAC'.center(17) + '  ' + 'IP'.center(15) + '  ' + '  HOST' + '\n'
            headerlines = 1
            for host in hosts:
                text += '{}  {}  {}\n'.format(host.mac, host.ip.ljust(15, ' '), host.hostname)
            info_text.setText(text)
            # prettify the text
                # if host in current_hosts:
                #     tag_index = int(time_i / len(current_hosts) * len(time_tags))
                #     info_text.tag_add(time_tags[tag_index], start, stop)
                # else:
                #     info_text.tag_add(old_tag, start, stop)
            # info_text.tag_raise("sel")
        last_time_sorted_hosts = time_sorted_hosts

    # see https://stackoverflow.com/a/59094300
    timer = QTimer()
    timer.timeout.connect(update_text)
    timer.setInterval(100)
    timer.start()

    app.exec()
    server.close()

if __name__ == '__main__':
    main()

