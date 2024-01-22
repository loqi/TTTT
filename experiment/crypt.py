from Crypto.PublicKey import ECC
from Crypto.Hash import SHAKE128
from Crypto.Protocol.DH import key_agreement

# This KDF has been agreed in advance
def kdf(x):
        return SHAKE128.new(x).read(32)

# In a real scenario, this long-term key already exists
U_static = ECC.generate(curve='p256')

# This ephemeral key is generated only for this session
U_ephemeral = ECC.generate(curve='p256')

# In a real scenario, this long-term key is received from the peer
# and it is verified as authentic
V_static = ECC.generate(curve='p256').public_key()

# In a real scenario, the peer generated this ephemeral key only
# for this session. It doesn't need to be authenticated if the
# static key of V already has been.
V_ephemeral = ECC.generate(curve='p256').public_key()

session_key = key_agreement( static_priv=U_static
                           , static_pub =V_static
                           , eph_priv   =U_priv
                           , eph_pub    =U_pub
                           , kdf        =kdf
                           )

# session_key is an AES-256 key, which will be used to encrypt
# subsequent communications

session_key
