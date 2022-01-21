#!/usr/bin/env python3

# This script starts the Agent Zero daemon.

import daemon
import zero

agent0 = AgentZero()
with daemon.DaemonContext():
    agent0.start()
