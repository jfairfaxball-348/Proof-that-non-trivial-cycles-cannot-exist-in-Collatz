# RL194 bounded red team — rank corridor and owned prefix

Status: **PASS**, scratch only, **NOT PROMOTED**.
BASE_HEAD: `4ded9b73d84cd3f9101c9eaef81d783e14390914`.
Date: 2026-08-31.

This review audited only the two requested completed subtask candidates and
their verifiers.  It introduced no new research route, phase scan, historical
audit, authority edit or Git mutation.  The parent-established incoming gate
and current RL193 ledgers were accepted under verification economy.

## Audited bytes

SHA256:

- `agent_rank_order/RANK_ORDER_AND_CORRIDOR.md`:
  `2b5a6ad4b3883bea3d8ba107de013e356b8ad02157ecb577a7bb71300dd817d2`
- `agent_rank_order/verify_rank_order.py`:
  `aaa10b9103ce03de34ede1f58ee4d24f4dc4c5c0cd067d01c50511181d4a5ca3`
- `agent_owned_prefix/OWNED_PREFIX_RESULT.md`:
  `cf2fe96a023bbbc866b89e365df277b29d2921b26cbe2286a86a5141704d8538`
- `agent_owned_prefix/verify_owned_prefix.py`:
  `a6ab9fac24ccf6dd9860cdcf38397d59758085954c52023bd7fd3797f86ef7c6`

All four paths are relative to `.rl-work/RL194/`.

## Rank order and K-corridor audit

**Global rank monotonicity: PASS.**  For rank difference `d>=1`, the exact
log-ratio numerator is `d ln2+(i-j)delta`.  The strict bounds
`ln2>2/3`, `(L-1)2^-40<1/6` and `i-j>=-(L-1)` give a strict lower bound
`>2d/3-1/6>=d/2`.  This covers every canonical pair analytically.  No
sampling is substituted for the full rank domain.

**Atom seam and phase convention: PASS.**  The lower atom's factor `2^38`
is exactly reduced by two when its start rank is written `r-Q+L`.
The upper atom uses `2^37` with start rank `r-Q`.  Both give
`F(r)=2^37 exp(((Q-r)ln2+a(r)delta)/L)` with canonical
`a(r)=((r-Q)p) mod L`.  The same bounded chronological correction proves
strict reverse rank order through the seam.  Necessary comparison values
are not claimed to be realized.  A wrapped 37-zero start would have
canonical terminal in `0..36`, already excluded by the inherited floor 71;
the physical start and terminal therefore lie in one canonical interval.

**Corridor endpoints and coverage: PASS.**  The four exact rational log
enclosures have the reported strict signs.  Global monotonicity consequently
proves the gap-free corridor-test interval
`[75446746413,102504571503]`, not merely four isolated tests.
The proof correctly distinguishes passing this one necessary test from
physical sufficiency.

**Deletion counts and finite boundaries: PASS.**  The incoming 24 isolated
deletions are reconstructed from complete finite carry/early-window ranges.
Exactly the two old E endpoints fall outside the new interval; 22 remain.
The surviving necessary-rank cardinality is `27057825069`, with
`3963343140` additional exclusions beyond RL193.  These are explicitly not
physical populations.  The reported phase floors 73 overall/upper and 78
lower follow from the inherited floor plus the complete stated small ranges.
The boundary survivors are not realizations.  Both carry-buffer witness
ranks survive the stated rank filters, so this corridor refinement alone
does not improve the inherited 11/5 and 4/7 buffers.

**Quantified prefix signs: PASS.**  The already-deleted ranks `Q-1,Q` are
handled before using `Q-2,Q+1` as the nearest available comparator ranks.
Monotonicity, `exp(x)>1+x` and `1-exp(-y)>y/(1+y)` justify the strict
physical prefix bounds `>417/100` and `<-19/10`.  They are canonical signed
displacement inequalities, not unsigned-variation or time-order claims.

