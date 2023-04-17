# What is an agency or an agent?

The distinction between an agent and an agency is fairly arbitrary. They are technically
equivalent concepts: a software peer-server representing the interests of one or more users
who control their node(s) via a boss client interface. An agency is just an agent representing
more than one user's interests on the TTTT network. Either word is technically accurate to
describe TTTT network peer-server software at any scale, but if we want to emphasize that
a particular network agent provides service on behalf of a number of humans, we say agency.

## Graph data maintained by an agency to model the greater TTTT network topology

An agency maintains a simplified model of the global TTTT graph with three flavors of
node:

* An **endod** (endo-node) is a node formally represented by this agency.
* An **exod** (exo-node) is a foreign node with a direct TTTT link to an endod
* A **xenod** (xeno-node) is a foreign node without direct TTTT link to an endod

Any agency is responsible for keeping the "source of truth" of all endods it serves, of
all dunbar relationships between its endods and one another, and of all dunbar relationships
between its endods and exods (nodes managed by foreign agents that are dunbars of nodes
managed by this agent). Exod-exod and exod-xenod relationships are modeled in the local graph
database for efficient lane discovery, but in radically simplified form. For instance, there
are countless lanes in existence in the global TTTT network between any pair of xenodes, but
this knowledge is never needed for the duties performed by this agency, so such links are not
represented in the local graph database. Although real TTTT links in the global topology are
always two-way in the underlying protocol, this agency only records outbound exod-xenod links
in its internal representation of that topology because it is never called upon to find a
lane originating at, or passing through a xenod. The only place a xenod can appear in a lane
needed by this agency would be at the terminis.

Using a graph-oriented DBMS, the agency models its own fully up-to-date inner topology and
tries to remember an inferred, mostly accurate, simplified model of the relevant parts of the
global transitive trust topology. It authoritatively knows about its own endods and their links
to all their dunbars regardless of whether those dunbars are local or foreign to this agency.
Entirely intramural TTTT traffic takes place directly in the agency database along :DB links.
Border traffic (endod-exod and exod-endod) is mediated by actual TTTT jots over IP6 datagram.
Traffic between node pairs without at least one endod is entirely out of the view of this agency
and is assumed to eventually take place or be lost within a reasonable time interval.

The TTTT base relationships are modeled by three flavors of link at each intimacy distance:
* `:DB` (intramural) links are extremely low friction. Traffic is mediated within the database.
* `:TTTT` (border) links are mediated by actual TTTT traffic over IP datagrams.
* `:DARK` links are inferred to exist entirely out of view, as lanes of unknown length.

So link label `:DB` represents a TTTT dunbar link between two endods which can do its business
entirely within the graph database without need of generating IP datagrams. A link label `:TTTT`
represents a dunbar link between a foreign and domestic node, thus requiring IP datagrams or similar
means of cross-border communication with the foreign node's agent. A link label `:DARK` represents
a TTTT dunbar link or multi-hop lane with any number of intermediary nodes that somehow connects those
two foreign nodes.

