# RL194 weighted chronological speed: independent bounded red team

Status: **PASS — NOT PROMOTED**.
Date: 2026-08-31.  BASE_HEAD: `4ded9b73d84cd3f9101c9eaef81d783e14390914`.

Audited main scratch certificate:
`../artifacts/chronological_speed_limit.py`, SHA-256
`e33d783c8ad28ded9a053659acb491ac2994401f76779e86d88a1d2a789b2d58`.

The audit did not extend the scan, change the frozen corridor result, edit
authority or make a Git change.  It read the complete main checker, replayed
it, and independently replayed exactly starts 1..1,826,035.
The final main-checker replay also passed the subsequently added exact count,
survivor-list and final sum-width assertions.

## 1. Physical inequality and canonical scope

Before the carry, an ordinary epsilon is a difference of two positive dyadic
numbers at most one.  Therefore `|epsilon_i|<1`, and
`|f_i|<rho_i<=1`.  This gives the strict unit-speed bound `|F_a|<a`, where
`F_a=sum_(0<=i<a)f_i=3(K_a-K0)`.

The anchored inherited signature has zero flows at sources 0..23 and negative
flows at sources 24..28.  Hence the lower atom, whose F_a is positive, must
satisfy

`F_a < sum_(29<=i<a)rho_i`.

The upper atom, whose F_a is negative, must satisfy

`-F_a < sum_(24<=i<a)rho_i`.

These strict formulas apply to all hypothetical physical starts here: RL193
already gives terminal phase at least 71, hence canonical start at least 34.
They need not be stated as strict inequalities for an empty negative-envelope
sum at an arbitrary start a<=24.  No such case is used as an exact hit by the
checker.  The ordinary unit-speed bound remains valid for all checked a>0.

Every checked start and terminal is less than z=72,057,431,991.  Thus no carry
source occurs in a checked prefix, and there is no quasi-periodic rho/K wrap
inside these prefixes.  A canonical start zero is already impossible: its
zero block would meet the known nonzero window and its terminal rank Q is
an inherited deletion.  Wrapped canonical terminal phases 0..36 are excluded
by the inherited terminal floor; this separate fact is needed when converting
start floors to canonical terminal floors by adding 37.

## 2. Coarse-filter logic

With d=|r-Q|, the lower atom has positive x and

`F_a=3K0(exp(x)-1)>2K0*d/L`.

For the upper atom, y=(d ln2-a delta)/L is positive, since
`(L-1)delta<ln2`.  The inherited physical corridor K_a>KLO gives

`-F_a=3K_a(exp(y)-1)
 > (2KLO*d-3KLO*a/2^40)/L`.

Both coarse tests in the main checker are exactly the necessary conditions
obtained by comparing these strict lower bounds with a.  Thus skipped cases
cannot hide a physical speed-compatible candidate.  The upper coarse test
uses the inherited K corridor; it is not a statement about arbitrary
nonphysical values lacking that corridor.

No rank-Q case is sent to the positive-y routine.  On canonical starts
1..1,826,035, rank Q would require a=0 mod L, which is impossible.

## 3. Indexing, outward rounding and transcendental bounds

The main recurrence starts with exact scaled rho_0.  At loop start a, it adds
the enclosure for source a-1 to the relevant prefix sum *before* advancing
rho by `2^c/3`.  The resulting sums therefore cover exactly [29,a) and [24,a),
with no one-source shift.  The mechanical rank used for c is the rank of
that same source.

For integer scaled endpoints, floor of the lower endpoint times `2^c/3`
remains a lower bound.  `(upper*2^c+2)//3` is precisely the ceiling and remains
an upper bound.  Induction proves both rho and cumulative-sum enclosures at
every phase, independently of whether their width is small.

The 80-term rational atanh logarithm enclosure and the eight-term positive
exponential series with its geometric tail are correctly oriented.  For the
upper atom, the map `u -> 1-1/u` is increasing, so the reciprocal exponential
enclosures also have the correct orientation.  All interval comparisons use
Fractions; decimal conversions are display only.  An unresolved interval
comparison would abort rather than silently classify a case.

## 4. Independent replay

`weighted_speed_independent_check.py` uses:

- a different, deliberately looser coarse filter `|r-Q|<a`;
- 128-bit rather than 96-bit outward-rounded rho intervals;
- 96 logarithm terms and ten exponential terms;
- direct floor differences for the mechanical digit, independent of the
  main checker's rolling rank implementation.

