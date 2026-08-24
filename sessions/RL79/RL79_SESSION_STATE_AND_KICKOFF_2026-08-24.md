# RL79 SESSION STATE AND KICKOFF

Date: 2026-08-24

## 0. Authority and scope

**AUTHORITATIVE OUTGOING RL79 RESEARCH STATE.** Gate A remains open globally, Gate B remains open globally, and no RL/nontrivial-cycle/Collatz closure is claimed.

RL79 completed the post-tournament common-barrier synthesis requested by the RL78 handover and generated/tested new theorem architectures.

Detailed mathematics:

`RL79_POST_TOURNAMENT_COMMON_BARRIER_SYNTHESIS_AND_UNIT_INCREMENT_RESET.md`.

Selected next target:

`RL80_BLUE_DYADIC_FUNNEL_AND_CERTIFIED_BASIN_TARGET.md`.

## 1. Verification economy rule — retained

After the current bundle checksum, internal manifest, and fast verifier suite pass, accept the frozen incoming proof-state ledger as authoritative. Do not recursively rerun historical expensive certificates unless a new load-bearing argument depends on an unresolved historical definition, a verifier fails, or an apparent contradiction triggers stop-and-repair.

## 2. Incoming RL78 gate

The uploaded RL78 gate passed before RL79 mathematics:

- outer RL78 sidecar: **PASS**;
- freshly unpacked RL78 internal `SHA256SUMS.txt`: **PASS**;
- `bash verification/run_fast_rl78_verifiers.sh`: **PASS**.

The first internal-manifest command was run one directory above the ZIP's top-level bundle directory and returned only a path error. It was immediately rerun from the actual bundle root and passed. No checksum or mathematical verifier failed.

No expensive historical suite was recursively rerun.

## 3. Strategic baseline

RL72 global audit and RL75 route tournament were recovered selectively from GitHub provenance. RL75 ranked:

1. owned macro periodicity/packing;
2. product/growth/CF + modern full phase;
3. global `D|Q`/ownership bounded-radius Gate B;
4. two-scale pump Diophantine incompatibility.

RL76–RL78 seriously tested the first three and exposed the free-scale, coordinate-change and ownership-defect barriers.

## 4. New RL79 theorem A — canonical generalized-increment cycle

For a binary word `w`, `D=2^A-3^L>0`, rotation numerators `Q_m`,

`g=gcd(D,Q_0)`, `s=D/g`, `n_m=Q_m/g`,

one has exactly

`2n_(m+1)=n_m` on a `0` bit,

`2n_(m+1)=3n_m+s` on a `1` bit.

The `n_m` are positive integers, their parities are exactly the word bits, and `gcd(n_m,s)=1`. If the word is primitive, the states are distinct and form a primitive positive integer cycle of

`T_s(n)=n/2` (even), `(3n+s)/2` (odd).

Genuine Collatz ownership is exactly `s=1`.

Classification: **analytic theorem**.

## 5. New common barrier — unit increment / homogeneity

The generalized maps satisfy

`T_(cs)(cn)=cT_s(n)`

for positive odd `c`, and `x=n/s` satisfies the ordinary rational `+1` affine recurrence.

Therefore any invariant homogeneous in `(states,s)` or expressed only in normalized rational phases `n/s` cannot distinguish genuine `s=1` from ownership-defect `s>1`.

Classification: **analytic method barrier**.

## 6. New RL79 theorem B — polynomial rotation algebra collapses modulo D

Modulo `D`, every rotation numerator is

`Q_m==u_m Q_0`, `u_m=3^(P_m)2^(-m)`.

Hence every polynomial in all rotation numerators reduces to a one-variable polynomial in `Q_0`; homogeneous degree-`r` expressions reduce to `Q_0^r` times a word-unit coefficient.

Quadratic/higher cross-rotation minors at modulus `D` therefore do not provide a second independent ownership condition.

Classification: **analytic method barrier**.

## 7. New RL79 theorem C — full owned monodromy degeneracy

The full word map satisfies

`2^A(F_w(x)-x)=Q-Dx`.

If `D|Q`, then `F_w(x)==x (mod M)` for every `M|D` and every integer `x`.

Thus pure multiplicative/affine order analysis of the full return map modulo denominator prime powers is structurally degenerate.

Classification: **analytic method barrier**.

## 8. New RL79 theorem D — Vandermonde identity and 2-adic collapse

For a primitive positive `T_s` cycle with even states `E`, odd states `O`, `|O|=L`,

`2^(C(A,2)) |prod_(e,o)(e-o)|`

`=3^(C(L,2)) |prod_(e,o)(e-3o-s)|`.

Its attractive 2-adic consequence

`sum_(e,o) v2(e-3o-s)=C(A,2)`

collapses exactly to the pure word identity

`sum_(i:d_i=0,j:d_j=1) LCP(rot_(i+1)w,rot_(j+1)w)`

`=C(A-L,2)+C(L,2)`.

