#!/usr/bin/env python3

# This Python script interacts directly with the TTTT agent of our home node (Agent0) via TCP commands.
# For now the only user interface for controlling the agent is edit the Python script and run it.
# It works by creating a new AgentZero and starting it as a non-daemon process.
# It then calls the methods of that object directly to get it to do its job.

# TODO: Make a real API and user-interface client that lets our TTTT agent's human ask it to do things.

import ../agent/zero

agent0 = AgentZero()
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
