# RL169 — ordered-chain gap capacity barrier

Date: 2026-08-29

## Outcome and classification

RL169 uses the exact chronological increment of `z_j=q_j y_j` to obtain a
multi-phase physical gap theorem. It then proves that the direct capacity of
every chronological increasing-defect chain exceeds `L`, so this aggregation
cannot restrict the defect distribution.

New results:

1. **RL169.1 — ordered chronological gap theorem** (analytic, ordinary `+1`,
   physical coprime `g=1` first-survivor least-root scope).
2. **RL169.2 — ordered-chain capacity barrier** (analytic, using inherited
   `5theta<1`).

No cycle is constructed or excluded. This is neither a count/product,
local-cylinder, phase-boundary-order, nor rank-one-closure result.

## 1. Exact chronological affine increment

Keep RL168 notation: `q_j=2^(S_j)/3^j`, `E_j=Aj-LS_j`, and `z_j=q_j y_j`.
The ordinary accelerated equation gives

`z_(j+1)-z_j=q_j/3`.

Consequently, for `0<=j<k<L`,

`z_k-z_j=(1/3)sum_(i=j)^(k-1)q_i>0`.                       (1.1)

RL168 gives `E_j<E_k => q_j>lambda q_k` and `y_j<y_k`.

## 2. RL169.1 — pairwise ordered gap

For `j<k` with `E_j<E_k`,

`q_k(y_k-y_j)`
` = (z_k-z_j)+(q_j-q_k)y_j`
` > (q_j-q_k)m`
` > (lambda-1)q_k m`.

Hence

`y_k-y_j>(lambda-1)m`.                                     (2.1)

Every forward chronological pair whose lifted defects increase therefore has
an actual state gap strictly larger than `(lambda-1)m`. This couples the
full chronological affine increment to RL168's all-pair least-root order; it
is not the individual rank lower bound of RL168.

## 3. RL169.2 — chain capacity barrier

Let

`j_0<j_1<...<j_t`, `E_(j_0)<...<E_(j_t)`,

and suppose all phases have `h<=H`. Summing (2.1) gives

`y_(j_t)-y_(j_0)>t(lambda-1)m`.

The inherited state envelope, `rho_j>1/2`, and `h_j<=H` give

`y_(j_t)<lambda 2^(H+1)m`, while `y_(j_0)>=m`.

Thus

`t < [lambda 2^(H+1)-1]/[lambda-1]`.                        (3.1)

RL134 certifies `5theta<1`. Since `theta=LDelta/log(2)` and
`log(2)<1`, we have `Delta<1/(5L)`. Also `0<Delta<1/2` and
`exp(-Delta)>1-Delta`, so

`lambda-1=exp(Delta)-1 < Delta/(1-Delta)<2/(5L)`.

Therefore

`1/(lambda-1)>5L/2>L`.                                     (3.2)

The numerator of (3.1) exceeds one for every `H>=0`. Its right-hand side is
therefore greater than `5L/2`, while a chronological chain has at most `L`
phases. The direct monotone-chain aggregation cannot contradict any shallow
height bound, even at `H=0`.

This is a barrier only for the stated chain packing route. It does not
construct a jointly realizable cycle or rule out non-chain correlations,
exact residues, or another global invariant.

## 4. Exact audit and red teams

`RL169_CERTIFICATES/verify_ordered_chain_gap.py` uses exact rational and
integer arithmetic. It re-certifies `5theta<1`, verifies
`1/(2Delta)>5L/2>L`, and checks the ordinary increment on 5,460 bounded
accelerated words with rational trajectories.

- **Ordinary increment:** PASS. The positive term `q_j/3` is from the
  actual `+1` recurrence.
- **Simultaneity:** PASS. Distinct chronological phases are coupled and their
  physical gaps summed; this is not an individual rank envelope.
- **Order separation:** PASS. `E` is RL168's state-value order, not modular
  phase adjacency.
- **Inputs:** PASS. Only inherited internal `5theta<1` is used; the external
  minimum floor is not needed.
- **No false closure:** PASS. No state model, dense-closure discharge, or
  cycle exclusion is claimed.

## 5. Next target

Seek a non-chain simultaneous relation using exact affine increments and the
full permutation between chronological and lifted-defect order. It must add
information beyond chain gaps, individual rank packing, count/product mass,
bare residues, or the one dense closure condition.
