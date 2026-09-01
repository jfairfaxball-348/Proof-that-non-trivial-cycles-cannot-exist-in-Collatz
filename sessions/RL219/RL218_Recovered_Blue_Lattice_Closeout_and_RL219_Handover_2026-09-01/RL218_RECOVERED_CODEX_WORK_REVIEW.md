# RL218 recovered Codex work review

Date: 2026-09-01.

## Source identity

Recovered source: the repository file formerly at `authoritative/RL218 work - closing.zip`.

- Git blob: `bf6b9bd06442bfaec51cb6ef786af4858c916806`
- size: `606,019 bytes`
- research BASE_HEAD recorded in scratch: `ffcc8711a8512b6f8d05438b6247ec1cb1d9d46c`

The exact source ZIP is preserved under `sessions/RL218/provenance/`.

## What was recoverable and reviewed

The scratch checkpoint records:
- backward-word algebra verifier PASS:
  `65,408 raw; 135,036 grouped; 45,046 bases; zero LTE-comb screens`;
- bounded reverse-tree verifier PASS:
  `depths 0..86; 45,045 lattices; 43,370 odd in-range endpoints; zero matches`;
- no corrections/demotions;
- no promoted exact candidate ranges;
- all **139,581,280** RL217 candidates still uncovered by certified-blue membership.

The proof artifact `RL218_BACKWARD_WORD_ALGEBRA.md` was decoded and reviewed. Its finished content supplies the terminal-legality theorem, odd-only normal form, RL217 lattice pullback, phase-cylinder intersection rule, fixed-seed singleton barrier, and the exact all-prefix RL80 comb exclusion argument.

## Incomplete/abandoned work

The scratch itself marks:
- fixed-seed depth growth as a singleton equality probe;
- all depths >86 untested by the bounded seed-1 certificate;
- a certified-interval / blue-floor automaton interrupted before its intended horizon;
- a 40,003-candidate forward-floor sample as computational evidence only.

Those incomplete pieces are not promoted.

## Classification decision

Promoted:
- finished analytic backward-word/lattice algebra;
- fixed-seed singleton/quantifier barrier;
- two exact bounded negative screens, with zero candidate/rank deletions.

Not promoted:
- unfinished forward-floor automation/sample;
- any extrapolation beyond the certified bounded scopes;
- any claim of exact blue membership from congruence or legal-branch membership alone.
