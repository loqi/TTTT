# 1. Create a new domestic node, generating a new key pair for it

# 2. Pair a domestic node with another domestic node in a dunbar tunnel

# 3. Pair a domestic node with a foreign node in a dunbar tunnel

# 4. Clone an a domestic node when we already have a specific key pair

# 5, Make a new user record (boss cluster)

# 6. Register a boss client node to manage a user cluster

# 7. Provide all these functions in the form of a pretty boss client


def new_domestic_node():
    pass

def import_domestic_node(pubkey, kSECRET):
    pass

def make_domestic_tunnel(first_node, second_node):
    pass

def make_border_tunnel(this_node, that_node):
    pass

def new_user_record():
    pass

def user_owns_node(user, node):
    pass





"""


synode, endode, exode, dunbar, xenode

boss - a hub 
user - 
client -
hub - the set of synods controlled by a user
ambit - the set of synods and dunbars controlled by a user

webapp - 
    admin: create a new hub with one user and one starter synode (pseudonymous persona)
    login as a user
    logout as a user
    register a panic to bump off all users and delay
    create a new synode within the hub
    perform a TRIE query
    perform a SEEK on an addr or card
    perform a PING with an implied SEEK
    perform a WEND with an implied PING, modifying lane as it goes
    perform a 3milmo/GIVE with an implied WEND
    


Structure:
agent
    TTTT boss HTTP UI
    TTTT in via IP6 UDP
    TTTT out via IP6 UDP


"""