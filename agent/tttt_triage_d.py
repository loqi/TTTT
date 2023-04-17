# 0. Listen at localhost+UDP socket for triage datagram.
# 1. Convert all jots in arrive.db into triage.db pending tasks.
# 2. Execute all priority tasks, converting outgoing to depart.db.
# 3. If any task has ripened, notify tttt_depart_d via UDP socket.
# 4. Loop back to listening.


# Import the neo4j dependency
from neo4j import GraphDatabase

# Create a new Driver instance
driver = GraphDatabase.driver("neo4j://localhost:7687", auth=("neo4j", "neo")) # Unencrypted
# For more information on additional authentication methods, see the Authentication and
# authorization section [https://neo4j.com/docs/operations-manual/current/authentication-authorization/]
# of the Neo4j Operations Manual [https://neo4j.com/docs/operations-manual/current/].

# The driver() function also accepts additional configuration parameters.
# This object allows you to provide advanced configuration options, for example setting the
# connection pool size or changing timeout limits.
# GraphDatabase.driver(uri, auth=auth,
#     max_connection_lifetime=30 * 60,
#     max_connection_pool_size=50,
#     connection_acquisition_timeout=2 * 60)
# For more information or a full list of configuration options, please visit the Neo4j Python
# Driver manual [https://neo4j.com/docs/python-manual/current/get-started/].

# Verify the connection details
driver.verify_connectivity()
