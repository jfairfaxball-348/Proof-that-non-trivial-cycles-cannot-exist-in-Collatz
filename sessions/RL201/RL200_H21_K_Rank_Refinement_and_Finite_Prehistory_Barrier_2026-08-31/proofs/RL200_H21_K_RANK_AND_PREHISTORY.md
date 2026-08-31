# RL200 proof — H21 terminal K rank cut and finite reverse-prehistory barrier

Date: 2026-08-31. Scope remains the inherited sole high branch `(37,0,23,-1)`.

## A. Rank-resolved terminal K

Let `r=iB mod L`, `i=pr mod L`, and write `Ai=nL+r`.  Then
`rho(r)=2^n/3^i`.  The H21 terminal normalized gap is the inherited
`Delta=7*3^35/2^21`, so `K(r)=rho(r)Delta`.

For `r<s`,

`log rho(r)-log rho(s)=((i_r-i_s)delta+(s-r)log2)/L`.

Here `delta=A log2-L log3`, `0<delta<2^-40`.  Since `|i_r-i_s|<L` and
`s-r>=1`, the right side is greater than `(log2-L delta)/L>0`.
Thus K is strictly decreasing in canonical mechanical rank.

Rigorous rational atanh-series logarithm bounds certify

`K(25583192105)>146795909391`,
`K(25583192106)<146795909391`,
`K(41775866136)>128081997553`.

Hence the inherited H21 interval intersects the global K corridor exactly in
`[25583192106,41775866136]`.

Twelve of the inherited fourteen isolated H21 rank deletions remain in that interval, giving
`16192674031-12=16192674019` necessary ranks and exactly `2213738806` new deletions relative to
the inherited post-deletion count.

## B. First extra prehistory mechanical bits

Subtracting chronological rank displacements from the refined terminal interval gives

`r-34B: [40886621976,57079296006]`,
`r-36B: [17517168678,33709842708]`,
`r-37B: [74596464685,90789138715]` modulo L.

The latter two intervals lie respectively below and above the mechanical threshold
`R=57079296007`, so the first two newly exposed backward source bits are exactly `1,2`.

## C. Uncoupled reverse extension

For a current positive odd unit y and prescribed source mechanical bit c, a reverse odd
predecessor has the form

`x=(2^a y-1)/3`.

Integrality requires `2^a y=1 mod3`; unit status of x requires
`2^a y!=1 mod9`.  Since `2^a mod9` has period six, the first condition admits three classes
modulo six and exactly one is forbidden by the second.  Two safe classes remain, each with
arbitrarily large positive exponents.

The source height is `h+a-c`, so sufficiently large representatives preserve nonnegativity.
Induction gives a reverse extension through every finite prescribed mechanical word.

This is deliberately an independent-endpoint theorem.  It does not preserve an additional
coupled pair numerator, defect sequence, complete global height word, fixed-K0 moment, or
rank-resolved signed K successor datum.

Therefore no one of RL199's four eta classes is removed by this local reverse consumer.
