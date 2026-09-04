# RL248 closeout report

Date: 2026-09-04
Classification: **`R4_BRIDGE_REDUCED`**.

## Scope

RL248 resumed only the audited RL246 Radius-4 global bridge after RL247's `R3_R4_SCOPE_AUDIT_PASS`. The Radius-4 theorem is not invoked anywhere in RL248. Its positive/full-D/primitivity/exact cyclic-distance/same-root/full-phase eligibility remains mandatory.

Gate A remains open. Gate B remains open. Radius 5 remains inactive. Branches A, B, and C remain formally open.

## Promoted RL248 frontier

### 1. Internal shifted-singleton multiplicity and physical amplification

For Branch C, with `b=beta(P)>=6`, at most two shifted singleton `10` edges can lie outside the internal word `x`. Hence at least `b-2>=4` shifted `10` signatures are wholly internal.

For each selected singleton, with internal canonical boundary heights `d0,d1,d2>=1`, the genuine companion envelope is exactly

`(E_(i-1),E_i,E_(i+1))=(-d0,-1-d1,-d2)`.

The selected neighbourhoods are disjoint, therefore

`beta(E) >= 4(b-2) >= 16`.

With selected height excess

`H_I=sum[(d0-1)+(d1-1)+(d2-1)]`,

one has `0<=H_I<=H` and

`beta(E) >= 4(b-2)+H_I`.

If `e_I` selected blocks take a canonical event arm then `H_I>=e_I`, hence

`beta(E) >= 4(b-2)+e_I`.

The rigid `11,00` arm retains exact mod-3 height-parity fingerprints and RL248 adds exact mod-4/mod-8 entry cylinders. A shifted internal `10` occupying the final two internal columns is forced to enter at

`(d,J)=(2,2^(k+2)-2)`

and then reaches the exact terminal `(1,2^k)` through `10,00`.

### 2. Zero-budget contraction

Let `z=a-ell`, `N=beta(P)`, and let the number of zeros of the internal word be

`m=z-k+2`.

Distinct internal shifted `10` signatures consume distinct internal zeros, giving

`N-2 <= m`,

so

`N <= z-k+4`.

In particular `N>=6` gives `z>=k+2`.

The extremal equality `z=k+2` is analytically impossible. In that equality case all four internal zeros are forced singleton `10` endpoints, giving a separated-zero grammar. Exact canonical barriers for the deterministic `(d,J)` automaton keep the exit `J<0`, contradicting the full-phase terminal `J=2^k>0`. Thus `z>=k+3`.

### 3. Exact run-compressed finite certificate

For a canonical run of input bit `1`, at odd `J` define

`R_J=J+2^d-1`.

Then exactly `R_J' = 3 R_J/2`. Every one-run either reaches the negative fixed point `J=1-2^d`, becomes even and descends in `d`, or becomes illegal at `d=1`. Therefore every one-run has a finite exact closure, and for fixed zero budget `m` the complete canonical state set is finite despite unbounded word length.

A fresh independent C++ replay at closeout enumerates the complete unrestricted canonical superset through `m=16`. At `m=16` it contains exactly

`41,178,667`

states, including

`9,399,300`

height-one states. The exact positive powers of two reachable at height one have exponents

`{1,3,5,7,9,11,13,15,17,21,23}`.

No `J=2^k` with `k>=31` occurs for any `m<=16`. Therefore every simultaneous Branch-C survivor satisfies

`m>=17`,

hence

`boxed: a-ell >= k+15`.

Using the frozen simultaneous-survivor lower bound `k>=31`,

`boxed: a-ell >= 46`.

The attempted `m=17` unrestricted expansion exceeded the live-session resource envelope. That is not mathematical evidence and is not used in any promoted claim.

### 4. Exact normalized prefix-scale cocycle and bounded-counterflow floor

For

`S_i=2^i/3^(U_i)`, `R=2^a/3^ell`, `P_i=r-W_i(q)`, `ar-qell=2`,

define

`F_i=S_i/R^(i/a)`.

Then the exact cyclic cocycle is

`F_(i+q)/F_i = 3^(P_i-2/a)`.

Equivalently, with `G_i=F_i^a=S_i^a/R^i`,

`G_(i+q)/G_i = 3^(a P_i-2)`.

If `b=beta(P)`, partial q-orbit sums and `gcd(a,q) in {1,2}` give the absolute physical prefix-scale theorem

`boxed: S_i > 3^(-(b+2))`

for every physical prefix.

This is conditional on the actual bounded counterflow `b`; it is not generic physical-scale anti-concentration.

### 5. Absolute internal phase gain at beta(P)=6

Every wholly internal singleton `01` block has exact two-column phase gain

`DeltaPhi_01 >= (2/3) S_entry`,

and every wholly internal `10` block has

`DeltaPhi_10 >= (1/3) S_entry`.

In Branch C with `b=6`, at least three singleton `01` blocks are wholly internal and disjoint. Combining them with the new absolute scale floor gives

`boxed: DeltaPhi_selected_01 > 2/6561`.

Numerically this exceeds `1/4374`, but this is **not** a revival of RL246's demoted uniform single-packet claim. It is a differently scoped aggregate theorem conditional on `beta(P)=6`, now with an exact absolute scale proof.

## Corrections, demotions, and red-team boundaries

- RL246's old scratch statement `DeltaPhi_packet > 1/4374` uniformly for one packet remains **DEMOTED / NOT PROMOTED**.
- The new `>2/6561` statement is an aggregate `b=6` theorem over at least three disjoint internal `01` blocks, not the old claim.
- Large `beta(E)` does not imply exact cyclic adjacent-transposition distance 4.
- Local `(1,2,1)` topology does not by itself satisfy Radius-4 ownership/global-distance hypotheses.
- The fixed-form q-window Branch-C regression remains a word-level countermodel only; its canonical path fails legality and it is not a full-phase retained object.
- The `m=17` resource wall is non-evidentiary.
- No elimination of Branch A or Branch B is claimed.

## Closeout verification

Fresh closeout checks:

- `verify_rl248_bridge_fast.py`: PASS
  - rigid checks: 16,384
  - terminal-selector checks: 31
  - extremal barrier audit checks: 7,741
  - fixed-form red-team beta: 6
  - canonical red-team failure reproduced at internal step 4, `(d,J,u)=(1,-6,1)`
- `verify_rl248_bounded_counterflow_scale.py`: PASS
  - determinant tuples: 21
  - deterministic word checks: 420
  - physical sites: 27,140
  - local phase cases: 637
  - exact `b=6` aggregate `2/6561 > 1/4374`
- fresh C++ exact run-compressed replay through `m=16`: PASS
  - `m=14`: 4,828,447 states
  - `m=15`: 14,012,393 states
  - `m=16`: 41,178,667 states
  - `m=16` height-one states: 9,399,300
  - maximum height-one `J`: 77,393,553,539,624
  - power exponents: `1,3,5,7,9,11,13,15,17,21,23`
  - no exponent `>=31`

## Successor

RL249 should attack the newly isolated `beta(P)=6` Branch-C phase-budget problem rather than extend the unrestricted `m=17` superset.

Primary task: consume the valid absolute aggregate phase gain against the exact full-phase/ordered-state ledger. Prove either:

1. `beta(P)=6` is incompatible with full-phase completion; or
2. any compensation forces explicit canonical `10` descent/event structure that yields enough height/rank information for Gate A or supplies an audited exact Radius-4 eligible encounter.

If `beta(P)=6` is eliminated, propagate the same cocycle method to higher `beta(P)` before returning to Branch A/B as needed.
