# RL81 — auxiliary basin transfer, physical lift separation, and terminal common-mode barrier

Date: 2026-08-24

## 0. Executive outcome

RL81 executed the RL80-selected basin-transfer target from a checksum-clean incoming state.

No Gate A, Gate B, RL/nontrivial-cycle, or Collatz closure is claimed.

The strongest positive RL80 fact survives unchanged: for a terminal all-`11` synchronized suffix, the auxiliary height-one quotient entry

`J_0 = 2^j(2^k+1)/3^j - 1`

is in the ordinary Collatz basin of `1`, and for `k>=3`

`n_0=(J_0-1)/2`

is also in that basin.

RL81 recovers the exact physical lift and proves that this basin capture lives in the **difference coordinate**, not in either physical cycle coordinate.

The key exact reconstruction is

`J = 3A-B+1`

at height one, where `A,B` are the genuine positive shortcut-Collatz states of the two RL48 half-trajectories.

For a terminal all-`11` suffix of length `j` ending at `J_j=2^k`, write

`q=(2^k+1)/3^j`.

Then the quotient trajectory is

`J_r = 2^(j-r)3^r q - 1`.

But the physical lift has a free common-mode parameter. For every sufficiently large integer `a` in one explicit residue class, set

`b=3a-q`,
`A_0=2^j a-1`,
`B_0=2^j b-1`.

Then the same synchronized `11^j` quotient trajectory occurs, and after the canonical terminal `(1,0)` edge and `t=k-3` zero tail the physical trajectories land at

`N+4` and `N`

with

`N = [3^(j+1)a - 2^k - 2]/2^(k-2)`.

Varying `a` by `2^(k-2)` changes `N` by `3^(j+1)` while leaving the entire auxiliary `J` suffix unchanged. A subprogression has `N==3 (mod8)` and arbitrarily large `N`.

This proves a sharp route barrier:

> **The terminal all-`11` blue auxiliary coordinate does not determine, or basin-transfer to, a physical cycle state by the existing quotient reconstruction. The quotient deliberately cancels the common-mode cycle value.**

The exact RL50 normalized lifts `U,V` do retain the common mode, but only as rational rescalings of the physical states:

`U_i = 2^(i+3)A_i/3^(p_x+2)`,
`V_i = 2^(i+3)B_i/3^(p_y+3)`.

Recovering `A_i,B_i` from them requires powers of `3` as well as powers of `2`; this is not an ordinary-Collatz basin-preserving operation. The difference quantities `R,L,J,n` contain the quotient separation, while `U,V` contain the physical common mode, and no inherited theorem supplies a basin-preserving bridge between the two layers.

RL81 also consumes the RL66 all-`11` phase-digit refinements on the currently open Gate-A range `27<=k<=165`, odd `k`. An exact finite certificate checks every RL66-allowed all-`11` suffix and rules out the simplest possible accidental promotion:

`J_0` and `n_0` are never equal to either full-phase midpoint `N` or `N+4`.

Therefore the all-`11` architecture—the most favorable case because `11` on `J` is literally the ordinary odd Collatz step—fails at the coordinate-transfer layer. Per the RL81 stop condition, mixed/all-`00` basin capture is not expanded.

The blue route is now frozen as a useful **recognition theorem plus transfer barrier**, not a closing route.

RL82 is redirected to RL79's surviving non-homogeneous class:

# absolute unit-lattice / exact-content consequences of the specialization `s=1`.

---

## 1. Incoming verification economy gate

The uploaded RL80 bundle has outer SHA-256

`ffb3be580c01e14fc8a5ab4bac466cd42f0cace6a16fc3584b11f1c6d0bdd78d`

and matches its supplied sidecar.

Fresh unpack:

- internal `SHA256SUMS.txt`: PASS;
- inherited RL79 sidecar: PASS;
- `bash verification/run_fast_rl80_verifiers.sh`: PASS;
- RL80 blue-basin verifier: PASS.

Under the verification-economy rule the frozen RL80 ledger was accepted. No historical expensive finite suite was recursively rerun.

---

## 2. Frozen inherited proof state

Retain RL80 exactly:

