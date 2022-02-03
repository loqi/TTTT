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
#   to/from a dunbar:
#         2 - format descriptor
#               1 - version 00......
#               1 - format  00..00..
#         6 - GUID
#        16 - HMAC
#       104 - payload
#       72  - data payload
#       (0..9)*128 - extended payload
#
#   to/from a stranger:
#        8 - format descriptor and arguments
#               1 - version 00......
#               1 - format  00..01..
#       16 - cryptographic signature
#       32 - sender's public key
#       72 - data payload
#       (0..9)*128 - extended payload
