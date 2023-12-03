# TTTT root verbs

The Transitive Trust Topology Tunneler protocol functions at the Internet "application layer" and is designed to facilitate higher-level applications to be invented on top of the TTTT layer. To the Internet, TTTT and all of its higher-level applications are all just one protocol. To TTTT-aware software, the TTTT protocol is further subdivided into protocol "clades" which serve the needs of applications running on top of (or inside of) TTTT root-level wrappers. Think of application protocol clades as extra layers within the Internet's formal application layer that provide arbitrarily deep inner layers for more specific functionality that relies on the TTTT infrastructure to get its job done.

Infrastructure below the Internet application layer just sees TTTT traffic passing through. To TTTT-aware applications, there are inner (higher level) layers of meaning serving the needs of more specific TTTT applications. Such applications may use inner protocols nested arbitrarily deep. We call any branched subtree of the TTTT protocol a clade, which is understood to mean the set of all applications and associated protocols built on the infrastructure of that subtree of TTTT, including all known,unknown, or future applications to rely on that level of infrastructure.

By this terminology, the TTTT clade is at the root of all current and future TTTT protocols and applications. This clade is the entire tree of the TTTT protocol, including all its well-known, little-known, or abandoned inner applications. Think of TTTT as providing functionality to manage the basic plumbing-works of the transitive trust network of dunbar tunnels. This infrastructure then provides an arena for more specific *inner* (higher level) applications to do something interesting within that arena with more specialized functionality.

These inner applications include clades such as `ding` (Sideband message heraldry) and `3milmo` (Third Millennium Money) may themselves serve as infrastructure for even more specialized application clades (deeply nested protocols). In this way, any process that understands `TTTT` but not `TTTT/3milmo` can handle traffic at the root TTTT level; a process that understands `TTTT/3milmo` but not `TTTT/3milmo/my_awesome_clade` can operate at the 3milmo level without concerning itself with the more specialized and less widely supported inner meaning of my experimental extension of 3milmo. Think of clades as branches in a nested heirarchy of an inheritance tree, where more specific functionality branches out from (is built on top of and inherits from) a more basic set of functionality which that clade relies on to do its work.

The TTTT root clade allows us to see the global Internet (or any internet) as a graph of nodes connected in a transitive-trust topology. The global Internet is a graph (network) of hosts linked along dynamically adaptive routers into a global topology correlating to conveniently deployed communication links. That graph serves the need of getting arbitrary data from one device to some distant device by any means that gets that job done. We can think of the Internet as a *pysical graph* that is good at naively moving data around.

A TTTT network is a *logical graph* that uses the physical graph of the Internet to impose symantic meaning to its routing connections *(dunbar tunnels)* modeling actual trust levels of real human relationships. In this sense, a TTTT arena is technically a form of "social media" but a form of social media far different from the dysfunctional forms we are familiar with.

 as a graph whose topology is opaque to outsiders. Even insiders cannot directly see beyond a one-hop horizon.

router links along pragmatically convenient communication links. Where the global Internet is organized along 

application doing its own thing.

 designed to facilitate the implementa

* `NOOP` - Discard this jot upon arrival
* `ECHO` - Request a trivial dunbar reply
* `YARN` - Continue an ongoing conversation
* `OPEN` - Create a dunbar tunnel
* `INIT` - Refresh this tunnel's crpytography
* `SHUT` - Sever this tunnel
* `SYNC` - Compare liminal records; identify discrepency
* `WARN` - Announce a suspicious anomaly
* `TRIE` - Disambiguate a keystub
* `SEEK` - Explore for any path to an endpoint
* `PING` - Verify an endpoint is curretly live
* `SEND` - Send one freeform kilobyte to an endpoint
* `WEND` - Send an appjot to an endpoint along a sensible fray


## `NOOP`
### Call:
    no argument
### Return:
    never returns
### Function:
    Receiving node simply discards the jot

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




* `NOOP` - Do nothing: A jot that takes space in a wad but can be ignored upon arrival
* `ECHO` - Request a trivial reply: A jot that asks a dunbar to demonstrate cryptograpic presence
* `YARN` - Continue a conversation that has previously been initiated, for a back-and-forth sequence
* `OPEN` - Notify a xenode that you have designated it as an incoming dunbar. Implied invitation to reciprocate
* `SHUT` - Sever a dunbar relationship. Notify a dunbar it is now a xenode for future incoming wads
* `SYNC` - Refresh a dunbar tunnel. Request a dunbar re-negotiate a tunnel key and reset its wax records
* `BOOK` - Compare our records with the records of a dunbar node to identify any hidden discrepencies
* `TTLS` - TTTT Transport Layer Security. Perform handshake and open a socket with a xenode
* `WARN` - Give notification of a potentially dangerous anomaly discovered in traffic
* `TRIE` - Given a stub, query a dunbar for a priveleged addr12 and a sample of extensions
* `SEEK` - Given a stub, attempt to discover a TTTT path to a matching node, and that node's key
* `PING` - Given a recent path, verify the distant endpoint is currently responsive and controls that key
* `SEND` - Given a recent path, send a one-time one-way TTTT 1KB end-to-end encrypted data payload
* `WEND` - Given a recent path, explore a fray appropriate to a given higher-level apcode's needs










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
