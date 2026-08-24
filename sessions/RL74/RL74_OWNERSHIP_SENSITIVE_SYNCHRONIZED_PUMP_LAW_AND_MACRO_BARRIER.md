# RL74 — Ownership-sensitive synchronized pump law and macro endpoint barrier

Date: 2026-08-24

## 0. Status

RL74 continues from the checksum-clean authoritative RL73 state. It does **not** prove Gate A, Gate B, RL closure, nontrivial-cycle exclusion, or the Collatz conjecture.

RL74 attacked the RL73 giant post-first-mismatch height-one macro exactly as requested. The direct endpoint/telescope attack does not close the low-`k` band. Instead RL74 proves two useful things:

1. a stronger **canonical-reachability method barrier**: even from the exact canonical start, at fixed area `H=4`, there are legal post-first-mismatch positive maximal height-one synchronized blocks with arbitrarily many aligned `00` columns, while the corrected inherited `Jg`/`Psi` bounds can remain uniformly satisfied;
2. a new exact **full-phase synchronized pump law**: repeating any fixed closed synchronized subword inside a fixed global context makes the full-phase quotient a Möbius function of `(3^s/2^n)^q`. Therefore full phase does see zero-area pump depth. For a fixed surrounding context the admissible repeat count is finite except for one exact algebraic degeneracy in which the quotient is constant and pump deletion/insertion preserves full phase wherever the denominator remains positive.

This materially sharpens the RL73 target. The missing theorem is no longer “use endpoints somehow”; it is a **uniform context-control theorem** strong enough to turn the fixed-context pump finiteness into a bound uniform over all genuine full-phase completions with `27<=k<=165`, or else a theorem forcing a deletable/contradictory pump inside the giant macro.

---

## 1. Incoming RL73 gate

The current gate was checked before new mathematics:

- outer RL73 sidecar: **PASS**;
- freshly unpacked RL73 internal `SHA256SUMS.txt`: **PASS**;
- `bash verification/run_fast_rl73_verifiers.sh`: **PASS**.

A first manifest command was run one directory above the ZIP's top-level bundle directory and returned only a path error. Rerunning from the actual bundle root passed. No checksum, verifier, or mathematical assertion failed.

The verification-economy rule was then applied. No expensive historical finite certificate was recursively rerun.

---

## 2. Exact inherited interfaces used

RL74 uses only the following already-frozen interfaces.

### 2.1 Height-one quotient maps

At `d=1`, odd `J` has synchronized maps

`00: J -> (J+1)/2`,

`11: J -> (3J+1)/2`.

An even height-one state must leave through `01`.

### 2.2 Normalized weight and synchronized telescope

In the inherited RL47/RL50 normalization, write

`g=2^i/3^(p_x)`.

Across a column, `g` is multiplied by `2` when `x=0` and by `2/3` when `x=1`.

At height one,

`Psi=g(J+1)/2`.

On a synchronized block:

- `00` increases `Psi` by exactly the current zero weight `g`;
- `11` leaves `Psi` unchanged.

Hence for any synchronized height-one block

`Psi_out-Psi_in = sum_(00 in block) g_j`.            (2.1)

### 2.3 Corrected positive `Jg` bound

RL62's repaired bound is

`Jg <= (9/2) zeta 3^d`,                              (2.2)

not the false decreasing-height RL59 bound. RL74 uses (2.2) only in its valid direction.

### 2.4 Full-phase word condition

For a binary word `w` of length `a`, weight `ell`,

`Q(w)=sum_(i:w_i=1) 2^i 3^(ell-rank(i))`.

For the RL64 full-phase half-word `v`, with

`M=2^a-3^ell>0`,

the ownership/full-phase condition is

`M | Q(v)+4*3^ell`,

with positive quotient

`N=(Q(v)+4*3^ell)/M`, `N==3 (mod8)`.

---

## 3. New theorem A — canonical fixed-area post-first-mismatch pump family

Use `1` for synchronized `11` and `0` for synchronized `00` only in compact words below.

For integers `p,q>=0`, start from the exact canonical quotient state

`(d,J,H)=(1,-13,0)`

and follow the legal column word

`(101)^p 100, 01,00,00,11,10, (10)^q 0`.             (3.1)

Then:

