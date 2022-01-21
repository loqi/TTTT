#!/usr/bin/env python3

# This Python script interacts directly with the TTTT agent of our home node (Agent0) via TCP commands.
# Right now, the user interface for controlling our agent goes like this:
# you just edit the code of this file and run it.

# A boss is a client 

# Agent Zero talks TTTT to dunbars and occasionally to strangers across the TTT graph.
# Boss uses either a client API or direct method calls to make requests of Agent 0, which then talks TTTT.

# TODO: Make a real API and user-interface client that lets our TTTT agent's human ask it to do things.

import ../agent/zero

agent0 = _zero.agentZero()

agent0.start()
agent0.noop()
agent0.stop()

# # listen
# me = tttt.Myself()
# me.listen()
#
# # send
# me = tttt.Myself()
# me.send("::1", 5150, "Hello, World!")
