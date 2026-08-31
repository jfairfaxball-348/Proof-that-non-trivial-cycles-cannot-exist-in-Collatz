# RL195 physical-window subtask — scope and dependency checkpoint

Status: **NOT PROMOTED**, pending parent review/red team.
BASE_HEAD: `df980ce3df6fa3e8906a934692221917af25644a`.
No authority, session, tracked file, Git object, or remote ref was mutated.

## Current exact checkpoint

The proof note gives an exact reconstruction theorem and odd-denominator
equivalence, not a new independent window obstruction.  The supplied
physical transport telescope and corrected owned-gap coordinate are
explicitly inherited, with targeted RL175/RL181 provenance.  There is no
claim of priority over unconsulted history.

Critical hypothesis: a complete L-periodic nonnegative integral height word
with h0=0 must satisfy every `a_i=c_i+h_i-h_(i+1)>=1`.  Merely requiring
one-step height rise<=1 does not suffice.
The exact inherited definition `h_i=floor(Ai/L)-sum_(j<i)a_j` makes the
one-step law universal, including mechanical switches, the p-shift carry,
and the period boundary.  Both narrowly consulted RL175/RL181 main reports
state this height construction explicitly.

Critical distinction: without exact dyadic K0, rational reconstruction need
not be integral; with the exact moment K0=2^37 and global admissibility,
the Bezout unit theorem already forces odd integrality.  An initial wording
that odd-integrality would always remain an additional missing constraint
was rejected during research before any candidate promotion; no inherited
claim was invalidated or demoted.

## Authoritative dependencies read

- `authoritative/START_HERE.md`
- `authoritative/RL195_PHYSICAL_WINDOW_TRANSPORT_AND_ZERO_HEIGHT_INCIDENCE_TARGET.md`
- `authoritative/RL194_RANK_ORDER_WEIGHTED_SPEED_HEIGHT_OCCUPATION_AND_OWNED_PREFIX_2026-08-31.md`
- `authoritative/proofs/RL194_WEIGHT_ORDER_AND_ZERO_HEIGHT_OCCUPATION.md`
- `authoritative/RL194_CERTIFIED_FACTS_AND_PROOF_LEDGER.md`
- `authoritative/RL194_CORRECTION_DEMOTION_LEDGER.md`

The parent reports the fresh incoming gate passed at the above BASE_HEAD.
This subtask does not rerun the expensive inherited certificate ranges.

## Targeted historical provenance reads

Only the main report, proof ledger, and correction ledger in each directory:

- `sessions/RL182/RL181_Shallow_Pair_Gap_Corridor_and_Normalized_Width_Occupancy_2026-08-30/`
- `sessions/RL176/RL175_Corrected_P_Shift_Flow_Consumer_2026-08-29/`

RL175.1 already records physical q*y arc transport and full-period closure.
RL181.1 already records corrected K=alpha*T_shift-T and the normalized
rank chain.  The RL175 sparse resultant is not used or revived as an
independent generic obstruction.  No other history was audited.

## Verification and exact coverage

`verify_rl195_window_reconstruction.py` performs exact Fraction arithmetic.
Its finite coverage is the256 bounded `(A,L)=(8,5)` height assignments,
the7 that satisfy all positive-exponent constraints, their35 cyclic gap
checks and175 source/arc-length checks, plus the trivial1-cycle regression.
The actual giant D is not constructed; its coprimality statement has the
symbolic proof `Ap-u0L=1` and the small identity is checked directly.

No actual-constant phase scan or partial computation exists in this subtask.
Nothing about the actual high-branch population is inferred from the toys.
Inherited rank cardinality27057465824, terminal floors190574/1826072,
spacing>=1001, N0 floor43742681439, RL191 flow/variation and the H21 budget
are untouched by this result.

## Files

- `PHYSICAL_WINDOW_RECONSTRUCTION_AND_DENOMINATOR.md`
- `verify_rl195_window_reconstruction.py`
- `SCOPE_AND_DEPENDENCIES.md`

Verifier run: `python3 .rl-work/RL195/agent_window_physical/verify_rl195_window_reconstruction.py`
returned PASS (256 arrays,7 admissible words,35 gaps,175 arcs, trivial1-cycle).
No failed verifier, inherited contradiction, or incomplete range occurred.

Next action: submit the proof and ownership-scope boundary to the parent
for independent red-team review.  No closure or promotion is authorized
for this subtask.
