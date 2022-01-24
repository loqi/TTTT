# When any TTTT request arrives to Agent0, that encrypted message is delegated to this module.

# Here, it gets authenticated, then decrypted, then queued for later action. At some near future time, entries in
# that queue will be evaluated and moved to a priority queue where tasks are scheduled for action in a priority queue.

class Intake:
    """An assistant to AgentZero, that processes a TTTT request coming in from another agent by authenticating,
    decrypting, sanity-checking, and then queueing that request if it passes all integrity filters. The sender
    may be a stranger using public-key encryption or a dunbar encrypted by dunbar tunnel."""

    counter = 0

    def got(self, datagram, spoofable_addr):
        host = ipaddress.ip_network(spoofable_addr)
        agent = dunbar_at_host[host] or stranger_at_host[host]
        _queue_for_triage(plain_from_hmac1280(datagram))
        return True

    def _queue_for_triage(plainBytes)
        filename = f"{self.queue_index:06}.request"
        self.queue_index++
        # Create new file f'{queue_index:06}.request' and then output plainBytes
