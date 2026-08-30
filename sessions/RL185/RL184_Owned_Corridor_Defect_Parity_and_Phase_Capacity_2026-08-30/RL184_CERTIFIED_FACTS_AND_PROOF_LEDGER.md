# RL184 certified facts and proof ledger

## New proved analytic mathematics

- **RL184.1 — one-state mechanical overlap.** In strict p-rank order adjacent normalized states are separated by more than `128,081,997,553`, while the `c=1/c=2` overlap interval has width `1/3`. Hence at most one physical state lies in the overlap. Only rank `R=57,079,296,007` can be a late state below `4m/3`; every late rank `r>R` lies strictly above `4m/3`.
- **RL184.3 — signed affine-intercept identity.** On a clean ordinary common-mechanical transition,
  `q_i(2^G_i-1)=rho_i 2^-M D`,
  where `D=2^(M-b)-2^(M-a)`. Thus `sign(D)=sign(G)` and `D=0` exactly when `G=0`.
- **RL184.4 — shallow zero-defect lifetime.** A clean zero-defect run obeys
  `2^(sum d_j) C_(i+n)=3^n C_i`, with every `d_j>=1`. Since an `h<=1` start has `C_i<587,183,637,564<2^40`, forty consecutive zero-defect transitions are impossible.
- **RL184.4a — extremal 39-run rigidity.** A 39-zero run from an `h<=1` start forces initial type `(1,1)`, `C_i=2^39`, every `d_j=1`, exactly 23 late mechanical bits, terminal common height 24, and terminal numerator `3^39`; therefore the next ordinary defect is nonzero.
- **RL184.5 — distinct nonzero-defect incidence.** At least `10,075,174,499` clean 40-edge physical corridors exist, each containing a nonzero defect. Therefore at least `251,879,363` distinct physical phases have nonzero defect.

## Analytic results with exact integer certificates

Inside the surviving `(37,0,23,-1)` high branch only:

- the only actual length-three chronological mechanical words are
  `121, 122, 212, 221`;
- the RL183 three-transition necessary vocabulary shrinks to `1,818` templates and `270` composite affine maps;
- some necessary template is physically used at least `5,541,901` times;
- some composite affine map is physically used at least `37,315,462` times;
- exactly `210` necessary three-transition templates have zero composite intercept, representing only `4` zero-intercept maps, and every such template has zero defect on all three transitions;
- refined shallow late-state counts at or above `4m/3` are
  `16,722,313,937`,
  `24,526,523,998`,
  `27,725,426,286`,
  `29,184,838,816`
  for cutoffs 1 through 4.

## Exact verifier output

`verification/verify_rl184_defect_parity_phase_capacity.py`: PASS.

## New method barrier

The forced nonzero-defect incidence is not yet a signed compensation contradiction. Counting nonzero defects without separating positive and negative corrected flow does not by itself violate the inherited K corridor. Longer unconstrained local template enumeration remains non-closure-grade.

## Inherited correction / scope state

- Corrected `G_i=S_(p+i)-S_p-S_i` remains authoritative.
- The physical corrected-flow functional remains the `2^G` functional.
- RL173's `3^-G` quantity remains auxiliary only.
- Necessary automata/templates/maps remain one-way filters, not physical existence certificates.
- RL175's sparse ownership resultant is not revived as a generic gap obstruction.
- RL168-RL171 rank/chain/inverse-rank barriers remain in force.
- All RL180-RL184 refined floors, m bounds, pair-gap facts, suffix/corridor ownership, map repetition, defect incidence, and phase-location facts remain internal to `(37,0,23,-1)`.

## Global status

The sole zero-height `v=37` negative-sign high type survives. The preferred `h_p=0` branch, positive-height branch, Gate A, Gate B, global non-trivial-cycle exclusion, and Collatz remain open.
