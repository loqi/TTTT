#!/usr/bin/env python3

import myself

class TmmDunbar(Dunbar):
    iou = 0 # Integer balance in millikudos. Negative sign means I am owed; positive means I owe.
    iouForeign = {}
    booked = []

class Tmm:
    """A 3milmo agent knows how to mediate money with another 3milmo agent.

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

    def dunsay(dunbar):
        print('SENDING ['+to_ip6+']:'+str(udp_port)+']    "'+message+'"')
        sock.sendto(message.encode("UTF-8"), (to_ip6, udp_port))
