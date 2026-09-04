# RL245 — six-unit valley geometry and singleton-swap checkpoint

Date: 2026-09-04

Classification: **R4_BRIDGE_REDUCED** (checkpoint only; RL245 remains open).

## 0. Scope and authority

This checkpoint continues only the prepared RL245 target from the authoritative RL244 closeout.

Frozen retained data:

- every simultaneous Gate-A/Gate-B survivor satisfies `beta(P)>=6`;
- `P_i=r-W_i^u(q)` with `ar-q ell=2`;
- the retained resonance gives `min(q,a-q)>=8`;
- `P` is integer-valued and cyclic with
  `P_(i+1)-P_i in {-1,0,1}` and `sum_i P_i=2`;
- on the final retained doubled route the two genuine determinant-4 physical envelopes over the same u-half roots are
  `{P_i, P_i-h_(i+q)}` with `h_(i+q) in {0,1}`;
- RL242 has already eliminated dyadic full-cycle carry and placed every physical cyclic full-word root in the canonical box;
- RL238/RL239 Radius 4 is a theorem only for an **eligible primitive full-D self-rotation at exact global adjacent-transposition distance 4**.

No statement below treats the auxiliary half-flow `P` itself as a Radius-4 theorem input.

Gate A and Gate B remain distinct and open. Radius 5 remains inactive.

---

## 1. Same-root physical negativity is exact

For every root `i`, if `P_i<0`, then

`P_i-h_(i+q) <= P_i < 0`.

Hence every negative `P` root is simultaneously negative in both genuine doubled physical envelopes at the **same cyclic root**.

This is stronger than a purely auxiliary sign statement, but it is not yet Radius-4 eligibility: a negative physical prefix/flow value does not by itself say that the corresponding full-D self-rotation pair has exact global distance 4.

---

## 2. Exact q-window derivative

With the cyclic q-window convention

`W_i^u(q)=u_i+u_(i+1)+...+u_(i+q-1)`,

one has

`W_(i+1)^u(q)-W_i^u(q)=u_(i+q)-u_i`.

Therefore

`boxed: P_(i+1)-P_i = u_i-u_(i+q)`.

Thus every strict down-step of `P` is exactly a local mismatch

`u_i=0, u_(i+q)=1`,

and every strict up-step is exactly

`u_i=1, u_(i+q)=0`.

This is an exact word-level interpretation of the determinant-2 valley boundary; no asymptotic or packing estimate is used.

---

## 3. Singleton valley = exact local adjacent transposition

Let `i` be an isolated negative root, meaning

`P_(i-1)>=0, P_i<0, P_(i+1)>=0`.

Because `P` is integral and 1-Lipschitz, necessarily

`(P_(i-1),P_i,P_(i+1))=(0,-1,0)`.

The derivative identity then gives

- entering the valley:
  `u_(i-1)=0`, `u_(i-1+q)=1`;
- leaving the valley:
  `u_i=1`, `u_(i+q)=0`.

Hence

`boxed: (u_(i-1),u_i)=01,  (u_(i-1+q),u_(i+q))=10`.

So every isolated negative root is an exact local `01 <-> 10` adjacent-transposition signature between `u` and its q-shift.

Because `min(q,a-q)>=8`, the two length-2 blocks belonging to a single signature are disjoint in the cyclic half-word.

This is genuine local word geometry, but it still does **not** assert that the full q-shift differs by only this swap.

---

## 4. Six-unit trichotomy

Let

`S={i : P_i<0}`.

Since `beta(P)>=6`, one of the following mutually exhaustive geometric branches holds.

### Branch A — adjacent negative pair

There exist `i` with

`P_i<0` and `P_(i+1)<0`.

This includes every valley of depth at least 2: if `P_i<=-2`, 1-Lipschitzness forces both neighbours to be at most `-1`.

This is the **thick/overlapping valley branch**.

### Branch B — no adjacent pair, but a stride-2 pair

Assume Branch A does not occur. Then every negative root is isolated and therefore equals `-1`. Since each contributes exactly one negative unit,

`|S|=beta(P)>=6`.

If there exist roots `i,i+2 in S`, then necessarily

`(P_(i-1),P_i,P_(i+1),P_(i+2),P_(i+3))=(0,-1,0,-1,0)`.

