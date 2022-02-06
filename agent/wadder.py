# When any TTTT request arrives to Agent0, that encrypted message is delegated to this module.

# Here, it gets authenticated, then decrypted, then queued for later action. At some slightly later time, entries in
# that queue will be evaluated by tttt_triage_d where pending reqests are handled according to priority.

class Wadder:
    agent = Agent();

    # guid
    # gSid
    # ip6
    # port
    # pubk
    # name

    def wad__plain(plain): # Given a string of plaintext, create the appropriate wad for sending
        wad = b""
        return wad

    def plain__wad(wad): # Given a wad of any format as received, convert it to plaintext string
        plain = ""
        return plain

# Wad formats:
#
#   to/from a stranger:
#        8 - format descriptor and arguments
#               1 - version 0001....
#               1 - format  0000....
#               6 - GIUD (must match public key)
#       16 - signature by sender - demonstratos control of public key and reveals content tampering
#       32 - sender's public key derives to gSid and guid - serves as both TTT address and encryption
#       72 - message payload
#       (0..9)*128 - extended payload
#
#   to/from a dunbar:
#         2 - format descriptor
#               1 - version 0001....
#               1 - format  0001.... - means dunbar tunnel traffic
#         6 - GUID
#       128 - message payload encrypted by dunbar tunnel symetric cypher
#       (0..9)*128 - extended payload
