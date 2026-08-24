# RL48 continuation — full phase = exact four-swap return

Date: 2026-08-22

## Status

**Analytic from the RL45/RL47 conventions present in the RL47→RL48 bundle.**

This note removes more of the historical black-box dependence than the earlier same-root note.  It does **not** claim that the inherited radius-3 theorem has been matched line-by-line, because the exact RL18/RL19 theorem statement is not present in the current bundle.  It proves that the live full phase condition is exactly an integer Collatz two-half return exchanging two values separated by `4`.

## 1. General one-excursion word reconstruction

RL45 uses full half-words

`u = 11 alpha`, `v = 11 beta`.

RL47's fixed-`t` automaton starts *after* the mandatory local column `(alpha,beta)=(0,1)`, stores an internal pair word `(x,y)` of length

`m=a-(t+3)-1`,

with each of `x,y` having weight

`r=ell-3`,

and omits the terminal local `(1,0)` column.  The remaining terminal tail has length `t` and is synchronized zero motion.  Therefore the full words are forced to be

`u = 110 x 1 0^t`,

`v = 111 y 0^(t+1)`.

The length is `a` and the weight is `ell` on both sides.

This reconstruction is not a dimensional guess: it is exactly the composition of RL45's `11 alpha,11 beta` convention with the RL47 start/terminal convention.

## 2. Q-polynomials

For a binary word `w` of length `a` and weight `ell`, define

`Q(w)=sum_{i:w_i=1} 2^i 3^(ell-rank(i))`.

For the internal words put

`Qx=sum_j 2^a_j 3^(r-j)`,

`Qy=sum_j 2^b_j 3^(r-j)`.

Writing `U=Q(u)`, `V=Q(v)`, direct rank bookkeeping gives

`U = 15*3^r + 24 Qx + 2^(a-t-1)`,

`V = 19*3^r + 8 Qy`.

The fixed prefixes account for `15*3^r` and `19*3^r`; the internal `x` block acquires a factor `24` because it is shifted three positions but only two ranks, whereas the internal `y` block acquires a factor `8` because it is shifted three positions and three ranks.

## 3. The proper-factor identity follows from RL47's terminal identity

RL47 gives

`3Qx-Qy = 14*3^r + 2^(a-1)-2^(a-k-1)`,

with `k=t+3`.

Hence

`U-V`

`= -4*3^r + 8(3Qx-Qy) + 2^(a-t-1)`

`= 108*3^r + 4*2^a`

because `8*2^(a-k-1)=2^(a-t-1)` cancels the terminal-one term.

Since `108*3^r=4*3^ell`,

`boxed: U-V = 4(2^a+3^ell)`.

Thus the inherited proper-factor identity is independently reconstructed from the live RL47 terminal geometry.

## 4. Concatenation factorization

Put

`X=2^a`, `Y=3^ell`, `M=X-Y`.

For concatenated equal-length/equal-weight words,

`Q(uv)=Y U + X V`.

Using `U=V+4(X+Y)`,

`Q(uv)`

`=Y[V+4(X+Y)]+XV`

`=(X+Y)(V+4Y)`.

Therefore

`boxed: Q(uv)=(X+Y)(V+4Y)`.

Since the full denominator for the length-`2a`, weight-`2ell` word `uv` is

`X^2-Y^2=(X+Y)(X-Y)`,

the full cycle divisibility is exactly

`X^2-Y^2 | Q(uv)`

if and only if

`boxed: M | V+4Y`.

But the earlier RL48 same-root theorem proved that the full phase condition is exactly `M | V+4Y`.

So the apparently separate `X+Y` proper-factor condition and `X-Y` phase condition are literally the two factors of the full cycle denominator.

## 5. The phase quotient is the actual cycle value

Assume the full phase condition and define

`N=(V+4Y)/M`.

All quantities are positive and `M>0`, so `N>0`.

Then

`Y(N+4)+V = XN`,

