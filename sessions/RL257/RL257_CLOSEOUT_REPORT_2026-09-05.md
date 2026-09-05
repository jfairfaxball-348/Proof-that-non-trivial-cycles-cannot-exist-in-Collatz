# RL257 closeout report

Date: 2026-09-05  
Classification: **R4_BRIDGE_REDUCED**

RL257 repairs the historical endpoint convention and strictly contracts the
unique first halving frontier.

Promoted:

- exact internal terminal boundary is `(d,J)=(1,2^k)` **before** the omitted
  terminal `(1,0)`;
- `H_sel=14` is not identified with canonical accumulated area;
- `k=33` is eliminated analytically because RL256 forces
  `u_3u_4u_5u_6=1111`, while the exact internal start `(1,-13)` cannot admit
  even three leading internal `x=1` bits;
- the frontier is now `k=31` only;
- for `k=31`, the first nine internal bits have weighted zero cost at least
  `11`, attained only by `110110111` and `110111010`;
- therefore the final ten internal bits have weighted zero budget at most
  `16`, hence at most five zeros;
- exact enumeration leaves 141 universal left-flank x-patterns, 3064
  right/left flank pairs after the E-budget, and 2719 after exact complement
  isolated-root capacity.

The bundled verifier reproduces every finite count and the k=33 local
contradiction exactly.

No Gate closes. Radius 4 is not invoked. Radius 5 remains inactive. Global
non-trivial-cycle exclusion remains open.

RL258 is prepared to attack the remaining `k=31` finite two-flank family by
adding exact backward terminal `(d,J)` ownership and long-middle compatibility.
