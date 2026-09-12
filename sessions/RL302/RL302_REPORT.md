# RL302 — Bellman P/8 shared-endpoint contraction, wall cascade normal forms, and conditional O2 collapse

Date: 2026-09-12
Base commit: `daf7739976b914b4fa62e70446d0f1da90e5fb91`

## Classification

`P8_TWO_OBLIGATION_REDUCTION_TIGHT_WALL_CASCADE_NORMAL_FORMS_AND_CONDITIONAL_SECOND_OBLIGATION_COLLAPSE_PROVED`

Gate A remains OPEN. Gate B remains OPEN. The RL301 physical/resonance branch remains frozen at the externally certified selector frontier `a=7354673373747273032`. Radius 6+ remains frozen. Lean formalisation is separate. No global non-trivial-cycle exclusion is claimed.

## 1. Outcome

RL302 returned to the RL297 weak-green Bellman/P route. It does **not** prove the requested all-depth identity

`m_P(E)=m_8(E)+2`

for every positive even checkpoint `E!=2`, and it does not prove `Bcal(P)<=1`.

It does, however, materially contract the all-depth problem. The universal P/8 identity is reduced exactly to two fixed-source domination theorems; the first is reduced to two one-parameter tight-wall families; both wall and second-source departures admit exact cascade normal forms; and a new index-shift splice shows that the odd leading-P residuals of the second obligation are not independent but conditionally sink into the first obligation with a growing quadratic margin.

This meets RL302's theorem-sized structural-success criterion without overclaiming Gate A.

## 2. Exact Bellman front reduction

Use K-coordinate states

- `P=(2,J=3,K=6)`;
- `A=(2,J=4,K=7)`;
- checkpoint `2=(1,J=2,K=3)`;
- checkpoint `8=(1,J=8,K=9)`;
- `R2=(2,K=9)`;
- `R3=(3,K=27)`;
- `D0=(3,J=17,K=24)`.

The zero-area boundary component through `J=3,5` gives, for every reachable positive even checkpoint `E!=2`,

`m_3(E)=min(m_2(E),m_8(E))`.

Checkpoint 2 has a forced zero-cost launch to `R2`, and `R2` has children `R3` and boundary `3`, each at cost one. Hence

`m_2(E)=1+min(m_R3(E),m_2(E),m_8(E))`.

Because a finite minimum cannot satisfy `m_2=m_2+1`, exactly

`boxed: m_2(E)=1+min(m_R3(E),m_8(E))`.

Also

`m_P(E)=1+min(m_A(E),m_2(E))`

and

`m_A(E)=1+min(m_2(E),m_D0(E))`.

Therefore the full P/8 identity is equivalent to the pair

`(O1) m_R3(E)>=m_8(E)`,

`(O2) m_D0(E)>=m_2(E)-1`.

This is an exact all-depth logical reduction, not a bounded certificate.

## 3. O1 tower zipper and exact tight-wall reduction

Define

`R_d=(d,K=3^d)`,

`S_d=(d-1,K=(3^d-1)/2)`.

Then

`R_d --0--> R_(d+1)`,

`R_d --1--> S_d`.

Every nonempty checkpoint-ending future from `R3` has a unique first tower departure at some `S_d`.

For odd `D` define the RL295 tight walls

`L_D=(D,K=(5*3^D-3)/4)`,

`R_D=(D,K=(9*3^D-3)/4)`.

Exact substitution in the canonical recurrence gives the all-depth zipper:

- even `d=D+1`: `S_d --0--> L_D`, `S_d --1--> R_D`;
- odd `d=D`: `S_d --0--> L_D`, `S_d --1--> R_(D-2)`.

Put

`B_L(D)=(D^2+D-6)/2`,

`B_R(D)=(D^2+3D-4)/2`.

The alternating tight branches reach `L_D` and `R_D` at exactly these source credits; the sibling branches have explicit additional slack. Consequently O1 is implied by only the two wall-family inequalities

`m_8(E)<=B_L(D)+m_LD(E)`,

`m_8(E)<=B_R(D)+m_RD(E)`

for every odd `D>=3`.

