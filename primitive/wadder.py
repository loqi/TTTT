# When any TTTT wad arrives, that encrypted message is delegated to this module.

# Here, it gets authenticated, then decrypted, then priority-queued for later action.
# At some slightly later time, entries in that queue will be evaluated by tttt_triage_d
# where pending reqests are handled.

# Dunbar wad format (dunwad):
# 8     wax     - int64 identifying tunnel stamp (occasionally ambiguous)
# 8     seal    - int64 vandalism reveal hash
# ---             encryyted below via tunkey
#   1   len     - length of jot in 4-octet segs, 00 is one-byte NOOP code. 01 is null canvas.
#   1   vim     - offered reward for servicing this jot
#   1   lag     - declaration of urgency: low means fast; 255 means super slow
#   1   verb    - opcode: NOOP CARD YARN ANTE WARN HINT SYNC BOOK TRIE SEEK PING SEND WEND OPEN SHUT
#   ?   canvas  - varies in length (4 octet increments) by verb
# repeat arbitrarily many jot sequences, not to exceed total length 1280 octets.
#
# Xenode wad format (xewad):
# --- the whole thing is encrypted by recipient's public key
# 32    from    - full public key of sender node
# 8     seal    - signed by sender's private key
#   1   len
#   1   vim
#   1   lag
#   1   verb    - opcode: NOOP CARD YARN ANTE WARN HINT SEND
#   ?   canvas
# repeat arbitrarily many jot sequences, not to exceed total length 1280 octets.
 
class Wadder:

    # WEND 34 110 d7B5rV 3milmo{PUSH 89.381 fare 0.231 need 0.102 } binaryEncryptedData...
    def compile(plain): # Given a string of plaintext, create the appropriate wad for sending
        wad = b""
        return wad

    def decompile(wad): # Given a wad of any format as received, convert it to plaintext string
        plain = bytes.fromhex(wad)
        return plain