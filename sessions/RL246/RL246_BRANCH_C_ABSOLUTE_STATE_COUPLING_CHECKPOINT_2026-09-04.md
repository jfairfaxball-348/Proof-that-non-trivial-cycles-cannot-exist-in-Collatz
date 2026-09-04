# RL246 — Branch-C absolute canonical-state / full-phase coupling checkpoint

Date: 2026-09-04
Classification: **analytic reduction; R4_BRIDGE_REDUCED closeout**.

## 0. Frozen incoming state and discipline

Retain RL245 exactly:

- every simultaneous Gate-A/Gate-B survivor has `beta(P)>=6`;
- `P_(i+1)-P_i=u_i-u_(i+q)`;
- every isolated negative root has `(P_(i-1),P_i,P_(i+1))=(0,-1,0)` and exact q-shift signature
  `u_(i-1..i)=01`, `u_(i-1+q..i+q)=10`;
- Branch C consists of at least six such singleton valleys, pairwise separated by at least three roots;
- the genuine doubled physical envelopes are `{P_i, P_i-h_(i+q)}`;
- use only corrected `h>=0`, with **internal** canonical `h=d>=1`;
- the canonical u-driven `(v,d,J)` automaton is deterministic from parity legality, with legal `10` descent `J'=J/2`;
- `P` and `Q` are not Radius-4 theorem inputs.

No statement below uses the demoted RL245 global `h in {0,1}` assertion.

## 1. Internal-singleton extraction in Branch C

The full half-word is

`u=110 x 1 0^t`.

A singleton signature uses one oriented `01` transition edge and one oriented `10` transition edge. Outside the internal `x` block there are at most five transition edges capable of participating in such a signature: the fixed-prefix `10`, the prefix-to-`x` boundary, the `x`-to-terminal-1 boundary, the terminal `10` when present, and the cyclic return transition when present.

A fixed oriented transition edge can belong to at most one singleton signature. Since Branch C has at least six singleton signatures, at least one singleton has both of its signature edges wholly internal to the canonical internal path.

Fix such a singleton and write `e=i-1` and `j=e+q`.

## 2. Exact physical prefix-scale notch

Let

`S_r = 2^r / 3^(U_r)`

where `U_r` is the number of u-ones before position `r`. Put

`c=S_(e+q)/S_e`.

The forced bit pairs `01` and `10` imply exactly

`S_(e+q)/S_e = c`,

`S_(e+1+q)/S_(e+1) = c/3`,

`S_(e+2+q)/S_(e+2) = c`.

Thus the singleton produces an exact factor-three q-shift scale notch at its central root.

If the determinant-flow constant is denoted `r_det` to avoid collision with RL64's unrelated notation, then `P_e=0` gives `W_e(q)=r_det`, and `a r_det-q ell=2` yields

`c^a = R^q/9`, where `R=2^a/3^ell`.

Using the retained resonance `1<R`, `R^2<16/15`, and `a>=27`,

`3^(-2/27) < c < sqrt(16/15)`.

This is only a relative scale control. No uniform positive lower bound for `S_e` is claimed.

## 3. Positive full-phase packet

RL47's exact phase increment on an internal pair column `(x,y)` is

`Delta Phi = S_r * ((1-x) - (1-y)/3^d)`.

For the extracted singleton, canonical legality gives a strictly positive four-column packet. Without assuming a parity pattern one obtains a positive relative bound; in the rigid all-odd case of Section 4 the packet is exact:

`DeltaPhi_packet = S_e[(1-3^(-D)) + (2c/3)(1-3^(-d))]`,

where `D,d>=1` are the canonical heights at the unshifted and shifted two-column blocks.

Hence in that rigid case

`DeltaPhi_packet > [2/3 + (4/9)3^(-2/27)] S_e > 1.07637 S_e`.

This is a **relative** full-phase increment, not an absolute uniform constant.

## 4. Canonical event-or-rigid-valley dichotomy

At the shifted internal u-block the two u-bits are `10`.

Let `(d,J_j)` be the canonical state at its first column.

### Event arm

If `J_j` is even, parity legality forces the first column to be the genuine mismatch `10`, so

`J_(j+1)=J_j/2`.

If `J_j` is odd but `J_(j+1)` is even, then the second u-bit `0` forces the genuine mismatch `01`.

Thus unless both boundary states are odd, the extracted Branch-C singleton directly contains a canonical even-J rank/mismatch event.

### Rigid arm

If both `J_j` and `J_(j+1)` are odd, parity legality forces the shifted u-bits `10` to be realized as synchronized columns `11,00`. Height stays constant at `d` across those two columns.

Because the genuine companion envelope is `E_r=P_r-h_(r+q)` and internal `h=d`, the singleton triple becomes exactly

`boxed: (E_(i-1),E_i,E_(i+1))=(-d,-d-1,-d)`.

For `d=1` this is the local negative-depth shape `(-1,-2,-1)`, corresponding in absolute magnitudes to the Radius-4 height-two topology `(1,2,1)`. **No Radius-4 theorem is applied:** local topology is not the missing primitive full-D exact-global-distance-4 hypothesis.

For `d>=2`, these three roots alone contribute at least `3d+1` units of genuine negative counterflow.

## 5. Exact J fingerprints in the rigid arm

Across synchronized `11,00` at height `d`,

`J_(j+2) = [3J_j + 2*3^d - 2^d - 1]/4`.

Therefore

- if `d` is odd, `J_(j+2)==0 (mod3)`;
- if `d` is even, `J_(j+2)==1 (mod3)`.

At the unshifted internal u-block `01`, if both corresponding canonical boundary states are odd, the columns are synchronized `00,11` at entry height `D`, giving

`J_exit = [3J_entry + 3^(D+1) - 2^D - 2]/4`,

so

- if `D` is odd, `J_exit==2 (mod3)`;
- if `D` is even, `J_exit==0 (mod3)`.

Thus the all-odd exceptional singleton records exact canonical height-parity information in absolute J-state residues.

## 6. Promoted reduction and open obligation

Promoted from RL246:

1. Branch C contains an internal canonical singleton signature.
2. That singleton has an exact factor-three q-shift physical prefix-scale notch with determinant-controlled shoulder ratio.
3. It gives a strictly positive RL47 full-phase packet; in the rigid all-odd arm the exact relative lower bound exceeds `1.07637*S_e`.
4. The shifted `10` boundary obeys the dichotomy:
   - a forced canonical even-J mismatch/descent event; or
   - a rigid genuine physical valley `(-d,-d-1,-d)` with exact J mod-3 height-parity fingerprints.

Not promoted:

- no absolute uniform lower bound on the packet;
- no Radius-4 application from the local `(1,2,1)` shape alone;
- no claim that Branch A or Branch B is closed;
- no Gate-A or Gate-B closure;
- no global non-trivial-cycle exclusion.

The current mathematical attack is frozen here pending the successor Radius-3/Radius-4 integrity audit.
