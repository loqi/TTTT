# 0. Listen at localhost+UDP socket for triage datagram.
# 1. Convert all jots in arrive.db into triage.db pending tasks.
# 2. Execute all priority tasks, converting outgoing to depart.db.
# 3. If any task has ripened, notify tttt_depart_d via UDP socket.
# 4. Loop back to listening.
