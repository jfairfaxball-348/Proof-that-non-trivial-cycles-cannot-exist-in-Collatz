# Collatz R# Research Handover — XCORL Re-centred Hostile Cylinder Attack

**Date:** 2026-08-19  
**Session mode:** direct attack, not review/audit  
**Next session requested by project owner:** review/audit + RO road-map setting

## 1. Executive result

This session began from the frozen XCORL 7-shadow endpoint and attacked recurrence directly.

The sequence of results is now:

1. The frozen `7 mod 3^86` antichain remains an exact one-shot supercritical certificate: 345,183 prefix-free leaves, `B<=85`, `L<=158`, leading mass `1.0005926243594434...`, and physical harmonic weight at least leading weight on positive lifts.
2. A nested same-7-shadow recurrence is impossible by a huge margin in the tested envelope: the best common-tail-compatible same-shadow leading return overcount is `<1/7000`.
3. Reusing the same 345,183-word library after transfer to other shadows also fails: a rigorous two-generation overcount is `<1/27`.
4. Fresh state-dependent re-centering **does** restore supercriticality on some shadows. In the exact fresh-centred finite Bellman class defined below, the original 7-shadow has value `1.006722938589731...`, and many sampled nonzero shadows have much larger values.
5. However, fresh re-centering is **not uniformly supercritical**. An explicit admissible phase-1 cylinder modulo `3^83` has exact optimal fresh-centred Bellman value `<603/1000` on every one of its 27 modulo-`3^86` extensions.
6. On all 27 of those extensions, an exhaustive cylinder-universal xi-saturation search inside the same `B<=85`, every-prefix dilation `<2^24` envelope finds **zero** xi-kill words.

Therefore the naive state-dependent completion

> “if the frozen library fails after transfer, just rebuild a fresh supercritical antichain around each nonzero child”

is now rigorously false in the stated finite XCORL class.

This is a **restricted hostile-cylinder certificate**, not global XCORL-C and not a Collatz contradiction.

## 2. Frozen starting point

Authoritative frozen 7-shadow data:

- root cylinder `x == 7 (mod 3^86)`;
- 345,183 selected prefix-free leaves;
- `max L = 158`;
- `max B-count = 85`;
- leading mass

  `182795969850318941327359246597002250523603379419 /
   182687704666362864775460604089535377456991567872`

  `= 1.0005926243594434...`;
- selected endpoint leading dilation `<2^24`;
- physical harmonic weight is at least leading weight for the selected positive lifts.

The authoritative parent TARL/Xi handover and the nested-common-tail attack bundle are included under `prior_session_inputs/`.

## 3. Previously closed during this XCORL attack

### 3.1 Same-shadow nested common-tail recurrence

For a frozen leaf with length `L`, B-count `b`, base endpoint `y`, and common root

`x = 7 + 3^86 T`, 

the exact endpoint is

`z(T) = y + 2^L 3^(86-b) T`.

Returning to `7 mod 3^86` imposes one exact congruence on the *same* tail `T`. After exact compatibility aggregation:

- only 2,469 frozen leaves can return at all;
- their total leading mass before common-tail compatibility is `<1/500`;
- the exact maximum compatible nested return mass is

  `0.00013421653711543773... < 1/7000`.

An exhaustive larger same-shadow search over all legal inverse words with `B<=85` and every-prefix leading dilation `<2^24` gives the same maximum. This kills the “clever nested 7->7 survivor” route in that envelope.

### 3.2 Fixed-library cross-shadow iteration

The frozen word library is supercritical only on an extremely deep receptive spine. It is in fact robustly supercritical on

`x == 7 (mod 3^85)`

if the final endpoint-phase digit is selected adaptively, with uniform leading epsilon

`>= 4.822163785254395e-05`.

But composing the frozen library with itself across the first-generation endpoints collapses. Of 345,183 first-generation leaves:

- 342,714 have second-library availability fixed independently of the unresolved common tail;
- only 2,469 remain tail-dependent;
- assigning every dependent leaf the **global maximum** second-library gain independently gives the rigorous overcount

  `two-generation mass < 0.03644763104133 < 1/27`.

Thus the same frozen library cannot be made recurrent merely by allowing cross-shadow transfer.

## 4. Exact fresh re-centred Bellman class

To attack genuine state-dependent re-centering, a new exact finite Bellman solver was constructed.

For a fully specified root residue `r mod 3^86`, consider all legal inverse A/B paths subject to:

- `B <= 85`;
- every prefix satisfies `2^L / 3^b < 2^24`;
- nonzero mod-3 states may be stopped with normalized value 1;
- phase-0 states cannot be stopped;
- the root itself cannot stop;
- A has leading harmonic factor `1/2`;
- B has leading harmonic factor `3/2`.

