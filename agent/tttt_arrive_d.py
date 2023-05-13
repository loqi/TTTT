# This is the TTTT agent network listener.

# import daemon
# with daemon.DaemonContext():
#     AgentZero().start()

import socket
import sys
# import socketserver

"""
Run as a daemon
Open stamp.db to associate a jot to a tunnel
    stamp8 : tunn_id
Open table: tunnel.db
    tunnel_id : from_id, to_id, tunnkey

Open table: injot.db - due_at 

Listen for incoming wads via many sockets
    When a wad comes in,
    strip off stamp, seal, and wad
    Look in stamp.db for wax[0..7]: tunn_id
        loop to read all consecutive increments, where tunn_id=0 is skipped
    query tunnel.db to get all (usually just one) tunnel records
    seal = wax[8..15]
    find a key that decrypts wad and matches seal
    if so, parse the wad into binjots
    perform basic sanity checks and write binjots to injot.db
    remove stamp from stamp.db by:
        zero it out.
        scan forward along stamps until reaching blank or non-zeroed stamp
        if it terminated by a null one, then delete all the ending zeroed stamps going backward.
    repeat
"""



def log(msg):
    print(msg, file=sys.stderr)


# Set up UDP socket connection
IP6_ADDR = "::" # Equivalent to IPv4 0.0.0.0
UDP_PORT = 5150
log('Creating socket.')
try:
    sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    log('Socket created.')
except socket.error as err :
    log(f'Failed to create socket: {err}')
    sys.exit()

# Bind the socket to the endpoint
log(f'Starting UDP server [{IP6_ADDR}]:{UDP_PORT}')
try:
    sock.bind((IP6_ADDR, UDP_PORT))
except socket.error as err:
    log(f'Failed to bind socket: {err}')
    sys.exit()

while True:
    log('\nWaiting to receive UDP datagram...')
    data, addr = sock.recvfrom(1280)
    log(f'Received {len(data)} bytes from {addr}\n{data}\n')
    if data:
        log(f'Sending {len(data)} bytes back to {addr}')
        length = sock.sendto(data, addr)
        log(f'Confirmed {length} bytes sent')

# class TtttAgent(socketserver.BaseRequestHandler):

#     def handle(self):
#         data = self.request[0].strip()
#         socket = self.request[1]
#         print("{} wrote:".format(self.client_address[0]))
#         print(data)
#         socket.sendto(data.upper(), self.client_address)

# if __name__ == "__main__":
#     HOST, PORT = "localhost", 9999
#     with socketserver.UDPServer((HOST, PORT), TtttAgent) as server:
#         server.serve_forever()


# 0. Listen at ip6 address and UDP port for any traffic.
# 1. Receive a datagram from that socket.
# 2. Attribute that datagram to a sending TTTT node.
#       if unattributable, discard it and log the event.
# 3. Authenticate that the datagram is genuine and untampered.
#       if defective, discard it and log the event.
# 4. Parse that datagram into jots, each with a priority rating.
# 5. Add those jots to the arrive.db task pool database.
# 6. Loop back to listening.
