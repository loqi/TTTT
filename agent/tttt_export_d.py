import socket
import sys

def log(msg):
    print(msg, file=sys.stderr)

# Set up UDP socket connection
IP6_ADDR = "::1"
UDP_PORT = 5150
log('Creating socket.')
try:
    sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    log('Socket created.')
except socket.error as err:
    log(f'Failed to create socket: {err}')
    sys.exit()

# Initial message to be sent and echoed back
message = bytes.fromhex('dead beef')

try:
    # Send data
    log(f'Sending {len(message)} bytes:\n{message}\n')
    length = sock.sendto(message, (IP6_ADDR, UDP_PORT))
    log(f'Confirmed {length} bytes sent.')
except socket.error as err:
    log(f'Failed to send data: {err}')
    sys.exit()

    # Receive response
try:
    log('Waiting for echo...')
    data, server = sock.recvfrom(4096)
    log(f'Received {len(data)} bytes:\n{data}\n')
except socket.error as err:
    log(f'Failed to receive data: {err}')
    sys.exit()

finally:
    log('Closing socket')
    sock.close()

# HOST, PORT = "localhost", 9999
# data = " ".join(sys.argv[1:])

# # SOCK_DGRAM is the socket type to use for UDP sockets
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# # As you can see, there is no connect() call; UDP has no connections.
# # Instead, data is directly sent to the recipient via sendto().
# sock.sendto(bytes(data + "\n", "utf-8"), (HOST, PORT))
# received = str(sock.recv(1024), "utf-8")

# print("Sent:     {}".format(data))
# print("Received: {}".format(received))


# 0. Listen at localhost+UDP socket for dispatch datagram.
# 1, Parsing datagram, identify which dunbar is to be recipient.
# 2. Build a departing datagram with all the ripest jots that fit in 1280 max.
# 3. Pad that datagram with a random tail to obfuscate length.
# 4. Mark those jots in depart.db as sent.
# 6. Loop back to listening.
