# RL335 closeout

Date: 2026-09-16
Status: CLOSED AND FROZEN
Incoming BASE_HEAD: `a22d083d82bce4e09657c4e5a39bb941d7230a11`
Successor: RL336

RL335 is closed with a verified all-length owned-return compression. Exact physical pruning through p=4 leaves every anonymous surviving return at length at least five. Because each added positive contributes +43 true slack, the p=5 fallback is uniformly worst for every q<43. The resulting 37-state / 2,242-edge graph proves `28(K-2H)-S<=28`.

The q=29 obstruction is now localized to one baseline family: five-positive `N37->N37`, exact slack 141 and q=29 surplus +4. Longer returns are automatically easier.

The inherited consumer contracts the carry cap from 32,546,313,237 to 32,546,289,530, an improvement of 23,707. R1 and the global proof remain open.

RL336 must target an affine/exact-state/support-uniform elimination or >=4 surcharge for that five-positive self-return. It must not revert to an unbounded p=5,p=6,... enumeration strategy.
