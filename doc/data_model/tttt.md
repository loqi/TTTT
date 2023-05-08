The benefit of not trusting anyone ever about anything is that you cannot be hurt by misplacing
your trust. The benefit of trusting people to take responsible risks with what matters to you is
you can work together to build a relationship where you each benefit by doing right by one another.
A central skill neccessary for your successful participation in a TTTT network is your ability
to accurately asses whom to trust, in what domain, and to what extent; and to periodically update
your codified quantifications of your changing levels of trust in each actual person as you gain
experience in relating with that person.

A useful mnemonic to keep the polarity meaning straght in your mind while reading graph
ball-and-stick diagrams is to imagine the arrow links as actual arrows - dangerous weapons
pointed at you by the people you trust. By extending your trust to someone, you are willingly
putting yourself into a position of vulnerability. That person is in a position to hurt you
at any time by betraying your trust and abusing the power you have granted. You control how
much trust is at stake for each arrow pointed at you. You and only you can at any time, nerf
or buff that arrowhead without the notice or participation of that arrowtail's dunbar. Likewise,
your dunbars can each, at any moment, do the same to the arrowhead you have pointed at them,
with or without explicitly informing you about it.

TTTT traffic flows along these dunbar ralationship links in the direction of the arrows. Formal
responsibility for that traffic is vouched for by each node (and ultimately by the person who
owns that node) in the opposite direction. If your dunbar, through algorithmic error or through
human malice, betrays you in such a way as to cause you to betray someone else, you are responsible
for the arrowhead dunbar hurt by what your node did, just as your arrowtail dunbar is responsible
for any damage done to you. If such a betrayal is small, it will likely be settled algorithmically
with little or no human attention paid to the incident -- adjustments will be made to various
numbers in the data and everything continues slightly differently.

A sizable betrayal may rise to the level of human intervention. Typically, such a betrayal was
caused by a specific anti-social choice by a person, or by a high-stakes error happening somewhere
and propagating forward. In such a case, one of your nodes may have unwittingly participated in
a chain of harm. Nobody expects an automated TTTT node to identify an individual antisocial act
and interrupt its propagation in real time. When such an incident occurs, it usually indicates at
least one person has overestimated the trustworthiness of another person, or a person has suddenly
become less trustworthy and done something harmful, or an automated process someone excessively
trusted contains a dangerous bug causing it to go rogue. In each case, the trusting party is
rightfully responsible for having trusted, and so on down the chain of harm between promblem and
consequence.

If some stranger somewhere has betrayed his dunbar, thus causing me to betray someone I have a human
relationship with through some automated harm propogation, ultimately resulting in some dozen TTTT
nodes ralaying harm forward, I am responsible to the one I harmed because I trusted someone in the
direction of the source of harm. Likewise, my downstream dunbar is responsible to me becasue that
node (and thus that person) is even closer to the source of harm. If it's a big enough harm to warrant
human attention, I have a responsibility to "make it right" with the person my node affected -- by
their standards and to their satisfaction, just as the upstream node has a similar responsibility to
me -- person to person. If it's a small harm, it can be handled algorithmically by adjusting database
values and going about the day slightly differently as a result.

This is what gives a TTTT network its power. We don't normally attempt to discern the value and risk
associated with each individual little packet of information flowing through the network. Instead we
try our best to accurately evaluate and update the algorithmically quantified trustworthiness of the
person behind the nodes directly connected to our nodes ("dunbar" nodes or the dunbar people controlling
them) and then grant them the leeway to risk harm to us for the promise of a potentially fruitful
relationship full of benefit.

This risk/benefit model puts the authority to do good/bad actions in the hands of anyone who initiates
such action by putting a TTTT jot (actionable piece of TTTT data) into motion on the network. The
judgement of whether that jot had a good or bad effect is in the care of each node it touches along
the way, especially the destination node's algorithmic agent, which is ultimately representing the
the human controlling that node. This judgement is entirely according to the specific sensibilities of
real living people and their automated software representatives. The usual consequence of a anti- or
pro-social action is a slightly weakened/strengthened connection at each hop along the journey. A
very anti-social action may result in rifts along the path, requiring human intervention to repair
human relationships, and to remedy the technical conditions that led to such a big harm. In the joyous
end of the spectrum, an extremely pro-social act can rise to the level of human celebration along the
path of connection, and technical commendations being awarded to database variables along the route.

Each `tttt` dunbar relationship quantifies the level of low-level access to the greater TTTT network
that one node grants to another. In order for any application protocol (3milmo, ding) dunbar link to
exist, there must be an underlying TTTT dunbar link to support any direct TTTT traffic at all. The
`tttt` link directionality indicates which way TTTT wads (compressed collections of jots) flow. The
node that is trusting is the one arrowed toward (the "arrowhead node") by the node that is trusted
(the "arrowtail node"). The arrowhead node is the one accepting vulnerability for future gripes or
praise in response to TTTT traffic allowed to TTTT traffic flow along that link, and is the node
controlling the properties of that arrow link. TTTT wads flow "downstream" in the direction of the
arrows, while social responsibility (potentially) flows "upstream" against the direction of traffic.

Each `tttt` relationship carries state properties:
    cap (int) - Service limit. When `net` reaches `cap` traffic has been too one-way.
    net (int) - Net service balance. Positive: arrowhead node has given more than it got.

All TTTT dunbar pairs are two-way links (double, seprate dirgraph arrows). The arrowhead node
controls the `cap` value, and the `net` value counts up/down with TTTT traffic in each direction.
The `cap` value of each paired arrow must always sum to zero. That is, whenever a node has
provided more service requested by its TTTT dunbar node than it has received from that node, this
`net` number will be positive in the ahead-node's arrowhead link and invariably equally negative
in its arrowtail link. Opposing `net` values that do not sum to zero indicate corrupted data.

One node may unilaterally choose to accept TTTT traffic from another node, establishing a new
dunbar relationship by creating a link with itself at the arrowhead and a `cap` property above
zero. This requires a second opposing arrow be created with a `cap` of zero (until the dunbar
node chooses to raise that limit). A positive `cap` value in one direction and a zero `cap` the
other way means the arrowhead node of the zero `cap` arrow (the node controlling that arrow's
properties) is unwilling to give its dunbar more service than it has already been successfully
given.

The universal expectation is that asking for and receiving TTTT service obligates service
reciprocation whenever practicable with a reasonable amount of computational effort. Thus,
when one node notifies another node of its willingness to serve that second node's TTTT
requests (the initiating of a rudimentary dunbar relationship), and then later that second
node takes the first node up on the offer by requesting service, and then at least one jot
is successfully serviced by the first node, that second node enters a state of indebtedness,
implicitly having promised to serve a comparable volume of jots upon request of the first node.

By TTTT social convention, it is considered somewhat rude for a node to be unwilling to allow
its dunbar to run a negative net service balance after demonstrating willingness to carry a
positive net service balance in the other direction. A socially acceptable series of steps
to establish a new dunbar pairing goes like this:

    1. Node A configures itself to accept TTTT traffic from Node B - { cap:100 net:0 }
    2. Node A informs Node B that it is now willing to serve its TTTT traffic accordingly.
    3. Node B informs Node A that it intends to use this dunbar relationship sometime.
    4. At some later time, Node B requests TTTT service of Node A, one or more times.
    5. After some satisfactory TTTT service have been provided, Node B reciprocates.
    6. Node B decides to allow Node A to net positive or negative `net` - {cap:100}
    7. After mutually beneficial TTTT experience, `cap` values are further loosened.
