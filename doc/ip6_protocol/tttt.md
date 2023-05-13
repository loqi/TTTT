# TTTT root verbs

The Transitive Trust Topology Tunneler protocol functions at the Internet *application layer* and is designed to facilitate higher-level applications to be innovated on top of the TTTT layer.

A TTTT arena is a graph whose topology is opaque to outsiders. Not even insiders can directly see beyond a one-hop horizon. This one-hop vilibility horizon comprises a node's *ambit,* inside which the controlling human *owner* is free to operate as an despotic ruler. Anyone is free to carefully build or carelessly squander the trust previously accrued by any or all of their nodes according to the current opinion of their dunbar nodes.

To the Internet, TTTT and all of its higher-level applications are all just one protocol. To TTTT-aware software, the TTTT protocol is further subdivided into protocol "clades" which serve the needs of applications running on top of (or inside of) TTTT root-level wrappers. Think of application protocol clades as extra layers within the Internet's formal application layer to provide additional layers of application protocol for more specific functionality that relies on the TTTT infrastructure to get its job done.

Infrastructure below the Internet application layer just sees TTTT traffic passing through. To TTTT-aware applications, there are inner (higher level) layers of meaning serving the needs of more specific TTTT applications. Such applications may use inner protocols nested arbitrarily deep. We call any branched subtree of the TTTT protocol a clade, which is understood to mean the set of all applications and associated protocols built on the infrastructure of that subtree of TTTT, including all known,unknown, or future applications to rely on that level of infrastructure.

A note on nomenclature: in engineering, we often use the term "low level" to denote "close to the metal" and "high level" to mean more abstract thought, bigger actions with less attention to fiddly details. We use the term "subclass" to mean a more specific version of a concept. We say a subset has some of the members of a set, which could be thought of as a "more specific version" of the bigger set. A protocol clade can be said to be "inside" a more general clade, just as a branch of a tree is just part of the whole tree. Sometimes the metaphors clash, since nested brackets are "lower level" details in a mathematical expression. An inner protocol clade is a higher-level protocol, because the lower level protocol delivers it, just as a bag of mail is a lower-level way of delivering mail on trucks between cities, while an individually addressed letter is a higher-level way of delivering mail to a specific person.

By this terminology, the TTTT clade is at the root of all current and future TTTT protocols and applications. This clade is the entire tree of the TTTT protocol, including all its well-known, little-known, or abandoned inner applications. Think of TTTT as providing functionality to manage the basic plumbing-works of the transitive trust network of dunbar tunnels. This infrastructure then provides an arena for more specific *inner* (higher level) applications to do something interesting within that arena with more specialized functionality.

These inner applications include clades such as `ding` (Sideband message heraldry) and `3milmo` (Third Millennium Money) may themselves serve as infrastructure for even more specialized application clades (deeply nested protocols). In this way, any process that understands `TTTT` but not `TTTT/3milmo` can handle traffic at the root TTTT level; a process that understands `TTTT/3milmo` but not `TTTT/3milmo/my_awesome_clade` can operate at the 3milmo level without concerning itself with the more specialized and less widely supported inner meaning of my experimental extension of 3milmo. Think of clades as branches in a nested heirarchy of an inheritance tree, where more specific functionality branches out from (is built on top of and inherits from) a more basic set of functionality which that clade relies on to do its work.

## TTTT verbs

* `NOOP` - A jot meant to be sent and discarded
* `ECHO` - Ask a dunbar for a trivial tunnel reply
* `OPEN` - Create a dunbar tunnel
* `INIT` - Refresh this tunnel's crpytography
* `WARN` - Announce a suspicious anomaly
* `SHUT` - Sever this tunnel
* `SYNC` - Compare liminal records; identify discrepency
* `TRIE` - Disambiguate a keystub
* `SEEK` - Explore for any path to an endpoint
* `PING` - Verify an endpoint is curretly live
* `SEND` - Send one freeform kilobyte to an endpoint
* `WEND` - Send an appjot to an endpoint along a sensible fray
* `YARN` - Continue an ongoing conversation

-----

### `NOOP` expected action
    The receiving agent simply discards the jot
#### `NOOP` source texjot
    tttt/NOOP;
#### `NOOP` binjot equivalent
    1 verb  00h means tttt/NOOP; - smallest possible actionable jot
#### `NOOP` an initiating texjot may carry a pad
    tttt/NOOP "This string is to be discarded." ;
#### `NOOP` binjot equivalent
    1 verb  01h means long-form NOOP
    1 vim   00h customary to offer no vim credit for a NOOP
    1 lag   00h no reply is expected so lag can be anything
    1 len   00h means "" padding string, 01h means four bytes, etc.
    * pad   "This string is to be discarded.\0"
