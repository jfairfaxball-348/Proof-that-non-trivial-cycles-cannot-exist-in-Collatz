# RL222 research report

Date: 2026-09-01.

RL222 attacked the requested full-period quotient-residue discriminator directly.

The decisive observation is exact and finite: with `D=2^A-3^L`,
`D mod 2^76 = 67904378415918967567359`, while every current live root has
`y0 <= 31285589992934194300574`.  The inherited sign `D>0` therefore forces
`D >= 67904378415918967567359 > y0`.

This changes the strategic interpretation of the proposed `Qfull mod D^2` attack.
For a physical full word RL214 already gives `Qfull=D*y0`; because `y0<D`, this
quantity is strictly below `D^2`.  Thus `Qfull mod D^2` recovered through ownership
is exactly `D*y0`, and the quotient residue is exactly the already-known `y0`.
It cannot shrink the current 139,581,280-candidate family.

RL222 then isolated the proper candidate-wise return target after the e=16 prefix:
the independently generated remaining-tail numerator must equal
`2^(A-24)y0-3^(L-16)y16`.  It also proved that comparing only leading-tail
numerators modulo powers of two is automatic from the local recurrence and hence
cannot certify full return.

No candidate/prefix/rank deletion is promoted.  The useful output is a sharper
method barrier and a precise successor interface: compute an independent full-tail
endpoint/return-defect observable, starting with odd-modulus coupling rather than
another ownership-derived or local 2-adic residue.
