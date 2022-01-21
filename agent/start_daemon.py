#!/usr/bin/env python3

# This script starts the Agent Zero daemon.

import daemon
import zero

with daemon.DaemonContext():
    AgentZero().start()