#### `NOOP` reply
    (there is never a reply to a NOOP action)

-----

### `ECHO` purpose
    The initiator asks its dunbar to send an ECHO reply. This is a way of confirming the attentiveness of the agent, verifying both sides of the cryptographic tunnel, and obfuscating traffic patterns against eavesdroppers by introducing additional activity.
#### `ECHO` parameters (initiating)
    1. vim    typically 1 vim credit is offered for an ECHO
    2. lag    the lag rating describing turnaround time expectation
    3. cargo  optional bytes to be echoed back in return tunnel
#### `ECHO` outgoing source texjot (initiating)
    tttt/ECHO 1 40 "This is a text of the emergent habitrail system." ;
#### `ECHO` outgoing compiled binjot (initiating)
    1 verb   02h means tttt/ECHO
    1 vim    01h customary to offer one vim credit for an ECHO reply
    1 lag    40h (see lag discussion)
    1 len    0Ch cargo is 48 bytes long (12 four-byte words)
    * cargo  "This is a text of the emergent habitrail system."
#### `ECHO` outgoing source texjot (replying)
    tttt\ECHO 1 31 yArNr6_LDX7m1
        cargo "This is a text of the emergent habitrail system."
        ;echo
#### `ECHO` outgoing compiled binjot (replying)
    1 verb   03h means tttt\ECHO
    1 vim_   01h customary to accept that one vim credit
    1 lag_   1Fh indicates the time elapsed at the send of reply
    1 len    02h means nothing more than yarn code is provided
    8 yarn   Yarn code to associate reply with conversation
    * cargo  "This is a text of the emergent habitrail system."

-----

### `OPEN` purpose
    Notify a xenode that the initiator now considers it to be a dunbar. That is, the initiating node has declared its willingness to service incoming wads from the recipient of this OPEN action via a new one-way dunbar tunnel created by the initiator.
#### `OPEN` parameters (initiating)
    1. vim     typically 01h to indicate one vim credit
    2. lag     see lag notes
    3. to32    full 32-byte public key address of initiating node
    4. tunn32  initial 32-byte symetric tunnel key
    5. greet   human-readable greeting message
#### `OPEN` source texjot (initiating)
    tttt/OPEN 1 160
        to32 D2Xe1N_01hJ2K_..._Q5Vm0t_EN8ytT
        tunn32 A5LX4C_9U7HWQ_..._R9ym3F_01hJ2K
        greet "Hi Alice, it's Bob from the class reunion."
        ;open
#### `OPEN` equivalent compiled binjot (initiating)
     1 verb    12h means tttt/OPEN
     1 vim     00h customary to offer no vim credit for an OPEN
     1 lag     40h this can expect a long or short delay for reply
     1 len     15h means only tunn32 and to32 are provided, no greet
    32 tunn32  32-byte symetric tunnel key
    32 to32    32-byte initiating node
       greet   "Hi Alice, it's Bob from the class reunion.\0\0"
#### `OPEN` texjot reply
    tttt\OPEN 1 138 YArNm7_Ke9MRJ ;
#### `OPEN` equivalent decompiled texjot from incoming binjot (replying)
     1 verb   13h means tttt\OPEN
     1 vim_   01h customary to accept that one vim credit
     1 lag_   8Ah indicates the time elapsed at the send of reply
     1 len    02h yarn code is 8 bytes, so len is 2
     8 yarn   Yarn code to associate reply with conversation

-----

### `SHUT` action
    Notify a dunbar that it is now a xenode of the initiator. That is, the initiating node has already decided it will no longer be servicing incoming wads via this tunnel, and is notifying the other node of this status. After a SHUT action is initiated, the tunnel will usually accept a SHUT reply within the `lag` limit, but otherwise that tunnel is closed to further traffic.
#### `SHUT` initiating parameters
    1. vim   01h customary vim value for a SHUT action
    2. lag   FFh customary lag value for a SHUT action
    3. bye   human-readable goodbye message
#### `SHUT` initiating texjot example
    tttt/SHUT 255 255 "I may have been hacked!" ;
#### `SHUT` initiating binjot
    1 verb  10h means tttt/SHUT
    1 vim   01h customary to offer no vim credit for a SHUT
    1 lag      - 40h this can expect a long or short delay for reply
    1 len      - 10h means only tunn32 and to32 are provided, no greet
      bye      - character array of goodbye message
#### `SHUT` texjot reply example
    tttt<<SHUT 1 138 YArNm7_Ke9MRJ ;shut