The wall intervals are consecutive in RL294 dual coordinates and the credit increments agree with the adjacent-cell widths:

`B_L(D)-B_R(D-2)=D`,

`B_R(D)-B_L(D)=D+1`.

## 4. Autonomous paired transport and cascade identification

For a source `(d,K)` and owner `(d+delta,L)`, put

`r=(L-K)/3^d`.

Choose the owner input so source and owner have the same canonical output. The exact relative update is

`delta'=delta+x-z`,

`r'=(3^x/2)[r+(1-z)3^delta-(1-x)]`,

and the synchronized edge-area difference is exactly `delta`.

After the change of variables `m=-delta`, `U=-3^m r`, this is exactly the ordinary canonical K-recurrence for the left cascade factor. Thus the relative transducer is not an additional dynamical system: it is the RL294 cascade algebra in quotient coordinates.

In particular

`boxed: L_D = R_2 o R_(D-2)`.

This proves structurally the RL297 scratch merger

`boxed: L_D 101100 = R_(D-2) 000001`

for every legal odd-D instance, with the `R_(D-2)` continuation exactly two area units cheaper.

## 5. Tight-wall run-length normal form

A stronger universal normal form holds for every `k>=0` whenever the displayed prefixes are legal:

`boxed: L_D 0 1^k 01 = R_D 1^(k+1) 00`,

with the `R_D` continuation cheaper by exactly `k+2`.

The complementary sibling is

`boxed: endpoint(L_D 0 1^k 00) = P o endpoint(R_D 1^(k+1) 01)`,

again with owner-side continuation cheaper by `k+2`.

Thus after an initial zero at a tight L-wall and the next zero, the future has only two algebraic outcomes: exact merger into the adjacent R-wall route, or one leading-P cascade factor. This is a true all-depth run-length normal form.

An unrestricted attempt to classify all first wall hits of the relative `R2` factor is deliberately rejected as circular: those wall hits are exactly the checkpoint-2 future problem in different coordinates. The successor should work with the tight-wall/run-length structure, not rebuild checkpoint 2 as a wall grammar.

## 6. O2 zero-spine and F/S normal forms

Define

`V_d=(d,K=3^d-3)`,

`W_d=(d,K=3^d-2)`.

Then `D0=V_3` and

`V_d --0--> W_d --0--> V_(d+1)`.

Every checkpoint-ending D0 future therefore has a unique first `1` departure from this two-state spine.

Put

`F_d=(d-1,K=(3^d-3)/2)`,

`A_d=(d,K=(3^(d+1)-9)/2)`,

and retain `S_d=(d-1,K=(3^d-1)/2)` from the checkpoint-2 tower. One has

`A_d=F_d o Z`, with `Z=(1,K=0)`.

At `F_d/S_d`, the checkpoint-2 owner enters with exact historical credit

`(d^2-d-4)/2`.

For odd `d` and every `j>=0`, the exact normal form is

`boxed: F_d 00 1^j 01 = S_d 1^(j+2) 00`,

with the `S_d` continuation cheaper by `j+3`, while the sibling is

`boxed: endpoint(F_d 00 1^j 00)=P o endpoint(S_d 1^(j+2) 01)`.

For even `d`, the normal form closes after three columns:

- if `d==2 mod 4`: `F_d010=S_d010`, while `endpoint(F_d011)=endpoint(S_d011)o P`;
- if `d==0 mod 4`: `F_d011=S_d011`, while `endpoint(F_d010)=endpoint(S_d010)o P`.

In each even case the S-route is exactly two area units cheaper.

The mod-4 split is exact and arises from the parity of the post-`01` cascade factor.

## 7. Generic P-insertion monotonicity is false

The P siblings above cannot be closed by a blanket claim that adding a P factor makes checkpoint travel more expensive.

Exact counterexamples:

- leading P: `(1,K=13)` reaches checkpoint `6` at cost 4, while `P o (1,K=13)` reaches the same checkpoint at cost 3;
- trailing P: checkpoint `2=(1,K=3)` reaches checkpoint `32` at cost 10, while `(1,K=3) o P` reaches it at cost 7.

