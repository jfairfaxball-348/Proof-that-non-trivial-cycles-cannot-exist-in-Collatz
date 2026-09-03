# RL244 checkpoint — zero-counterflow determinant-2 tail rigidity

Date: 2026-09-03

Classification: **`R4_BRIDGE_REDUCED`**.

This is a research checkpoint, not a full authoritative promotion. `authoritative/START_HERE.md` remains the RL244 kickoff inherited from checksum-clean RL243. Gate A remains open uniformly, Gate B remains open, global non-trivial-cycle exclusion remains open, and Radius 5 remains inactive.

## 1. Incoming authority and verification economy

Live incoming authority is RL243, commit `caf5f931879682afd248cb7e6b59e828ab00ea79`, canonical ZIP SHA256

`4e7a85402d9af86ec7c0dc3282aafcec18acf97f9c8ca1402849e99cb7afa08f`.

The frozen RL243 fresh-unpack record reports:

- fresh unzip: PASS;
- internal SHA256SUMS: PASS;
- portable fast verifier: PASS;
- cyclic interval checks: 1,495;
- small-word flow checks: 1,711;
- entry-crossing checks: 5,103.

Under the repository verification-economy rule, the incoming RL243 ledger is accepted after this gate; historical expensive certificates were not recursively rerun.

The live RL244 split is retained exactly. In RL243 notation

`P_i = r-W_i^u(q)`, `Q_i=r-W_i^v(q)`, `ar-qell=2`,

with

`Q_i-P_i=h_i-h_(i+q)`.

The auxiliary `P,Q` are not Radius-4 theorem inputs.

## 2. Zero-counterflow support rigidity

Assume the RL244 branch

`beta(P)=0`.

RL243/RL244 supplies that `P` is integer-valued, cyclic adjacent-1-Lipschitz, and has signed mass

`sum_i P_i = ar-qell = 2`.

Since `beta(P)=0`, every `P_i>=0`. If some `P_i>=2`, adjacent 1-Lipschitzness forces both cyclic neighbours to be at least 1; as `a>=27` on the retained `ell>=17` resonance branch, these are distinct and the total mass would be at least 4. Therefore

`P_i in {0,1}` for every `i`,

and exactly two indices have `P_i=1`.

The two unit defects need not be separated: they may be adjacent. This distinction matters below.

At an owned zero-to-positive entry crossing `i`, put

`c_i=h_(i+q)>0`.

Then

`Q_i=P_i-c_i`.

If `E={i:h_i=0<h_(i+q)}` and `Gamma_q=sum_(i in E)c_i`, the exact entry contribution is

`sum_(i in E)(-Q_i)_+ = Gamma_q - |supp(P) intersect E|`.

Thus the inherited `Gamma_q-2` floor is sharp only if both unit defects land on entry crossings; otherwise it improves by one or two. This support-aware sharpening is useful bookkeeping but is not by itself a Radius-4 encounter.

## 3. The two defects force near-periodicity of the physical half-word

The length-`q` cyclic window recursion gives the exact identity

`P_(i+1)-P_i = u_i-u_(i+q)`.

Hence the mismatch edges between `u` and its `q`-rotation are exactly the transition sites of `P`.

Because `P` is the indicator of two sites:

- if its two unit defects are adjacent in the ordinary `i` coordinate, `P` has exactly 2 cyclic transitions;
- otherwise it has exactly 4 cyclic transitions.

Therefore the `q`-ordered word `u` has at most two zero blocks (and at most two one blocks) across all `q`-orbits. This converts zero counterflow into a rigid near-periodicity statement about the genuine physical half-word rather than an abstract mass bound.

Also, from

`ar-qell=2`,

`g=gcd(a,q)` divides 2, so

`g in {1,2}`.

Write

`z=a-ell`,

so `z` is the number of zeroes in `u`. The retained RL243 resonance

`19/12 < a/ell < 8/5`

implies

`7a/19 < z < 3a/8`.

The exact full-phase word form inherited from RL64-RL65 is

`u=110 x 1 0^t`,

with

`t=k-3`

and inherited RL66 gives odd `k>=3`.

## 4. Coprime determinant case: `gcd(a,q)=1`

Let `s=q^(-1) mod a`, with `1<=s<a`. Reducing the determinant identity modulo `a` gives

