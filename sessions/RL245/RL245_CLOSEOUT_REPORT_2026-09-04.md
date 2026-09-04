# RL245 closeout report

Date: 2026-09-04

Classification: **`R4_BRIDGE_REDUCED`**.

RL245 closes after a mandatory stop-and-repair event.

Retained analytic frontier:

1. inherited simultaneous-survivor floor `beta(P)>=6`;
2. exact derivative `P_(i+1)-P_i=u_i-u_(i+q)`;
3. isolated negative roots give exact q-shift `01 <-> 10` adjacent-swap signatures;
4. every survivor lies in Branch A (thick valley), Branch B (exact local `0101 <-> 1010` factor), or Branch C (at least six sparse singleton valleys);
5. pure `sum/beta/Lipschitz` information cannot eliminate Branch C;
6. exact envelope relation `{A_i,B_i}={P_i,P_i-h_(i+q)}` together with safe `h>=0` keeps every negative P root negative in both genuine doubled physical envelopes at the same root;
7. RL64 parity legality makes the canonical internal path deterministic from the current u-bit and `(d,J)` state: odd J forces `y=x`, even J forces `y=1-x` subject to `d>1` for `10`;
8. the resulting exact J updates are
   - odd J, x=0: `J'=(J+3^d-2^d)/2`;
   - odd J, x=1: `J'=(3J+2^d-1)/2`;
   - even J, x=0: `J'=(3J+3^(d+1)-2^d-1)/2`;
   - even J, x=1: `J'=J/2`;
9. therefore local u-bit shape alone cannot certify a canonical mismatch/rank event: the absolute full-phase-selected J-state is essential.

Correction: the committed checkpoint's global-looking `h in {0,1}` strengthening is demoted and replaced by exact `h>=0` (internal `h=d`).

Not promoted: the scratch determinant-sector no-Radius-4 conclusion.

Open: no eligible exact-distance-4 full-D encounter, no exact full-phase contradiction, Gate A open uniformly, Gate B open, Radius 5 inactive, global exclusion open.

Successor RL246 is narrowed to absolute canonical-state/full-phase coupling of the six common physical valleys.
