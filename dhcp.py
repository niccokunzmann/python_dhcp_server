import time
import threading
import struct
import queue
import collections

from listener import *

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
    
    def __init__(self):
        pass

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
        print('discover:\n {}'.format(str(discovery).replace('\n', '\n\t')))
        self.send_offer(discovery)

    def send_offer(self, discovery):
        # https://tools.ietf.org/html/rfc2131
        offer = WriteBootProtocolPacket()
        offer.parameter_order = discovery.parameter_request_list
        mac = discovery.client_mac_address
        ip = offer.your_ip_address = self.server.get_ip_address(mac, discovery.requested_ip_address)
        # offer.client_ip_address = 
        offer.transaction_id = discovery.transaction_id
        # offer.next_server_ip_address =
        offer.relay_agent_ip_address = discovery.relay_agent_ip_address
        offer.client_mac_address = mac
        offer.client_ip_address = discovery.client_ip_address or '0.0.0.0'
        offer.bootp_flags = discovery.bootp_flags
        offer.dhcp_message_type = 'DHCPOFFER'
        offer.client_identifier = mac
        offer.subnet_mask = self.configuration.subnet_mask
        offer.router = self.configuration.router
        offer.ip_address_lease_time = self.configuration.ip_address_lease_time
        offer.server_identifier = self.configuration.server_identifier
        offer.domain_name_server = self.configuration.domain_name_server
        offer.broadcast_address = self.configuration.broadcast_address
        self.server.broadcast(offer)
    
    def received_dhcp_request(self, request):
        if self.is_done(): return 
        self.server.client_has_chosen(request)
        self.close()
        if request.server_identifier in self.server.server_identifiers or \
           not server.is_valid_client_address(request.requested_ip_address):
            self.acknowledge(request)

    def acknowledge(self, request):
        ack = WriteBootProtocolPacket()
        ack.parameter_order = request.parameter_request_list
        ack.transaction_id = request.transaction_id
        # ack.next_server_ip_address =
        ack.bootp_flags = request.bootp_flags
        ack.relay_agent_ip_address = request.relay_agent_ip_address
        mac = request.client_mac_address
        ack.client_mac_address = mac
        requested_ip_address = request.requested_ip_address
        ack.client_ip_address = request.client_ip_address or '0.0.0.0'
        ack.your_ip_address = self.server.get_ip_address(mac, requested_ip_address) # todo: should be asked from the server who knows it
        ack.subnet_mask = self.configuration.subnet_mask
        ack.router = self.configuration.router
        ack.dhcp_message_type = 'DHCPACK'
        ack.ip_address_lease_time = self.configuration.ip_address_lease_time
        ack.server_identifier = self.configuration.server_identifier
        ack.domain_name_server = self.configuration.domain_name_server
        ack.broadcast_address = self.configuration.broadcast_address
        self.server.broadcast(ack)

    def received_dhcp_inform(self, inform):
        self.close()
        self.server.client_has_chosen(inform)

class DHCPServerConfiguration(object):
    
    dhcp_offer_after_seconds = 10
    dhcp_acknowledge_after_seconds = 0
    length_of_transaction = 20

    server_identifier = '0.0.0.0'
    network = '192.168.173.0'
    broadcast_address = '255.255.255.255'
    subnet_mask = '255.255.255.0'
    router = None
    # 1 day is 86400
    ip_address_lease_time = 300 # seconds
    domain_name_server = None
    


class DHCPServer(object):

    def __init__(self, configuration = None):
        if configuration == None:
            configuration = DHCPServerConfiguration()
        self.configuration = configuration
        self.socket = socket(type = SOCK_DGRAM)
        self.socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.socket.bind(('', 67))
        self.delay_worker = DelayWorker()
        self.ip_number = 5
        self.closed = False
        self.transactions = collections.defaultdict(lambda: Transaction(self)) # id: transaction

    def close(self):
        self.socket.close()
        self.closed = True
        self.delay_worker.close()
        for transaction in list(self.transaction.values()):
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
            print('received:\n {}'.format(str(packet).replace('\n', '\n\t')))

    def client_has_chosen(self, packet):
        print('client_has_chosen:\n {}'.format(str(packet).replace('\n', '\n\t')))

    def is_valid_client_address(self, address):
        a = address.split('.')
        s = self.configuration.subnet_mask.split('.')
        n = self.configuration.network.split('.')
        return all(s[i] == '0' or a[i] == n[i] for i in range(4))

    def get_ip_address(self, mac_address, requested_ip_address):
        if self.is_valid_client_address(requested_ip_address):
            return requested_ip_address
        self.ip_number = (self.ip_number + 1) % 200 + 5
        return self.configuration.network[:-1] + str(self.ip_number)

    @property
    def server_identifiers(self):
        return gethostbyname_ex(gethostname())[2]

    def broadcast(self, packet):
        print('broadcasting:\n {}'.format(str(packet).replace('\n', '\n\t')))
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

if __name__ == '__main__':
    configuration = DHCPServerConfiguration()
    server = DHCPServer(configuration)
    server.run_in_thread()