`q ell == -2 (mod a)`.

Multiplying by `s` and using `z=a-ell` gives

`2s == z (mod a)`.

Because `0<z<a`, exactly one of

`2s=z`,

`2s=a+z`

holds as an integer equality.

If odd `k>=7`, the terminal block `0^t` contains four consecutive ordinary zeroes. In the `q`-ordered coordinate these four zeroes occur at

`{0,s,2s,3s}`

up to a cyclic translation.

### Case 4.1: `2s=z`

The four points are

`{0,z/2,z,3z/2}`.

Their cyclic gap lengths are

`z/2, z/2, z/2, a-3z/2`.

A union of at most two cyclic integer intervals containing all four points has minimum cardinality

`a - [(a-3z/2)+(z/2)] + 2 = z+2`.

But the entire word contains exactly `z` zeroes. Contradiction.

### Case 4.2: `2s=a+z`

Here `z>7a/19>a/3`, and the four points sort as

`{0,(3z-a)/2,z,(a+z)/2}`.

The cyclic gap lengths are

`(3z-a)/2, ell/2, ell/2, ell/2`.

Again the two largest gaps have total length `ell`, so any two cyclic intervals containing the four points have minimum cardinality

`a-ell+2=z+2`,

again impossible.

Thus in the coprime determinant case `beta(P)=0` forbids every odd `k>=7`.

## 5. Two-orbit determinant case: `gcd(a,q)=2`

Write

`a=2A`, `q=2Q`.

Dividing the determinant identity gives

`Ar-Qell=1`,

so `gcd(A,Q)=1`.

Put

`delta=ell-A`.

The retained resonance gives

`A/4 < delta < 5A/19`,

and

`z=a-ell=A-delta`.

Let `s=Q^(-1) mod A`. Reducing `Ar-Qell=1` modulo `A` gives

`Qell == -1 (mod A)`,

hence

`s == -ell == A-delta == z (mod A)`.

The `q`-rotation has exactly the two parity orbits, each of length `A`.

For `k>=5`, the terminal tail has at least two consecutive zeroes and therefore places a zero in each parity orbit. No orbit can have zero transitions: it cannot be all ones because it contains a terminal zero, and it cannot be all zeroes because that would contribute `A>z` zeroes. Each cyclic orbit therefore has at least two transitions.

Since the total number of mismatch transitions is only 2 or 4, it must be exactly 4, split 2+2. Consequences:

1. the two unit defects of `P` are non-adjacent in the ordinary coordinate;
2. the zero set in each parity `q`-orbit is one cyclic interval.

### 5.1 Excluding `k>=9`

For `k>=9`, the terminal zero tail contains at least six zeroes; five consecutive zeroes suffice. Among five consecutive ordinary positions, one parity supplies three consecutive reduced positions and the other supplies two.

In reduced parity coordinates, ordinary step 1 maps in `q`-order by

`s=z=A-delta == -delta (mod A)`.

A single cyclic zero interval containing three consecutive reduced zero positions therefore needs at least

`2delta+1`

zeroes. The other parity zero interval containing two consecutive reduced zero positions needs at least

`delta+1`.

Thus the whole word would need at least

`3delta+2`

zeroes. But

`z=A-delta < 3delta`

because `delta>A/4`. Contradiction.

Hence `k<=7` in this case.

### 5.2 Excluding `k=7`

Now `t=4`, and use the fixed beginning and terminal tail of

`u=110 x 1 0000`.

In the even reduced parity orbit:

- coordinate `0` is `u_0=1`;
- coordinate `1` is `u_2=0`;
- coordinates `A-2,A-1` are terminal zeroes.

In the odd reduced parity orbit:

- coordinate `0` is `u_1=1`;
- coordinates `A-2,A-1` are terminal zeroes.

Under multiplication by `s=A-delta` into `q`-order,

`1 -> A-delta`,

`A-1 -> delta`,

`A-2 -> 2delta`.

Each parity zero set is one cyclic interval and must avoid q-order coordinate 0, because that coordinate contains the fixed initial one. Therefore:

- the even zero interval contains `delta,2delta,A-delta` while excluding 0, forcing size at least `A-2delta+1`;
- the odd zero interval contains `delta,2delta` while excluding 0, forcing size at least `delta+1`.

