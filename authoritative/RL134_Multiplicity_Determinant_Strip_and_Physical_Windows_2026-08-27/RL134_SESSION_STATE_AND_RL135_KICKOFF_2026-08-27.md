# RL134 session state and RL135 kickoff

Date: 2026-08-27

## Completed RL number

`RL134`

## BASE_HEAD

`196ee7fe627c09889664f3508962b7a1e12025bf`

## Frozen promoted results

At the first reduced survivor

`(A,L)=(217,976,794,617,137,528,045,312)`,

RL134 promotes:

1. For full counts `(gA,gL)`, every physically positive proper prefix with determinant `r=SL-jA` satisfies the exact strip
   `0<r+j epsilon<gL epsilon`, `epsilon=Delta/log2`, and belongs to the explicit translate family determined by `r`.
2. The certified shell constant is `theta=L epsilon=0.1783030376029087...`.
3. For `g<=6`, every positive proper prefix is a canonical contact `(kA,kL)`. No off-axis positive prefix is possible.
4. For `7<=g<=11`, the only additional candidate prefixes are the determinant-one families
   `W+k(A,L)` with `0<=k<=g-7` and
   `U+k(A,L)` with `6<=k<=g-1`,
   where
   `W=(114208327604,72057431991)` and
   `U=(103768467013,65470613321)`.
5. On `g=1`, the least odd state satisfies `m<2^75`.
6. Conditional on inherited external `R#>=2^71`,
   `#{h<=3}>=176421674`,
   `#{h<=4}>=3399794205`,
   with the corresponding actual odd states below `2^79` and `2^80`, respectively.

## Scope / correction ledger

No inherited theorem is demoted.

No frontier advance:

- internal primitive ordinary frontier: `L>=190537`;
- conditional on inherited external `R#>=2^71`: `L>=49547666544`.

The `g=1` branch remains open. Multiplicity is not bounded: the explicit low-shell classification stops at `g=11`, and determinant-two shells enter at `g=12`.

Gate A, Gate B, global nontrivial-cycle exclusion, and Collatz remain open.

## Verification

`verification/run_fast_rl134_verifiers.sh` reconstructs the rigorous log intervals, survivor/neighbor determinants, multiplicity strip thresholds, `g<=11` shell classification inequalities, the `g=1` `m<2^75` bound, sharpened top-rho population constants, and absolute shallow-state windows.

Fresh-unpack sidecar, internal manifest, and fast verifier all pass in the closeout package.

## RL135 kickoff

Continue with `RL135_LOW_MULTIPLICITY_CANONICAL_CONTACT_AND_ABSOLUTE_WINDOW_TARGET.md`.

Prioritize actual ownership at the canonical contacts for `2<=g<=6`, the two determinant-one neighbor families for `7<=g<=11`, and the `g=1` absolute physical windows. Do not restart bare CF, fixed-depth complete residue-prefix descent, or count-only gcd blocks.
