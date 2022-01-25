# Agent Zero (the first-person agent residing at our home node of the TTT graph) often speaks TTTT
# to its dunbars (trusted agents residing at adjacent TTT nodes) and occasionally speaks to strangers
# untrusted agents two or more degrees distant). Agent Zero is controlled by a user via a client,
# which tpyically serves just one or very few authorized users ("owners"). The client uses an API
# to instruct Agent Zero, which in turn figures out how to carry out the client request via TTTT
# communications with other agents.
#
# This module defines the AgentZero class, as well as Dunbar, Stranger, and Agent which is the base
# class of all three. Dunbars each have a cryptographic tunnel arrangement and the methods to support
# this. AgentZero has methods to initiate TTTT messages with other agents in the TTT graph, and methods
# to listen for TTTT traffic and act on it as it arrives.
#
# The TTTT protocol operates entirely in IPv6. IPv4 addresses are reachable through a compatibility
# map in the IPv6 standard. An IPv4 address through IPv6 is at eighty 0-bits, sixteen 1-bits, and the
# thirty-two bits of IPv4 address. It can even be represented in dot-decimal notation at the end of the
# IPv6 text address representation format. So the IPv4 address "192.168.10.1" is reachable through the
# IPv6 address "::ffff:192.168.10.1"
#
# UDP is the transport layer protocol for TTTT messaging.
# A standard TTTT message must not exceed 1280 bytes in length.
# Messages may occasionally be dropped. That is normal operation.
# Any agent may become or overwhelmed, or forgetful, or shut down.
# TTTT routes around trouble when nodes are sufficiently well connected.
# Critical messages are to be explicitly acknowledged by agents.
# Network congestion or damage is to be explicitly adapted to by agents.
#
# Remember:
# 'TTT' transitive trust topology is the graph of trust. An agent cannot directly see beyond its dunbars.
# 'TTTT' transitive trust topology tinker (or "tabletop") is the protocol of the TTT graph
# 'clade' extends TTTT with specific talents, i.e. 3milmo (credit money), ding (message ratings)
# 'node' is a locus on the TTT graph (a virtual place)
# 'agent' is a software process that speaks TTTT (a daemon) on the TTT graph
# 'agent zero' is the first-person agent residing at the local node
# 'owner' is the person or similar entity who controls an agent
# 'dunbar' is an agent at an adjacent TTT node, one where there's a little trust
# 'stranger' is any TTT agent without sufficient trust to link directly as a dunbar
# See doc/glossary for a more complete jargon reference.

# PIP modules:
import ipaddress
import socket
# time
# base64

# Local modules:
import protocol/api as tttt


class Agent:    # Any node of the TTT graph and the agent residing there: strangers, dunbars, and even AgentZero
    """A TTT network has an agent operating at every node. An agent talks TTTT with other agents."""
    guid = 0        # "globally unique identifier" 48-bits hashed from gSid
    gSid = 0        # "globally secure identifier" 128-bits hashed from public key
    ip6  = "::1"    # The IPv6 address at which this agent listens for incoming TTTT traffic
    port = 5150     # The UDP port this agent listen for TTTT
    pubk = ""       # General-purpose public key. Source material for gSid and guid values.
    name = ""       # Only unique within the scope of Agent Zero. That agent's familiar name around here.


class Stranger(Agent):  # List of memorable non-dunbar nodes.
    """A stranger is an agent at least two degrees distant in the TTT graph."""
    via = []            # List of dunbars that had previously demonstrated path continuity with this stranger


class Dunbar(Agent):    # My VIP list of TTT agents on adjacent nodes because there's some amount of trust.
    """A dunbar is a node and agent at one degree of separation (directly trust-linked to my node)."""
    seed = "seed"       # Shared secret for deterministic random bit generator initialization
    index = 0           # Next index to use in DRBG - can increment or skip forward but never go backward.

    guid_str = base64(guid)

    # TODO: make these real
    hmac1280_from_plain(self, plain):
        """Return an encrypted and HMAC-tagged datagram length-padded to 1280 bytes"""
        # FAKE: Signify NUL character and long pseudorandom padding by appending ".**"
        ret = plain + ".**" # Pad datagram with NUL + random bytes to 1280 length
        # FAKE: Signify dunbar-tunnel encryption by putting braces around padded msg
        ret = "{ "  + ret + " }" # Encrypt datagram for dunbar tunnel
        # FAKE: Signify 16-byte HMAC tag stepping on last 16 bytes by appending guid
        ret = ret + str(guid_str) # Append HMAC to end
        return ret
    plain_from_hmac1280(self, hmac1280)
        """Perform authentication and dunbar-tunnel decryption of a 1280-length HMAC datagram"""
        # FAKE: Verify hmac was originated by this dunbar
        if hmac1280[-8:] != guid_str:
            # throw error Intake.hmac_mismatch
        ret = hmac1280[:-8]
        # FAKE: Signify dunbar-tunnel decryption by removing enclosing braces
        if ret[:1] != "{ " or msg[-2:] != " }":
            # throw error Intake.decrypt_fail
        ret = msg[2:-3]
        if ret[-3:] != ".**"
            # throw error Intake.decrypt_fail
        ret = ret[:-3]
        return ret


class AgentZero(Agent):
    """AgentZero is the first-person agent - the one residing at zero degrees of separation."""
    gSid = 0x9bdd3ad7b8f9737498d0c01ecef0967a   # Big node number (128 bit) of local node
    guid = 0xc01ecef0967a   # Little node number (48 bit) of local node
    name = "*me*"           # My name for myself

    # dunbarSet = []          # "dunbar set" - complete collection of all my dunbars
    # strangerSet = []        # "stranger set" - collection of strangers I care to remember
    # request_count = 0

    def start(self):
        """Start the first-person TTTT listener"""
        sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
        sock.bind((self.ip6, self.port))
        while True:
            datagram, spoofable_addr = sock.recvfrom(1280) # recvfrom => (bytes, address)"
            host = ipaddress.ip_network(spoofable_addr)
            agent = dunbar_at_host[host] or stranger_at_host[host]
            req = plain_from_hmac1280(datagram)
            # write req to queue in database



# Set up asynchronous serving of requests and scheduling of outgoing messages

    # def start(self):
    #     """Start the TTTT listener"""
    #     # TODO: Possibly structure start and stop as a  background process.
    # def stop(self):
    #     """Stop the TTTT listener"""

    def send_udp(ip6, port, plain_data):
        """Send a UDP datagram. Low-level send as-is."""
        sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
        sock.sendto(datagram, (ip6, port))

    def send_to_dunbar(guid, plain):
        """Encrypt and HMAC the message before sending it as a UDP 1280-length datagram."""
        # dunbar = dunbarS[guid]
        datagram = dunbar.hmac1280(plain)
        send_udp(dunbar.ip6, dunbar.port, datagram)

# # listen
# me = tttt.Myself()
# me.listen()
#
# # send
# me = tttt.Myself()
# me.send("::1", 5150, "Hello, World!")


def ip6_host()