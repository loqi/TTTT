# tttt{PUSH
#      cargo 3milmo{REMIT
#                   purse frag{TOSS
#                              value 0.002
#                              atom 500
#                              }222
#                   fare 30
#                   need 12
#                   }111
#      from AAA
#      to ZZZ
#      nav [...]
#      weight 3
#      }000



# {tttt:PUSH cargo {3milmo:REMIT purse {frag:TOSS value 0.002 atom 500 }/-222
#                                fare 30 need 12 }@$111
#            from AAA to ZZZ nav [...] weight 3 }~^000



# NOOP (agent0) -- Queue a wad for departure and then discard it
#   Example - Do nothng and move on to the next task:
#       > tttt ~^{NOOP }yarncode

# PING (dunbar or xenode) Direct trivial contact to be acknowledged
#   Ex - Directly ping a node and receive an acknowledgement:
#       > tttt ~^{PING }yarncode
#         < ~^yarncode yes .

# BECKON (xenode) Invitation to establish a dunbar relationship
#   Ex - Set up a one-way dunbar tunnel toward initiator 100 tttt per day:
#       > tttt ~^{BECKON width 100 tunkey AAAAnR...Uc8eS6ka }yarncode
#         < ~^yarncode yes
#       > ~^yarncode .

# AVOW (dunbar) Publicly announce a new node and discover any GUID collision
#   Sample syntax:
#       > tttt~^{AVOW guid f7YE9pRj pubkey 8yG...6ka sig RFc..Iv2 }yarncode
#         < ~^yarncode no/err/mismatch { guid f7YE9pRj pubkey e4S...sNt }

# SEEK (dunbar) Discover whether a route exists through dunbar to a distant node
#   Sample syntax:
#       > tttt~^{SEEK to f7YE9pRj from d89SvkpG }yarncode
#         < ~^yarncode no/exhaust .
#       or< ~^yarncode yes .

# PUSH (dunbar) Send a payload of an inner clade through the TTT network
#   Sample syntax:
#       > tttt/3milmo ~^{PUSH to f7YE9pRj from d89SvkpG @${REMIT ...}inyarn }outyarn
#         < ~^inyarn yes { ... }

# ~^ PULL  (dunbar) Receive a payload through the TTT network

# ~^ SYNC  (dunbar) Verify your records match my records


# Queue a trivial wad for departure. That wad should reach the departure process and then be discarded.
# This verb is meant for diagnostic testing to verify local plumbing is in place..

    def noop(self, guid):
        _dunbar_send(guid, "~^ ** NOOP .")



    # def echo(self, ip6, port, message):
    #     sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    #     print('SENDING ['+ip6+']:'+str(port)+'    "'+message+'"')
    #     sock.sendto(message.encode("UTF-8"), (ip6, port))





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