Every possible stop at `(L,b)` has exact root-normalized leading weight

`3^b / 2^L`.

Because the largest admissible `L` is 158, every Bellman candidate can be represented on the common denominator `2^158` by the exact integer numerator

`3^b 2^(158-L)`.

Hence the full stop/expand Bellman optimum can be computed with no floating decision at all: at every node compare the exact stop numerator to the sum of exact child numerators.

The root residue is propagated exactly modulo the remaining known ternary precision. Since `B<=85` and the root supplies 86 ternary digits, every B-legality and endpoint phase used by this finite operator is cylinder-universal.

### Ownership interpretation

This Bellman optimiser does **not** impose additional nonlocal ancestry/ownership restrictions beyond prefix-free stop/expand selection. Therefore its optimum is an **upper bound** for any subclass obtained by imposing extra ownership restrictions. A subcritical value here cannot be rescued merely by enforcing ownership more strictly.

## 5. Positive check: re-centering genuinely can work locally

The fresh exact operator gives, on the original shadow residue 7,

`V_fresh(7) = 1.0067229385897311814... > 1`.

So the re-centering idea was worth testing: resetting a bounded-dilation budget can recover one-shot surplus even where direct reuse of the frozen library fails.

Other sampled nonzero residues produced exact values well above 1; examples observed include approximately `2.0`, `2.7`, `3.4`, `4.87`, `5.66`, and `6.93`.

These samples are discovery diagnostics only and are not used as theorem claims.

## 6. New exact hostile-cylinder certificate

A random exact-shadow probe found the phase-1 residue

`34348038346992359775237190975196113494742 (mod 3^86)`

with exact fresh Bellman optimum

`0.60097229374642258533... < 1`.

The lower 83 ternary digits of this residue are

`r83 = 2421331193493640338963217570617321212926`.

This satisfies

- `r83 mod 3 = 1`;
- `r83 mod 9 = 7`;

so it is not removed by the frozen canonical mod-3/mod-9 least-red exclusions.

All 27 possible extensions of this cylinder from modulus `3^83` to modulus `3^86` were then solved exactly.

### Exact result

For every

`R == r83 (mod 3^83)`,

after resolving the three remaining digits needed by this `B<=85` operator,

`V_fresh(R mod 3^86) < 603/1000`.

The largest of the 27 exact values is

`27495071655020406923636910864553324258302677807 /
 45671926166590716193865151022383844364247891968`

`= 0.6020125263543891... < 0.603`.

The smallest is approximately

`0.6005555870381626`.

This is a genuine finite cylinder statement, not a sample statement: there are exactly `3^(86-83)=27` required extensions, and all were enumerated.

## 7. Xi attack on the same hostile cylinder

For each of the same 27 depth-86 extensions, a second exhaustive solver enumerated every legal inverse word in the same finite envelope:

- `B<=85`;
- every-prefix `2^L/3^b < 2^24`.

At every node it propagated the exact root cylinder, computed the guaranteed `v3(y+1)` saturation exponent, and tested the exact cylinder-universal inequality

`(2/3)^m (y+1) < R#+1`

whenever the saturated affine slope was `<1`.

Result:

`xi_uniform_kill_count = 0`

on **all 27 extensions**.

Therefore this depth-83 candidate least-red cylinder is simultaneously:

- fresh-leading-Bellman subcritical by a uniform factor `<0.603` in the tested class; and
- not eliminated by a cylinder-universal xi witness anywhere in that same tested class.

This is the strongest new obstruction from the session.

## 8. Dilation stress test

To test whether the hostile state is merely a knife-edge `2^24` budget artefact, the representative extension

`34348038346992359775237190975196113494742 mod 3^86`

was recomputed with progressively larger every-prefix dilation caps, keeping `B<=85`:

| cap | exact Bellman value (decimal rendering) |
|---:|---:|
| `2^20` | `0.5589535538190982` |
| `2^22` | `0.5808028065211440` |
| `2^24` | `0.6009722937464226` |
| `2^25` | `0.6097356761536185` |
| `2^26` | `0.6181383558588715` |
| `2^27` | `0.6257656343153257` |
| `2^28` | `0.6328720980311974` |
| `2^29` | `0.6391056082766942` |

Each listed value came from the exact integer Bellman solver; the table displays decimal renderings.

The cap was enlarged by a factor of 512 across this curve and the representative remains far below 1.

**Do not promote this curve to a theorem about all larger caps or the whole depth-83 cylinder.** It is an exact finite stress specimen showing that the obstruction is not immediately removed by a modest budget increase.

