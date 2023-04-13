# A node is a TTTT entity capable of maintaining dunbar relationships with other nodes.

class Node
    # create a new node owned by the agency.
    def create()
        return

    # # Given a secret+public key, create a node for it.
    # def create(pubkey, kSECRET)
    #     return

    # # bind this node to another node in a swarm.
    # def twin(node)
    #     return

    # Establish a dunbar tunnel of this node trusting another node.
    def trust(guid, argS)
        # If it's a local node, just do it locally in the DB
        # If it's a foreign node, do it via the DB and then notify the node.
        return
