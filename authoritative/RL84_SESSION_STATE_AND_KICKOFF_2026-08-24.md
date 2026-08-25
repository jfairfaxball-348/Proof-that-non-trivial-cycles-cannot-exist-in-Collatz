# RL84 SESSION STATE AND KICKOFF

Date: 2026-08-24

## Authority

**AUTHORITATIVE OUTGOING RL84 RESEARCH STATE.**

Detailed mathematics:

`RL84_RLFLAT_RLSHARP_EXTREMAL_OWNERSHIP_COMPARISON_AND_CYLINDER_HEIGHT.md`

Selected next target:

`RL85_RLSHARP_RLFLAT_EXTREMAL_OWNERSHIP_BRIDGE_TARGET.md`

No Gate A, Gate B, RL/nontrivial-cycle, or Collatz closure is claimed.

## Verification economy

The supplied RL83 sidecar, internal manifest, and supplied fresh-unpack fast-verifier record are clean.  Accept the frozen RL83 ledger; do not recursively replay historical expensive certificates absent a new unresolved dependency or verifier failure.

## Frozen closure state

- radius-3 primitive/full-`D`: closed local theorem;
- Gate A even terminal `k`: closed analytically;
- Gate A terminal `k<=25`: closed by exact finite certificate;
- Gate A odd `k>=27`: open;
- Gate A globally: open;
- Gate B globally: open;
- RL/nontrivial-cycle exclusion: open;
- Collatz conjecture: not proved.

## New RL84 results

1. **Extremal ownership inversion.**  At the true minimum `R`, the cycle-owned predecessor is the even inverse `2R`; any legal odd inverse lies below `R` and is external.  At the maximum `M`, the cycle-owned predecessor is `(2M-1)/3` and the even inverse `2M` is external.
2. **Canonical feeder.**  Every `2^kM`, `k>=1`, is an external feeder to the actual maximum.
3. **Cylinder transfer.**  The RL82/RL83 cylinder of `M` maps bijectively to a cylinder for `2M` modulo `4*3^o`, preserving normalized cylinder height.
4. **Minimum-prefix surplus theorem.**  Every nonzero backward prefix from the genuine cycle minimum has `2^i>3^{o_i}`.
5. **Opposite extremal rotations.**  Under inherited `R>=2^71`, the maximum-rooted rotation has no surplus through depth `114,208,327,603`, while the minimum-rooted rotation is surplus at every nonzero depth.
6. **Canonical arc factorization.**  If `u=2^d/3^o` is the raw factor on `R->M` and `v` on `M->R`, then `lambda=uv` and `v>M/R>3/2`.
7. **Low arc or huge length.**  Either `u<1`, giving a canonical owned low-excess extremal arc, or `L>3R log(3/2)`.  At `R>=2^71`, the huge branch has
   `L>=2,872,132,254,754,669,047,880`.
8. **First-Farey cylinder height.**  At `(p,q)=(114208327604,72057431991)`, every physical first-surplus word must have normalized cylinder height
   `theta<200000000000/2^q`.
9. **Half-height consequence.**  If the least even cylinder representative is `m=2n`, then `n<3^((q+1)/2)`.
10. **Envelope adversary excluded at first pair.**  `O^qE^(p-q)` cannot satisfy the full first-Farey cylinder/ceiling collision, even though RL83 correctly showed it survives balance + count-envelope + `mod162` tests.

## Route decision

Do **not** revert to RL75 yet.  The user-requested RL#/RL♭ comparison has produced a new owned extremal low/high object and a canonical feeder/max coupling.  RL85 is a focused historical-hypothesis comparison session.

If RL85 shows these couplings add no non-dyadic/full-cycle information, freeze RL♭ and return to RL75's hybrid owned-macro periodicity/packing route.

## Verification

`python3 verification/verify_rl84_extremal_comparison.py`: PASS.

Exact certified values include:

- first-Farey defect `>1/(200000000000)`;
- `floor(3*2^71*log(3/2))=2872132254754669047879`;
- integer huge-branch floor `L>=2872132254754669047880`.

---

# Self-contained kickoff for RL85

Continue from the authoritative RL84 bundle and matching sidecar.

First verify only:

1. outer RL84 sidecar;
2. internal `SHA256SUMS.txt` after fresh unpack;
3. `bash verification/run_fast_rl84_verifiers.sh`.

Then apply the verification-economy rule.

Primary target:

`RL85_RLSHARP_RLFLAT_EXTREMAL_OWNERSHIP_BRIDGE_TARGET.md`.

Mandatory strategic instruction: before reverting to the RL75 route, seriously interrogate the structural differences and transferable lemmas between the historical RL#/first-number/entry-side architecture and the new RL♭ maximum architecture.  Preserve exact object ownership: historical feeder/entry objects, genuine minimum `R`, maximum `M`, and auxiliary variables are not interchangeable.

Close out with a next numbered authoritative bundle and sidecar.
