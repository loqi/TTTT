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

# Remember:
# 'TTT' is transitive trust topology - or 'tripod' - graph of trust. We only see the local part.
# 'TTTT' is transitive trust topology tinker - or 'tabletop' - the protocol of TTT
# 'node' is a locus on the TTT graph (a virtual place)
# 'agent' is a software process that speaks TTTT (a daemon)
# 'boss' is the interface allowing a user to control an agent

import socket
import daemon
# import time

class Agent:    # Any node of the TTT graph and the agent residing there: strangers, dunbars, and even myself
    """A TTT network has an agent operating at every node. An agent talks TTTT with other agents."""
    gsid = 0        # "globally secure identifier" 128-bits derived from pub key
    guid = 0        # "globally unique identifier" 48-bits derived from gSid
    ip6  = "::1"    # I listen at this address for TTTT traffic (testing the software at localhost)
    port = 5150     # Port this dunbar likes to listen at
    pubk = ""       # General-purpose public key. Source material for gSid hash.
    name = ""       # Human-format name, only unique in the scope of this node. - familiar name

class Stranger(Agent):   # List of memorable non-dunbar nodes
    """A dunbar is a node one degree away. That is, a node whose agent directly trust-links with my agent."""
    via = []            # Previously successful paths had reached this stranger via these dunbars

class Dunbar(Agent):    # My VIP list of TTT agents
    """A dunbar is a node and agent at one degree of separation (directly trust-linked to my node)."""
    seed = "seed"       # For initializing deterministic random bit generator
    index = 0           # For indexing deterministic random bit generator

class Agent0(Agent):
    """Agent0 is agent and node at zero degrees of separation. (Our first-person agent)"""
    gsid = 0x9bdd3ad7b8f9737498d0c01ecef0967a   # Big node number (128 bit) of myself:
    guid = 0xc01ecef0967a   # Little node number (48 bit) of myself
    name = "*me*"           # My name for myself

    def start(self):
        sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
        sock.bind((self.ip6, self.port))
        with daemon.DaemonContext():
            while True:
                datagram, addr = sock.recvfrom(1280)
                got_request(datagram)

    def noop(self, guid):
        _dunbar_send(guid, "~^ ** NOOP .")


def send_udp(ip6, port, datagram):
    sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    sock.sendto(datagram, (ip6, port))

def send_to_dunbar(guid, plain_bytestring):
    # dunbar = dunbarS[guid]
    # encrypt plain_bytestring as crypt_bytestring
    send_udp(dunbar.ip6, dunbar.port, crypt_bytestring)

# dunbarS = []          # "dunbar set" - complete collection of all my dunbars
# strangerS = []        # "stranger set" - collection of strangers I care to remember

    # def echo(self, ip6, port, message):
    #     sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    #     print('SENDING ['+ip6+']:'+str(port)+'    "'+message+'"')
    #     sock.sendto(message.encode("UTF-8"), (ip6, port))

# TRUST 
# NOOP receive message
# ECHO
# AVOW

# Initialize me as the TTTT user
me = Boss()

# B
me.start()



# Stranger applies to be trusted:
# ptext = """TRUST "Hi Jose, this is Park and I would like to become a dunbar of yours." ~^b6iR98"""
# ctext = cypher(pk[jose], ptext)
# tag   =   sign(pk[park], ctext)
# ~^ ?/ tag ctext
# means "TTTT" "pubkey" "verification it came from me" "encrypeted greeting"
# Occasionally check the keys.

    def got_request(datagram):
        # Leading bytes of datagram "~^ "=TTTT "?? "=public key
        # differentiate between stranger or dunbar
        # decrypt the datagram
        # normalize the datagram
        # parse the datagram






# def do_something():
#     while True:
#         with open("/tmp/current_time.txt", "w") as f:
#             f.write("The time is now " + time.ctime())
#         time.sleep(5)
#
#
# if __name__ == "__main__":
#     run()





    # def dunsay(dunbar):
    #     print('SENDING ['+to_ip6+']:'+str(to_port)+']    "'+message+'"')
    #     sock.sendto(message.encode("UTF-8"), (ip6, port))
