#!/usr/bin/env python3

# This script starts the Agent Zero daemon.

import daemon
import server.agency as agency

with daemon.DaemonContext():
    AgentZero().start()