#### `OPEN` binjot reply
     1 verb     - 11h means tttt<<SHUT
     1 vim      - 01h customary to accept that one vim credit
     1 lag      - 8Ah indicates the time elapsed at the send of reply
     1 len      - 02h 
     8 yarn     - Yarn code to associate reply with conversation

-----






### `SEEK` purpose
    Ask a dunbar to explore for any path to any xenode matching a stub.
#### `SEEK` source texjot (initiating)
    tttt/SEEK 60 50
        to12 YYYYYY_YYYYYY_YYYYYY
        nav [
            WWWWWW_WWWWWW_WWWWWW
            TTTTTT_TTTTTT_TTTTTT
            PPPPPP_PPPPPP_PPPPPP
            MMMMMM_MMMMMM_MMMMMM
            ]
        via [ AAAAAA_AAAAAA_AAAAAA ]
        ;seek
#### `SEEK` compiled binjot (initiating)
    2 len     0000h
    1 verb    24h means tttt/SEEK
    1 vim     3Ch customary to offer no vim credit for an OPEN
    1 lag     32h this can expect a long or short delay for reply
    1 navlen  Length of nav array   
      [ nav ] Array of 12-byte addresses
    1 vialen  Length of via array
      [ via ] Array of 12-byte addresses
#### `SEEK` texjot reply
    tttt\SEEK 33 47 yARN0t_VQ2eLP
        to32 YYYYYY_YYYYYY_YYYYYY_..._YYYYYY
        via [ AAAAAA_AAAAAA_AAAAAA
              BBBBBB_BBBBBB_BBBBBB
              EEEEEE_EEEEEE_EEEEEE
              HHHHHH_HHHHHH_HHHHHH
              MMMMMM_MMMMMM_MMMMMM
              WWWWWW_WWWWWW_WWWWWW
            ]
        ;seek
#### `SEEK` equivalent decompiled texjot from incoming binjot (replying)
      2 len    00__h yarn code is 8 bytes, so len is 2
      1 verb   25h means tttt\SEEK
      1 adverb
      1 vim_
      1 lag_
      8 yarn   Yarn code to associate reply with conversation
     32 key
      1 vialen
        via

-----

### `PING` purpose
    Given a recent path and a destination key, ask a dunbar to forward PING to that destination node. The destination node is expected to demonstrate presence by originating a PING reply.
#### `PING` source texjot (initiating)
    tttt/PING 60 30
        to32 YYYYYY_YYYYYY_YYYYYY_..._YYYYYY
        crypt "icUCrd22nuS2Ski8di73xHJbi"
        ;ping
#### `PING` compiled binjot (initiating)
     1 verb    26h means tttt/PING
     1 vim    
     1 lag    
     1 len     in 4-byte words
    32 to32    destination node being pinged
       crypt   (binary encrypted string)
#### `PING` texjot reply
    tttt\PING 43 22 YarmNP_XK8Mr5
        crypt "base64stringInReply..." 
        ;ping
#### `PING` equivalent decompiled texjot from incoming binjot (replying)
    2 len    00__h yarn code is 8 bytes, so len is 2
    1 verb   27h means tttt\PING
    1 vim_
    1 lag_
    8 yarn   Yarn code to associate reply with conversation
    1 pong   1 means node at to32 is requesting a counter-ping
    1 cryptlen
      crypt
    1 vialen
      via    array of 12-byte addresses

-----
* `SEND` - Send one freeform kilobyte to an endpoint
* `SEND` - Given a recent path, send a one-time one-way TTTT 1KB end-to-end encrypted data payload

* `WEND` - Send an appjot to an endpoint along a sensible fray
* `WEND` - Given a recent path, explore a fray appropriate to a given higher-level apcode's needs
-----

### `WEND` purpose
    Ask a dunbar to forward an inner protocol's cargo jot to that destination node. The intervening nodes along the path are expected to make some effort to deviate from the original path, thus discovering a possibly better fray capable of delivering at a lower cost or more throughput according to the needs of the inner protocol.
#### `WEND` source texjot (initiating)
    tttt/WEND 80 60
        to32 YYYYYY_YYYYYY_YYYYYY_..._YYYYYY
        cargo tttt/3milmo/PUSH
            net 100.0
            plus 0.8425
            fare 0.1575
            crypt "base64{ re XYAB42_r65MKa memo "blablabla" }"
            ;push
        crypt "icUCrd22nuS2Ski8di73xHJbi"
        ;wend
#### `WEND` compiled binjot (initiating)
     1 verb      30h means tttt/WEND
     1 vim       80
     1 lag       60
     1 len       in 4-byte words
    32 to32      destination node
     0 cargo
         2 verb    0308h means 3milmo/PUSH
         1 len     length of inner binjot in 4-byte words
         4 net
         4 plus
         4 fare
           crypt   string in binary
       crypt   (binary encrypted string)
