# RL133 session state and RL134 kickoff

Date: 2026-08-27

## Completed RL number

`RL133`

## BASE_HEAD

`1ccace214c348589f5771f786dbbad03bb54a433`

## Frozen promoted results

At the first reduced above-side survivor

`(A,L)=(217,976,794,617,137,528,045,312)`,

RL133 proves the following for the **coprime full-count realization `g=1`**:

1. Rooting an actual cycle at its least odd state and writing accelerated prefix exponent sums `S_j`, every proper prefix obeys
   `S_j log2-j log3 < 0`.
2. Rigorous log intervals give the exact floor lock
   `floor(j log_2 3)=floor(Aj/L)` for every `1<=j<L`, hence
   `S_j<=floor(Aj/L)`.
3. The defect `h_j=floor(Aj/L)-S_j` is a nonnegative excursion from zero to zero, rises by at most one, and gives physical height bands
   `2^h m/rho < y < lambda 2^h m/rho`.
4. Conditional on inherited external `R#>=2^71`, exact arithmetic forces at least `176,343,262` odd phases with `h<=3` and at least `3,370,832,656` with `h<=4`.
5. The zero-defect mechanical extremal has a determinant-one cyclic shift of adjacent-transposition distance `1`; by the inherited closed radius-three engine it cannot be an actual primitive nontrivial cycle. Therefore any `g=1` survivor must have nonzero defect somewhere.

## Scope / correction ledger

No inherited theorem is demoted. A scratch-level overreach is explicitly not promoted: the first **reduced** survivor does not force `g=1`. Full counts `(gA,gL)` with `g>1` remain open and the new all-prefix theorem is not asserted there.

The frontiers are unchanged:

- internal primitive ordinary frontier: `L>=190,537`;
- conditional on inherited external `R#>=2^71`: `L>=49,547,666,544`.

Gate A, Gate B, global nontrivial-cycle exclusion, and Collatz remain open.

## Verification

`verification/run_fast_rl133_verifiers.sh` regenerates the exact CF neighborhood, survivor discrepancy/floor lock, determinant-one mechanical shift, mechanical-mass upper bound, and shallow-defect population constants. Fresh-unpack sidecar, internal manifest, and fast verifier all pass in the closeout package.

## RL134 kickoff

Continue with `RL134_DEFECT_EXCURSION_AND_MULTIPLICITY_TARGET.md`.

Do not restart bare CF, fixed-depth complete residue-prefix descent, or count-only gcd blocks. Work the physical defect excursion on `g=1` and the physically owned multiplicity extension on `g>1` as the two live branches.