Supra-TTTT application protocols use links labeled as their own app identifier regardless of intimacy
distance. Relationship identifiers such as `:DING` (message heraldry) `:M3M` (3milmo, or third millennium
money) and `:GAB` (codified gossip) appear at all intimacy distances: endod-endod (`:DB` at the base
level, endod-exod (`:TTTT` at base level), exod-exod (`:DARK`), or exod-xenod (`:DARK`) pairings. These
classes of node pairing each carry a different set of attributes appropriate to the role of an intramural,
border, or dark link. It is the responsibility of the query author to keep in mind which variant of link
exists at each intimacy distance. The database uses distinct variants of relationship label at the TTTT
(base) level as a documentation aid for us humans. When formulating a graph query for a generic TTTT lane,
we emphasize these three distinct intimacy distances with technically unneccessary, but cognitively useful
distinct relationship labels. For supra-TTTT application layers we dispense with distance-emphasizing link
labels and instead rely on our understanding that, for example, an exod-exod link is always dark, and an
endod-exod link is always crosses the border. Remember, each intimacy distance has a different set of state
attributes appropriate to that distance, despite having the same relationship label for protocols above the
TTTT level.

The optimal continuity lane from an enode to another enode is usually intramural, and can be rapidly queried.
However sometimes there exists a better lane that crosses the border. The basic strategy is for the agent to
query the graph database for a probably-optimal intramural solution and then occasionally try a promising
looking or even a randomly selected cross-border attempt to keep the agency's endods in meaningful competition
with exods. Each time a border-crossing lane is discovered to outperform an intramural lane, this is valuable
knowledge to be recorded for future performance gains.

The following invariants must be satisfied by the agency's simplified graph model of the TTTT network:
* An endod may be fully orphaned. Such a node cannot participate in dunbar operations of any kind.
* An endod may link another endod. This allows direct database operations without network friction.
* An endod may link an exod, representing a cross-border link needing dunbar wads over IP6 datagrams.
* An endod may **not** link a xenod. Such a link indicates that xenod is a miscategorized exod.
* An endod must only have two-way links. Each such link must be with an exod or another endod.
* An exod must always link at least one endod, otherwise that exod is a miscategorized xenod.
* An exod may link another exod. This implies a lane (compound path) has been inferred at least once.
* An exod may link **to** any number of xenods. We often need to discover a lane terminating at a xenod.
* An exod may **not** link **from** a xenod. We never need a lane with a xenod anywhere but the end.
* A xenod may **not** link another xenod. Any such link must be streamlined as xenod one hop **from** exod.

## Tabular data model

user            -- A user owns one or more endods
    id          int8
    uname       string24
    long_name   string
    nodeC       int8        Number of endods owned by this user

boss            -- Client software that commands a user agent via high-privelege dunbar TTTT link 
    id          int8
    user_id     int9
    ip6_pool_id int8

ip6_pool.db     -- IP6 endpoint pool translating logical address to physical
    id          int8        (0 indicates null set)
    poolS[]     byte16
    udpS[]      int2
    tcpS[]      int2 -->

enod.db         -- A node represented by this agency
    id          int8
    pubkey      byte32      Public key used to identify and cryptographically contact this node
    kSECRET     byte32      PRIVATE KEY needed to prove agency over node
    stublen     int1        Current length of regionally-unambiguous node address.
    stub_og     int1        Original `stublen` at enode inception.
    user_id     int8        User who owns this node.

exod.db         -- A foreign node which is a dunbar of at least one domestic node
    id          int8
    pubkey      byte32      Public key (guid & crypto) of this exod.
    stublen     int1        Current length of regionally-unambiguous exod address.
    stub_og     int1        Original `stublen` when exod was first inferred.
    ip6_pool_id int8        Contact information for IP6 datagram I/O.

xenode.db       -- A stranger node, not directly linked to an enode, inferred through traffic
    id          int8
    pubkey      byte32      Public key (guid & crypto) of this xenod.
    stublen     int1        Current length of regionally-unambiguous xenod address.
    og_lev      int1        Original `stublen` when xenod was first inferred. 
    ip6_pool_id int8        Contact information for IP6 datagram I/O.
    score__prot hashmap     Success score lookup by protocol.


---- Cypher for Neo4j development sample graph reset all data and create graph
```cypher
MATCH (n) DETACH DELETE n;
CREATE  ( endo_a:Endod { pubkey :"AAA45678901234567890123456789012"
                        , kSECRET:"a__45678901234567890123456789012" 
                        , stublen:1
                        , stub_og:1
                        , user_id:1
                        }
        )
    ,   ( endo_b:Endod { pubkey :"BBB45678901234567890123456789012"
                        , kSECRET:"b__45678901234567890123456789012"
                        , stublen:1
                        , stub_og:1
                        , user_id:1
                        }
        )
    ,   ( endo_c:Endod { pubkey :"CCC45678901234567890123456789012"
                        , kSECRET:"c__45678901234567890123456789012"
                        , stublen:1
                        , stub_og:1
                        , user_id:1
                        }
        )
    ,   ( endo_d:Endod { pubkey :"DDD45678901234567890123456789012"
                        , kSECRET:"d__45678901234567890123456789012"
                        , stublen:1
                        , stub_og:1
                        , user_id:1
                        }
        )
    ,   ( endo_e:Endod { pubkey :"EEE45678901234567890123456789012"
                        , kSECRET:"e__45678901234567890123456789012"
                        , stublen:1
                        , stub_og:1
                        , user_id:1
                        }
        )
    ,   ( endo_f:Endod { pubkey :"FFF45678901234567890123456789012"
                        , kSECRET:"f__45678901234567890123456789012"
                        , stublen:1
                        , stub_og:1
                        , user_id:1
                        }
        )
    ,   ( endo_g:Endod { pubkey :"GGG45678901234567890123456789012"
                        , kSECRET:"g__45678901234567890123456789012"
                        , stublen:1
                        , stub_og:1
                        , user_id:1
                        }
        )
    ,   ( endo_h:Endod { pubkey :"HHH45678901234567890123456789012"
                        , kSECRET:"h__45678901234567890123456789012"
                        , stublen:1
                        , stub_og:1
                        , user_id:1
                        }
        )
    
    
    ,   ( exo_j:Exod   { pubkey      :"JJJ45678901234567890123456789012"
                        , stublen    :1
                        , stub_og    :1
                        , ip6_pool_id:1
                        }
        )
    ,   ( exo_k:Exod   { pubkey      :"KKK45678901234567890123456789012"
                        , stublen    :1
                        , stub_og    :1
                        , ip6_pool_id:2
                        }
        )
    ,   ( exo_m:Exod   { pubkey      :"MMM45678901234567890123456789012"
                        , stublen    :1
                        , stub_og    :1
                        , ip6_pool_id:3
                        }
        )
    ,   ( exo_n:Exod   { pubkey      :"NNN45678901234567890123456789012"
                        , stublen    :1
                        , stub_og    :1
                        , ip6_pool_id:4
                     }
        )
    ,   ( exo_p:Exod   { pubkey      :"PPP45678901234567890123456789012"
                        , stublen    :1
                        , stub_og    :1
                        , ip6_pool_id:5
                        }
        )
    ,   ( exo_q:Exod   { pubkey      :"QQQ45678901234567890123456789012"
                        , stublen    :1
                        , stub_og    :1
                        , ip6_pool_id:6
                        }
        )
    ,   ( exo_r:Exod   { pubkey      :"RRR45678901234567890123456789012"
                        , stublen    :1
                        , stub_og    :1
                        , ip6_pool_id:7
                        }
        )
    ,   ( xeno_t:Xenod { pubkey     :"TTT45678901234567890123456789012"
                     , stublen    :1
                        , stub_og    :1
                        , ip6_addr_id:1
                        // , score__prot:{ tttt:381 , m3m:460 , ding:230 }
                        }
        )
    ,   ( xeno_v:Xenod { pubkey     :"VVV45678901234567890123456789012"
                        , stublen    :1
                        , stub_og    :1
                        , ip6_addr_id:2
                        // , score__prot:{ tttt:381 , m3m:460 , ding:230 }
                        }
        )
    ,   ( xeno_w:Xenod { pubkey     :"WWW45678901234567890123456789012"
                        , stublen    :1
                        , stub_og    :1
                        , ip6_addr_id:3
                        // , score__prot:{ tttt:381 , m3m:460 , ding:230 }
                        }
        )
    ,   ( xeno_x:Xenod { pubkey     :"XXX45678901234567890123456789012"
                        , stublen    :1
                        , stub_og    :1
                        , ip6_addr_id:4
                        // , score__prot:{ tttt:381 , m3m:460 , ding:230 }
                        }
        )
    ,   ( xeno_y:Xenod { pubkey     :"YYY45678901234567890123456789012"
                        , stublen    :1
                        , stub_og    :1
                        , ip6_addr_id:5
                        // , score__prot:{ tttt:381 , m3m:460 , ding:230 }
                        }
        )

    // There is no limit to endod-to-endod intramural communications at the base TTTT layer.
    // It all happens directly in the database, and requires no IP6 datagram traffic.
    , (endo_a) -[:DB]-> (endo_b) -[:DB]-> (endo_a)
    , (endo_b) -[:DB]-> (endo_c) -[:DB]-> (endo_b)
    , (endo_c) -[:DB]-> (endo_d) -[:DB]-> (endo_c)
    , (endo_d) -[:DB]-> (endo_e) -[:DB]-> (endo_d)
    , (endo_e) -[:DB]-> (endo_f) -[:DB]-> (endo_e)
    , (endo_f) -[:DB]-> (endo_a) -[:DB]-> (endo_f)
    , (endo_c) -[:DB]-> (endo_g) -[:DB]-> (endo_c)
    , (endo_g) -[:DB]-> (endo_h) -[:DB]-> (endo_g)

    , (exo_j) -[:TTTT{cap:10,net:0}]-> (endo_a) -[:TTTT{cap:10,net:0}]-> (exo_j)
    , (exo_k) -[:TTTT{cap:10,net:0}]-> (endo_a) -[:TTTT{cap:10,net:0}]-> (exo_k)
    , (exo_k) -[:TTTT{cap:10,net:0}]-> (endo_b) -[:TTTT{cap:10,net:0}]-> (exo_k)
    , (exo_m) -[:TTTT{cap:10,net:0}]-> (endo_b) -[:TTTT{cap:10,net:0}]-> (exo_m)
    , (exo_m) -[:TTTT{cap:10,net:0}]-> (endo_c) -[:TTTT{cap:10,net:0}]-> (exo_m)
    , (exo_n) -[:TTTT{cap:10,net:0}]-> (endo_c) -[:TTTT{cap:10,net:0}]-> (exo_n)
    , (exo_n) -[:TTTT{cap:10,net:0}]-> (endo_h) -[:TTTT{cap:10,net:0}]-> (exo_n)
    , (exo_p) -[:TTTT{cap:10,net:0}]-> (endo_h) -[:TTTT{cap:10,net:0}]-> (exo_p)
    , (exo_p) -[:TTTT{cap:10,net:0}]-> (endo_g) -[:TTTT{cap:10,net:0}]-> (exo_p)
    , (exo_q) -[:TTTT{cap:10,net:0}]-> (endo_e) -[:TTTT{cap:10,net:0}]-> (exo_q)
    , (exo_q) -[:TTTT{cap:10,net:0}]-> (endo_d) -[:TTTT{cap:10,net:0}]-> (exo_q)
    , (exo_r) -[:TTTT{cap:10,net:0}]-> (endo_e) -[:TTTT{cap:10,net:0}]-> (exo_r)

    , (exo_j) -[:DARK{rank:100}]-> (exo_k) -[:DARK{rank:130}]-> (exo_j)
    , (exo_k) -[:DARK{rank:200}]-> (exo_m) -[:DARK{rank:230}]-> (exo_k)
    , (exo_m) -[:DARK{rank:300}]-> (exo_n) -[:DARK{rank:330}]-> (exo_m)
    , (exo_n) -[:DARK{rank:400}]-> (exo_p) -[:DARK{rank:430}]-> (exo_n)
    , (exo_q) -[:DARK{rank:600}]-> (exo_r) -[:DARK{rank:630}]-> (exo_q)
    , (exo_r) -[:DARK{rank:700}]-> (exo_j) -[:DARK{rank:730}]-> (exo_r)

    , (exo_j) -[:DARK{rank:2000}]-> (xeno_t)
    , (exo_k) -[:DARK{rank:3000}]-> (xeno_t)
    , (exo_k) -[:DARK{rank:4000}]-> (xeno_v)
    , (exo_m) -[:DARK{rank:5000}]-> (xeno_v)
    , (exo_m) -[:DARK{rank:6000}]-> (xeno_w)
    , (exo_p) -[:DARK{rank:7000}]-> (xeno_w)
    , (exo_n) -[:DARK{rank:8000}]-> (xeno_x)
    , (exo_q) -[:DARK{rank:9000}]-> (xeno_x)
    , (exo_r) -[:DARK{rank:1500}]-> (xeno_y)
    , (exo_r) -[:DARK{rank:2500}]-> (xeno_t)


    // , (exo_m) -[:X_TTTT{score:312}]-> (xeno_t) -[:X_TTTT{score:220}]-> (exo_m)


    // , (endo_a) -[:M3M {att:0,lim:10,bal:0        }]-> (endo_b) -[:M3M {att:0,lim:50,bal:0}]-> (endo_a)
    // , (endo_a) -[:DING{ready:5,daily:10,zmax:9999}]-> (endo_b)
    // , (endo_a) -[:TTTT{cap:5,net:3               }]-> (endo_c) -[:TTTT{cap:20,net:-3             }]-> (endo_a)
    // , (endo_a) -[:M3M {att:0,lim:50,bal:-84      }]-> (endo_c) -[:M3M {att:0,lim:21,bal:84       }]-> (endo_a)
    // , (endo_a) -[:DING{ready:5,daily:10,zmax:9999}]-> (endo_c) -[:DING{ ready:0,daily:2,zmax:9999}]-> (endo_a)
    // , (endo_a) -[:TTTT{cap:3,net:2               }]-> (endo_e) -[:TTTT{cap:10,net:-2      }]-> (endo_a)
    // , (endo_a) -[:M3M {att:0,lim:25,bal:-27      }]-> (endo_e) -[:M3M {att:0,lim:99,bal:27}]-> (endo_a)
    // , (endo_a) -[:DING{ready:1,daily:10,zmax:9999}]-> (endo_e)
    // , (endo_a) -[:TTTT{cap:15,net:15      }]-> (endo_g) -[:TTTT{cap:20,net:-15            }]-> (endo_a)
    // , (endo_a) -[:M3M {att:0,lim:99,bal:95}]-> (endo_g) -[:M3M {att:0,lim:45,bal:-95      }]-> (endo_a)
    // ,                                          (endo_g) -[:DING{ready:2,daily:12,zmax:9999}]-> (endo_a)
    // , (endo_b) -[:TTTT{cap:5,net:3                     }]-> (endo_f) -[:TTTT{cap:20,net:-3                   }]-> (endo_b)
    // , (endo_b) -[:M3M {att:0,lim:50,bal:-84}]-> (endo_f) -[:M3M {att:0,lim:21,bal:84 }]-> (endo_b)
    // , (endo_b) -[:DING{ready:5,daily:10,zmax:9999      }]-> (endo_f) -[:DING{ ready:0,daily:2,zmax:9999      }]-> (endo_b)
    // , (endo_b)-[:TTTT{cap:3,net:2                     }]->(endo_g) -[:TTTT{cap:10,net:-2                  }]-> (endo_b)
    // , (endo_b)-[:M3M {att:0,lim:25,bal:-27}]->(endo_g) -[:M3M {att:0,lim:99,bal:27}]-> (endo_b)
    // ,                                                     (endo_g) -[:DING{ready:1,daily:10,zmax:9999     }]-> (endo_b)
    // , (endo_b)-[:TTTT{cap:15,net:15                   }]->(endo_h)-[:TTTT{cap:20,net:-15                  }]->(endo_b)
    // , (endo_b)-[:M3M {att:0,lim:99,bal:95 }]->(endo_h)-[:M3M {att:0,lim:45,bal:-95}]->(endo_b)
    // , (endo_b)-[:DING{ready:2,daily:12,zmax:9999      }]->(endo_h)
    // , (endo_c)-[:TTTT{cap:10,net:9                    }]->(endo_f)-[:TTTT{cap:10,net:-9                   }]->(endo_c)
    // , (endo_c)-[:M3M {att:0,lim:15,bal:-18}]->(endo_f)-[:M3M {att:0,lim:25,bal:-18}]->(endo_c)
    // , (endo_c)-[:DING{ready:5,daily:10,zmax:9999      }]->(endo_f)
    // , (endo_c)-[:TTTT{cap:15,net:15                   }]->(endo_h)-[:TTTT{cap:20,net:-15                  }]->(endo_c)
    // , (endo_c)-[:M3M {att:0,lim:99,bal:95 }]->(endo_h)-[:M3M {att:0,lim:45,bal:-95}]->(endo_c)
    // , (endo_c)-[:DING{ready:2,daily:12,zmax:9999      }]->(endo_h)
    // , (endo_d)-[:TTTT{cap:10,net:9                    }]->(endo_e)-[:TTTT{cap:10,net:-9                   }]->(endo_d)
    // , (endo_d)-[:M3M {att:0,lim:15,bal:-18}]->(endo_e)-[:M3M {att:0,lim:25,bal:-18}]->(endo_d)
    // , (endo_d)-[:DING{ready:5,daily:10,zmax:9999      }]->(endo_e)
    // , (endo_d)-[:TTTT{cap:15,net:15                   }]->(endo_f)-[:TTTT{cap:20,net:-15                  }]->(endo_d)
    // , (endo_d)-[:M3M {att:0,lim:99,bal:95 }]->(endo_f)-[:M3M {att:0,lim:45,bal:-95}]->(endo_d)
    // , (endo_d)-[:DING{ready:2,daily:12,zmax:9999      }]->(endo_f)
    // , (endo_e)-[:TTTT{cap:10,net:9                    }]->(endo_g)-[:TTTT{cap:10,net:-9                   }]->(endo_e)
    // , (endo_e)-[:M3M {att:0,lim:15,bal:-18}]->(endo_g)-[:M3M {att:0,lim:25,bal:-18}]->(endo_e)
    // , (endo_e)-[:DING{ready:5,daily:10,zmax:9999      }]->(endo_g)
    // , (endo_f)-[:TTTT{cap:15,net:15                   }]->(endo_g)-[:TTTT{cap:20,net:-15                  }]->(endo_f)
    // , (endo_f)-[:M3M {att:0,lim:99,bal:95 }]->(endo_g)-[:M3M {att:0,lim:45,bal:-95}]->(endo_f)
    // , (endo_f)-[:DING{ready:2,daily:12,zmax:9999      }]->(endo_g)
    // , (endo_f)-[:TTTT{cap:10,net:9                    }]->(endo_h)-[:TTTT{cap:10,net:-9                   }]->(endo_f)
    // , (endo_f)-[:M3M {att:0,lim:15,bal:-18}]->(endo_h)-[:M3M {att:0,lim:25,bal:-18}]->(endo_f)
    // , (endo_f)-[:DING{ready:5,daily:10,zmax:9999      }]->(endo_h)
    // , (endo_g)-[:TTTT{cap:15,net:15                   }]->(endo_h)-[:TTTT{cap:20,net:-15                  }]->(endo_g)
    // , (endo_g)-[:M3M {att:0,lim:99,bal:95 }]->(endo_h)-[:M3M {att:0,lim:45,bal:-95}]->(endo_g)
    // , (endo_g)-[:DING{ready:2,daily:12,zmax:9999      }]->(endo_h)
    // , (endo_a)-[:TTTT{cap:40,net:7                    }]->(exo_j)-[:TTTT{cap:40,net:-7                   }]->(endo_a)
    // , (endo_a)-[:M3M {att:0,lim:10,bal:0        }]->(exo_j)-[:M3M {att:0,lim:50,bal:0        }]->(endo_a)
    // , (endo_a)-[:DING{ready:5,daily:10,zmax:9999      }]->(exo_j)
    // , (endo_a)-[:TTTT{cap:40,net:7                  }]->(exo_k)-[:TTTT{cap:40,net:-7                 }]->(endo_a)
    // , (endo_a)-[:E_M3M {att:0,lim:10,bal:0      }]->(exo_k)-[:E_M3M {att:0,lim:50,bal:0      }]->(endo_a)
    // ,                                                      (exo_k)-[:E_DING{ready:5,daily:10,zmax:9999   }]->(endo_a)
    // , (endo_a)-[:TTTT{cap:40,net:7                  }]->(exo_n)-[:TTTT{cap:40,net:-7                 }]->(endo_a)
    // , (endo_a)-[:E_M3M {att:0,lim:10,bal:0      }]->(exo_n)-[:E_M3M {att:0,lim:50,bal:0      }]->(endo_a)
    // ,                                                     (exo_n)-[:E_DING{ready:5,daily:10,zmax:9999    }]->(endo_a)
    // , (endo_a)-[:TTTT{cap:40,net:7                  }]->(exo_r)-[:TTTT{cap:40,net:-7                 }]->(endo_a)
    // , (endo_a)-[:E_M3M {att:0,lim:10,bal:0      }]->(exo_r)-[:E_M3M {att:0,lim:50,bal:0      }]->(endo_a)
    // , (endo_a)-[:E_DING{ready:5,daily:10,zmax:9999    }]->(exo_r)
    // , (endo_b)-[:TTTT{cap:40,net:7                    }]->(exo_k)-[:TTTT{cap:40,net:-7                   }]->(endo_b)
    // , (endo_b)-[:M3M {att:0,lim:10,bal:0        }]->(exo_k)-[:M3M {att:0,lim:50,bal:0        }]->(endo_b)
    // , (endo_b)-[:DING{ready:5,daily:10,zmax:9999      }]->(exo_k)
    // , (endo_b)-[:TTTT{cap:40,net:7                    }]->(exo_m)-[:TTTT{cap:40,net:-7                   }]->(endo_b)
    // , (endo_b)-[:M3M {att:0,lim:10,bal:0        }]->(exo_m)-[:M3M {att:0,lim:50,bal:0        }]->(endo_b)
    // , (endo_b)-[:DING{ready:5,daily:10,zmax:9999      }]->(exo_m)
    // , (endo_b)-[:TTTT{cap:40,net:7                    }]->(exo_p)-[:TTTT{cap:40,net:-7                   }]->(endo_b)
    // , (endo_b)-[:M3M {att:0,lim:10,bal:0        }]->(exo_p)-[:M3M {att:0,lim:50,bal:0        }]->(endo_b)
    // , (endo_b)-[:DING{ready:5,daily:10,zmax:9999      }]->(exo_p)
    // , (endo_b)-[:TTTT{cap:40,net:7                    }]->(exo_q)-[:TTTT{cap:40,net:-7                   }]->(endo_b)
    // , (endo_b)-[:M3M {att:0,lim:10,bal:0        }]->(exo_q)-[:M3M {att:0,lim:50,bal:0        }]->(endo_b)
    // , (endo_b)-[:DING{ready:5,daily:10,zmax:9999      }]->(exo_q)
    // , (endo_c)-[:TTTT{cap:40,net:7                    }]->(exo_j)-[:TTTT{cap:40,net:-7                   }]->(endo_c)
    // , (endo_c)-[:M3M {att:0,lim:10,bal:0        }]->(exo_j)-[:M3M {att:0,lim:50,bal:0        }]->(endo_c)
    // , (endo_c)-[:DING{ready:5,daily:10,zmax:9999      }]->(exo_j)
    // , (endo_c)-[:TTTT{cap:40,net:7                    }]->(exo_p)-[:TTTT{cap:40,net:-7                   }]->(endo_c)
    // , (endo_c)-[:M3M {att:0,lim:10,bal:0        }]->(exo_p)-[:M3M {att:0,lim:50,bal:0        }]->(endo_c)
    // , (endo_c)-[:DING{ready:5,daily:10,zmax:9999      }]->(exo_p)
    // , (endo_c)-[:TTTT{cap:40,net:7                    }]->(exo_r)-[:TTTT{cap:40,net:-7                   }]->(endo_c)
    // , (endo_c)-[:M3M {att:0,lim:10,bal:0        }]->(exo_r)-[:M3M {att:0,lim:50,bal:0        }]->(endo_c)
    // , (endo_c)-[:DING{ready:5,daily:10,zmax:9999      }]->(exo_r)
    // , (endo_d)-[:TTTT{cap:40,net:7                    }]->(exo_j)-[:TTTT{cap:40,net:-7                   }]->(endo_d)
    // , (endo_d)-[:M3M {att:0,lim:10,bal:0        }]->(exo_j)-[:M3M {att:0,lim:50,bal:0        }]->(endo_d)
    // , (endo_d)-[:DING{ready:5,daily:10,zmax:9999      }]->(exo_j)
    // , (endo_d)-[:TTTT{cap:40,net:7                    }]->(exo_k)-[:TTTT{cap:40,net:-7                   }]->(endo_d)
    // , (endo_d)-[:M3M {att:0,lim:10,bal:0        }]->(exo_k)-[:M3M {att:0,lim:50,bal:0        }]->(endo_d)
    // , (endo_d)-[:DING{ready:5,daily:10,zmax:9999      }]->(exo_k)
    // , (endo_d)-[:TTTT{cap:40,net:7                    }]->(exo_n)-[:TTTT{cap:40,net:-7                   }]->(endo_d)
    // , (endo_d)-[:M3M {att:0,lim:10,bal:0        }]->(exo_n)-[:M3M {att:0,lim:50,bal:0        }]->(endo_d)
    // , (endo_d)-[:DING{ready:5,daily:10,zmax:9999      }]->(exo_n)
    // , (endo_d)-[:TTTT{cap:40,net:7                    }]->(exo_q)-[:TTTT{cap:40,net:-7                   }]->(endo_d)
    // , (endo_d)-[:M3M {att:0,lim:10,bal:0        }]->(exo_q)-[:M3M {att:0,lim:50,bal:0        }]->(endo_d)
    // , (endo_d)-[:DING{ready:5,daily:10,zmax:9999      }]->(exo_q)
    // , (endo_e)-[:TTTT{cap:40,net:7                    }]->(exo_p)-[:TTTT{cap:40,net:-7                   }]->(endo_e)
    // , (endo_e)-[:M3M {att:0,lim:10,bal:0        }]->(exo_p)-[:M3M {att:0,lim:50,bal:0        }]->(endo_e)
    // , (endo_e)-[:DING{ready:5,daily:10,zmax:9999      }]->(exo_p)
    // , (endo_e)-[:TTTT{cap:40,net:7                    }]->(exo_q)-[:TTTT{cap:40,net:-7                   }]->(endo_e)
    // , (endo_e)-[:M3M {att:0,lim:10,bal:0        }]->(exo_q)-[:M3M {att:0,lim:50,bal:0        }]->(endo_e)
    // , (endo_e)-[:DING{ready:5,daily:10,zmax:9999      }]->(exo_q)
    // , (endo_e)-[:TTTT{cap:40,net:7                    }]->(exo_r)-[:TTTT{cap:40,net:-7                   }]->(endo_e)
    // , (endo_e)-[:M3M {att:0,lim:10,bal:0        }]->(exo_r)-[:M3M {att:0,lim:50,bal:0        }]->(endo_e)
    // , (endo_e)-[:DING{ready:5,daily:10,zmax:9999      }]->(exo_r)
    // , (endo_f)-[:TTTT{cap:40,net:7                    }]->(exo_j)-[:TTTT{cap:40,net:-7                   }]->(endo_f)
    // , (endo_f)-[:M3M {att:0,lim:10,bal:0        }]->(exo_j)-[:M3M {att:0,lim:50,bal:0        }]->(endo_f)
    // , (endo_f)-[:DING{ready:5,daily:10,zmax:9999      }]->(exo_j)
    // , (endo_f)-[:TTTT{cap:40,net:7                    }]->(exo_k)-[:TTTT{cap:40,net:-7                   }]->(endo_f)
    // , (endo_f)-[:M3M {att:0,lim:10,bal:0        }]->(exo_k)-[:M3M {att:0,lim:50,bal:0        }]->(endo_f)
    // , (endo_f)-[:DING{ready:5,daily:10,zmax:9999      }]->(exo_k)
    // , (endo_f)-[:TTTT{cap:40,net:7                    }]->(exo_n)-[:TTTT{cap:40,net:-7                   }]->(endo_f)
    // , (endo_f)-[:M3M {att:0,lim:10,bal:0        }]->(exo_n)-[:M3M {att:0,lim:50,bal:0        }]->(endo_f)
    // , (endo_f)-[:DING{ready:5,daily:10,zmax:9999      }]->(exo_n)
    // , (endo_g)-[:TTTT{cap:40,net:7                    }]->(exo_m)-[:TTTT{cap:40,net:-7                   }]->(endo_g)
    // , (endo_g)-[:M3M {att:0,lim:10,bal:0        }]->(exo_m)-[:M3M {att:0,lim:50,bal:0        }]->(endo_g)
    // , (endo_g)-[:DING{ready:5,daily:10,zmax:9999      }]->(exo_m)
    // , (endo_g)-[:TTTT{cap:40,net:7                    }]->(exo_n)-[:TTTT{cap:40,net:-7                   }]->(endo_g)
    // , (endo_g)-[:M3M {att:0,lim:10,bal:0        }]->(exo_n)-[:M3M {att:0,lim:50,bal:0        }]->(endo_g)
    // , (endo_g)-[:DING{ready:5,daily:10,zmax:9999      }]->(exo_n)
    // , (endo_g)-[:TTTT{cap:40,net:7                    }]->(exo_p)-[:TTTT{cap:40,net:-7                   }]->(endo_g)
    // , (endo_g)-[:M3M {att:0,lim:10,bal:0        }]->(exo_p)-[:M3M {att:0,lim:50,bal:0        }]->(endo_g)
    // , (endo_g)-[:DING{ready:5,daily:10,zmax:9999      }]->(exo_p)
    // , (endo_h)-[:TTTT{cap:40,net:7                    }]->(exo_k)-[:TTTT{cap:40,net:-7                   }]->(endo_h)
    // , (endo_h)-[:M3M {att:0,lim:10,bal:0        }]->(exo_k)-[:M3M {att:0,lim:50,bal:0        }]->(endo_h)
    // , (endo_h)-[:DING{ready:5,daily:10,zmax:9999      }]->(exo_k)
    // , (endo_h)-[:TTTT{cap:40,net:7                    }]->(exo_m)-[:TTTT{cap:40,net:-7                   }]->(endo_h)
    // , (endo_h)-[:M3M {att:0,lim:10,bal:0        }]->(exo_m)-[:M3M {att:0,lim:50,bal:0        }]->(endo_h)
    // , (endo_h)-[:DING{ready:5,daily:10,zmax:9999      }]->(exo_m)
    // , (endo_h)-[:TTTT{cap:40,net:7                    }]->(exo_r)-[:TTTT{cap:40,net:-7                   }]->(endo_h)
    // , (endo_h)-[:M3M {att:0,lim:10,bal:0        }]->(exo_r)-[:M3M {att:0,lim:50,bal:0        }]->(endo_h)
    // , (endo_h)-[:DING{ready:5,daily:10,zmax:9999      }]->(exo_r)
    // , (endo_h)-[:TTTT{cap:40,net:7                    }]->(exo_k)-[:TTTT{cap:40,net:-7                   }]->(endo_h)
    // , (endo_h)-[:M3M {att:0,lim:10,bal:0        }]->(exo_k)-[:M3M {att:0,lim:50,bal:0        }]->(endo_h)
    // , (endo_h)-[:DING{ready:5,daily:10,zmax:9999      }]->(exo_k)
    // , (endo_h)-[:TTTT{cap:40,net:7                    }]->(exo_m)-[:TTTT{cap:40,net:-7                   }]->(endo_h)
    // , (endo_h)-[:M3M {att:0,lim:10,bal:0        }]->(exo_m)-[:M3M {att:0,lim:50,bal:0        }]->(endo_h)
    // , (endo_h)-[:DING{ready:5,daily:10,zmax:9999      }]->(exo_m)
    // , (endo_h)-[:TTTT{cap:40,net:7                    }]->(exo_r)-[:TTTT{cap:40,net:-7                   }]->(endo_h)
    // , (endo_h)-[:M3M {att:0,lim:10,bal:0        }]->(exo_r)-[:M3M {att:0,lim:50,bal:0        }]->(endo_h)
    // , (endo_h)-[:DING{ready:5,daily:10,zmax:9999      }]->(exo_r)
    // , (exo_j) -[:X_TTTT{score:312}]-> (xeno_t) -[:X_TTTT{score:220}]-> (exo_j)
    // , (exo_j) -[:X_M3M {score:520}]-> (xeno_t) -[:X_M3M {score:918}]-> (exo_j)
    // , (eko_j) -[:X_DING{score:712}]-> (xeno_t)
    // , (exo_j) -[:X_TTTT{score:140}]-> (xeno_w) -[:X_TTTT{score:520}]-> (exo_j)
    // , (exo_j) -[:X_M3M {score:390}]-> (xeno_w) -[:X_M3M {score:661}]-> (exo_j)
    // , (exo_j) -[:X_DING{score:720}]-> (xeno_w)
    // , (exo_j) -[:X_TTTT{scroe:119}]-> (xeno_x) -[:X_TTTT{score:498}]-> (exo_j)
    // , (exo_j) -[:X_M3M {score:477}]-> (xeno_x) -[:X_M3M {score:632}]-> (exo_j)
    // ,                                 (xeno_x) -[:X_DING{score:357}]-> (eko_j)
    // , (exo_k) -[:X_TTTT{score:312}]-> (xeno_v) -[:X_TTTT{score:220}]-> (exo_k)
    // , (exo_k) -[:X_M3M {score:520}]-> (xeno_v) -[:X_M3M {score:918}]-> (exo_k)
    // , (eko_k) -[:X_DING{score:712}]-> (xeno_v)
    // , (exo_k) -[:X_TTTT{score:140}]-> (xeno_w) -[:X_TTTT{score:520}]-> (exo_k)
    // , (exo_k) -[:X_M3M {score:390}]-> (xeno_w) -[:X_M3M {score:661}]-> (exo_k)
    // , (exo_k) -[:X_DING{score:720}]-> (xeno_w)
    // , (exo_k) -[:X_TTTT{scroe:119}]-> (xeno_x) -[:X_TTTT{score:498}]-> (exo_k)
    // , (exo_k) -[:X_M3M {score:477}]-> (xeno_x) -[:X_M3M {score:632}]-> (exo_k)
    // ,                                 (xeno_x) -[:X_DING{score:357}]-> (eko_k)
    // , (exo_m) -[:X_TTTT{score:312}]-> (xeno_t) -[:X_TTTT{score:220}]-> (exo_m)
    // , (exo_m) -[:X_M3M {score:520}]-> (xeno_t) -[:X_M3M {score:918}]-> (exo_m)
    // , (eko_m) -[:X_DING{score:712}]-> (xeno_t)
    // , (exo_m) -[:X_TTTT{score:140}]-> (xeno_x) -[:X_TTTT{score:520}]-> (exo_m)
    // , (exo_m) -[:X_M3M {score:390}]-> (xeno_x) -[:X_M3M {score:661}]-> (exo_m)
    // , (exo_m) -[:X_DING{score:720}]-> (xeno_x)
    // , (exo_m) -[:X_TTTT{scroe:119}]-> (xeno_y) -[:X_TTTT{score:498}]-> (exo_m)
    // , (exo_m) -[:X_M3M {score:477}]-> (xeno_y) -[:X_M3M {score:632}]-> (exo_m)
    // ,                                 (xeno_y) -[:X_DING{score:357}]-> (eko_m)
    // , (exo_n) -[:X_TTTT{score:312}]-> (xeno_w) -[:X_TTTT{score:220}]-> (exo_n)
    // , (exo_n) -[:X_M3M {score:520}]-> (xeno_w) -[:X_M3M {score:918}]-> (exo_n)
    // , (eko_n) -[:X_DING{score:712}]-> (xeno_w)
    // , (exo_n) -[:X_TTTT{score:140}]-> (xeno_x) -[:X_TTTT{score:520}]-> (exo_n)
    // , (exo_n) -[:X_M3M {score:390}]-> (xeno_x) -[:X_M3M {score:661}]-> (exo_n)
    // , (exo_n) -[:X_DING{score:720}]-> (xeno_x)
    // , (exo_n) -[:X_TTTT{scroe:119}]-> (xeno_y) -[:X_TTTT{score:498}]-> (exo_n)
    // , (exo_n) -[:X_M3M {score:477}]-> (xeno_y) -[:X_M3M {score:632}]-> (exo_n)
    // ,                                 (xeno_y) -[:X_DING{score:357}]-> (eko_n)
    // , (exo_p) -[:X_TTTT{score:312}]-> (xeno_t) -[:X_TTTT{score:220}]-> (exo_p)
    // , (exo_p) -[:X_M3M {score:520}]-> (xeno_t) -[:X_M3M {score:918}]-> (exo_p)
    // , (eko_p) -[:X_DING{score:712}]-> (xeno_t)
    // , (exo_p) -[:X_TTTT{score:140}]-> (xeno_v) -[:X_TTTT{score:520}]-> (exo_p)
    // , (exo_p) -[:X_M3M {score:390}]-> (xeno_v) -[:X_M3M {score:661}]-> (exo_p)
    // , (exo_p) -[:X_DING{score:720}]-> (xeno_v)
    // , (exo_p) -[:X_TTTT{scroe:119}]-> (xeno_w) -[:X_TTTT{score:498}]-> (exo_p)
    // , (exo_p) -[:X_M3M {score:477}]-> (xeno_w) -[:X_M3M {score:632}]-> (exo_p)
    // ,                                 (xeno_w) -[:X_DING{score:357}]-> (eko_p)
    // , (exo_q) -[:X_TTTT{score:312}]-> (xeno_v) -[:X_TTTT{score:220}]-> (exo_q)
    // , (exo_q) -[:X_M3M {score:520}]-> (xeno_v) -[:X_M3M {score:918}]-> (exo_q)
    // , (eko_q) -[:X_DING{score:712}]-> (xeno_v)
    // , (exo_q) -[:X_TTTT{score:140}]-> (xeno_w) -[:X_TTTT{score:520}]-> (exo_q)
    // , (exo_q) -[:X_M3M {score:390}]-> (xeno_w) -[:X_M3M {score:661}]-> (exo_q)
    // , (exo_q) -[:X_DING{score:720}]-> (xeno_w)
    // , (exo_q) -[:X_TTTT{scroe:119}]-> (xeno_x) -[:X_TTTT{score:498}]-> (exo_q)
    // , (exo_q) -[:X_M3M {score:477}]-> (xeno_x) -[:X_M3M {score:632}]-> (exo_q)
    // ,                                 (xeno_x) -[:X_DING{score:357}]-> (eko_q)
    // , (exo_r) -[:X_TTTT{score:312}]-> (xeno_v) -[:X_TTTT{score:220}]-> (exo_r)
    // , (exo_r) -[:X_M3M {score:520}]-> (xeno_v) -[:X_M3M {score:918}]-> (exo_r)
    // , (eko_r) -[:X_DING{score:712}]-> (xeno_v)
    // , (exo_r) -[:X_TTTT{score:140}]-> (xeno_x) -[:X_TTTT{score:520}]-> (exo_r)
    // , (exo_r) -[:X_M3M {score:390}]-> (xeno_x) -[:X_M3M {score:661}]-> (exo_r)
    // , (exo_r) -[:X_DING{score:720}]-> (xeno_x)
    // , (exo_r) -[:X_TTTT{scroe:119}]-> (xeno_y) -[:X_TTTT{score:498}]-> (exo_r)
    // , (exo_r) -[:X_M3M {score:477}]-> (xeno_y) -[:X_M3M {score:632}]-> (exo_r)
    // ,                                 (xeno_y) -[:X_DING{score:357}]-> (eko_r) -->

    ;
```
