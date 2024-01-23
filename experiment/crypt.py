# from Crypto.PublicKey import ECC
# from Crypto.Hash import SHAKE128
# from Crypto.Protocol.DH import key_agreement

# # This KDF has been agreed in advance
# def kdf(x):
#         return SHAKE128.new(x).read(32)

# # In a real scenario, this long-term key already exists
# U_static = ECC.generate(curve='p256')

# # This ephemeral key is generated only for this session
# U_ephemeral = ECC.generate(curve='p256')

# # In a real scenario, this long-term key is received from the peer
# # and it is verified as authentic
# V_static = ECC.generate(curve='p256').public_key()

# # In a real scenario, the peer generated this ephemeral key only
# # for this session. It doesn't need to be authenticated if the
# # static key of V already has been.
# V_ephemeral = ECC.generate(curve='p256').public_key()

# session_key = key_agreement( static_priv=U_static
#                            , static_pub =V_static
#                            , eph_priv   =U_priv
#                            , eph_pub    =U_pub
#                            , kdf        =kdf
#                            )

# # session_key is an AES-256 key, which will be used to encrypt
# # subsequent communications

# session_key

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

# Generate a private key for use in the exchange.
private_key = X25519PrivateKey.generate()

# In a real handshake the peer_public_key will be received from the
# other party. For this example we'll generate another private key and
# get a public key from that. Note that in a DH handshake both peers
# must agree on a common set of parameters.
peer_public_key = X25519PrivateKey.generate().public_key()
shared_key = private_key.exchange(peer_public_key)

# Perform key derivation.
derived_key = HKDF( algorithm=hashes.SHA256()
                  , length=32
                  , salt=None
                  , info=b'handshake data'
                  ).derive(shared_key)

# For the next handshake we MUST generate another private key.
private_key_2 = X25519PrivateKey.generate()
peer_public_key_2 = X25519PrivateKey.generate().public_key()
shared_key_2 = private_key_2.exchange(peer_public_key_2)
derived_key_2 = HKDF( algorithm=hashes.SHA256()
                    , length=32
                    , salt=None
                    , info=b'handshake data'
                    ).derive(shared_key_2)

peer_public_key