The loose filter is justified because d>=a forces the lower magnitude above
a using `2K0>L`, and the upper magnitude above a using the exact inequality
`2KLO-3KLO/2^40>L`.  It retains 26 candidates for exact weighted comparison,
including cases the main coarse filter skips.  All comparisons resolve.

Both implementations give the first compatible necessary starts:

| atom | first start | terminal rank | canonical terminal floor |
| --- | ---: | ---: | ---: |
| lower / 2^38 | 190537 | 88514759934 | 190574 |
| upper / 2^37 | 1826035 | 88515371864 | 1826072 |

These are first survivors of the stated necessary envelope, not physically
realized starts or terminals.  The independent replay ends at the same upper
first hit; no post-1,826,035 scan was run or certified.

Independent checker SHA-256:
`3ef9dfbaa68e2301a9fb54950d766bed54d94055c006b2d9f51c7ccc4507d6bf`.

## 5. Full finite-prefix filter and independent intersection counts

The main checker continues to test lower candidates after their first hit,
through the entire common range 1..1,826,035.  Its result is therefore stronger
than the two earliest-terminal floors alone.  Intersecting with the frozen
new corridor [75446746413,102504571503] minus its 22 inherited isolated
deletions gives the following independently reproduced counts:

| atom | eligible ranks in scanned start range | weighted survivors | new rejections |
| --- | ---: | ---: | ---: |
| lower / 2^38 | 173508 | 9 | 173499 |
| upper / 2^37 | 185747 | 1 | 185746 |
| total | 359255 | 10 | 359245 |

The nine lower survivors are starts `190537*n` for n=1..9.  The only upper
survivor in this range is start 1826035.  These ten survive this filter only.

Because Bp=1 mod L and the scanned start interval has length less than L,
`a -> (a+37)B mod L` is injective.  The finite phase rejection counts are
therefore distinct rank deletions.  Eligibility checks make them disjoint
from the 22 earlier deletions.  The combined necessary-rank cardinality is

`27057825069-359245 = 27057465824`.

No statement is made that the unscanned rank/phase complement passes this
speed filter; it remains untested by this finite certificate.  The displayed
cardinality is the core after the *proved* exclusions only, not a complete
full-period speed-survivor count, physical population or ownership bound.

## 6. Verdict and commands

No indexing, rounding, first-hit, finite-count, canonical-scope or inherited
dependency defect was found.  No mathematical correction/demotion is needed.
Both result types are exact finite necessary-state certificates, supported
by the displayed conditional physical inequalities.  They do not release the
H21 budget, prove realization, improve inherited spacing, or close a branch
or global gate.

Commands replayed successfully:

`python3 .rl-work/RL194/artifacts/chronological_speed_limit.py`

`python3 .rl-work/RL194/agent_rank_order/weighted_speed_independent_check.py`

Final bounded audit status: **PASS**, for the audited hashes and stated
range only.  Everything remains **NOT PROMOTED** pending parent closeout.

## 7. Main proof wording review under CLOSEOUT_LOCK

The complete `../artifacts/CHRONOLOGICAL_WEIGHTED_SPEED.md` was also read.
Its indexing, physical inequalities, exact-tail formulas, first-hit claims,
finite-prefix deletion rule, count interpretation and canonical-anchor
restrictions match the verified checker.  In particular it correctly treats
the ten-entry rule as a finite-prefix filter and makes no decision outside
the scanned start interval.

One small scope clarification was requested in its final paragraph: wording
that "spacing between distinct extremal terminals ... remain open" should
explicitly preserve the inherited spacing >=1001, and state that no
improvement to that bound is claimed.  This is not a failed mathematical
check or demotion, but prevents ambiguity about the inherited bound.  The
parent has been notified; final wording readback is pending.

Resolution: the revised final paragraph was read back.  It explicitly keeps
H21 counts/charging unchanged, preserves inherited spacing >=1001, claims no
spacing improvement, and leaves the sole high branch/global gates open.
The sole wording clarification is resolved.  The final proof SHA-256 is
`313734081422ce410f4798a3a103cffa220601fc582b1d9bbc77712d8c5d1aaa`.

Final combined proof-and-code sign-off: **PASS**, no outstanding finding.
The same resolved scope paragraph was also read back from the packaged
candidate at `../candidate/authoritative/proofs/RL194_CHRONOLOGICAL_WEIGHTED_SPEED.md`.