Applying the singleton-swap identity twice gives two disjoint local swaps:

`u_(i-1..i)=01`, `u_(i-1+q..i+q)=10`,

and

`u_(i+1..i+2)=01`, `u_(i+1+q..i+2+q)=10`.

Equivalently, on the four unshifted sites

`u_(i-1..i+2)=0101`

while the corresponding q-shifted four sites are

`1010`.

This is an exact **two-local-swap candidate**. It is the sharpest immediate interface candidate for producing a Radius-4 topology, but the remainder of the full-D rotation must still be proved to have the required ownership/exact-distance behaviour before RL238 can be applied.

### Branch C — sparse singleton family

Assume neither Branch A nor Branch B occurs. Then all negative roots are isolated `-1` valleys, there are at least six of them, and every pair of consecutive negative roots in cyclic order is separated by at least three positions.

Consequently

`a>=18`.

Moreover, among any six negative roots at least two have the same index residue modulo 3. Each root carries the exact singleton `01 <-> 10` signature of Section 3.

Thus the remaining obstruction is a **sparse family of at least six exact local q-shift transpositions**, with a forced repeated mod-3 root class, not an amorphous negative-mass statement.

This is precisely the branch in which RL64-RL69 ordered-state/full-phase information must do real work; bare spatial packing cannot finish it.

---

## 5. Red team: flow-level invariants alone cannot force Branch A or B

The following cyclic integer sequence is a concrete abstract countermodel to any argument using only

- integrality,
- cyclic 1-Lipschitzness,
- `sum P=2`, and
- `beta(P)>=6`:

`(-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,1,2,2,2,1,0)`.

It has length 23, sum `2`, negative mass `6`, and all cyclic increments in `{-1,0,1}`. Its six negative roots have cyclic gaps

`3,3,3,3,3,8`,

so it has neither an adjacent negative pair nor a stride-2 negative pair.

This sequence is **not claimed to arise from a retained physical full-phase word**. Its role is narrower and important: it proves that the frozen scalar flow invariants by themselves cannot manufacture the desired Radius-4 encounter. Any proof of the sparse branch must consume additional q-window word structure and/or exact full-phase ordered-state ownership.

This red team blocks an invalid shortcut before it can enter the authoritative ledger.

---

## 6. Exact remaining ownership/interface lemma

After this checkpoint, RL245 can be stated more sharply.

It is enough to prove the following physical extraction statement for every retained primitive full-phase object:

> **Owned-interface extraction target.** For the common physical negative-root set of `P`, one of Branch A, B, C must force either
> 1. two full-D cyclic roots forming an eligible primitive exact-distance-4 self-rotation and satisfying every RL238/RL239 hypothesis, with the selected same-root/full-phase data preserved; or
> 2. a contradiction to exact full-phase extendability / ordered prefix legality in the RL64-RL69 sense.

The three branches expose different concrete input geometry:

- A: an overlapping/thick valley;
- B: an exact `0101 <-> 1010` two-swap factor;
- C: at least six isolated exact swap signatures with a repeated mod-3 root class.

The missing theorem is therefore no longer “turn beta>=6 into Radius 4” in the abstract. It is an **owned full-D interface extraction theorem for one of these three explicit geometries**.

---

## 7. What is and is not promoted

Promoted at this checkpoint:

1. every negative `P` root is a common negative root of both genuine doubled physical envelopes;
2. the exact derivative `P_(i+1)-P_i=u_i-u_(i+q)`;
3. every isolated negative root is exactly a local `01 <-> 10` q-shift adjacent transposition;
4. every `beta(P)>=6` survivor lies in Branch A, B, or C above;
5. Branch B contains an exact local `0101 <-> 1010` two-swap factor;
6. pure `sum/beta/Lipschitz` information cannot eliminate Branch C.

Not promoted:

- no application of RL238 Radius 4;
- no claim that `P` is itself a Radius-4 flow;
- no claim that a local two-swap factor has exact global distance 4;
- no claim that a negative unit is a separately owned full-D object;
- no Gate-A or Gate-B closure;
- no global non-trivial-cycle exclusion.

RL245 remains open on the owned-interface extraction target of Section 6.
