# RL51 — coupled elimination of z=31

Date: 2026-08-23

## Status

**ANALYTIC MASS/DEFECT REDUCTION + EXACT TERMINAL CERTIFICATE.**

For the sole stable continued-fraction survivor, `z=31` is impossible. Parity therefore upgrades the stable survivor to

`z>=33`.

## 1. The 26th x-zero is still forced into a bounded prefix

At `z=31` there are 30 x-zeros. Let `P=p_26`, the number of x-ones before the 26th x-zero.

For fixed `P`, the first 25 x-zero mass is maximized by the greedy sequential-cap prefix, while zeros 27--30 are maximized by continuing greedily from `P`.

At `P=54`, even this relaxed maximum is only

`11.8476476823... <= 143/12`.

Larger `P` only lowers the current/future mass. Since the cap itself forces `P>=45`, any survivor must have

`45 <= p_26 <=53`,

hence

`u_26=p_26+25 <=78`.

## 2. Nine delayed matching y-zeros already force too much E

Suppose at least nine of `y_1,...,y_26` occur after `u_26`. Order forces these to be indices `18,...,26`.

Put `P=p_26` and `c=u_26=P+25`. Their earliest possible positions are `c+1,...,c+9`, so for `j=18,...,26`,

`r_j >= P+9-p_j`.

Because

`w_j = 2^(j-1) (2/3)^p_j`,

we have the exact cancellation

`w_j (2/3)^(P+9-p_j) = 2^(j-1) (2/3)^(P+9)`,

independent of `p_j`.

Let `M_17` be the exact greedy maximum of the first 17 zero weights and let `F(P)` be the exact greedy maximum of zeros 27--30 starting from `P`. From `Zx>143/12`, the mass `T` on zeros 18--26 obeys

`T > 143/12 - M_17 - F(P)`.

Therefore their defect contribution satisfies

`E > 143/12 - M_17 - F(P) - C_9(P)`,

where

`C_9(P)=sum_{j=18}^{26} 2^(j-1)(2/3)^(P+9)`.

Exact rational evaluation for every possible `P=45,...,53` gives the uniform lower bound

`E > 2.0240875200... > 5/3`.

Contradiction. Hence at most eight of the first 26 matching y-zeros lie after `u_26`.

The four later zero pairs force at most `8+4=12` y-zero edges in the suffix after `u_26`, while exactly four x-zero edges remain.

## 3. Terminal suffix certificate

An exact backward residue BFS with budgets

`x-zero <=4`, `y-zero <=12`

proves

`maximum terminal suffix length = 38`.

But `u_26<=78`, while the internal length at `z=31` is `ell+27`, so the actual suffix has length at least

`ell-52 = 77692117359936589351`.

Contradiction.

Thus `z=31` is impossible, and parity gives `z>=33`.

## Verification

Run:

`python3 rl51_research/verify_rl51_z31_coupled_elimination.py`
