# RL324 local propagation barrier

Status: VERIFIED METHOD BARRIER FOR RL324 CLOSEOUT

The validated zero-carry -> unit-minus-one adjacent bridge creates a bounded two-rank physical box, but that boundedness cannot be propagated to later matched ranks using only the local defect recurrence and local state lower bounds.

Use

`Delta=2^d P-Q`.

Start with

`d=3`,
`Delta=1`,
`Q=8P-1`

for odd `P`.

For any chosen `a>=2`, choose an arbitrarily large odd representative satisfying

`v2(3P+1)=a`.

Then

`P'=(3P+1)/2^a`

is odd, while

`3Q+1=2(12P-1)`

has exact 2-adic valuation one, so

`Q'=12P-1`,
`b=1`.

Therefore

`d'=3+a-1=a+2`

and

`Delta'=2^(a+2)P'-(12P-1)=5`.

Thus an arbitrarily large next matched displacement is compatible with genuine ordinary odd-to-odd transitions and a tiny positive defect.

By increasing the residue-class representative, all physical states in this local construction can be placed above any fixed positive floor.

This is not a cycle and does not satisfy the global full-return ownership/minimality architecture. Its use is only negative: no theorem based solely on the local matched-defect recurrence, positivity, unit-minus-one quotient form, and local least-state lower bounds can propagate the RL324 bounded crossing box to an arbitrary later canonical rank.

The surviving route must use a genuinely global ingredient absent here.
