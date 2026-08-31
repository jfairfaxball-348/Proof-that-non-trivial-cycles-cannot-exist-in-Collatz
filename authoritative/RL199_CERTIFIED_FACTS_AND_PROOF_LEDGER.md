# RL199 Certified Facts and Proof Ledger

Date: 2026-08-31. Conditional physical branch remains `(37,0,23,-1)`.

## Newly proved analytic mathematics

- Every surviving H21 `tau=34` co-owner has a unique positive oriented lift index `eta` with
  lower/upper odd endpoints
  `2^34 eta-1` and `2^34(eta+21)-1`.
- Through the first 33 unit-exponent transitions,
  `Y_t^-=2^(34-t)3^t eta-1` and
  `Y_t^+=2^(34-t)3^t(eta+21)-1`.
  The preterminal difference is exactly `14*3^34`.
- The `tau=35` predecessor layer plus the cycle-state unit-mod-3 law sharpens the two global
  states to
  `011 <=> eta=0 mod 9`,
  `111 <=> eta=8 mod 9`.
- Terminal orientation is exactly parity of `eta`.
  Even `eta` makes the lower endpoint reach height 21; odd `eta` makes the upper endpoint do so.
- Writing `nu` for the extra 2-adic valuation on the odd parameter, the terminal signed defect is
  `+nu` for even `eta`, `-nu` for odd `eta`, with physical `1<=nu<=21`.
- The two remaining bits are therefore the four necessary classes
  `eta=0,8,9,17 mod 18`.
- `3^(-34) mod 2^22 = 1893305`. Terminal nonnegative height excludes exactly one lift residue
  modulo `37748736=9*2^22` inside each mod-18 class:
  `18670500, 1893284, 6087609, 27059129` in classes `0,8,9,17` respectively.
- The complete `tau=34`-through-preterminal common pair-difference sequence and the terminal
  numerator are `eta`-independent. An oriented endpoint/signed datum is required to select a class.
- The inherited K drift sees the sign first through
  `±rho(2^nu-1)/(3*2^21)`, of magnitude `<1/3`.

## Exact certificate

`verification/verify_rl199_h21_oriented_lift.py` checks all fixed constants, the 33-step affine
tail, mod-18 state/sign classification, terminal numerator invariance, Hensel inverse and CRT
forbidden residues, and representative local arithmetic for every surviving class.

## Inherited state retained

RL198's global state reduction `011,111`, no-owned-zero-edge result, valuation saturation,
preterminal height/mechanical bit, and H21 charging scope are unchanged. RL197's local six-state
classification remains valid at its prehistory-free scope. All prior physical-versus-necessary,
finite-cutoff, rank/time, and variation/excursion guardrails remain binding.

## Open obligations

RL199 does not select one `eta mod 18` class, exclude either H21 state, establish physical
population/incidence of a class, release the H21 budget, close the sole branch or Gate A/Gate B,
exclude non-trivial cycles, or prove Collatz.
