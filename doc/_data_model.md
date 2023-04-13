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



---- Cypher for Neo4j development sample graph reset all data and create graph
MATCH (n) DETACH DELETE n;

CREATE

(a:HERE { pubkey:"AAAAAA_AAAAAA_AAAAAA_AAAAAA_AAAAAA_AAAAAA_AAAAAA_AAAAAA" , stublen:1 }),
(b:HERE { pubkey:"BBBBBB_BBBBBB_BBBBBB_BBBBBB_BBBBBB_BBBBBB_BBBBBB_BBBBBB" , stublen:1 }),
(c:HERE { pubkey:"CCCCCC_CCCCCC_CCCCCC_CCCCCC_CCCCCC_CCCCCC_CCCCCC_CCCCCC" , stublen:1 }),
(d:HERE { pubkey:"DDDDDD_DDDDDD_DDDDDD_DDDDDD_DDDDDD_DDDDDD_DDDDDD_DDDDDD" , stublen:1 }),
(e:HERE { pubkey:"EEEEEE_EEEEEE_EEEEEE_EEEEEE_EEEEEE_EEEEEE_EEEEEE_EEEEEE" , stublen:1 }),
(f:HERE { pubkey:"FFFFFF_FFFFFF_FFFFFF_FFFFFF_FFFFFF_FFFFFF_FFFFFF_FFFFFF" , stublen:1 }),
(g:HERE { pubkey:"GGGGGG_GGGGGG_GGGGGG_GGGGGG_GGGGGG_GGGGGG_GGGGGG_GGGGGG" , stublen:1 }),
(h:HERE { pubkey:"HHHHHH_HHHHHH_HHHHHH_HHHHHH_HHHHHH_HHHHHH_HHHHHH_HHHHHH" , stublen:1 }),

(j:NEAR { pubkey:"JJJJJJ_JJJJJJ_JJJJJJ_JJJJJJ_JJJJJJ_JJJJJJ_JJJJJJ_JJJJJJ" , stublen:1 }),
(k:NEAR { pubkey:"KKKKKK_KKKKKK_KKKKKK_KKKKKK_KKKKKK_KKKKKK_KKKKKK_KKKKKK" , stublen:1 }),
(m:NEAR { pubkey:"LLLLLL_LLLLLL_LLLLLL_LLLLLL_LLLLLL_LLLLLL_LLLLLL_LLLLLL" , stublen:1 }),
(n:NEAR { pubkey:"MMMMMM_MMMMMM_MMMMMM_MMMMMM_MMMMMM_MMMMMM_MMMMMM_MMMMMM" , stublen:1 }),
(p:NEAR { pubkey:"NNNNNN_NNNNNN_NNNNNN_NNNNNN_NNNNNN_NNNNNN_NNNNNN_NNNNNN" , stublen:1 }),
(q:NEAR { pubkey:"QQQQQQ_QQQQQQ_QQQQQQ_QQQQQQ_QQQQQQ_QQQQQQ_QQQQQQ_QQQQQQ" , stublen:1 }),
(r:NEAR { pubkey:"RRRRRR_RRRRRR_RRRRRR_RRRRRR_RRRRRR_RRRRRR_RRRRRR_RRRRRR" , stublen:1 }),

(t:FAR  { pubkey:"LLLLLL_LLLLLL_LLLLLL_LLLLLL_LLLLLL_LLLLLL_LLLLLL_LLLLLL" , stublen:1 }),
(v:FAR  { pubkey:"MMMMMM_MMMMMM_MMMMMM_MMMMMM_MMMMMM_MMMMMM_MMMMMM_MMMMMM" , stublen:1 }),
(w:FAR  { pubkey:"NNNNNN_NNNNNN_NNNNNN_NNNNNN_NNNNNN_NNNNNN_NNNNNN_NNNNNN" , stublen:1 }),
(x:FAR  { pubkey:"QQQQQQ_QQQQQQ_QQQQQQ_QQQQQQ_QQQQQQ_QQQQQQ_QQQQQQ_QQQQQQ" , stublen:1 }),
(y:FAR  { pubkey:"RRRRRR_RRRRRR_RRRRRR_RRRRRR_RRRRRR_RRRRRR_RRRRRR_RRRRRR" , stublen:1 }),

(a) -[:M3M  { lim:0    , bal:-12 }]-> (b) <-[:M3M  { lim:50   , bal:+12 }]- (a),
(a) -[:DING { wid:200  , cost:1  }]-> (b) <-[:DING { wid:100  , cost:2  }]- (a),

(a) -[:M3M  { lim:100000 , bal:+88461 }]-> (d) <-[:M3M  { lim:300000 , bal:-88461 }]- (a),
(a) -[:DING { wid:200 , cost:1        }]-> (d) <-[:DING { wid:750 , cost:3        }]- (a);
