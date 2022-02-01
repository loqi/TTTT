# When any TTTT request arrives to Agent0, that encrypted message is delegated to this module.

# Here, it gets authenticated, then decrypted, then queued for later action. At some near future time, entries in
# that queue will be evaluated and moved to a priority queue where tasks are scheduled for action in a priority queue.

class Wad:
    