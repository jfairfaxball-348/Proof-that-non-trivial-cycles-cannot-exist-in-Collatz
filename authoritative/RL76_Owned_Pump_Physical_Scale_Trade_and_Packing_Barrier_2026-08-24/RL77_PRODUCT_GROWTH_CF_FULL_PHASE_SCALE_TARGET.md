# RL77 target — Product/growth/continued-fraction plus full-phase physical-scale coupling

Date: 2026-08-24

## Purpose

RL76 sharpened the periodicity-or-packing route but did not close it. The periodic branch now has an exact physical-scale normal form, and the canonical `c=10` reciprocal packing cost is bounded independently of repeat depth. The aperiodic branch remains shortcut-Collatz-conjugate without a global upper-state consumer.

Per the RL75 route tournament stop criterion, RL77 should pivot to the deliberate alternative:

# **Product/growth/continued-fraction + modern full phase**

## Frozen RL76 interface

For any closed synchronized height-one pump `c`, with

`P=2^|c|`, `R=3^wt(c)`, `alpha=(J-1)/2`,

and repeat depth `q`, the paired physical states satisfy

`A_0=alpha+P^q m`,

`B_0=alpha+3P^q m`,

`A_q=alpha+R^q m`,

`B_q=alpha+3R^q m`.

The normalized weight obeys

`g_out(A_out-alpha)=g_in(A_in-alpha)`.

For the RL75 determinant,

`D_*=3m(R-P)2^|A_ctx|3^wt(B_ctx)M_q`,

so for fixed context

`m_q M_q=K_ctx`.

For `c=10`,

`A_0-1=(4/3)^q(A_q-1)`.

RL76 also proves the entire reciprocal odd-state mass of the two synchronized `c=10` chains is `<4/(2^71-1)`, independently of `q`.

## Primary theorem target

Derive a genuinely global restriction that couples this pump scale to the near-resonant exponent data.

A successful theorem should have one of the following forms:

1. **Reduced-ratio restriction:** show that a pump scale `(P/R)^q` of the RL73-required magnitude forces the reduced `a/ell` convergent or `gcd(a,ell)` into an impossible class under full phase.
2. **Complement-growth budget:** show that the complementary half-cycle needed to compensate a contraction pump contributes a mandatory product/population cost that exceeds the RL73 phase-resonance window.
3. **Scale integer bound:** bound `K_ctx=mM_q` or `m` using full-phase denominator/quotient and terminal `k<=165`, uniformly over contexts.
4. **Two-scale Diophantine equation:** reduce the pump plus complement to a bounded-parameter exponential equation suitable for exact CF/two-logarithm analysis.

## Required inherited tools

Use selectively:

- RL19 odd-step product and weighted population/state packing;
- RL20 coprime-6 packing and continued-fraction gate;
- RL48/RL64 full-phase denominator and quotient;
- RL65 exact defect quotient;
- RL73 phase squeeze, denominator floor and skew floor;
- RL75 `N==19 mod24` and primitive pump nondegeneracy;
- RL76 physical-scale normal form and determinant normalization.

## Required red-team tests

Reject any candidate theorem that:

- is merely another approximation to `log_2 3` without a new RL-specific restriction;
- prices only reciprocal mass of the `c=10` chain (RL76 proves that cost is q-independent);
- silently assumes a global upper bound on cycle states;
- collapses to endpoint `Psi`, raw `(2-N)M`, local synchronized grammar, or another finite q-digit selector.

## Stop criterion

If full phase still leaves the physical scale parameter `m` and complementary context unrestricted after a serious product/CF attack, pivot next to the `D|Q`-sensitive bounded-radius Gate-B reconnaissance from RL75 rather than returning to local Gate-A digit extensions.

## Close-out requirement

Freeze exact proofs, failures, dependencies, correction ledger and verifier status; create the next numbered authoritative bundle and sidecar; verify internal manifest and fresh-unpack fast suite.
