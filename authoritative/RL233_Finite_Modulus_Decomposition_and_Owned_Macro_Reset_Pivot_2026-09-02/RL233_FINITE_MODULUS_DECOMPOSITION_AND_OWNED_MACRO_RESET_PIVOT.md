# RL233 — finite-modulus decomposition and owned macro-reset pivot

Date: 2026-09-02

## 0. Outcome and scope

RL233 continues the sole surviving high branch `(v,H,J,d)=(37,0,23,-1)` from the verified RL232 state.

**Outcome: Success C.**

RL233 does not prove the desired combined H17 incidence bound `N17<=1,615`. It proves a precise no-go/scaling theorem for the owned endpoint / higher-modulus route at the scope where the finite modulus itself is supposed to be the consumed long-range resource.

For every legal owned-pair path

`2^d_j C_(j+1) = 3 C_j + E_j`, with `d_j>=1`,

all finite congruence information derived solely from the owned numerator / endpoint-return recurrence decomposes into three exhaustive behaviours:

1. the 2-primary component has forced divisibility and exact quotient rebasing;
2. the 3-primary component has finite source-term memory of at most `b` transitions at precision `3^b`;
3. the component coprime to 6 is a reversible affine coordinate for any fixed legal transition-label sequence.

Therefore increasing the endpoint modulus by itself cannot manufacture the missing H17 macro reset cost. A congruence can become useful only through an independently proved restriction on the actual physical legal-tail language, or by adjoining genuinely noncongruential physical information.

No necessary terminal rank is deleted. The frozen frontier remains `13,415,865,870`; e=4 terminal rank `31,435,476,727` remains live with `3,856,660,232` combined arithmetic survivors through transition 43. Combined H17 spacing `>=1001`, the sole high branch, Gate A, Gate B, and global non-trivial-cycle exclusion remain open.

## 1. Exact owned-return telescope

Put

`D_k = sum_(j<k) d_j`

and

`Q_k = 2^D_k C_k - 3^k C_0`.

For every `0<=k<=n`, exact concatenation gives

`Q_n = 3^(n-k) Q_k + 2^D_k T_(k,n)`,

where

`T_(k,n) = 2^(D_n-D_k) C_n - 3^(n-k) C_k`.

For an H17-terminal to H17-terminal return both endpoint maxima are 17, so the inherited exact height telescope `d_j=c_j+M_j-M_(j+1)` gives `D_n` equal to the mechanical exponent sum over the interval.

Classification: proved analytic algebra, conditional only on the exact owned-pair recurrence already inherited by RL232.

## 2. 2-primary component — exact rebasing

The telescope gives

`Q_n - 3^(n-k)Q_k = 2^D_k T_(k,n)`.

Thus every endpoint-return congruence modulo `2^s` with `s<=D_k` is forced automatically. If `s>D_k`, dividing the exact forced factor `2^D_k` gives precisely the suffix return problem `T_(k,n) mod 2^(s-D_k)` based at the exact current owned state `C_k`.

Repeated extraction of higher binary digits therefore does not create a second independent owned return coordinate. It re-bases the same endpoint problem.

Classification: proved analytic state-coboundary / no-go theorem at the dyadic endpoint-modulus scope.

## 3. 3-primary component — finite source-term memory

Modulo `3^b`, every `2^d_j` is invertible. Write `u_j=2^(-d_j) mod 3^b`. Iteration gives

`C_n = 3^n(prod_(t=0)^(n-1) u_t) C_0`

`      + sum_(j=0)^(n-1) 3^(n-1-j)(prod_(t=j)^(n-1)u_t) E_j   (mod 3^b)`.

If `n>=b`, the explicit source term vanishes and all summands with `j<n-b` vanish. Consequently `C_n mod 3^b` is determined by the final `b` transition labels `(d_j,E_j)`.

Scope is important: this is a theorem about the standalone residue state. The legal transition labels may themselves encode earlier physical history. Any such effect belongs to an additional legal-language/physical-state coupling, not to source memory intrinsic to the residue coordinate.

The natural H17 terminal numerators are

`C_A=11*3^32`, `C_B=5*3^33`.

Their natural 3-primary terminal divisibility therefore supplies only local intrinsic residue memory. To make a standalone `3^b` source-term coordinate retain the original source over the spacing-only scale that would itself force `N17<=1,615`, one needs

