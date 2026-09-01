# RL217 — universal prefix-wide phase-51 height-automaton theorem

Date: 2026-09-01.

## Theorem T1: prefix-independent phase-16 physical coordinate

For every e=16 arithmetic prefix in the inherited RL216 family, let the lifted parameter be

`eta = eta_* + 3^17 k`.

The exact phase-16 odd state is

`y_16 = 2^34 eta - 1 - 3^16*2^13`,

with mechanical height `h_16=1`. Therefore, after setting `x=eta`, the complete deterministic odd trajectory and height recurrence from phase 16 depend on `x` alone and not separately on the prefix label `Q`.

**Proof.** The displayed formula is the inherited exact e=16 coordinate identity. The accelerated odd map sends `y_i` deterministically to `(3y_i+1)/2^v2(3y_i+1)`, while the mechanical height update depends only on `h_i`, `b_(i+1)-b_i` and that same valuation. Induction on `i` gives the claim. ∎

## Theorem T2: exact modular cylinder criterion through a finite horizon

Fix a finite horizon `H>=16`. On a residue cylinder `x=r+2^m t`, suppose the current odd state has affine form `y_i=A t+B`. Then

`3y_i+1 = 3A t + (3B+1)`.

If `v2(3B+1)<v2(3A)`, the acceleration exponent is constant on the cylinder. If the two valuations have not yet separated, splitting `t` by parity raises the known 2-adic precision by one and gives two exact child cylinders. Hence repeated exact splitting partitions the integers into disjoint cylinders on which every acceleration exponent through horizon `H` is fixed.

On a fixed cylinder, if at any phase

`a_i > h_i + b_(i+1)-b_i`,

then `h_(i+1)<0` for every integer in that cylinder, so the cylinder cannot contain a physical H21 word through that phase.

**Proof.** This is the elementary 2-adic valuation dichotomy applied to the affine numerator, followed by the inherited exact height recurrence. Parity splitting is exhaustive and disjoint. ∎

## Corollary T3: congruence selector on each prefix parameter

For a live universal cylinder `x=r mod2^m` and a prefix `eta=eta_*+3^17 k`, since `3^17` is invertible modulo `2^m`, membership is exactly

`k = (r-eta_*) (3^17)^(-1) mod 2^m`.

Thus universal height-cylinder membership is an exact residue selector on `k`, and its intersection with a finite `k` interval is countable by range arithmetic without enumerating its members.

## Certified H=51 instance

The RL217 finite verifier applies T2 at `H=51` and certifies 3,132,617 disjoint live cylinders and 1,705,547 failure cylinders. Exact range intersection with the inherited RL216 prefix windows leaves 139,581,280 arithmetic candidates and removes 192,346,636. No complete remaining prefix or higher structural class becomes empty.

This corollary is a necessary-condition sieve only. It does not identify arithmetic candidates with physical H21 occurrences and it makes no assertion beyond phase 51.