## 9. What is now rigorously killed

Within the explicitly stated finite envelopes, do not spend another session on any of these as if still open:

1. nested same-`7 mod 3^86` survivor recurrence of the frozen 345,183-leaf certificate;
2. cross-shadow recurrence obtained by reusing the same frozen word library;
3. the assertion that a fresh state-dependent nonzero re-centred Bellman certificate is supercritical on every admissible nonzero shadow.

The third point is new in this session and is certified by the hostile depth-83 cylinder.

## 10. What remains live

The hostile cylinder is **not XCORL-C globally**. The following mechanisms remain outside the closed class or are not yet globally resolved:

1. **Xi/slack refinement beyond the tested local envelope.** A child state carries physical height relative to `R#`; a residue-only fresh Bellman state does not encode all useful barrier slack.
2. **Nonlocal phase-0 ownership transfer.** The current Bellman upper bound shows stricter ownership cannot fix the hostile nonzero block locally, but a larger typed block may move resource between states before returning.
3. **Endpoint-only bounded dilation.** The exhaustive hostile search used an every-prefix bound. Paths that temporarily exceed the cap and later recover through B-steps are outside the theorem.
4. **More ternary precision / larger B-depth.** The exact hostile cylinder is tied to the `B<=85`, depth-86 state inherited from the frozen 7-shadow certificate.
5. **A multi-state typed operator.** A state with local scalar value `<1` can in principle participate in a supercritical vector-valued cycle if other states compensate and ownership is exact.
6. **A genuine dual potential/unavoidability theorem.** To claim XCORL-C, one still needs a positive superharmonic certificate on an unavoidable recurrent class, not merely one hostile cylinder.
7. **Global RO contradiction.** No contradiction excluding an unbounded Collatz orbit has yet been obtained.

## 11. Why this matters for the RO branch

Before this session, the main uncertainty was whether the one-shot `>1` certificate might become repeatable after one of three relatively local repairs: nested tail selection, cross-shadow reuse, or fresh local re-centering.

All three simple repairs have now been tested and fail in exact finite forms.

That narrows the RO problem substantially. The remaining proof cannot be a scalar local antichain argument of the same kind. It must use at least one genuinely new ingredient already anticipated by XCORL:

- barrier/xi slack as a live state variable;
- nonlocal ownership transfer;
- a vector-valued multi-state regeneration cycle;
- or a rigorous dual obstruction that forces a strategic pivot away from inverse-proliferation.

The next session should assess how much of the RO proof chain outside XCORL is already frozen and complete, and therefore whether XCORL is truly the last major mathematical bridge or only one of several remaining bridges.

## 12. Status labels for the audit

### Frozen / exact

- 7-shadow one-shot leading supercritical certificate.
- Same-shadow nested common-tail `<1/7000` no-go in stated envelope.
- Same frozen-library two-generation `<1/27` no-go.
- Exact fresh re-centred Bellman formulation for a full depth-86 shadow.
- Depth-83 hostile cylinder: all 27 depth-86 extensions have Bellman optimum `<603/1000` at cap `2^24`.
- Zero cylinder-universal xi witnesses on all 27 extensions inside that same cap/B-depth envelope.

### Exact finite diagnostics, not structural theorem

- Representative hostile dilation curve through cap `2^29`.
- Sample high-value fresh-centred shadows.

### Still open

- XCORL-A globally.
- XCORL-B globally.
- XCORL-C globally.
- RO contradiction.

## 13. Reproduction

From `current_attack/` and `verification/`:

```bash
# Exact fresh Bellman on one depth-86 root residue
./xcorl_recenter_bellman 34348038346992359775237190975196113494742

# Same with a changed every-prefix cap exponent
./xcorl_recenter_bellman_cap 34348038346992359775237190975196113494742 29

# Exhaustive cylinder-universal xi search at cap 2^24
./xcorl_recenter_xi_envelope 34348038346992359775237190975196113494742
```

`verification/hostile_mod83_exact.tsv` contains all 27 exact Bellman numerators.  
`verification/hostile_mod83_joint.txt` records the corresponding Bellman decimals and zero xi-kill counts.

## 14. Recommended next-session posture

The next session should **not continue attacking immediately**. It should perform the requested audit/review/road-map reset and answer, as quantitatively as the frozen corpus allows:

> How far is the programme from excluding the RO (unbounded-orbit) side of a hypothetical counterexample?

In particular, reconstruct the proof dependency chain from least-red assumptions to RO contradiction, mark every link as proved / finite-certified / conditional / open / failed, identify whether XCORL is the unique remaining central bridge, and then set the next research road map accordingly.
