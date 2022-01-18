#!/usr/bin/env python3

import socket

GUID = "SvhC3Nza"
PUBK = "ed25519 AAAASvhC3Nza"

class Agent:
    """Agent is the primary actor on a TTT network. It talks TTTT with other agents to run applications."""

    udp_port = 5150
    ip6_here = "::1" # localhost

    sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    sock.bind((ip6_here, udp_port))

    def listen():
        while True:
            data, addr = sock.recvfrom(1280)
            print("got message:", data.decode("UTF-8"))

    def send(to_ip6, message):
        print('SENDING ['+to_ip6+']:'+str(udp_port)+']    "'+message+'"')
        sock.sendto(message.encode("UTF-8"), (to_ip6, udp_port))