while the proper-factor identity gives

`YN+U = X(N+4)`.

Thus the standard Collatz half-step affine maps attached to the two words satisfy

`boxed: F_u(N)=N+4`,

`boxed: F_v(N+4)=N`.

Here

`F_w(n)=(3^ell n+Q(w))/2^a`.

The divisibility by `2^a` is not merely a rational affine identity.  For a binary word `w`, the congruence

`3^ell n+Q(w)=0 (mod 2^a)`

selects exactly the residue class whose first `a` Collatz parity bits are `w`.  This follows inductively from

- `Q(0w')=2Q(w')`,
- `Q(1w')=3^wt(w')+2Q(w')`.

Hence these are genuine integer Collatz trajectory segments with the claimed parity words.

Consequently `uv` is a positive nontrivial cycle word and

`Q(uv)=N(X^2-Y^2)`.

The midpoint values of this cycle are exactly `N` and `N+4`.

## 6. The radius-three local shape is explicit

The forced prefixes are

`u=110...`, `v=111...`.

Therefore the cycle value satisfies

`N = 3 (mod 8)`,

and `N+4 = 7 (mod 8)`.

The two values agree in their first two parity decisions and split at the third.  Thus the full phase condition produces an actual `4`-separated, depth-three local pair rather than merely a common root of three polynomials.

This is the strongest concrete radius-3 bridge formulation currently available.

## 7. Exact meaning of the RL T-coordinate

Let `A_i` and `B_i` be the actual integer trajectories of `N` and `N+4` after the common leading `11` and the mandatory local `01`, then along the internal pair columns.  If `d_i` is the RL height, then

`boxed: T_i = 3^(d_i) A_i - B_i`.

At the local start,

`A_0=(9N+5)/8`,

`B_0=(27N+127)/8`,

so `3A_0-B_0=-14`, exactly the canonical RL start.

Under a pair column `(x,y)`, the identity evolves as

`T'=[3^y T + x 3^(d+y-1)-y]/2`,

which is precisely the RL recurrence.

At terminal,

`T=2^(t+3)-1`.

The omitted terminal pair `(1,0)` converts the trajectory separation to `2^(t+2)`, and the following `t` synchronized zero columns divide it down to exactly `4`.

So the terminal valuation target is literally the amount of 2-adic separation that must be shed before the two half-trajectories return to a gap of `4`.

## 8. Consequence for the bridge roadmap

The same-root/root-selection problem is no longer the substantive Gate-B obstacle.  Algebraically, the full phase condition already **is** the exact `4`-swap cycle closure.

What remains is a provenance match:

- If the audited radius-3 theorem is stated as exclusion/uniqueness of exactly such a `4`-separated depth-three pair in a positive Collatz cycle, then Gate B is bridged directly by this theorem.
- If the radius-3 theorem instead imposes additional sparse-support/orientation/gcd hypotheses, those hypotheses must be checked against `u,v` above.  The missing task is then a hypothesis audit, not a new resultant or same-root construction.

No global RL closure is claimed here because the exact inherited radius-3 theorem statement is absent from the current handover.

## 9. Recovery of the canonical physical gap-9 entrance

Write `N=8c+3`.  The first two bits of both half-words are `11`.  After those two common odd steps,

- the `u` trajectory is at `18c+8`,
- the `v` trajectory is at `18c+17`.

Their difference is exactly `9`.

The third bits are respectively `0` and `1`, so the mandatory local column is `(0,1)`.  After it the local values are

`A_0=9c+4`,

`B_0=27c+26=3A_0+14`,

hence `T_0=3A_0-B_0=-14`.

This identifies the abstract RL47 local start with the literal positive-orbit gap-9 entrance generated by the `4`-separated radius-three pair.  In other words, the full phase quotient does not merely produce some positive cycle: it produces the exact physical pair whose first two synchronized odd steps create the canonical gap `9` used throughout the RL43–RL47 excursion analysis.
