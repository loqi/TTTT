#!/usr/bin/env python3

# The TTTT protocol operates entirely in IPv6. IPv4 addresses are reachable through a compatibility map in the IPv6
# standard. An IPv4 address through IPv6 is at eighty 0-bits, sixteen 1-bits, and the thirty-two bits of IPv4 address.
# It can even be represented in dot-decimal notation at the end of the IPv6 text address representation format.
# So the IPv4 address "192.168.10.1" is reachable through the IPv6 address "::ffff:192.168.10.1"

# UDP is the primary transport layer protocol for TTTT messaging.
# Standard messages must fit within a 1280 byte datagram.
# Messages may occasionally be dropped. That is normal operation.
# TTTT routes around trouble when nodes are sufficiently well connected.
# Critical messages are explicitly acknowledged by agents.
# Network congestion is to be explicitly adapted to by agents.

import socket

class Agent:        # Any node of the TTT graph and the agent living there including strangers, dunbars, and even myself
    gsid = 0            # "globally secure identifier" 128-bits derived from pub key
    guid = 0            # "globally unique identifier" 48-bits derived from gSid
    ip6  = "::1"        # I listen at this address for TTTT traffic (testing the software at localhost)
    port = 5150         # Port this dunbar likes to listen at
    pubk = "pubk here"  # General-purpose public key. Source material for gSid hash.
    name = "anonymous"  # Human-format name, only unique in the scope of this node. - familiar name

class Dunbar(Agent): # An agent directly trust-link with me
    seed = "seed here"  # For initializing deterministic random bit generator
    index = 0           # For indexing deterministic random bit generator

class Stranger(Agent):   # A stranger object is any agent worth remembering who is more than one degree distant
    via = []            # Previously successful paths had reached this stranger via these dunbars

class Myself(Agent): # This agent and its home node
    """A TTTT agent is the primary actor on a TTT network. It exchanges secure protocol messages with other agents."""

    gsid = 0x9bdd3ad7b8f9737498d0c01ecef0967a   # My big node number
    guid = 0xc01ecef0967a   # My little node number
    name = "*me*"           # My name for myself

    # dunbarS = []        # "dunbar set" - complete collection of all my dunbars
    # strangerS = []      # "stranger set" - collection of strangers I care to remember

    def listen(self):
        sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
        sock.bind((self.ip6, self.port))
        print('LISTENING ['+self.ip6+']:'+str(self.port))
        while True:
            data, addr = sock.recvfrom(1280)
            print(addr)
            print(data.decode("UTF-8"))

    def send(self, ip6, port, message):
        sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
        print('SENDING ['+ip6+']:'+str(port)+'    "'+message+'"')
        sock.sendto(message.encode("UTF-8"), (ip6, port))

# NOOP
# ECHO
# AVOW

    # def dunsay(dunbar):
    #     print('SENDING ['+to_ip6+']:'+str(to_port)+']    "'+message+'"')
    #     sock.sendto(message.encode("UTF-8"), (ip6, port))