- radius-3 primitive/full-`D` local obstruction: closed;
- Gate A even terminal `k`: closed analytically;
- Gate A terminal `k<=25`: closed by exact finite-certificate corollary;
- Gate A odd `27<=k<=165`: open;
- Gate A globally: open;
- Gate B globally: open;
- RL/nontrivial-cycle exclusion: open;
- Collatz conjecture: not proved.

Retain RL79's mandatory red-team principle: a successful global route must use a non-homogeneous fact special to the ordinary `+1` map, not merely a homogeneous generalized-`T_s` identity.

---

## 3. Exact physical coordinate recovery

RL48's full phase produces genuine shortcut-Collatz half-trajectories from midpoint values `N` and `N+4`.

Along the internal pair path write their current physical states as `A_i,B_i`. The exact RL coordinate is

`T_i = 3^(d_i) A_i - B_i`.

At height `d=1`,

`J=T+1`,

so

`boxed: J = 3A-B+1`.                                      (3.1)

RL50 then defines

`n=(J-1)/2=T/2`,
`g=2^i/3^(p_x)`,
`R=gT/3^d`,
`L=g(J-1)/2` at height one,

and normalized physical lifts

`boxed: U_i=2^(i+3)A_i/3^(p_x+2)}`,
`boxed: V_i=2^(i+3)B_i/3^(p_y+3)}`.                    (3.2)

They satisfy

`U_i-V_i=(8/9)R_i`.

At the canonical internal entrance,

`U_0=N+5/9`,
`V_0=N+127/27`,
`R_0=-14/3`.

Classification: **exact inherited coordinate recovery**.

### Interpretation

The coordinates split into two kinds.

1. `J,n,T,R,L` are separation/difference coordinates; at fixed path weights they forget a common physical mode.
2. `U,V` retain the physical mode, but they are rationally normalized by powers of `2` and `3`.

This distinction is the central RL81 transfer issue.

---

## 4. Exact terminal physical states

RL48 proves that before the omitted terminal pair `(1,0)` one has

`J=2^k`, `k=t+3`.

Let the physical states at that point be `A_j,B_j`.

The omitted `(1,0)` step followed by `t=k-3` synchronized zero steps returns the two half-trajectories to the midpoint pair `N+4,N`.

Therefore exactly

`(3A_j+1)/2 = 2^t(N+4)`,
`B_j/2 = 2^t N`.

Hence

`boxed: B_j=2^(k-2)N}`,                                  (4.1)

`boxed: A_j=[2^(k-2)(N+4)-1]/3}`.                       (4.2)

Then

`3A_j-B_j = 2^k-1`

and so `J_j=2^k`, as required.

Classification: **new analytic unpacking of the exact RL48 terminal geometry**.

### Consequence 4.1 — terminal `J` deletes the physical midpoint

Equations (4.1)-(4.2) contain `N`, while

`J_j=3A_j-B_j+1=2^k`

contains no `N`.

Thus the terminal auxiliary power of two is exactly a cancellation of the physical common mode.

---

## 5. All-`11` physical lift theorem

Assume the terminal synchronized suffix is `11^j`, `j>=1`.

RL64 gives

`3^j q=2^k+1`,
`q` odd,

and

`J_0+1=2^j q`.

### Theorem A — quotient trajectory

For `0<=r<=j`,

`boxed: J_r=2^(j-r)3^r q-1}`.                           (5.1)

In particular `J_j=2^k`.

Classification: **inherited analytic theorem**.

### Theorem B — full family of physical lifts of the same quotient suffix

Choose an integer `a` and define

`b=3a-q`,
`A_0=2^j a-1`,
`B_0=2^j b-1`.

Then for `0<=r<=j`,

`boxed: A_r=2^(j-r)3^r a-1}`,
`boxed: B_r=2^(j-r)3^r b-1}`.                           (5.2)

Every input for the first `j` columns is odd, so `(A_r,B_r)` follows `11^j`, and

`3A_r-B_r+1 = J_r`

for every `r`.

Classification: **new analytic physical-lift theorem**.

### Proof

The ordinary odd shortcut map sends

`2^m c-1 -> 3*2^(m-1)c-1`.

Iterating gives (5.2). Also

`3a-b=q`,

so

`3A_r-B_r+1=2^(j-r)3^r q-1`.

