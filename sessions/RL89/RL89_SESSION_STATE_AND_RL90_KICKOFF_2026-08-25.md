# RL89 SESSION STATE AND RL90 KICKOFF

Date: 2026-08-25

## Frozen global status

- radius-3 primitive/full-`D`: closed local theorem;
- Gate A even terminal `k`: closed analytically;
- Gate A terminal `k<=25`: closed by inherited exact finite certificate;
- Gate A odd `k>=27`: open globally;
- Gate A globally: open;
- Gate B globally: open;
- RL/nontrivial-cycle exclusion: open;
- Collatz conjecture: not proved.

The first-Farey branch has been narrowed further, but remains branch-specific.

## Incoming RL89 gate

- outer SHA-256: PASS;
- fresh internal manifest: PASS;
- RL88 fast verifier: PASS.

Verification economy was applied. No historical expensive suite was recursively replayed.

## Frozen RL89 main results

### Saturated excursion grammar

Let `E=H-e`.

- If `E=0`, every complete excursion is exactly `01,10`.
- If `E=1`, exactly one excursion is `01,00,10` or `01,11,10`; all others are `01,10`.

### Cofactor recurrences

For block entry `delta=2^n m`, signed odd `m`, and `s` synchronized `11` columns:

- minimal `01,10`:
  `3^(s+1)m-1=2^(n_next+2)m_next`;
- plateau `01,00,10`:
  `3^(s+1)m-3=2^(n_next+3)m_next`;
- plateau `01,11,10`:
  `3^(s+2)m-5=2^(n_next+3)m_next`.

### Exact 2-adic finite certificate

For every signed odd

`0<|m|<2^29`

and every physical exponent

`1<=a<=42,150,931,629`,

the exact modulo-`2^64` discrete-log scan finds only

`(m,a)=(101,319,985,27,039,197,284)`

and

`(303,959,955,27,039,197,283)`.

Both have

`v2(3^a m-1)=65`.

Therefore:

`C-n<=28` + minimal excursion => `n_next<=63`.

### Transition-deficit theorem

For `b` actual nonempty blocks, `D_b=Cb-Q`, and

`G_28>=b-floor(D_b/29)`,

every survivor must satisfy

`G_28 <= (k-1-b)+floor(D_b/(C-63)).`

The first term on the right pays for nonminimal/zero-successor exceptions; the second pays for forced short nonempty successors.

### First-Farey endpoint eliminated

The RL88 lower endpoint

`k=2,921,384,819`

is impossible in both feasible block-count cases.

Updated exact first-Farey odd window:

`boxed: 2,921,384,821 <= k <= 42,150,931,559.}`

No global Gate-A promotion is made.

### Next odd localization

At

`k1=2,921,384,821`,

the two low block-count cases are impossible. Every survivor must satisfy

`boxed: b>=k1-2=2,921,384,819.}`

Hence only `b=k-2` or `b=k-1` remains, and all complete excursions are minimal except at most one single height-two plateau in the `H=e+1` case; at most one zero-length return slot can occur.

### Fixed block-count interval exclusions

- `b=2,921,384,817` impossible through `k=3,527,154,083`;
- `b=2,921,384,818` impossible through `k=3,116,403,917`.

These are block-count-stratum exclusions, not full `k`-interval elimination.

## Authoritative RL90 live obligation

Continue the same near-capacity 2-adic transition attack at `k1`.

The surviving strata are now:

1. `b=k-2`, actual deficit `106,858,350,489`, average deficit about `36.58`;
2. `b=k-1`, actual deficit `149,009,282,117`, average deficit about `51.01`.

For `b=k-2`, at least `33,321,293` blocks have deficit `<=36`. A covering theorem for cofactors `|m|<2^37` that leaves only very few long-reset exceptions would close this stratum.

Priority:

1. build a certified 2-adic covering/sieve for the deficit-36 cofactor range without enumerating all `2^37` values;
2. factor out powers of `3` in `m` and work with 3-free seed cofactors;
3. quantify the sparse set of `m` for which `v2(3^a m-1)` can exceed the short-successor threshold with `a<=C+1`;
4. combine the exception count with the tiny total block deficit and `H-b<=1` in the `b=k-2` stratum;
5. if closed, repeat at the deficit-51 `b=k-1` stratum;
6. only then seek a common-mode selector if multiplicity of exceptional cofactors becomes the obstruction.

## Sustained attack rule — mandatory from RL90 onward

A theorem, certificate, endpoint elimination, or improved bound is a checkpoint, not a reason to close the session.

Continue through immediate consequences, case propagation, parameter extension, red-team, and the strongest adjacent continuation until context/compute pressure becomes genuinely prohibitive, a stop-and-repair condition occurs, or the route and its natural adjacent continuations are rigorously exhausted.

Do not convert this into extra historical verification. Keep the verification-economy rule:

> After the current bundle checksum, internal manifest, and fast verifier suite pass, accept the frozen incoming proof-state ledger as authoritative. Do not recursively rerun historical expensive certificates unless a new proof depends on an unresolved historical definition, a verifier fails, or an apparent contradiction triggers stop-and-repair. Prioritize new mathematics on the live obstruction.