1. `(101)^p` is the canonical stay-odd cycle
   `-13 -> -19 -> -9 -> -13`;
2. the synchronized exit `100` reaches the even first-mismatch entry `J=-4` at height one;
3. the fixed active core
   `01,00,00,11,10`
   reaches
   `(d,J,H)=(1,3,4)`;
4. the final synchronized word `(10)^q0` is a **maximal positive height-one block**:
   `3 --11--> 5 --00--> 3`
   repeats `q` times and the final `00` sends `3 -> 2`, the first even exit;
5. that block contains exactly

`boxed: q+1 aligned 00 columns`,                     (3.2)

while the entire path still has

`boxed: H=4`                                         (3.3)

at the block exit and fixed quotient endpoint `J=2`.

Therefore canonical reachability from the true RL start, fixed small area, positive block endpoints, and maximality do **not** impose any upper bound on the aligned-`00` count.

Classification: **analytic canonical-reachability method barrier**. It is not a full-phase countermodel because no claim is made that the paths (3.1) extend to an RL64 full-phase completion.

This strictly sharpens the older unrestricted height-one warning: the zero-area pumping obstruction already survives canonical reachability from `J=-13`.

---

## 4. New theorem B — the corrected `Jg` bound and `Psi` telescope still do not price count

Use the exact RL47 convention `g_start=2`. Along (3.1), after `(101)^p100` the first-mismatch entry `J=-4` has

`g_-4 = (16/3)(8/9)^p`.

After the fixed active core, the positive pump entry `J=3` has

`boxed: g_ent = (512/27)(8/9)^p`.                    (4.1)

Each closed `10` pump cycle multiplies `g` by `4/3`.

Now choose

`boxed: p=3q+15`.                                    (4.2)

Then every positive state in the fixed active core and the entire positive pump satisfies the stronger inequalities obtained from (2.2) by replacing `zeta` with `1`.

For the height-two part of the fixed core the largest positive `Jg` is

`(512/3)(8/9)^p < 81/2`.

For the height-one pump and its even exit the largest positive `Jg` is

`(2048/27)(8/9)^p(4/3)^q < 27/2`.

The second inequality follows from

`(8/9)^(3q+15)(4/3)^q`

`=(8/9)^15 (2048/2187)^q`

`< 729/4096`.

Since `zeta>1`, the actual corrected RL62 bounds are satisfied.

Meanwhile the exact aligned-zero weight in the maximal pump is, by the `Psi` telescope,

`boxed: M00(q)=g_ent[3(4/3)^q-2]`.                  (4.3)

Under (4.2),

`M00(q) < 3 g_ent (4/3)^q`

`= (512/9)(8/9)^15(2048/2187)^q`

`< 10`.                                              (4.4)

Thus the aligned-`00` **count** tends to infinity while the exact synchronized telescope mass remains uniformly bounded, and the corrected positive `Jg` cap remains satisfied.

Classification: **analytic method barrier**.

Consequence: the RL73 giant count cannot be converted into a contradiction using only canonical reachability, block endpoints, the synchronized `Psi` telescope, and the repaired uniform `Jg` upper bound. A successful theorem must use information that (3.1) does not impose—most naturally the exact RL64 full-phase divisibility, or another genuinely global invariant.

---

## 5. New theorem C — exact full-phase synchronized pump Möbius law

The previous barrier shows why the RL64 global condition must be brought inside the macro argument. RL74 derives the exact algebraic way in which full phase sees a repeated synchronized pump.

Let a full half-word be decomposed as

`v_q = A c^q B`,                                     (5.1)

where `c` is a fixed nonempty binary word of length `n`, weight `s`, and

`P=2^n`, `R=3^s`, `C=Q(c)`, `delta=R-P`.

Let

`L_A=|A|`, `w_B=wt(B)`,

`X0=2^(|A|+|B|)`,

`Y0=3^(wt(A)+wt(B))`.

Then the repeated-word identity is

`Q(c^q)=C (R^q-P^q)/(R-P)`.                          (5.2)

Define the integer coefficients

`A_* = delta 3^(w_B) Q(A)`

`      + 2^(L_A) 3^(w_B) C`

`      + 4 delta Y0`,

`B_* = delta 2^(L_A) Q(B)`