`b >= floor(L/1616)+1 = 85,103,989`.

The corresponding modulus has approximately 40.6 million decimal digits (about 134.9 million bits). This is a scaling theorem, not a computational-impossibility claim, and source memory alone would still not prove a return exclusion.

Classification: proved analytic finite-memory theorem plus exact scale consequence.

## 4. Unit component — reversible affine coordinate

Let `q` satisfy `gcd(q,6)=1`. For a fixed legal suffix transition-label sequence,

`C_n = A_(k,n) C_k + B_(k,n) (mod q)`,

where

`A_(k,n)=3^(n-k) 2^(-(D_n-D_k)) (mod q)`.

Since both 2 and 3 are units modulo q, `A_(k,n)` is a unit. Hence the q-coordinate is an affine bijection between source and endpoint numerator residues once the legal labels are fixed.

Equivalently, the unit-modulus endpoint return residue is lossless/reversible arithmetic. It has no intrinsic monotone depletion or reset-cost semantics. It can become a genuine consumer only if a separate theorem proves that the actual physical legal-tail language restricts the attainable transition labels/residues strongly enough to force deletion, packing, contradiction, or a useful cycle-average/reset bound.

Classification: proved analytic algebraic no-go theorem at the bare unit-residue scope.

## 5. Complete finite-modulus decomposition

Every integer modulus `m>=2` has the unique form

`m = 2^a 3^b q`, with `gcd(q,6)=1`.

By the Chinese remainder theorem, every finite congruence state derived solely from the owned numerator / endpoint-return recurrence is exactly a product of:

- a 2-primary component that only re-bases after forced divisibility;
- a 3-primary component whose explicit source term vanishes after `b` transitions at precision `3^b`;
- a prime-to-6 component that is reversible for fixed legal transition labels.

Therefore **bare finite-modulus escalation cannot itself supply the missing long-range H17 reset cost**.

This theorem does not rule out:

- a candidate-specific legal-tail automaton in which ownership/height/sign restrictions sharply limit attainable unit residues;
- a hybrid finite state containing genuinely noncongruential physical information;
- a finite automaton with a separately proved globally consumable cycle-average/reset theorem.

It rules out treating the modulus itself as the consumed resource.

## 6. Exact regression support

The portable verifier replays the complete RL232 depth-three owned-pair necessary paths:

- H17-A common word `121`: `14,244` paths;
- H17-B common word `212`: `16,976` paths;
- total: `31,220` paths.

For every path it checks the exact height/exponent telescope, the concatenated Q identity, dyadic rebasing, unit-modulus affine evolution for `q=5,7,11,13`, and the finite source-term formula modulo `3^b` for `b=1,2,3`.

This finite replay is regression support only. The promoted T1-T3/decomposition results are arbitrary-depth analytic statements.

## 7. Success-C conclusion and successor pivot

RL233 satisfies Success C of `RL233_OWNED_LONG_RETURN_DEFECT_AND_HIGHER_MODULUS_TARGET.md`:

- a precise no-go/scaling theorem is proved for the owned endpoint/higher-modulus route at the bare-modulus-consumer scope;
- the next missing state is isolated;
- the route pivots according to the RL227 fallback architecture.

The next missing object is either:

1. a **noncongruential owned macro reset cost** — sign/order, active weight, zero-area, height/mass, phase resource, or equivalent macro packing quantity; or
2. an **independently restricted physical legal-tail language** that turns an otherwise reversible unit residue into a genuinely consumable global state.

RL234 should prioritize the noncongruential owned macro route, using legal-tail residue coupling only if it can be converted into a global consumer rather than another selector.

## 8. Preserved open state

Unchanged:

- necessary terminal-rank frontier `13,415,865,870`;
- e=4 terminal rank `31,435,476,727` live;
- e=4 combined survivors through transition 43 `3,856,660,232`;
- combined H17 spacing `>=1001`;
- combined physical H17 incidence `<=1,615`: **not proved**;
- sole high branch: **open**;
- Gate A: **open**;
- Gate B: **open**;
- global non-trivial-cycle exclusion: **open**.

No necessary-state witness is promoted as a physical realization.
