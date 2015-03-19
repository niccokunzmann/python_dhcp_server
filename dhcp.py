import time
import threading
import struct
import queue
import collections

from listener import *

def get_host_ip_addresses():
    return gethostbyname_ex(gethostname())[2]


class WriteBootProtocolPacket(object):

    message_type = 2 # 1 for client -> server 2 for server -> client
    hardware_type = 1
    hardware_address_length = 6
    hops = 0

    transaction_id = None

    seconds_elapsed = 0
    bootp_flags = 0 # unicast

    client_ip_address = '0.0.0.0'
    your_ip_address = '0.0.0.0'
    next_server_ip_address = '0.0.0.0'
    relay_agent_ip_address = '0.0.0.0'

    client_mac_address = None
    magic_cookie = '99.130.83.99'

    parameter_order = []
    
    def __init__(self, configuration):
        for i in range(256):
            names = ['option_{}'.format(i)]
            if i < len(options) and hasattr(configuration, options[i][0]):
                names.append(options[i][0])
            for name in names:
                if hasattr(configuration, name):
                    setattr(self, name, getattr(configuration, name))

    def to_bytes(self):
        result = bytearray(236)
        
        result[0] = self.message_type
        result[1] = self.hardware_type
        result[2] = self.hardware_address_length
        result[3] = self.hops

        result[4:8] = struct.pack('>I', self.transaction_id)

        result[ 8:10] = shortpack(self.seconds_elapsed)
        result[10:12] = shortpack(self.bootp_flags)

        result[12:16] = inet_aton(self.client_ip_address)
        result[16:20] = inet_aton(self.your_ip_address)
        result[20:24] = inet_aton(self.next_server_ip_address)
        result[24:28] = inet_aton(self.relay_agent_ip_address)

        result[28:28 + self.hardware_address_length] = macpack(self.client_mac_address)
        
        result += inet_aton(self.magic_cookie)

        for option in self.options:
            value = self.get_option(option)
            #print(option, value)
            if value is None:
                continue
            result += bytes([option, len(value)]) + value
        result += bytes([255])
        return bytes(result)

    def get_option(self, option):
        if option < len(options) and hasattr(self, options[option][0]):
            value = getattr(self, options[option][0])
        elif hasattr(self, 'option_{}'.format(option)):
            value = getattr(self, 'option_{}'.format(option))
        else:
            return None
        function = options[option][2]
        if function and value is not None:
            value = function(value)
        return value
    
    @property
    def options(self):
        done = list()
        # fulfill wishes
        for option in self.parameter_order:
            if option < len(options) and hasattr(self, options[option][0]) or hasattr(self, 'option_{}'.format(option)):
                # this may break with the specification because we must try to fulfill the wishes
                if option not in done:
                    done.append(option)
        # add my stuff
        for option, o in enumerate(options):
            if o[0] and hasattr(self, o[0]):
                if option not in done:
                    done.append(option)
        for option in range(256):
            if hasattr(self, 'option_{}'.format(option)):
                if option not in done:
                    done.append(option)
        return done

    def __str__(self):
        return str(ReadBootProtocolPacket(self.to_bytes()))

class DelayWorker(object):

    def __init__(self):
        self.closed = False
        self.queue = queue.PriorityQueue()
        self.thread = threading.Thread(target = self._delay_response_thread)
        self.thread.start()

    def _delay_response_thread(self):
        while not self.closed:
            p = self.queue.get()
            if self.closed:
                break
            t, func, args, kw = p
            now = time.time()
            if now < t:
                time.sleep(0.01)
                self.queue.put(p)
            else:
                func(*args, **kw)

    def do_after(self, seconds, func, args = (), kw = {}):
        self.queue.put((time.time() + seconds, func, args, kw))

    def close(self):
        self.closed = True

