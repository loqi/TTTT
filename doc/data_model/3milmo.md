Each `3milmo` relationship quantifies the financial credit that one node extends to
another node for purposes of originating or relaying third-millennium money transactions.
The directionality indicates which way monetary value flows. The node that is trusting is
the one that is arrowed toward ("arrowhead node") by the node that is trusted (arrowtail
node). The arrowhead node is the one accepting vulnerability for the potential future
default of commitments. 3milmo jots flow in the direction of the arrow, while credit
risk flows against the arrow.

Each `m3m` relationship carries state properties:
    att (int) - "balance attractor" Ideal `bal` value declared by arrowhead node (μж)
    lim (int) - "credit limit" Maximum ordinarily-accrued balance (in microkudos μж)
    bal (int) - "balance" Negative: arrowhead-debtor; positive: arrowtail-debtor (μж)

Whenever a node pairs with another node in a 3milmo relationship, it must be a two-way pairing.
One node may unilaterally choose to financially trust another node, establishing a 3milmo arrow
link and a `lim` value greater than zero. This requires a second, opposing 3milmo arrow be created
with a `lim` of zero, until that dunbar node chooses to raise its credit limit. The arrowhead node
of the 3milmo relationship may update `att` or `lim` at any time, with or without informing the
arrowtail node. The `att` value declares the preferred balance named by the arrowhead node. In
most cases this will be zero. If a node's owner wants that node to be saving up monetary asset
or liability, this `att` value will be positive or negative. By setting `att` to zero, we are
saying "Please find ways to flow money through the network such that my significant negative or
positive 3milmo holdings co-annihilate through ordinary 3milmo traffic."

It is customary to always inform the arrowtail node of the founding of a new 3milmo pairing and
name some spoken credit limit at or below the actual codified credit limit. As 3milmo activity
is experienced, the `att` and `lim` values may change at the whim of the arrowhead node, with or
without notice to the arrowtail node. That is, either side of the dunbar relationship may raise
or lower their 3milmo trust in the other, and may or may not choose to say so explicitly. Of
course, the `bal` value only changes when monetary value flows from one dunbar to the other, a
transaction event which requires participation of by both 3milmo dunbar-paired nodes.

Upon initializing a new 3milmo pairing, both arrows of the 3milmo dunbar relationship are
created, each with `bal` value at zero. Additionally, the initiating node ought to have
arrowhead `lim` greater than zero. The opposing pair of `bal` values must invariably sum
to zero. That is, each time a node goes deeper or shallower into debt (a negative `bal`
representing that liability), the creditor dunbar reciprically carries that debt as an
asset (a positive `bal` of the same amplitude at opposite polarity). Whenever an opposing
pair of `bal` values does not sum to zero, this indicates corrupted data.
