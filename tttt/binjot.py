"""
1   len                 00 NOOP  01..FD (*4 bytes)  FE (1024 bytes)  FF (to the end of the wad)
1   vim                 Credit offered for the node doing the job (or saying it tried reasonably hard)
1   vex                 (1.06^vim - 1 seconds) 0=fast  1=60ms  2=124ms  3=191ms  50=17.4sec  63=38.3sec  127=27min  191=19hour  255=33day
    verb    00 inline texjot
            01 clade:tttt
            02 clade:ding
            03 clade:3milmo
            04 clade:vouch
            05 clade:cred
            70..7F clade:user-defined
            80..FE clade:user-defined by two bytes

            0100 ECHO
            0101 EDGE
            0102 SYNC
            0103 WARN
            0104 CARD
            0113 TRIE
            0114 SEEK
            0115 PING
            0116 SEND
            0117 WEND
            017E YARN

            0210 ding/HAIL      -- Notify a xenode of incoming communication
            0211 ding/CITE      -- Give feedback about a HAIL level mismatch

            0310 3milmo/PUSH    -- Pay money to a xenode
            0311 3milmo/PULL    -- Draw money from a xenode
            0316 3milmo/BOND    -- Float an interest-bearing bond
    
            0320 vouch/AVOW     -- Relay an attestanion to a xenode
            0321 vouch/`        -- Express a greivence 

"""