The full product is homogeneous in `(states,s)` and is also denominator-blind after normalization.

Classification: **analytic theorem + method barrier**.

## 9. New RL79 theorem E — generalized moment hierarchy

For `E_r=sum even states^r`, `O_r=sum odd states^r`, `O_0=L`,

`(2^r-1)E_r+(2^r-3^r)O_r`

`=sum_(j<r) C(r,j)3^j s^(r-j)O_j`.

In particular

`E_1-O_1=Ls`,

`3E_2-5O_2=6sO_1+Ls^2`.

The hierarchy is homogeneous in `(states,s)` and therefore does not itself force `s=1`.

Classification: **analytic global identities / raw route demoted**.

## 10. RL20 fake sharpened again

The exact radius-4 fake has `gcd(D,Q)=1`, hence `s=D`.

Its rotation numerators form a positive primitive **integer** `T_D` cycle with exactly the fake parity word and `gcd(state,D)=1` at every phase. It satisfies the RL79 moment and Vandermonde identities.

Thus fake compatibility extends far beyond rational phases: global integer permutation structure also survives once the odd increment is allowed to be `s`.

## 11. RL79 route decision

The post-tournament common failure is now sharper:

- normalized/coboundary algebra loses ownership;
- physical scale absorbs uniform costs;
- local grammar has canonical generalized cycles;
- homogeneous global invariants see only normalized rational phases and do not use `s=1`.

The genuinely live class is **non-homogeneous, ordinary-Collatz-specific information**.

Because RL79 is mainly a negative/common-barrier session, RL80 is deliberately pivoted to the requested **proved-blue dyadic funnel / certified basin** route. This is strategically justified because basin membership belongs specifically to the ordinary `+1` Collatz map and is not a homogeneous `T_s` invariant.

Retain as secondary: search for any other non-homogeneous unit-lattice/content obstruction forcing or exploiting `s=1`.

## 12. Correction/demotion ledger additions

Retain all RL72–RL78 corrections and add:

- generalized-increment realization theorem;
- ownership is exactly `s=1` after canonical reduction;
- homogeneous `(states,s)` identities are not ownership tests;
- nonlinear cross-rotation polynomial searches modulo `D` are rank-one reductions;
- full-return prime/order modulo `D` is degenerate under ownership;
- Vandermonde 2-adic energy is a pure word LCP tautology;
- raw moment hierarchy is denominator-blind after normalization;
- successful future routes must consume a non-homogeneous fact special to `s=1`.

## 13. Exact proof state after RL79

Unchanged global closure state:

- radius-3 primitive/full-`D`: **closed local obstruction**;
- Gate A even `k`: **closed analytically**;
- Gate A `k<=25`: **closed by exact finite-certificate corollary**;
- Gate A odd `27<=k<=165`: **open**;
- Gate A globally: **open**;
- Gate B globally: **open**;
- RL/nontrivial-cycle exclusion: **open**;
- Collatz conjecture: **not proved**.

## 14. RL79 verifier status

`python3 verification/verify_rl79_common_barrier_reset.py`: **PASS**.

Exact counts:

- primitive generalized-increment cycles checked: `1,578`;
- rotation polynomial-collapse checks: `148,730`;
- monodromy checks: `9,476`;
- generalized moment checks: `4,734`;
- small-word Vandermonde checks: `1,578`;
- all-word LCP-collapse checks: `1,578`;
- RL20 fake Vandermonde `v2` total: `16,836`.

---

# Self-contained kickoff for RL80

Continue the Collatz R-sharp / RL research from the authoritative RL79 bundle and matching `.sha256` sidecar.

First verify only the current RL79 gate:

1. outer RL79 sidecar;
2. freshly unpacked internal `SHA256SUMS.txt`;
3. `bash verification/run_fast_rl79_verifiers.sh`.

Apply the verification-economy rule after those pass.

The primary target is:

# **RL80 — infinite proved-blue dyadic funnel / certified basin obstruction**

Use `RL80_BLUE_DYADIC_FUNNEL_AND_CERTIFIED_BASIN_TARGET.md` as the authoritative research target.

The RL79 structural lesson is mandatory context: every primitive above-resonance word has a canonical positive integer generalized-`T_s` cycle, and homogeneous word/state identities usually ignore the distinction between `s=1` and `s>1`. Therefore the blue-basin route is valuable precisely because membership in the actual basin of `1` is a discrete property of the ordinary `s=1` Collatz map, not a homogeneous generalized-map invariant.

Do not reduce the blue-funnel investigation to density or powers-of-two abundance. Seek an unavoidable structural intersection between genuine RL ownership/dynamics and the rigorously certified basin. If pure dyadic saturation is too thin, broaden only to rigorously legal backward-preimage trees.

Retain RL79's non-homogeneous unit-lattice/content route as a secondary alternative.

Before ending, freeze exact proofs, failures, dependencies, corrections and verifier status; create the next numbered authoritative bundle and sidecar; verify internal manifest and fresh-unpack fast suite.
