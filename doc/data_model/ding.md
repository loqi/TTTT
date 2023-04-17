standard `zeal` urgency code reference points
    Levels 0..499 are network diagnostics; 500..999 are user test messages
    1000 Crumple a note into a ball and bury it in your trash can. (broadcast spam)
    1100 Humbly place a note face-up in your trash can. (targeted spam)
    1200 Boldly perch a note on the rim of your trash can. (maximally curated spam)
    1500 Place a note where you will eventually be. (weeks)
    2000 Address a letter to you and drop it in the mail. (days)
    2500 Leave a note with your doorman. (probably today)
    3000 Leave a note at your desk. (hours) - e.g. a fairly important email
    3500 Slip a note into your hand. (minutes) - e.g. a pressing text message
    4000 Wave you over from across the room. (seconds) - e.g. a quick callback request
    5000 Politely wait visibly in your presence. (nowish) - e.g. an ordinary voice phone call
    5500 Gently tap you on the shoulder and wisper. (now) - e.g. a pressing voice phone call
    6000 Brashly call you out of your seat at the theater. - e.g. a minor emergency
    7000 Emphatically wake you from your bed. - e.g. a substantial emergency
    8000 ALARM! "My house is on fire!"
    9000 ALARM! "Your house is on fire!"
    9999 Maximum possible value

Each `ding` relationship quantifies the trust that one node extends to another node for
purposes of originating or relaying communications messages. The directionality indicates
which way a ding jot can flow. The node that is trusting (the "arrowhead node") is the one
controlling the state properties of the arrow link. The node that is trusted (the "arrowtail
node) is limited in its use of the arrow link by the state properties, as controlled by
the trusting node. The arrowhead node is the one accepting vulnerability for any ding jot
propagated along this link. The arrowtail node is the one attesting to the pro-sociality of
such a jot. Ding jots flow in the direction of the arrows, while responsibility for anti-
and pro-social ding traffic passes against the arrows.

A `ding` relationship carries state properties:
    ready (int) - Number of ding jots currently available to initiate or propagate
    daily (int) - Number of dings per day (`ready` re-ups to this value each day)
    zmax  (int) - Maximum allowed zeal value to pass through this ding dunbar link.
Typical initial values would be { ready:5 daily:5 zmax:9999 }
After favorable ding experience accrues, the daily limit can loosen to a large number
appropriate to accommodate the expected use patterns - possibly in the dozens, hundreds,
or occasionally even thousands, depending on the surge needs and trust that such privelege
will not be abused.

A ding dunbar relationships may be one-way.
