#!/usr/bin/env python3

import socket

GUID = "SvhC3Nza"
PUBK = "ed25519 AAAASvhC3Nza"

class Node:
    guid = b"SvhC3Nza" # 8 binary bytes derived from public key
    ip   = "0000:0000:0000:0000:0000:0000:0000:0000"
    port = 5150 # Port that node listens and sends at

class Dunbar(Node):
    mnem = "" # short human-memorable name
    name = "" # long human-memorable name
    pubk = "" # general-purpose public key
    seed = "" # for deterministic random bit generator
    index = 0 # for deterministic random bit generator

class Tttt:
    """A TTTT agent is the primary actor on a TTT network. It exchanges secure protocol messages with other agents."""

    udp_port = 5150
    ip6_here = "0000:0000:0000:0000:0000:0000:0000:0000" # localhost "::1"
    sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    sock.bind((ip6_here, udp_port))

    def listen():
        while True:
            data, addr = sock.recvfrom(1280)
            print("got message:", data.decode("UTF-8"))

    def send(to_ip6, message):
        print('SENDING ['+to_ip6+']:'+str(udp_port)+']    "'+message+'"')
        sock.sendto(message.encode("UTF-8"), (to_ip6, udp_port))