Hence any successor proof must exploit the special wall/F-S ancestry and accumulated credit. Generic left- or right-P insertion monotonicity is false.

## 8. O2 conditionally collapses into O1 on all odd leading-P residuals

From the Section-2 equation, O1 immediately implies

`m_2(E)=m_8(E)+1`.

Therefore, conditional on O1, O2 becomes simply

`m_D0(E)>=m_8(E)`.

The two obstruction families then splice exactly. For every odd `D>=3`, put `d=D+2`. One has

`boxed: S_(D+2) --1--> R_D`

at cost `D`.

Combining this with the two leading-P sibling formulas gives

`boxed: endpoint(L_D 0 1^k 00)=endpoint(F_(D+2) 00 1^k 00)`.

So the tight-wall leading-P residual from O1 and the odd-F/S leading-P residual from O2 are literally the same physical state after the index shift `D -> D+2`.

Moreover the D0 route to that shared state is more expensive than the R3 route by exactly

`boxed: (D^2+7D+8)/2`.

This margin is already 19 at `D=3` and grows quadratically. Consequently, once O1 is proved, **every odd-d>=5 leading-P residual of O2 is automatically checkpoint-8 dominated by same-state splicing through the cheaper R3 history**.

The odd base `d=3` closes directly:

`D0 --01--> F_3` at cost 4,

`8 --011000--> F_3` at cost 4.

Thus O2 is no longer an independent full infinite problem. Conditional on O1, the genuinely new O2 residual is reduced to the even trailing-P sectors and the `A_d=F_d o Z` departure family.

## 9. Finite evidence retained only as evidence

The original finite audit remains strongly consistent with the all-depth identity:

- `m_2=m_8+1` on large tested common checkpoint sets;
- `m_R3=m_8+3` on the tested common R3/8 set;
- `m_A=m_2+1` on the tested common A/2 set;
- `m_P=m_8+2` on 36,207 tested common non-2 checkpoints in the RL302 scratch regression.

These counts are **not** promoted as substitutes for the all-depth theorem.

## 10. Corrections and route barriers

1. A checkpoint-3 scratch label reused `R1` for the auxiliary `(1,K=6)` state, conflicting with the established tower notation `R_d=(d,3^d)`. The auxiliary state is renamed `U=(1,K=6)`. No formula depending on the factorisation changes.
2. A finite wall-grammar attack is circular because the relative `R2` factor's wall hits encode checkpoint-2 futures.
3. Generic leading/trailing P monotonicity is false by the exact counterexamples above.
4. Blanket physical-state ownership remains false and is not revived.
5. No claim is made that O1, O2, the P/8 identity, `Bcal(P)<=1`, Gate A, or Gate B is proved.

## 11. Verification

Portable regression frozen in `sessions/RL302/verification/verify_rl302_structural.py`. It independently replays the promoted structural identities from the canonical recurrence and finishes with `RL302_STRUCTURAL_CLOSEOUT_GREEN`.

Fresh closeout output reproduces the tower/wall, wall-run, D0-spine, odd/even F/S, P-insertion-counterexample, and index-shift identities across broad legal parameter ranges, including 198 shared index-shift bootstrap samples and quadratic margins 19 through 988.

The loops are regression evidence. The promoted identities are algebraic consequences of the canonical recurrence and RL294 cascade product.

## 12. Exact remaining target

The primary unresolved theorem is now O1:

`m_R3(E)>=m_8(E)` for every positive even checkpoint E.

Use the tower zipper and tight-wall normal forms. Do not restart unrestricted wall-hit grammar or generic P-insertion monotonicity.

If O1 closes, finish O2 using the already-collapsed odd sectors and attack only:

- even-d trailing-P siblings;
- `A_d=F_d o Z` departures.

Then recover `m_P=m_8+2`. Only after the P/8 identity is proved should the programme use RL297's `Bcal(P)=Bcal(8)-2` reduction and attack checkpoint-8 excess-one. Even a P theorem does not by itself close Gate A: the RL296 non-P front-door residuals must still be discharged before any Gate-A claim.