## Owned-prefix audit

**Owned numerator and initial domain: PASS.**  The inherited ordinary gap
`Delta_t=3^37/2^21`, maximum height 21 and nonzero defect imply the exact
owned numerator `C=3^37`, with exactly 42 ordered unequal pairs of maximum
21.  The numerator is not replaced by a freely selected odd value.

**Common mechanical word and carry avoidance: PASS.**  The rank intervals
at source offsets 0,1,2 are respectively
`[72797034370,103818202602]`,
`[15717738363,46738906595]`,
`[96166487668,127187655900]`, giving common word `212`.
The source rank and its p-shift companion rank `r+1` have the same digit;
neither the switch at `R-1` nor carry at `L-1` is crossed within the stated
three ordinary transitions.  The cell splitter includes every rotated
wrap, switch and carry boundary and their adjacent integer cuts.  Therefore
testing both endpoints of every contiguous cell is gap-free, including
every successor-carry predicate used.  The report's reason for stopping
at depth 3 is also correct: offset 3 crosses the switch and the listed
larger interval contains rank `90789138715`, whose offset-4 source is the
carry.  This last exact boundary check is solely an audit of the stated
limitation, not a depth-4 propagation or extension.

**Necessary transition relation: PASS.**  Direct substitution of
`3X+1=2^alpha X'` and `3Z+1=2^beta Z'` yields the displayed N for both
signs of g and at g=0.  Unequal power exponents force `v2(N)` to their
minimum; equal exponents force a strictly larger valuation.  Dividing by
the smaller power gives the correct successor owned numerator for either
successor sign.  The nonnegative-height caps enumerate every permissible
positive accelerated exponent.  The independent normalized recurrence is
checked on every accepted edge.  Additional physical congruences are not
claimed to follow from this necessary parity filter.

**Immediate-zero interfaces and consecutive-zero prohibition: PASS.**
The first-step valuation table is correct.  For `g=+3`, the only zero
interface is `(alpha,beta)=(4,1)`, giving `(19,19,(3^38+7)/16)`.
For `g=-1`, it is `(1,2)`, giving `(21,21,(3^38-1)/4)`.
Each numerator has valuation exactly one.  At the next ordinary common-digit
source, another zero would require equal positive accelerated exponents d
and `v2(3C')>d`, impossible when `v2(3C')=1`.
All exceptional sign ranges and the nonexceptional sign/exponent
restrictions match the complete first-step enumeration.

**Finite coverage and parity-filter barrier: PASS.**  State merging uses the
full `(h,hp,C)` triple, preserving every allowed necessary successor.  The
initial signed difference uniquely identifies each of the 42 initial height
pairs and is retained through the three-step paths.  Hence the certificate
really verifies that all 42 have necessary paths through depth 3.  The
reported counts are correct:

- depth 1: 540 states / 540 edges; signs 268 negative, 2 zero, 270 positive;
- depth 2: 4202 / 4517; signs 2182, 16, 2004;
- depth 3: 25417 / 30977; signs 14766, 16, 10635.

There are 44 possible four-source sign patterns in this necessary graph.
The barrier is limited to this particular three-transition parity filter:
it eliminates no initial pair and sees the same word in both atoms.
No physical realization, impossibility of stronger congruence methods,
later-depth coverage or H21 consequence is inferred.

## Commands and result

Executed both supplied commands, each with exit status 0:

`python3 .rl-work/RL194/agent_rank_order/verify_rank_order.py`

`python3 .rl-work/RL194/agent_owned_prefix/verify_owned_prefix.py`

Both returned **PASS**.  All reported constants and graph counts matched.
No defect, inherited contradiction, scope escalation or required repair
was found in these two bounded candidates.  Their classification remains
conditional analytic results plus exact necessary-state certificates;
the inherited H21 budget, spacing, branch and global obligations remain open.

Final bounded audit status: **PASS** for the audited bytes above.
