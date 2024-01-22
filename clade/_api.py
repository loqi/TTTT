class Tttt:
    # wad   = ""    # received datagram: serialized, compressed, encrypted, padded, +hmac, +guid 
    # guid  = ""    # sender node excised from `wad` - could be a dunbar or stranger
    # hmac  = ""    # HMAC excised from `wad`
    # plain = ""    # plaintext decrypted from `wad`
    # nib:  = ""    # nib code parsed from `plain`
    # yarn  = ""    # yarn code parsed from `plain`
    # verb  = ""    # request verb parsed from `plain`
    # arg__parm = {}    # "argument keyed by parameter name" dict. `pos` key has array populated by positionals.

    def Tttt(wad): # Constructor
        # wad must be exactly length (128 * 2..10) otherwise return length error (maybe)
        self.guid   = wad[-8:]
        self.hmac   = wad[-136:-8]
        self.cypher = wad[:-136]
        self.plain  = plain__cypher(self.guid, self.cypher)
        self.nib    =   regex match  r"{\s*{~^\S*}\s+}"
        self.yarn   =   r"{\s+{~^\S+}\s+}"
        self.verb   =   r""
        self.pos    = []
        self.arg__parm = {}
        return self

# "~^@$ PUSH to uR6vFL92 nav [ rir6W7eN GpY+Bzc6 LpR20sVu qQHz1w7P ] re DyfGOz5J @$ REMIT 12.280 fare 0.281 need 0.186"



# TtttRequest object =
#       { verb:  "PUSH"
#       , sum:  12280
#       , to:   "uR6vFL92"
#       , from: "G7zR+Ftx"
#       , fare: 0.281
#       , need: 0.186
#       , nav:  [ "rir6W7eN", "GpY+Bzc6", "LpR20sVu", "qQHz1w7P" ]
#       }



    def wad__obj():
        ret = ""
        # Return wad ( ) from TtttRequest
        return ret

    def guid():
        # Read from wad

# recurse into clade subdirectories and import them into this.




# request = tttt.unpack(udp, ip6, datagram)
# "~^@$ PUSH @$ 12.280 @$b8F6sG to uR6vFL92 via [ rir6W7eN GpY+Bzc6 LpR20sVu qQHz1w7P ] from G7zR+Ftx fare 0.281 need 0.186"
# TtttRequest object =
#       { verb:  "PUSH"
#       , sum:  12.280
#       , of:   "kudos"
#       , to:   "uR6vFL92"
#       , from: "G7zR+Ftx"
#       , fare: 0.281
#       , need: 0.186
#       , via:  [ "rir6W7eN", "GpY+Bzc6", "LpR20sVu", "qQHz1w7P" ]
#       }