class Transaction(object):

    def __init__(self, server):
        self.server = server
        self.configuration = server.configuration
        self.packets = []
        self.done_time = time.time() + self.configuration.length_of_transaction
        self.done = False
        self.do_after = self.server.delay_worker.do_after

    def is_done(self):
        return self.done or self.done_time < time.time()

    def close(self):
        self.done = True

    def receive(self, packet):
        # packet from client <-> packet.message_type == 1
        if packet.message_type == 1 and packet.dhcp_message_type == 'DHCPDISCOVER':
            self.do_after(self.configuration.dhcp_offer_after_seconds,
                          self.received_dhcp_discover, (packet,), )
        elif packet.message_type == 1 and packet.dhcp_message_type == 'DHCPREQUEST':
            self.do_after(self.configuration.dhcp_acknowledge_after_seconds,
                          self.received_dhcp_request, (packet,), )
        elif packet.message_type == 1 and packet.dhcp_message_type == 'DHCPINFORM':
            self.received_dhcp_inform(packet)
        else:
            return False
        return True

    def received_dhcp_discover(self, discovery):
        if self.is_done(): return
        self.configuration.debug('discover:\n {}'.format(str(discovery).replace('\n', '\n\t')))
        self.send_offer(discovery)

    def send_offer(self, discovery):
        # https://tools.ietf.org/html/rfc2131
        offer = WriteBootProtocolPacket(self.configuration)
        offer.parameter_order = discovery.parameter_request_list
        mac = discovery.client_mac_address
        ip = offer.your_ip_address = self.server.get_ip_address(discovery)
        # offer.client_ip_address = 
        offer.transaction_id = discovery.transaction_id
        # offer.next_server_ip_address =
        offer.relay_agent_ip_address = discovery.relay_agent_ip_address
        offer.client_mac_address = mac
        offer.client_ip_address = discovery.client_ip_address or '0.0.0.0'
        offer.bootp_flags = discovery.bootp_flags
        offer.dhcp_message_type = 'DHCPOFFER'
        offer.client_identifier = mac
        self.server.broadcast(offer)
    
    def received_dhcp_request(self, request):
        if self.is_done(): return 
        self.server.client_has_chosen(request)
        self.acknowledge(request)
        self.close()

    def acknowledge(self, request):
        ack = WriteBootProtocolPacket(self.configuration)
        ack.parameter_order = request.parameter_request_list
        ack.transaction_id = request.transaction_id
        # ack.next_server_ip_address =
        ack.bootp_flags = request.bootp_flags
        ack.relay_agent_ip_address = request.relay_agent_ip_address
        mac = request.client_mac_address
        ack.client_mac_address = mac
        requested_ip_address = request.requested_ip_address
        ack.client_ip_address = request.client_ip_address or '0.0.0.0'
        ack.your_ip_address = self.server.get_ip_address(request)
        ack.dhcp_message_type = 'DHCPACK'
        self.server.broadcast(ack)

    def received_dhcp_inform(self, inform):
        self.close()
        self.server.client_has_chosen(inform)

class DHCPServerConfiguration(object):
    
    dhcp_offer_after_seconds = 10
    dhcp_acknowledge_after_seconds = 10
    length_of_transaction = 40

    network = '192.168.173.0'
    broadcast_address = '255.255.255.255'
    subnet_mask = '255.255.255.0'
    router = None # list of ips
    # 1 day is 86400
    ip_address_lease_time = 300 # seconds
    domain_name_server = None # list of ips

    ip_file = 'ips.csv'

    debug = lambda *args, **kw: None

    def load(self, file):
        with open(file) as f:
            exec(f.read(), self.__dict__)

    def adjust_if_this_computer_is_a_router(self):
        ip_addresses = get_host_ip_addresses()
        for ip in reversed(ip_addresses):
            if ip.split('.')[-1] == '1':
                self.router = [ip]
                self.domain_name_server = [ip]
                self.network = '.'.join(ip.split('.')[:-1] + ['0'])
                self.broadcast_address = '.'.join(ip.split('.')[:-1] + ['255'])
                #self.ip_forwarding_enabled = True
                #self.non_local_source_routing_enabled = True
                #self.perform_mask_discovery = True

class IPDatabase(object):

    delimiter = ';'

    def __init__(self, file_name):
        self.file_name = file_name
        with open(self.file_name, 'a'):
            pass # create file

    def get(self, key):
        lines = []
        with open(self.file_name) as f:
            for line in f:
                line = line.strip().lower().split(self.delimiter)
                if key.lower() in line:
                    lines.append(line)
        return lines

    def add(self, *args):
        with open(self.file_name, 'a') as f:
            f.write(self.delimiter.join(args) + '\r\n')

    def delete(self, key):
        lines = []
        with open(self.file_name) as f:
            for line in f:
                line = line.strip().lower().split(self.delimiter)
                if key.lower() not in line:
                    lines.append(line)
        with open(self.file_name, 'w') as f:
            for line in lines:
                f.write(self.delimiter.join(line) + '\r\n')

    def all(self):
        lines = []
        with open(self.file_name) as f:
            for line in f:
                lines.append(line.strip().split(self.delimiter))
        return lines

