user            -- A user owns one or more domestic nodes
    id          int8
    uname       string24
    longname    string
    nodeC       int8        Number of here-nodes owned by this user

crypt           -- Secret key store for all domestic nodes
    here_id     int8
    kSECRET     byte32

<!-- ip6.db          -- IP6 endpoint pool translating logical address to physical
    id          int8        (0 indicates null set)
    poolS[]     byte16
    udpS[]      int2
    tcpS[]      int2 -->

here            -- A domestic node (a node represented by this agent)
    id          int8
    pubkey      byte32
    stublen     int1        Length of guid stub
    user_id     int8

near            -- A foreign node which is a dunbar of at least one domestic node
    id          int8
    pubkey      byte32
    stublen     int1
    ip6_id      int8

far             -- A xenode with previous traffic flowing through this agency
    id          int8
    pubkey      byte32
    stublen     int1
    ip6_id      int8
    ratingS[]   int8    App-indexed rating of reliability (0 indicates non-participating).

heretun           -- A dunbar tunnel between a pair of domestic nodes
    id          int8
    here_lo     int8
    here_hi     int8
    net_loS[]   int8    Each app has a limit. Net negative or zero means exhausted.
    net_hiS[]   int8    hi is trust of lo by hi; lo is trust of hi by lo.

neartun          -- A dunbar tunnel between a domestic and a foreign (border) node
    id          int8    
    here_id     int8
    near_id     int8
    net_hereS[] int8    Net remaining trust of the there-node by the here-node indexed by app
    ratingS[]   int8    App-indexed rating of reliability (0 indicates non-participating).
    key         byte32