QED.

### Structural consequence

For fixed `(j,k)` the blue quotient `J_r` is fixed, but `a` is not. The physical states move in a one-parameter family.

Equivalently the height-one projection

`pi(A,B)=3A-B+1`

has the exact kernel direction

`(A,B) -> (A+h,B+3h)`.

This is the common-mode direction removed by the quotient.

---

## 6. Terminal-tail common-mode theorem

The physical lift must also pass the omitted `(1,0)` edge and the `t=k-3` synchronized zero tail.

From (5.2),

`A_j=3^j a-1`,
`B_j=3^j b-1`.

The terminal tail is integral exactly when

`boxed: 3^(j+1)a == 2 (mod 2^(k-2))}`.                 (6.1)

Because `3` is invertible modulo powers of `2`, (6.1) is one residue class modulo `2^(k-2)`.

For any sufficiently large positive representative in that class, define

`boxed: N=[3^(j+1)a-2^k-2]/2^(k-2)}`.                 (6.2)

Then the terminal `(1,0)` plus `k-3` zero columns sends the physical pair exactly to

`A -> N+4`,
`B -> N`.

### Theorem C — infinite terminal physical lift family

If `a` is one solution of (6.1), then so is

`a_m=a+m 2^(k-2)`,

and

`boxed: N_m=N+m 3^(j+1)}`.                              (6.3)

Thus a fixed all-`11` auxiliary suffix `(J_0,...,J_j)` is compatible with infinitely many positive physical terminal lifts.

Because `3^(j+1)` is odd, one residue class of `m mod8` gives

`N_m==3 (mod8)`.

Taking that class and increasing `m` by multiples of `8` gives arbitrarily large physical lifts with the exact radius-three midpoint congruence.

Classification: **new analytic route-barrier theorem**.

### Important scope

This theorem concerns the exact terminal/suffix geometry. The earlier full-phase word still selects a specific `N` by

`N=(V+4*3^ell)/(2^a-3^ell)`.

RL81 is not claiming that every member of the family completes the earlier prefix to a nontrivial cycle.

What the theorem proves is the needed methodological point: **the blue suffix quotient itself cannot determine the physical midpoint.** Any successful transfer must consume new earlier full-phase information that fixes the common mode.

---

## 7. Why the RL50 normalized lifts do not repair basin transfer

One might hope that `U,V` restore the missing physical mode. They do, but not in a basin-preserving coordinate.

From (3.2),

`A_i = 3^(p_x+2) U_i / 2^(i+3)`,
`B_i = 3^(p_y+3) V_i / 2^(i+3)`.

The reconstruction uses multiplication/division by powers of `3` as well as powers of `2`.

Ordinary Collatz basin membership is preserved under multiplication by powers of `2`, but there is no inherited theorem that arbitrary multiplication/division by `3`, or the affine combination between `U,V` and `J`, preserves the basin.

At the entrance the issue is visible immediately:

`U_0=N+5/9`,
`V_0=N+127/27`.

These are rational lift coordinates, not ordinary positive-integer Collatz states.

Classification: **analytic coordinate-transfer barrier**.

---

## 8. Forward-basin transfer fails on the open all-`11` range

For the current open Gate-A range,

`27<=k<=165`, `k` odd.

Since

`j<=1+v3(k)`,

one has

`j<=5`.

The RL80 blue orbit of `J_0` runs through

`J_0 -> J_1 -> ... -> J_j=2^k -> 2^(k-1) -> ... ->1`.

Therefore every forward iterate of `J_0` is at most `2^k`.

The RL80 blue orbit of `n_0` is also bounded below this terminal scale before reaching a power of two and then `1`.

Using the stable inherited physical floor `N>=2^71`, equations (4.1)-(5.2), and `j<=5`, every physical `A_r,B_r` in the terminal all-`11` block is strictly larger than `2^k`.

Thus no contemporaneous physical cycle state in the terminal all-`11` block is a forward iterate of `J_0` or `n_0`.

Classification: **analytic corollary on the frozen open parameter range**.

This does not rule out arbitrary long backward-tree constructions; it rules out the direct equality/forward-transfer architecture that RL80 made plausible.

---