The total number of zeroes is therefore at least

`A-delta+2=z+2`,

contradicting the exact zero count `z`.

Thus `k=7` is impossible as well.

## 6. Zero-counterflow tail-rigidity theorem

Combining Sections 4 and 5 with odd `k>=3`:

### Theorem RL244.ZC

For a retained determinant-2 full-phase object satisfying the RL243 resonance and `beta(P)=0`,

`k in {3,5}`.

Equivalently, every odd `k>=7` retained full-phase object has

`beta(P)>0`.

This is an analytic theorem. It does not apply Radius 4 to `P`, and it does not identify `P,Q` as physical theorem inputs.

## 7. Gate-A routing of the two residual exponents

The two residual exponents are handled without claiming a uniform Gate-A theorem.

### `k=3`

Inherited RL67 proves analytically that every canonical terminal path has `H>=3`. Thus `k=3` is Gate-A-safe.

### `k=5`

For a hypothetical Gate-A survivor one would need `H<5` and terminal

`(d,J)=(1,32)`.

The new portable verifier

`sessions/RL244/verification/verify_rl244_k5_low_area.py`

runs the exact frozen RL67 recurrence from `(d,T,H)=(1,-14,0)` and prunes only states with `H>=5`. Since each increment of `H` is nonnegative, this loses no `H<5` terminal.

The complete retained state set first repeats at depth 16 with the state set from depth 13:

- first repeat depth: 13;
- repeat depth: 16;
- exact period: 3;
- repeated state count: 47;
- checked state occurrences before repeat: 435;
- target `(d=1,J=32,H<5)`: absent.

Because the transition operator is deterministic on the complete set, exact repetition of the whole state set proves the target absent for all later depths as well. This is therefore an exhaustive finite-state certificate, not a bounded-depth extrapolation.

So `k=5` is Gate-A-safe too.

### Scope of this routing

This does **not** prove Gate B, and it does **not** prove uniform Gate A. It proves that a `beta(P)=0` determinant-2 object cannot remain a simultaneous unresolved survivor: the only possible terminal exponents are already discharged by Gate A.

Accordingly the unique unresolved RL244 combined obstruction is reduced to

`beta(P)>0`.

## 8. Remaining live obstruction

In the surviving branch there exists an index `i` with

`P_i<0`.

By the exact RL243 physical envelope identities, that same negative `P_i` is inherited at the same `u`-half index by both genuine determinant-4 physical flows. This is a **same-index double physical valley**, not two unrelated abstract negatives.

The next attack should remain narrowly on this branch:

1. choose/normalize a negative `P_i` with the strongest owned-prefix status available;
2. map the paired physical roots `i` and `i+a` into the canonical zero-carry states;
3. use the ordered RL64-RL69 `d,T,H,J` / rank interface to constrain those two states at the same index;
4. seek either an eligible primitive full-`D` exact-distance-4 self-rotation satisfying every RL238/RL239 hypothesis, or an exact contradiction to full phase;
5. do not revive generic packing, physical-scale anti-concentration, bare radius-shell arguments, Radius 5, or auxiliary-flow misuse.

## 9. Reproduction

From repository root:

`python3 sessions/RL244/verification/verify_rl244_k5_low_area.py`

Expected output:

`RL244 k=5 low-area automaton certificate: PASS`

`first_repeat_depth=13`

`repeat_depth=16`

`period=3`

`repeated_state_count=47`

`checked_state_occurrences=435`

`target=(d=1,J=32,H<5): absent for all depths`

## 10. Checkpoint status

Classification: **`R4_BRIDGE_REDUCED`**.

Promoted checkpoint facts:

- `beta(P)=0` forces exactly two unit defects;
- zero counterflow implies a 2-or-4-transition near-periodicity of the physical half-word;
- determinant arithmetic restricts the `q`-rotation to one or two cycles;
- the fixed `110` prefix, terminal `0^(k-3)` tail, and retained resonance prove `beta(P)=0 => k in {3,5}`;
- `k=3` is inherited analytically Gate-A-safe;
- `k=5` is now independently discharged by a tiny complete exact low-area automaton certificate;
- the only simultaneous unresolved RL244 branch is `beta(P)>0`, the same-index double physical valley.

No full closeout or authoritative promotion is performed at this checkpoint.
