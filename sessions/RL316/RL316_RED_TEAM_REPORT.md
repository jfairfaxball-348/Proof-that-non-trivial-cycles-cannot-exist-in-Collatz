# RL316 red-team report

Date: 2026-09-14
Status: PASS

## Scope and classification checks

1. The prefix-potential and row-energy results are classified as analytic
   identities.  Their regressions are not used as proofs.
2. The simultaneous-factor scan through `a<=22` is computational evidence
   only and is not promoted as a finite certificate.
3. The late and early shadows are positive rational fixed orbits, not integer
   Collatz cycles.  Their bracketing does not contradict physical leastness.
4. The envelope and row identities do not infer local `D0` ownership.
5. `g=1` remains separate and no proper reduced balanced return is asserted
   there.
6. Gate A, Gate B, and global positive non-trivial-cycle exclusion remain open.

## Algebraic red team

The portable row-energy verifier checks:

- the prefix-potential identity;
- the exact canonical interface construction;
- every normalized row formula;
- the telescope to `4(qH-Q(d))`;
- the `g=2` rankwise meet/join identities and envelope-gap implication.

It passes on 2,645 general canonical words and 224,325 balanced pairs.

The analytic proof in `RL316_CLOSEOUT.md` establishes the unrestricted result;
the bounded verifier is a regression only.

## Ownership/barrier red team

The dual-shadow verifier checks 111,350 ordered bounded pairs and exactly
replays two inherited countermodels:

1. RL21 `(65,41)` satisfies `Q(u)-Q(v)=4(X+Y)`, `epsilon=0`,
   `q_tau-q_sigma=4(X+Y)`, and `n=4X`, but fails
   `(X-Y)|(Q(u)+Q(v))`.
2. RL38's area-seven crossing saturates `q_tau-q_sigma=X+Y`.

Therefore the handover explicitly rejects any claim that `X+Y` ownership,
binary envelope geometry, or the dyadic `n` coordinate alone forces repetition.

## Required verifier commands

```sh
python3 -I verification/verify_rl316_row_energy.py
python3 -I verification/verify_rl316_g2_dual_shadow.py
```

Both passed in the promotion candidate and must pass again after fresh unpack.
