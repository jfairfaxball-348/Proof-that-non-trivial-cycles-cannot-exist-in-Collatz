# RL195 independent red team — owned local realizability

Date: 2026-08-31. **NOT PROMOTED — review artifact.**
Incoming RL195; BASE_HEAD `df980ce3df6fa3e8906a934692221917af25644a`.
Reviewer: the independent mechanical-zero-geometry worker, not the author.

## Status

**PASS — all findings resolved and repaired files independently read back.**
The analytic local-realizability theorem and the complete stated finite
certificate pass. One minor verifier-helper domain mismatch was repaired
by the main worker and is closed in section5. It did not invalidate the
analytic theorem or the declared replay, which uses `t=1 mod3^5`.
No inherited proof or mathematical bound is invalidated.

Reviewed in full:

- `agent_owned_realizability/OWNED_LOCAL_REALIZABILITY.md`, initial SHA256
  `ab7f99803db76db19fb2b4bed286652a2a41c555f438e2084c7dcfe048807211`;
- `agent_owned_realizability/verify_owned_local_realizability.py`, initial
  reviewed SHA256
  `1545c3769f56c3c96ff5692e72d6b02d43114e458e442445820ec9acddd8fdb4`.

These paths are relative to `.rl-work/RL195/`. The review used the current
authoritative RL194 owned-prefix proof and its explicit height/numerator
scope. No history replay, new phase scan, authority mutation or Git change
was performed.

## 1. Analytic checks

### Exact finite acceleration seed class — PASS

The recurrence `S_(j+1)=3S_j+2^A_j` gives
`X_j=(3^j X_0+S_j)/2^A_j`. Endpoint oddness is exactly the residue modulo
`2^(A_n+1)` in equation(1). It implies every earlier exact valuation,
not merely divisibility: starting from valuation A_n, subtracting `2^A_j`
from the next numerator of valuation `A_(j+1)>=A_j+1` leaves valuation
A_j; dividing by odd3 preserves it. This backward induction is valid at
every prefix, including the seed. Forward positivity follows once X_0>0.

An additional independently structured brute-force check exhausted all85
exponent words of lengths0..3 with each exponent1..4, testing all27,931
odd seed residues in their corresponding full dyadic modulus. Exactly the
claimed unique seed class survives for every word. These are finite lemma
regressions, not physical-branch phase coverage.

### Owned normalization and compatibility sign — PASS

For a path, `g_n=(eZ+B_n)-(eX+A_n)` and
`D_n=3^n C0+2^eZ T_n-2^eX S_n`. The raw owned equation at the endpoint
is `2^(eZ+B_n)Z_n-2^(eX+A_n)X_n=D_n`.
Factoring the smaller exponent proves equation(2), including the update
of that smaller exponent under every accepted graph edge.

The simultaneous seed/line condition is exactly
`C0+2^eX rX-2^eZ rZ=0 mod2^(m+1)`: the gcd of the two seed-variation
coefficients is `2^(m+1)`. Multiplying by odd `3^n` gives
`D_n+2^u-2^v`, with the signs as displayed in the proof. If u!=v, both
summands of valuation m have residue `2^m mod2^(m+1)` and cancel; if
u=v, the terms cancel and even C_n supplies the extra factor2. Thus the
graph's endpoint parity condition establishes actual two-word consistency.

The whole initial solution set is a nonempty dyadic residue class of the
single owned-line parameter. One parameter arm has coefficient1; the other
has a power-of-two coefficient. The power-division and stronger-compatible-
modulus construction in the code are valid, including a vacuous congruence
when its coefficient already contains the full modulus.

### Positivity, sizes and odd-modulus augmentation — PASS

Both initial odd states are affine functions of the parameter with positive
slope. After a sufficiently large positive choice, each finite acceleration
preserves positivity; all later states also have positive slope as functions
of the parameter. Consequently every fixed finite set of lower size bounds
is achievable. The theorem does not claim arbitrary upper size bounds.

The CRT step is valid for an odd D because `2^M` is invertible modulo D.
Any nonempty condition on the initial affine line modulo odd D contains a
residue class, and that class intersects the dyadic seed class in an
infinite progression. Multiple odd conditions must themselves be compatible
on the line. The proof explicitly excludes a claim that global conditions
or path-dependent identifications are automatically compatible.

In addition to the declared replay, the reviewer independently constructed
and directly replayed witnesses with **t=0 mod3 for all34,039 final paths**.
The initial odd states may then be divisible by3; all later states are
nonzero modulo3 and have the exact prescribed valuations. This separately
confirms that the general local theorem is not restricted to the author's
particular t=1 class. It remains an uncoupled local relaxation.

## 2. Complete finite certificate and path accounting — PASS

Ran successfully:

`python3 .rl-work/RL195/agent_owned_realizability/verify_owned_local_realizability.py`

The exact root set contains both `(21,j,C0)` and `(j,21,C0)` for every
`0<=j<=20`, with `C0=3^37=450283905890997363`: 42 distinct roots.
At each of exactly three depths with digits212, every positive integer
exponent pair within both nonnegative-height caps is tested. The code's
strict/equality valuation branches match the inherited necessary rule.

Merged-state counts: `540,4202,25417`.
Edges from merged states: `540,4517,30977`.
Full path counts: `540,4517,34039`.

The second traversal retains the root and the entire exponent/state record,
so state merging cannot erase cross-step consistency. It obtains transitions
from a complete per-depth state cache but constructs and checks a witness
for every full history at every depth. All roots have depth3 witnesses.
Every intermediate step checks exact v2 values, positivity, oddness, height
values and the exact owned numerator. The second member of each CRT family
also receives exact exponent replay.

All44 four-source sign patterns are counted from full depth3 records, not
from independently combinable edge signs. The deterministic replay digest
matches the report:

`34837dc796e7637e7044c1ad3393a31a2baef7129ea9b9154d7775928810277f`.

The two illustrated immediate-zero pairs also match their exact exponent
and height interfaces. The report correctly calls them depth1 illustrations
rather than relying on them as the complete depth3 certificate.

Additional audit command:

`python3 .rl-work/RL195/agent_zero_geometry/verify_owned_seed_red_team.py`

Output: `85` small words, `27931` odd residue tests, all `34039` final
paths under t=0 mod3, all `42` roots and `44` sign patterns — PASS.
This audit script does not edit the source component.

## 3. Scope and provenance — PASS

The proof consistently means two *uncoupled finite positive odd accelerated
trajectories*. It does not require Z_0 to be reached from X_0 after p steps,
or period-L closure, the fixed total-A global orbit, all p-edge relations,
the exceptional carry, canonical h_0, the early G signature, tau37
prehistory, K bounds, occupation/window moments or H21 ownership.

The initial height and numerator values are exact; their presence alone
does not restore those missing physical couplings. The common mechanical
word212 is inherited on the stipulated rank superset and is not extended
to a fourth transition. No speed-cutoff extension is made. None of the
state, edge, path or sign-pattern counts is presented as a physical terminal
population. Both atoms and every global closure obligation remain open.

The stated method barrier is therefore properly restricted: the present
forward local parity graph cannot be strengthened solely by requiring local
positive-odd consistency or *compatible initial* odd-modulus conditions.
Genuinely additional physical/prehistory/global conditions can still matter.

## 4. Resolved minor helper-domain finding, not a theorem failure

In the initially reviewed verifier, `choose_seed` advertises an arbitrary
odd modulus/residue but unconditionally asserts `x % 3 and z % 3` at its
line138. The compatible initial class t=0 mod3 is permitted by the stated
local relaxation but fails that extra helper assertion. The declared
finite replay always uses t=1 mod3^5, so its execution and digest are
unaffected, and the general CRT proof remains correct.

The requested narrow repair was to remove or condition the initial nonzero-mod3
assertion in the general helper, retaining the nonzero-mod3 checks in the
specific t=1 replay; alternatively narrow the helper's documented domain.
No mathematical correction/demotion is required. This reviewer did not
modify the author's files. The repair and its accepted readback follow.

## 5. Repair readback

The main worker repaired `choose_seed`: odd residues are normalized modulo
their odd modulus, and the unconditional initial nonzero-mod3 requirement
was replaced by the exact owned-line equivalence between initial divisibility
of X, Z and t when C is divisible by3. Successor nonzero-mod3 checks and
the original default t=1 mod3^5 witness family are preserved. The proof's
section5 now explicitly documents this interface repair without changing
the theorem's mathematical scope.

The reviewer read both repaired files completely and reran both the source
verifier and the independent audit script. All checks passed. The additional
source-helper regressions test336 cases (42 roots by eight inputs), including
modulus1, t=0 mod3, negative/noncanonical residue representatives;126 cases
have initial states divisible by3. Every checked step retains its exact
valuation and owned numerator. The original full-path counts,44 patterns
and witness digest are unchanged.

The independent alternate t=0 mod3 replay again covers all34,039 final
paths and42 roots. The small-word check again covers85 words and27,931 odd
residues. No new physical or chronological range is asserted by these checks.

Accepted repaired SHA256 identities:

- proof: `5ec3d6e89432ed7af95dd55b9abac3b13e3f2a74e3c0090f623d068f2357420c`;
- verifier: `502fa58d660d72711fa07e5fda110b84f6d5802abd043c67453e5714ba282389`.

Finding status: **CLOSED / PASS**. No unresolved mathematical, scope or
coverage finding remains in this component review.
