## The TTTT agent

clade/              the TTTT protocol root clade, nested with all specialization clades
    /_api           how to speak TTTT root protocol
    3milmo/         the "third millennium money" specialization clade
        /_api       how to speak TTTT/3milmo specialization
    ding/           the "ding" human pester management specialization clade
        /_api       how to speak TTTT/ding specialization

agent/              a TTT agent (peer-to-peer server) that speaks TTTT over the Internet with other agents
    /tttt_agent0_d  listens and speaks TTTT with other agents (e.g. dunbars, strangers) via UDP datagrams
    /agent_zero     the software brains of Agent0 (the agent residing at our home node, i.e. zero degrees away)

boss/               the boss (client ordering Agent0 around) interacting with the owner (?human user) and Agent0
    /tttt_boss0_d   listens to various unix or TCP mechanisms to interface between owner and Agent0
    /batch_boss     a hardcoded script simulating a client until we make usable client software
