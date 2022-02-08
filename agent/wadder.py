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
#   to/from a xenode:
#        8 - format descriptor and arguments
#               1 - version 0001.... - TTTT version 1
#               1 - format  0000.... - means public key traffic
#               6 - undefined bytes
#        8 - signature by sender - demonstrates control of public key. Reveals real-time content tampering
#       32 - sender's public key derives to gSid and guid - serves as both TTT address and encryption
#      208 - message payload encrypted in Curve25519 elliptic curve 256-bit public key (compressed, encrypted, padded)
#       (0..8)*128 - extended payload
#
#   to/from a dunbar:
#         8 - format descriptor
#               1 - version 0001.... - TTTT version 1
#               1 - format  0001.... - means dunbar tunnel traffic
#               6 - GUID identifying dunbar node
#         8 - 64-bit HMAC authenticating sender
#       240 - message payload encrypted by dunbar tunnel AES symetric-key cypher
#       (0..8)*128 - extended payload
