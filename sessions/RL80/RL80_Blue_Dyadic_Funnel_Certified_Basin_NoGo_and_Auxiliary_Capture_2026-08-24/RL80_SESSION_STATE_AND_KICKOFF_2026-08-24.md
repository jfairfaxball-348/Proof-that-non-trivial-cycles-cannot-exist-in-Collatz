# RL80 SESSION STATE AND KICKOFF

Date: 2026-08-24

## 0. Authority and scope

**AUTHORITATIVE OUTGOING RL80 RESEARCH STATE.** Gate A remains open globally, Gate B remains open globally, and no RL/nontrivial-cycle/Collatz closure is claimed.

Detailed mathematics:

`RL80_BLUE_DYADIC_FUNNEL_CERTIFIED_BASIN_RESULTS.md`.

Selected next target:

`RL81_AUXILIARY_BASIN_TRANSFER_AND_EQUALITY_LEVEL_CAPTURE_TARGET.md`.

## 1. Verification economy rule — retained

After the current bundle checksum, internal manifest, and fast verifier suite pass, accept the frozen incoming proof-state ledger as authoritative. Do not recursively rerun historical expensive certificates unless a new load-bearing argument depends on an unresolved historical definition, a verifier fails, or an apparent contradiction triggers stop-and-repair.

## 2. Incoming RL79 gate

The RL79 outer sidecar, fresh internal manifest, and fast verifier all passed before RL80 mathematics.

No historical expensive finite suite was recursively rerun.

## 3. Frozen inherited proof state

Retain RL79 exactly:

- radius-3 primitive/full-`D` local obstruction: closed;
- Gate A even terminal `k`: closed analytically;
- Gate A terminal `k<=25`: closed by exact finite-certificate corollary;
- Gate A odd `27<=k<=165`: open;
- Gate A globally: open;
- Gate B globally: open;
- RL/nontrivial-cycle exclusion: open;
- Collatz conjecture: not proved.

RL79's unit-increment/homogeneity barrier remains mandatory: a successful route must use a non-homogeneous fact special to ordinary `s=1` Collatz.

## 4. New RL80 theorem A — odd-core equivalence

For `N=2^v m` with `m` odd,

`N` reaches `1` iff `m` reaches `1`.

For a certified interval `[1,X]`, its dyadic saturation is exactly

`{N: oddcore(N)<=X}`.

Classification: analytic theorem.

## 5. New RL80 theorem B — dyadic saturation is cycle-intersection neutral

For every exact periodic orbit `C` and seed set `S`,

`C ∩ {2^k s:s in S,k>=0}` is nonempty iff `C ∩ S` is nonempty.

Thus the infinite blue doubling rays from a verified finite range do not strengthen the cycle minimum floor.

Classification: analytic no-go theorem.

## 6. New RL80 theorem C — arbitrary backward closure is also neutral as a set trap

For

`Pre*(S)={x:T^r(x) in S for some r>=0}`,

one has

`C ∩ Pre*(S) != empty iff C ∩ S != empty`

for every periodic orbit `C`.

Backward trees remain useful only if independent RL arithmetic forces exact equality with one of their nodes.

Classification: analytic no-go theorem.

## 7. New RL80 theorem D — LTE blue comb

For odd `k` and

`1<=j<=1+v3(k)`, define

`B(j,k)=2^j(2^k+1)/3^j-1`.

Then `B(j,k)` is a positive odd integer whose first `j` shortcut steps are odd and land at `2^k`, hence it reaches `1`.

There are infinitely many such blue numbers for every prescribed depth `j`.

Classification: analytic basin theorem.

## 8. New RL80 theorem E — logarithmically dense analytic blue mesh

The fractional parts of `log_2 B(j,k)` are dense in `[0,1)`.

Consequently, for every multiplicative tolerance `epsilon>0`, finitely many analytic blue dyadic rays form an `epsilon`-net on the log scale above some threshold.

This rigorously realizes a very strong blue-belt intuition but does not force exact integer intersection.

Classification: analytic theorem + proximity/quantifier barrier.

## 9. Modular audit

- modulo `2^a`: dyadic rays eventually become `0`;
- modulo `3^b`: `2` is a primitive root, so the single blue ray from `1` covers all units;
- modulo `24`: any certified interval with `X>=24` already covers all residues;
- modulo full odd `D`: each blue ray gives only a finite multiplicative `2`-orbit/coset.

No residue coverage implies exact basin membership without a size/equality theorem.

## 10. New RL80 theorem F — terminal all-11 auxiliary basin capture

