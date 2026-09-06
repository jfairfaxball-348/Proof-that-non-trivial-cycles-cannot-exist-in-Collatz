# Authoritative start — RL270 Radius-5 final determinant-one finite certificate

Incoming state: **RL270**.

Completed generation: **RL269 — `[1,1,1,1,1]` reduced to an exact finite certificate**.

RL269 promotes:
- five-component support cut `U5=floor(4A/5)`;
- mixed full-`D` bound `0<|E|<=5*3^(7+r)*2^(U5-r)`;
- conservative infinite reduction: non-bracketing `A<=1712`, bracketing `A<=690205`;
- exact 36-row Stern-Brocot traversal;
- exact mixed-bound cover of **2,234 determinant pairs**, maximum `A=690`;
- seven coarse bracketing survivors, ending at `(233,147;84,53)`;
- independent `A<=18` replay with 8,996 `[1,1,1,1,1]`, `|kappa|=1` instances, exact 4,498/4,498 orientation split, zero full-`D` hits, zero determinant mismatches and zero cut-correct edge-identity mismatches;
- explicit warning that the raw five-gap space is 618,391,058,390 configurations and has not been exhaustively enumerated.

RL269 classification: **RADIUS5_KAPPA1_11111_REDUCED_TO_FINITE_CERTIFICATE**.

Closed determinant-one topologies remain:
- `[3,2]`;
- `[3,1,1]`;
- `[2,2,1]`;
- `[2,1,1,1]`.

Still open:
- `[1,1,1,1,1]` only.

Read `RL270_RADIUS5_KAPPA1_11111_FINITE_CERTIFICATE_TARGET.md` first.

Primary target: complete the compressed finite structural certificate for `[1,1,1,1,1]` over the exact 2,234-pair RL269 domain. Prefer the `x_i-x_(i+m)=g_i-g_(i-1)` boundary-event/interlacing compression over raw five-gap enumeration.

Do not begin `|kappa|=3` or `|kappa|=5` until `[1,1,1,1,1]` is actually closed.

Frozen:
- `|kappa|=3` and `|kappa|=5` until determinant one closes;
- Gate A;
- fifth retained selector;
- selector enumeration;
- general Radius-n programme.

Radius 4 remains promoted locally. Gate B, Radius 5 and global non-trivial-cycle exclusion remain open.