## 9. RL66 phase-digit audit of the midpoint equality possibility

The simplest possible global rescue would be an accidental equality

`J_0=N`, `J_0=N+4`, `n_0=N`, or `n_0=N+4`.

RL81 checks this against the exact RL66 all-`11` necessary phase residues over every currently open odd terminal exponent `27<=k<=165`.

For each legal depth

`1<=j<=1+v3(k)`:

- if `j<v3(2^k+1)`, RL66's nonmaximal all-`11` selector is used;
- if `j=v3(2^k+1)`, RL66's maximality condition and next phase digit are used;
- the full-phase midpoint condition `N==3 (mod8)` is also imposed.

### Exact finite certificate D

For every RL66-allowed all-`11` case in the open range,

`boxed: J_0 notin {N,N+4}}`,
`boxed: n_0 notin {N,N+4}}`.

The bundled verifier checks:

- `71` RL66-allowed all-`11` `(k,j)` cases;
- `284` midpoint-equality negative checks.

Classification: **exact finite certificate**, dependent on the frozen finite `k` range and inherited RL66 selector theorems.

---

## 10. Basin-preserving-operation audit

RL81 tested the operations explicitly named in the target.

### 10.1 Equality with a genuine cycle state

No identity exists in the exact reconstruction. The terminal suffix has the infinite common-mode lift family of Theorem C. On the full midpoint pair the possible accidental equalities are excluded by exact finite certificate D in the current open range.

### 10.2 Multiplication by powers of `2`

This preserves basin membership, but the physical lift formulas are not dyadic lifts of `J_0` or `n_0`; they contain the independent common-mode `N`.

At the terminal endpoint,

`B_j=2^(k-2)N`.

This says `B_j` is basin-equivalent to `N`, which is tautological for a physical cycle state. It does **not** relate `B_j` to the blue `J_j=2^k`.

### 10.3 Finite forward shortcut-Collatz steps

On the all-`11` branch the auxiliary forward orbit is explicit and reaches `1`. It remains below the physical terminal-block states on the current open range, so it does not hit them.

### 10.4 Exact legal backward predecessors

A legal backward chain from a blue auxiliary remains blue, so equality with a cycle state would indeed close the branch.

But the RL48 lift does not express `A_i`, `B_i`, `N`, or `N+4` as such a predecessor chain from `J_0` or `n_0`. Instead it expresses them through the independent common-mode parameter and rational physical normalizations.

Allowing the predecessor choices to be chosen from the unknown `N` would simply restate the missing bridge: it would require proving that a genuine cycle state forward-hits the blue auxiliary.

No such theorem is inherited or proved in RL81.

### Audit conclusion

The existing exact reconstruction contains **no basin-preserving transfer operation** from the blue auxiliary coordinate to a genuine cycle integer.

Classification: **route barrier, not an impossibility theorem about every conceivable future relation**.

---

## 11. Why mixed/all-`00` tails are not expanded

RL81's target required the all-`11` branch first and instructed a fast stop if the exact coordinate map showed the capture to be only auxiliary.

That condition is met.

All-`11` is the strongest possible basin overlap because its `J` update

`J -> (3J+1)/2`

is literally the ordinary odd shortcut-Collatz branch.

Yet even there the quotient-to-physical lift loses the common mode.

A `00` quotient step is

`J -> (J+1)/2`

on odd `J`, not the ordinary even Collatz branch. Mixed tails therefore do not improve the transfer architecture and introduce an additional mismatch.

RL81 does not spend computation enumerating them.

Classification: **method stop / route freeze**.

---

## 12. Generalized-map red-team

The RL80 blue theorem is genuinely `s=1`-specific because the legal odd predecessor is

`(2y-1)/3`.

RL81's failure mechanism is different: it is the non-injectivity of the quotient projection from the two physical trajectories to their separation coordinate.

The exact physical identity

`J=3A-B+1`

uses the ordinary `+1` normalization, but the common-mode cancellation shows why merely making `J` an ordinary basin integer does not make either physical coordinate a basin integer.

Thus RL81 does not demote RL80's `s=1` discrimination. It shows that the discrimination is attached to the wrong coordinate for cycle closure.

A future basin theorem would need a genuinely `s=1` statement involving the **physical common mode `N` itself**, not only the quotient separation.

