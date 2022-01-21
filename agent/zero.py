# This script starts the Agent Zero server daemon.

# Agent Zero (the first-person agent residing at our home node of the TTT graph) often speaks TTTT to
# its dunbars (the agents at adjacent TTT nodes) and occasionally speaks to strangers (agents two or
# more degrees distant). Agent Zero is controlled by a user via a client, which tpyically serves
# just one or very few authorized users. This client process uses an API to instruct Agent Zero, which
# in turn figures out how to carry out the client request via TTTT communications with other agents.

# The TTTT protocol operates entirely in IPv6. IPv4 addresses are reachable through a compatibility
# map in the IPv6 standard. An IPv4 address through IPv6 is at eighty 0-bits, sixteen 1-bits, and the
# thirty-two bits of IPv4 address. It can even be represented in dot-decimal notation at the end of the
# IPv6 text address representation format. So the IPv4 address "192.168.10.1" is reachable through the
# IPv6 address "::ffff:192.168.10.1"

# UDP is the transport layer protocol for TTTT messaging.
# Standard messages may not exceed 1280 bytes in length.
# Messages may occasionally be dropped. That is normal operation.
# TTTT routes around trouble when nodes are sufficiently well connected.
# Critical messages are explicitly acknowledged by agents.
# Network congestion is to be explicitly adapted to by agents.

# Remember:
# 'TTT' is transitive trust topology - the graph of trust. An agent can only directly see its dunbars.
# 'TTTT' is transitive trust topology tinker - ("tabletop protocol") the protocol of the TTT graph
# 'node' is a locus on the TTT graph (a virtual place)
# 'agent' is a software process that speaks TTTT (a daemon) on the TTT graph
# 'Agent Zero' is the first-person agent residing at the local node
# 'owner' is the person or similar entity who controls an agent
# 'dunbar' is an agent at an adjacent TTT node, one where there's a little trust
# 'stranger' is any TTT agent without sufficient trust to link directly as a dunbar
# See doc/glossary for a more complete jargon reference.

import socket
# import time

class Agent:    # Any node of the TTT graph and the agent residing there: strangers, dunbars, and even AgentZero
    """A TTT network has an agent operating at every node. An agent talks TTTT with other agents."""
    gsid = 0        # "globally secure identifier" 128-bits hashed from public key
    guid = 0        # "globally unique identifier" 48-bits hashed from gsid
    ip6  = "::1"    # The IPv6 address at which this agent listens for incoming TTTT traffic
    port = 5150     # The UDP port this agent listen for TTTT
    pubk = ""       # General-purpose public key. Source material for gsid and guid values.
    name = ""       # Only unique within the scope of Agent Zero. That agent's familiar name around here.

class Stranger(Agent):  # List of memorable non-dunbar nodes.
    """A stranger is an agent at least two degrees distant in the TTT graph."""
    via = []            # List of dunbars that had previously demonstrated path continuity with this stranger

class Dunbar(Agent):    # My VIP list of TTT agents on adjacent nodes because there's some amount of trust.
    """A dunbar is a node and agent at one degree of separation (directly trust-linked to my node)."""
    drbg = "seed"       # Shared secret for deterministic random bit generator initialization

class AgentZero(Agent):
    """AgentZero is the first-person agent - the one residing at zero degrees of separation."""
    gsid = 0x9bdd3ad7b8f9737498d0c01ecef0967a   # Big node number (128 bit) of local node
    guid = 0xc01ecef0967a   # Little node number (48 bit) of local node
    name = "*me*"           # My name for myself
    # dunbarS = []          # "dunbar set" - complete collection of all my dunbars
    # strangerS = []        # "stranger set" - collection of strangers I care to remember


    # AgentZero is the one we control so there are methods:

    def start(self):
        """Start the first-person TTTT listener daemon"""
        sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
        sock.bind((self.ip6, self.port))
        while True:
            datagram, addr = sock.recvfrom(1280)
            got_request(datagram)

    def send_udp(ip6, port, datagram):
        sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
        sock.sendto(datagram, (ip6, port))

    def send_to_dunbar(guid, plain_bytestring):
        # dunbar = dunbarS[guid]
        # encrypt plain_bytestring as crypt_bytestring
        send_udp(dunbar.ip6, dunbar.port, crypt_bytestring)
