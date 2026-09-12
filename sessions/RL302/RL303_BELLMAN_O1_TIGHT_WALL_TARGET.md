# RL303 — Bellman O1 tight-wall completion target

Date prepared: 2026-09-12
Status: PREPARED, NOT STARTED

## Incoming classification

RL302 closes as

`P8_TWO_OBLIGATION_REDUCTION_TIGHT_WALL_CASCADE_NORMAL_FORMS_AND_CONDITIONAL_SECOND_OBLIGATION_COLLAPSE_PROVED`.

Gate A remains open. Gate B remains open. The RL301 physical/resonance branch remains frozen at externally certified selector frontier `a=7354673373747273032`.

## Primary objective A — prove or refute O1

The main unresolved theorem is

`m_R3(E)>=m_8(E)`

for every positive even checkpoint `E`, where `R3=(3,K=27)`.

RL302 reduced every R3 future through its unique tower departure to the tight wall families

`L_D=(D,(5*3^D-3)/4)`,

`R_D=(D,(9*3^D-3)/4)`

for odd `D`, with exact credits

`B_L(D)=(D^2+D-6)/2`,

`B_R(D)=(D^2+3D-4)/2`.

Target the two wall inequalities

`m_8(E)<=B_L(D)+m_LD(E)`,

`m_8(E)<=B_R(D)+m_RD(E)`.

Use the exact run-length normal form

`L_D 0 1^k 01 = R_D 1^(k+1)00`

with saving `k+2`, and its sibling

`endpoint(L_D 0 1^k 00)=P o endpoint(R_D 1^(k+1)01)`.

Seek a well-founded credit/refactorisation theorem for the leading-P sibling, or an exact counterexample. Do not replace this with bulk H-caps.

## Route barriers that must be respected

1. Do not build an unrestricted first-wall-hit grammar for the relative `R2` factor: RL302 showed this simply re-encodes checkpoint-2 futures and is circular.
2. Do not assume generic left-P or right-P checkpoint monotonicity: RL302 froze exact counterexamples to both.
3. Do not attempt blanket physical-state ownership; the target is checkpoint-ending min-plus transport.

## Primary objective B — immediately finish O2 if O1 closes

RL302 proved

`m_2(E)=1+min(m_R3(E),m_8(E))`.

Hence O1 gives `m_2=m_8+1`, and the second source obligation becomes

`m_D0(E)>=m_8(E)`, `D0=(3,K=24)`.

All odd-d leading-P O2 residuals already conditionally close into O1 by the exact index-shift splice

`endpoint(L_D 0 1^k00)=endpoint(F_(D+2) 00 1^k00)`

with D0 entering the shared state more expensively than R3 by

`(D^2+7D+8)/2`.

After O1, only the genuinely new O2 sectors remain:

- even-d trailing-P siblings from the F/S mod-4 normal form;
- the `A_d=F_d o Z` departure family.

Close these before claiming the P/8 identity.

## Primary objective C — after the P/8 identity

If O1 and O2 close, recover

`m_P(E)=m_8(E)+2` for every positive even `E!=2`.

Then use RL297's exact reduction

`Bcal(P)=Bcal(8)-2`

and attack checkpoint-8 `Bcal(8)<=3` / excess-one.

Even a proof of `Bcal(P)<=1` is not Gate A by itself: return afterward to the RL296 non-P front-door residuals and close them with their recorded allowances.

## Frozen branch policy

Do not resume the external delay ladder unless the Bellman route is decisively falsified or the user explicitly redirects the programme. Preserve RL301's finite physical frontier for future reuse.

## Success condition

RL303 succeeds with any one of:

- a proof or exact counterexample to O1;
- a theorem closing the tight-wall leading-P residual recursively;
- if O1 closes, completion of the contracted O2 residual and hence the P/8 identity;
- a decisive theorem/barrier that materially changes the Bellman strategy.

## Scope

Gate A OPEN.
Gate B OPEN.
Physical/resonance frontier frozen at `a=7354673373747273032` with external dependency.
Radius 6+ frozen.
RO/divergent-orbit work out of scope.
Lean formalisation separate.
No global non-trivial-cycle exclusion is claimed.