---

## 13. New exact verifier

`verification/verify_rl81_auxiliary_transfer.py` checks:

- `212` RL80 blue auxiliary instances (`J_0` and `n_0`);
- `71` RL66-allowed all-`11` cases in `27<=k<=165`;
- `284` midpoint-equality negative checks;
- `318` explicit terminal-tail physical lifts across the common-mode progressions;
- maximum legal all-`11` depth on the current open range: `5`.

Fresh result:

`RL81 auxiliary-transfer verifier: PASS`.

Classification: **exact finite audit/falsification evidence**.

---

## 14. Correction / demotion ledger additions

Retain all RL72-RL80 corrections and add:

1. **Auxiliary basin capture is not physical basin capture.** `J=3A-B+1` is a separation coordinate.
2. **Terminal common mode is explicitly free at suffix level.** A fixed blue all-`11` quotient suffix lifts to an infinite arithmetic progression of physical midpoint values.
3. **RL50 `U,V` are not basin coordinates.** They retain physical states through rational powers-of-`2`/`3` normalization, not through basin-preserving operations.
4. **Direct equality with the full-phase midpoint pair is closed on the current open all-`11` range.** Exact RL66 phase-digit certificate excludes `J_0,n_0` from `{N,N+4}`.
5. **Direct forward transfer is closed on the current open all-`11` range.** The blue auxiliary forward orbit lies below the terminal physical block.
6. **Mixed-tail basin expansion is frozen.** The most favorable all-`11` case already fails at coordinate transfer.
7. **Blue route reclassified.** Retain as a recognition theorem: if an independent argument ever identifies a genuine cycle state with an RL80 blue node, contradiction is immediate. Do not treat blue abundance or auxiliary capture as a standalone route.
8. **New required consumer.** Any future basin revival must involve the physical common mode `N` in a basin-preserving way.
9. **Strategic pivot.** Return primary attention to RL79's absolute unit-lattice / exact-content `s=1` class.

No inherited Gate-A or radius-3 closure is weakened.

---

## 15. Exact proof state after RL81

### New proved analytic mathematics

- exact terminal physical-state formulas (4.1)-(4.2);
- all-`11` physical lift family (5.2);
- terminal-tail integrality selector (6.1);
- infinite common-mode midpoint progression (6.3);
- quotient/common-mode separation theorem;
- coordinate-transfer barrier for `U,V` versus `J,n`;
- forward-transfer exclusion on the frozen open `k` range.

### Exact finite certificate/audit added

- RL66-compatible midpoint equality no-go over odd `27<=k<=165`;
- terminal physical lift regression checks;
- RL80 auxiliary basin regression checks.

### Externally inherited certificates

- stable `N>=2^71` verification floor retained without re-audit.

### Computational evidence only

- none promoted beyond bounded audit/certificate roles.

### Conjectures/open obligations

- no theorem rules out every conceivable future basin-preserving relation using the full earlier phase quotient;
- no physical-common-mode basin theorem is known;
- Gate A odd `27<=k<=165` remains open;
- Gate B remains open.

### Global closure state

Unchanged:

- radius-3 primitive/full-`D`: closed local obstruction;
- Gate A even `k`: closed analytically;
- Gate A `k<=25`: closed by exact finite-certificate corollary;
- Gate A odd `27<=k<=165`: open;
- Gate A globally: open;
- Gate B globally: open;
- RL/nontrivial-cycle exclusion: open;
- Collatz conjecture: not proved.

---

## 16. Route decision

The RL80/RL81 blue programme has achieved its useful endpoint:

- a strong analytic ordinary-Collatz basin family;
- a logarithmically dense blue mesh;
- exact auxiliary all-`11` basin capture;
- an exact proof that the captured coordinate is a quotient separation;
- an explicit infinite terminal physical lift family showing why the physical cycle state is not determined by that capture.

Continuing by generating more blue nodes, mixed-tail backward trees, residue coverage, or proximity estimates is not recommended.

RL82 should return to RL79's highest surviving non-basin class:

# **absolute unit-lattice / exact-content obstruction for `s=1`**

with the canonical generalized `T_s` cycle as the negative-control framework.