`      - 2^(L_A) 3^(w_B) C`.                        (5.3)

The full-phase numerator and denominator satisfy the exact identities

`boxed: delta [Q(v_q)+4Y0 R^q] = A_* R^q+B_* P^q`,  (5.4)

`boxed: M_q = X0 P^q-Y0 R^q`.                       (5.5)

Therefore, whenever `M_q!=0`, the exact phase quotient is

`boxed: N_q = [A_* z_q+B_*] / [delta(X0-Y0 z_q)]`,  (5.6)

where

`z_q=(R/P)^q`.

This is a Möbius function of the single exponential pump parameter `z_q`.

### 5.1 Fixed-context finiteness

Put

`D_* = A_* X0+B_* Y0`.                              (5.7)

If `D_*!=0`, the Möbius function (5.6) is injective in `z`, hence distinct repeat counts give distinct rational quotients.

- If `R>P`, then `M_q>0` itself forces
  `(R/P)^q < X0/Y0`, so only finitely many `q` are possible.
- If `R<P`, then `z_q -> 0` and `N_q -> B_*/(delta X0)`. Since the integer values of an injective convergent sequence can occur only finitely often, only finitely many `q` can satisfy full-phase integrality.

Thus, for a **fixed surrounding context `(A,B)`**, a fixed pump can be repeated in a genuine full-phase word only finitely many times unless the exact degeneracy below occurs.

### 5.2 Exact degeneracy

If

`boxed: D_*=0`,                                      (5.8)

then (5.6) is constant in `q`. Hence if one repeat count gives an integer full-phase quotient, every other repeat count for which the internal path remains legal and `M_q>0` has the same quotient.

When `c` is a closed synchronized height-one state cycle, inserting/deleting `c` preserves the local quotient state and area. Therefore (5.8) is a precise algebraic **deletion/descent hook**: subject to the genuine-RL primitiveness and `M>0` conditions, it is the case in which local pump deletion can preserve full phase.

RL74 does **not** promote a primitiveness contradiction here; the exact genuine-RL primitive/minimal interface must be audited before using that consequence.

Classification: **new analytic full-phase theorem**.

---

## 6. Two important special pumps

### 6.1 Canonical negative start cycle `c=101`

At `J=-13`, `101` is a closed synchronized cycle. Here

`P=8`, `R=9`, `C=7`.

For insertion immediately after the fixed `111` prefix of `v`, with suffix `B=y'0^(t+1)` and `r=wt(y')`, the exact formula simplifies to

`Q(v_q)=75*3^r*9^q + (8Q(y')-56*3^r)8^q`,           (6.1)

and

`Q(v_q)+4*3^(r+3+2q)`

`=183*3^r*9^q + (8Q(y')-56*3^r)8^q`.                (6.2)

Since `R>P`, a fixed suffix cannot support arbitrarily many such shrink cycles while retaining `M>0`.

### 6.2 Positive `3<->5` cycle `c=10`

At `J=3`, `10` is the closed synchronized cycle

`3 -> 5 -> 3`.

Here

`P=4`, `R=3`, `C=1`.

Since `R<P`, a fixed global context admits only finitely many full-phase repeat counts unless the exact determinant degeneracy (5.8) holds.

This is the first exact ownership-sensitive theorem in the RL74 attack that directly consumes a **repeatable** zero-area macro rather than merely its local residue class.

---

## 7. Why this still does not close the RL73 giant macro

The RL73 theorem guarantees a maximal post-first-mismatch height-one block containing at least

`40,249,491,324,522,944`

aligned `00` columns in every hypothetical low-`k` violation, but it does not say that the block is a repetition of one fixed closed synchronized cycle.

Even when a repeated closed pump is present, Theorem 5 is **fixed-context**. Its coefficients contain the entire prefix/suffix through `Q(A)`, `Q(B)`, `X0`, and `Y0`. No inherited theorem currently bounds those coefficients uniformly in terms of only

`27<=k<=165`, `H<k`, full phase, and the giant `00` count.

The canonical family of Sections 3–4 shows exactly why a context-free lower bound on the RL50 weights cannot be expected: a separate zero-area shrink pump can make the entry weight exponentially small while keeping area fixed.

