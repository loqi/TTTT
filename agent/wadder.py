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