Using the exact RL64 theorem,

`J_0+1=2^j q`, `3^j q=2^k+1`,

so

`J_0=B(j,k)`.

Therefore the terminal all-`11` full-phase auxiliary entry `J_0` is analytically certified blue.

For `k>=3`, the RL50 coordinate

`n_0=(J_0-1)/2`

is also analytically certified blue.

Classification: analytic synthesis from inherited full-phase formulas plus ordinary Collatz.

## 11. New limitation — auxiliary basin capture is not cycle-state capture

`J` and `n=(J-1)/2` are auxiliary quotient/full-phase coordinates. No theorem currently identifies either as an original cycle state or transfers their basin membership to one.

RL50's historical warning remains controlling: height-one synchronized dynamics can re-embed Collatz inside the quotient system.

The missing bridge is therefore an exact basin-preserving transfer from these auxiliary coordinates to a genuine owned cycle integer.

## 12. New selector clarification

For one synchronized height-one step on odd `J`,

- `11`: `J'=(3J+1)/2`;
- `00`: `J'=(J+1)/2`.

With `n=(J-1)/2`, integer shortcut-Collatz continuation requires the synchronized bit to equal `n mod2`, equivalently `J==1+2x mod4`.

Under that selector the next `J` stays odd, so a first-even terminal exit necessarily leaves the integer Collatz-conjugate continuation at its exit edge.

Classification: analytic coordinate/method barrier.

## 13. Generalized-map red-team

Pure dyadic closure uses only the unchanged even branch and is therefore not `s=1`-specific.

The legal odd predecessor `(2y-1)/3`, the LTE comb, and the all-`11` basin capture do use the absolute `+1`.

Exact negative control:

- ordinary map: `5 -> 8 -> 4 -> 2 -> 1`;
- `T_5`: `5 -> 10 -> 5`.

## 14. RL80 exact verifier

`python3 verification/verify_rl80_blue_basin.py`: PASS.

Counts:

- odd-core saturation checks: 131,072;
- LTE blue-comb checks: 227;
- RL50 auxiliary-blue checks: 226;
- primitive-root spot checks: 8;
- multiplicative-density checks: 99,752;
- ordinary `s=1` / generalized `s=5` negative control: PASS.

## 15. Correction/demotion ledger additions

Add:

- pure dyadic-belt closure is dead as a standalone cycle trap;
- full backward-tree abundance is not a stronger set-theoretic cycle trap;
- modular and multiplicative proximity arguments remain non-closing without exact equality;
- LTE blue comb is promoted as an analytic infinite basin family;
- logarithmically dense analytic blue mesh is proved but explicitly non-closing;
- terminal all-`11` auxiliary `J` and RL50 `n` basin capture is promoted;
- basin membership of auxiliary quotient coordinates is not cycle-state basin membership;
- a basin-preserving transfer/equality lemma is the live missing mechanism.

## 16. RL81 decision

RL81 should focus on the exact coordinate-transfer question:

**Can the RL64/RL50 basin-captured terminal all-`11` auxiliary coordinate be transferred, through exact RL48 full-phase reconstruction, to an actual owned cycle integer by basin-preserving operations?**

If the exact reconstruction proves this impossible, freeze the blue route as a barrier result and pivot back to RL79's other non-homogeneous `s=1`/unit-lattice/content programme.

---

# Self-contained kickoff for RL81

Continue the Collatz R-sharp / RL research from the authoritative RL80 bundle and matching `.sha256` sidecar.

First verify only the current RL80 gate:

1. outer RL80 sidecar;
2. freshly unpacked internal `SHA256SUMS.txt`;
3. `bash verification/run_fast_rl80_verifiers.sh`.

Apply the verification-economy rule after those pass.

The primary target is:

`RL81_AUXILIARY_BASIN_TRANSFER_AND_EQUALITY_LEVEL_CAPTURE_TARGET.md`.

Mandatory RL80 context:

- pure dyadic saturation and arbitrary backward closure are cycle-intersection neutral as set traps;
- the LTE family `B(j,k)` gives a real ordinary-Collatz analytic basin;
- terminal all-`11` RL64 auxiliary `J_0` is exactly one of those blue integers;
- RL50 `n_0=(J_0-1)/2` is also blue for `k>=3`;
- neither is currently an original cycle state;
- density/proximity/residue arguments are not acceptable substitutes for equality-level basin capture.

Before ending, freeze exact proofs, failures, dependencies, corrections and verifier status; create the next numbered authoritative bundle and sidecar; verify internal manifest and fresh-unpack fast suite.
