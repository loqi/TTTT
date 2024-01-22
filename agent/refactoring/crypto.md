An agency represents the interests of many users.
An agency manages many agents active at IP6 poles.
A poll is an IP6 socket endpoint monitored by an agent.
POLL PROPERTIES:
    ip6 - The IPv6 address monitored by this poll
    port - The IP port monitored by this poll
    pubkey - The public key for secure inbound traffic to this poll
    privSECRET - The secret key proving ownership of this poll
    (many links) endode whose traffic is handled by this poll
A poll serves many endodes.
An agent actively represents an agency at one or more IP6 polls.
A pole serves incoming and outgoing wads, which are cryptographically secure collections of jots.
A jot is an individual taks request from one TTTT node to another.
A user owns many endodes.
An endode links many endodes along domestic dunbar relationships.
    Such relationships are low-friction traffic paths implemented via direct DB manipulations.
An endode links many exodes along foreign dunbar relationships via IP6 border tunnels.
ENDODE PROPERTIES:
    pubkey - The universal stable identifier and cryptographic lock of any TTTT node
    privSECRET - The secret key proving ownership of this endode
An exode links many xenodes as reachable strangers via distant relationships.
EXODE PROPERTIES:
    pubkey - The universal stable identifier and cryptographic lock of any TTTT node
    mathSECRET - used to mark informal wads with inexpensive math lock
An inbound tunnel joins an exode toward an endode via an IP6 border tunnel.
INTUNNEL PROPERTIES:
    stamp - tunnel ID as addressed on inbound wads
    head - domestic node ID at receiving end of this tunnel
    tail - foreign node ID at sending end of this tunnel
    mathSECRET - used to mark an informal wad with inexpensive math lock
    baseSECRET - base key for inbound AES traffic
An outbound tunnel joins an endode toward an exode via an IP6 border tunnel.
OUTTUNNEL PROPERTIES:
    stamp - tunnel ID as addressed on outbound wads
    head - foreign node ID at receiving end of this tunnel
    tail - domestic node ID at sending end of this tunnel
    baseSECRET - base AES key for outbound traffic

Incoming wads are decrypted in this sequence:
    0. build fresh_exode data structure array of exodes [
            each with a hashmap of crytographic data {
                exode_id: local DB exode ID integer
                key16: sixteen-byte key (mathSECRET of exode)
                rnd1K: one kilobyte of pseoudorandom bits seeded by key16
                tunnS: array of inbound border tunnels with exode at tail [ {
                    stamp: int16 ID of this inbound tunnel
                    head: endode at receiving end of this tunnel
                    baseSECRET: base AES key for inbound traffic
                    } ]
                }
            ]
    1. await datagram at IP6 poll
    2. cypher_dg = that datagram
    3. if cypher_dg is stub chaff (too short to be real) discard and return to waiting at line 1
    4. determine whether datagram is an informal wad:
        walk index i through fresh_exode[]
            quo,mod = ( (dg[0..31] XOR (fresh_exode[i][rnd1K][0..31])) / (fresh_exode[i][key16]) )
            if (mod AND 0xFFFFFFFF_FFF00000) is not zero
                skip on to the next i in fresh_exode walk loop
            # we found enough zeros in the low-order bits to indicate exode #i is likely sender
            walk index tunn_i through tunn = fresh_exode[i]['tunnS'][tunn_i]
                aesKey = tunn['baseSECRET'] XOR quo XOR rnd1K[32..63]
                decrypt cypher_dg[256..511] # seal, stamp, serial

                plain_dg = aes_decrypt(aesKey, cypher_dg[32..])
                check MAC of wad
                see if wad is chaff
                check serial of wad
                record dropped wads
                add this wad to inwad.db



