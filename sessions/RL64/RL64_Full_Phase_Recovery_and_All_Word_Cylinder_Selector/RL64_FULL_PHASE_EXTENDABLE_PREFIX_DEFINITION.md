# RL64 — exact-source-derived full-phase extendable prefix definition

Date: 2026-08-24

## Status

This is a **new RL64 definition**, introduced to replace the informal word “ownership” with an explicit existential condition derived from the exact recovered RL45/RL47/RL48 conventions. It is not claimed to be a historically named predicate.

The purpose is to make the next Gate-A statement formally meaningful without inventing an inherited theorem.

---

## 1. Ambient one-excursion datum

A **full-phase extendable one-excursion datum** is a tuple

`(a,ell,t,x,y)`

satisfying the following exact-source-derived conditions.

Put

`k=t+3`,

`m=a-k-1=a-(t+3)-1`,

`r=ell-3`,

`X=2^a`, `Y=3^ell`, `M=X-Y`.

Require `t>=0`, `m>=0`, `r>=0`, and `M>0`.

The internal words `x,y` are binary words of common length `m` and common weight `r`.

The associated full half-words are exactly

`u=110 x 1 0^t`,

`v=111 y 0^(t+1)`.

Thus both full words have length `a` and weight `ell`.

---

## 2. Exact internal RL path condition

Start

`d_0=1`, `T_0=-14`, `H_0=0`,

and define

`J_j=T_j+3^(d_j)-2^(d_j)`.

For internal column `(x_j,y_j)`, use the exact historical recurrence

`T_(j+1)=[3^(y_j) T_j + x_j 3^(d_j+y_j-1)-y_j]/2`,

`d_(j+1)=d_j+y_j-x_j`,

`H_(j+1)=H_j+d_j-1`.

Require at every internal step:

1. the displayed numerator for `T_(j+1)` is even;
2. `d_(j+1)>=1`;
3. the frozen RL45 parity legality holds:
   - if `J_j` is odd, `(x_j,y_j)` is `00` or `11`;
   - if `J_j` is even, `(x_j,y_j)` is `01` or `10`;
   - `10` is used only when `d_j>1`.

Require the internal terminal state

`d_m=1`,

`T_m=2^k-1`.

Equivalently, at the internal terminal boundary,

`J_m=2^k`.

The historical RL48 source then appends the omitted terminal local `(1,0)` column followed by `t` synchronized zero columns as part of the full-word construction.

---

## 3. Exact full-phase divisibility condition

For a binary word `w` of length `a`, weight `ell`, define

`Q(w)=sum_{i:w_i=1} 2^i 3^(ell-rank(i))`.

Let `V=Q(v)`. The exact recovered RL48 full-phase condition is

`boxed: M | V+4Y`.

Equivalently, in the recovered RL48 theorem, this is the `X-Y` factor required together with the terminal/proper-factor identity to obtain full cycle divisibility.

A datum satisfying sections 1–3 is called **full-phase extendable**.

---

## 4. Full-phase extendable prefix / macro state

A finite internal prefix of pair columns

`((x_0,y_0),...,(x_(j-1),y_(j-1)))`

is called a **full-phase extendable prefix** if there exists at least one full-phase extendable one-excursion datum `(a,ell,t,x,y)` whose first `j` internal columns are exactly that prefix.

The quotient state `(d_j,H_j,J_j)` reached by such a prefix is called a **full-phase extendable macro state**.

A height-one synchronized block entry `(H,J_0)` is called **full-phase extendable** if it occurs at a boundary `d_j=1` of some full-phase extendable prefix and is followed by a maximal internal synchronized block (`00/11` columns) inside at least one full completion.

This is the precise RL64 replacement for the informal phrase “owned macro entry”.

---

## 5. Why this definition is safe

- It is existential: local quotient reachability alone is not enough.
- It uses the exact historical full-word forms and exact full-phase divisibility recovered in RL64.
- It preserves the RL45 parity/height legality rather than accepting arbitrary affine compositions.
- It includes the exact canonical terminal `J=2^k`.
- It does not claim that a named ownership theorem existed historically.

Any stronger inherited phase/rank/zero-position hypothesis used in a future proof must be cited separately with provenance; it should not be silently folded into this definition unless the exact source is recovered.

---

## 6. Gate-A target in this language

The desired ownership-sensitive theorem can now be stated without ambiguity:

> For every full-phase extendable one-excursion datum, with terminal `k=t+3` and accumulated terminal area `H_m`, prove `H_m>=k`.

Equivalently, prove that the terminal full-phase extendable macro state `J_m=2^k` satisfies

`v2(J_m)=k<=H_m=K_m`.

For a final synchronized suffix `w`, RL64 already proves the exact necessary equality

`3^s(J_0+1)+2D(w)=2^n(2^k+1)`.

The next task is to combine this suffix equality with the earlier full-phase extendable prefix constraints to prove the area lower bound.
