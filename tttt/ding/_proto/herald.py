
    def noop(self, guid):
        _dunbar_send(guid, "~^ ** NOOP .")



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