#### `WEND` texjot reply
    tttt\WEND 49 51 yArNVC_1UQ6rt
        inner 3milmo\PUSH
            net 88.541
            fare 0.4415
            ;push
        ;wend
#### `WEND` equivalent decompiled texjot from incoming binjot (replying)
    1 verb     31h means tttt\WEND
    1 vim_
    1 lag_
    1 len 
    8 yarn     Yarn code to associate reply with conversation
    2 inproto  03h means 3milmo
    1 inverb   09h means 3milmo\PUSH
    1 inlen
    4 net_
    4 fare_




* `WARN` - Announce a suspicious anomaly
* `WARN` - Give notification of a potentially dangerous anomaly discovered in traffic

* `SHUT` - Sever this tunnel
* `SHUT` - Sever a dunbar relationship. Notify a dunbar it is now a xenode for future incoming wads

* `INIT` - Refresh this tunnel's crpytography

* `SYNC` - Refresh a dunbar tunnel. Request a dunbar re-negotiate a tunnel key and reset its wax records
* `SYNC` - Compare liminal records; identify discrepency

* `BOOK` - Compare our records with the records of a dunbar node to identify any hidden discrepencies

* `TTLS` - TTTT Transport Layer Security. Perform handshake and open a socket with a xenode

* `TRIE` - Given a stub, query a dunbar for a priveleged addr12 and a sample of extensions
* `TRIE` - Disambiguate a keystub

* `YARN` - Continue an ongoing conversation
* `YARN` - Continue a conversation that has previously been initiated, for a back-and-forth sequence












## `WEND`
### call:
    1.  [vim]       0..255 Offering of maximum service credit
    2.  [lag]       0..255 Expected return pace
    3.  [to]        stub sufficient to disambiguate destination node
        inner       Inner (higher-level) app request. Inner app is responsible to vary fray
### return:
    1.  [vim]       Vim credit claimed by tunnel partner (less than or equal to WEND vim)
    2.  [lag]       Lag time consumed by tunnel partner (not excessively more than WEND lag)
    3.  [yarn]      Yarn code to associate jot with the ongoing convesation
        reply       key-value literal of the app's inner reply
### usage:

#### texjot (jot source code) formulated by node AAA to send to node BBB:
    tttt>>WEND 41 68
        to      7GHXbr
        inner   3milmo>>PUSH
                    net 35.0
                    plus 0.425
                    crypt "kRaDHes9aueSE2ihx45baesLNxpPPbahd8iYh2"
                    >>push
        >>wend

#### binjot (jot compiled from above texjot) waits to join a wad enroute to BBB:

        1 len   - in 4-byte words
        1 verb  - 40h is tttt>>WEND
        1 vim   - 29h is hex of 41 vim offered by AAA
        1 lag   - 44h is hex of 68 of lag spec requested by AAA
       12 stub  - 7GHXbr_000000_000000
                  --- inner PUSH within WEND
        1 app   - 03h is the 3milmo clade
        1 verb  - 40h is 3milmo>>PUSH verb
        4 net   - spars32 of 35.0
        4 plus  - spars32 of 0.425
        4 fare  - spars32 of 0.0  
     1+28 crypt - byte string of crypt base64
        0 pad   - to get a 4-byte multiple

#### Sometime later, a binjot reply appears in a wad from the BBB:AAA IP6 tunnel

        1 len   - in 4-byte words
        1 verb  - 41h is tttt<<WEND
        8 yarn  - yarn code dfR52A_CCW3eK to construct conversation
        1 vim   - 22h is hex of 34 vim claimed by BBB
        1 lag   - 36h is hex of 54 of lag asserted by BBB
       12 addr  - 7GHXbr_LWP3NV_N0TaGR
                  --- inner PUSH within WEND
        1 app   - 03h is the 3milmo clade
        1 verb  - 41h is 3milmo<<PUSH verb
        4 net   - spars32 of 24.6281
        4 fare  - spars32 of 0.2265  
        2 pad   - to get a 4-byte multiple

#### texjot (jot source code) decompiled from the above binjot received from BBB:

    BBB:AAA tttt<<WEND 34 54 dfR52A_CCW3eK
                reply { net 24.6281 fare 0.2265 }
                hist [ { to 7GHXbr
                         inner { verb "3milmo>PUSH"
                                 net     35.0
                                 plus    0.425
                                 crypt   "kRaDHes9aueSE2ihx45baesLNxpPPbahd8i"
                                 } } ]
                tttt<<wend