class DHCPServer(object):

    def __init__(self, configuration = None):
        if configuration == None:
            configuration = DHCPServerConfiguration()
        self.configuration = configuration
        self.socket = socket(type = SOCK_DGRAM)
        self.socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.socket.bind(('', 67))
        self.delay_worker = DelayWorker()
        self.closed = False
        self.transactions = collections.defaultdict(lambda: Transaction(self)) # id: transaction
        self.ips = IPDatabase(self.configuration.ip_file)

    def close(self):
        self.socket.close()
        self.closed = True
        self.delay_worker.close()
        for transaction in list(self.transactions.values()):
            transaction.close()

    def update(self, timeout = 0):
        reads = select.select([self.socket], [], [], timeout)[0]
        for socket in reads:
            packet = ReadBootProtocolPacket(*socket.recvfrom(4096))
            self.received(packet)
        for transaction_id, transaction in list(self.transactions.items()):
            if transaction.is_done():
                transaction.close()
                self.transactions.pop(transaction_id)

    def received(self, packet):
        if not self.transactions[packet.transaction_id].receive(packet):
            self.configuration.debug('received:\n {}'.format(str(packet).replace('\n', '\n\t')))

    def client_has_chosen(self, packet):
        self.configuration.debug('client_has_chosen:\n {}'.format(str(packet).replace('\n', '\n\t')))
        ip = packet.client_ip_address
        if ip == '0.0.0.0':
            ip = packet.requested_ip_address
            if not ip:
                return
        new_entry = [packet.client_mac_address,
                     ip,
                     packet.host_name or '']
        if not any(list(entry) == new_entry for entry in self.ips.all()):
            self.ips.add(*new_entry)

    def is_valid_client_address(self, address):
        if address is None:
            return False
        a = address.split('.')
        s = self.configuration.subnet_mask.split('.')
        n = self.configuration.network.split('.')
        return all(s[i] == '0' or a[i] == n[i] for i in range(4))

    def get_ip_address(self, packet):
        mac_address = packet.client_mac_address
        requested_ip_address = packet.requested_ip_address
        known_entries = self.ips.get(mac_address)
        ip = None
        if known_entries:
            for mac, _ip, host in known_entries:
                if self.is_valid_client_address(_ip):
                    ip = _ip
            print('known ip:', ip)
        elif self.is_valid_client_address(requested_ip_address):
            ip = requested_ip_address
            print('valid ip:', ip)
        if ip is None:
            for i in range(5, 250):
                ip = self.configuration.network[:-1] + str(i)
                if not self.ips.get(ip):
                    break
            print('new ip:', ip)
        if not any([entry[1] == ip for entry in known_entries]):
            self.ips.add(mac_address, ip, packet.host_name or '')
        return ip

    @property
    def server_identifiers(self):
        return get_host_ip_addresses()

    def broadcast(self, packet):
        self.configuration.debug('broadcasting:\n {}'.format(str(packet).replace('\n', '\n\t')))
        for addr in self.server_identifiers:
            broadcast_socket = socket(type = SOCK_DGRAM)
            broadcast_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
            broadcast_socket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
            packet.server_identifier = addr
            broadcast_socket.bind((addr, 67))
            try:
                data = packet.to_bytes()
                broadcast_socket.sendto(data, ('255.255.255.255', 68))
                broadcast_socket.sendto(data, (addr, 68))
            finally:
                broadcast_socket.close()

    def run(self):
        while not self.closed:
            self.update(1)

    def run_in_thread(self):
        thread = threading.Thread(target = self.run)
        thread.start()
        return thread

    def debug_clients(self):
        for line in self.ips.all():
            line = '\t'.join(line)
            if line:
                self.configuration.debug(line)

if __name__ == '__main__':
    configuration = DHCPServerConfiguration()
    configuration.debug = print
    configuration.adjust_if_this_computer_is_a_router()
    configuration.router #+= ['192.168.0.1']
    configuration.ip_address_lease_time = 60
    server = DHCPServer(configuration)
    server.run_in_thread()