Therefore RL74 does not claim an upper bound on the RL73 macro count and does not close the low-`k` Gate-A band.

The exact missing theorem is now one of the following equivalent-strength forms:

1. **uniform context bound:** control `Q(A),Q(B),X0,Y0` or the Möbius determinant for any giant owned block using `H,k` and full phase;
2. **pump extraction + descent:** prove that every sufficiently long owned block contains a closed synchronized subpump whose determinant degeneracy/deletion contradicts genuine RL primitiveness/minimality, or whose nondegenerate Möbius law forbids its repeat depth;
3. **aperiodic alternative bound:** if no usable repeated pump occurs, force an endpoint/state/weight growth large enough to contradict a global full-phase size budget.

These are genuine global ownership targets. They are not q-digit extensions.

---

## 8. Failed/rejected RL74 routes

### F1. “Huge aligned-zero count plus `Psi` telescope is enough.”

Rejected. Sections 3–4 give a canonical fixed-area family with unbounded count and uniformly bounded telescope mass.

### F2. “Block endpoints `(J_in,J_out,H)` bound the count.”

Rejected. The family `(10)^q0` has fixed positive entry `J=3`, fixed even exit `J=2`, fixed area `H=4`, and `q+1` aligned zeros.

### F3. “The repaired uniform `Jg` cap repairs the endpoint route.”

Rejected. Choosing `p=3q+15` makes the same canonical family satisfy the stronger `zeta=1` version of the positive `Jg` bound while `q` is arbitrary.

### F4. “Full phase is also blind to synchronized pumping.”

Rejected. Theorem 5 shows the opposite: full phase sees a fixed pump through an exact Möbius/exponential law.

### F5. “Fixed-context pump finiteness is already a uniform Gate-A theorem.”

Rejected. The context varies across hypothetical RL objects, and no current theorem bounds the context coefficients uniformly by `H,k`.

---

## 9. Exact proof state after RL74

Retain the RL73 state unchanged except for the following additions.

### New analytic theorems

- canonical fixed-area post-first-mismatch pump family, Sections 3–4;
- exact bounded-mass/corrected-cap barrier for that family;
- full-phase synchronized pump Möbius law (5.4)–(5.6);
- fixed-context full-phase pump finiteness outside determinant degeneracy;
- determinant-zero constant-quotient/deletion hook.

### Exact finite verifier/audit

`verification/verify_rl74_synchronized_pump_law.py` checks:

- `Q` concatenation and repeated-word identities over bounded exhaustive word families;
- the Möbius pump formula over bounded contexts and repeat counts;
- canonical `101` and positive `10` closed cycles;
- the canonical fixed-area family for many `(p,q)`;
- exact `g`, `Psi`, and corrected-cap inequalities for `p=3q+15` over a bounded audit range;
- the canonical-prefix specialization (6.1)–(6.2).

The verifier is an audit/falsification certificate, not the proof of the infinite algebraic statements.

### Global status

- radius-3 primitive/full-D local theorem: **closed local obstruction**;
- Gate A even terminal `k`: **impossible analytically**;
- Gate A terminal `k<=25`: **closed by exact finite-certificate corollary**;
- Gate A odd `27<=k<=165`: **open**; every violation still has the RL73 giant owned macro;
- Gate A globally: **open**;
- Gate B globally: **open**;
- RL/nontrivial-cycle exclusion: **open**;
- Collatz conjecture: **not proved**.

---

## 10. RL75 strategic consequence

RL74 has reached a natural stopping point for the narrow macro endpoint attack. The direct endpoint/weight route has a new exact canonical counterfamily, while the genuinely ownership-sensitive repair has become a fixed-context Möbius/integrality theorem whose missing uniform context control is theorem-sized.

Accordingly the next session should **not** automatically continue by polishing this one route. RL75 should perform the requested global closure-route tournament using RL72 as the baseline and RL73–RL74 as new inputs.

The RL74 pump law should be entered into that tournament as a reusable lemma for at least:

- full-phase arithmetic;
- zero-area ownership control;
- minimal-counterexample/descent;
- cyclic-word pump extraction;
- Diophantine approximation of competing zero-area pumps;
- hybrid Gate-A/packing routes.

The exact new question is whether any route can provide the missing **uniform context control** or avoid it entirely.
