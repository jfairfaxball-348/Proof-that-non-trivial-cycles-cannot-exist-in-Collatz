#!/usr/bin/env python3
"""Exact rational regression for the RL59 final synchronized-tail forcing lemma.

Hypotheses used (all inherited/audited within the sole safe-CF survivor):
  1 < zeta, zeta^2 < 136/135, K >= 25.
  terminal d=1, J=2^K, g=27*zeta/2^(K+1).
  every actual prefix has g <= (9/8) zeta^2.
  every x-zero has weight < 17/30.
  terminal-compatible positive d=2 state obeys J*g <= (9/2) zeta.
  after the final 10 return: J0=J2/2, g0=(2/3)g2.
  after that return only height-one synchronized 00/11 edges occur.

Conclusions checked:
  J0*g0 <= (3/2) zeta,
  g0 <= (3/4) zeta^2,
  Psi0 <= (3/4)zeta + (3/8)zeta^2,
  M00_final > 45/8,
  S11_final > 17/3,
  #00_final >= 10,
  #11_final >= 16,
  final synchronized tail has >=26 columns and >=5 maximal 00-runs.
"""
from fractions import Fraction as F

ZU2 = F(136,135)        # strict upper bound for zeta^2
KMIN = 25

# Post-return consequences are symbolic algebra; constants below are coefficient checks.
# J0*g0 = (J2/2)*(2g2/3) = (J2*g2)/3 <= (3/2) zeta.
assert F(9,2)/3 == F(3,2)
# g0=(2/3)g2 and g2 <=(9/8)zeta^2.
assert F(2,3)*F(9,8) == F(3,4)
# Psi0=(J0*g0+g0)/2.
assert (F(3,2)+F(3,4))/2 == F(9,8)  # coefficient split is 3/4 zeta +3/8 zeta^2, not mergeable

# M_final >= 6*zeta -(3/8)zeta^2 +(27/4)zeta*2^-K.
# Since 1<zeta and zeta^2<136/135<16, f(z)=6z-3z^2/8 is increasing
# throughout the allowed interval; hence f(zeta)>f(1)=45/8.
assert ZU2 < 16
assert 6 - F(3,8) == F(45,8)

# Each final 00 is an x-zero, so each has weight <17/30.
# Nine cannot carry >45/8.
assert 9*F(17,30) < F(45,8)

# S_final > 6*zeta -(27/4)zeta*2^-K.
# For a rigorous zeta-independent lower bound, use zeta>1 in the main 6*zeta
# and zeta < sqrt(136/135) < 136/135 in the tiny negative term.
S_LOWER_RELAX = F(6,1) - F(27,4)*F(136,135)*F(1,2**KMIN)
assert S_LOWER_RELAX > F(17,3)

# Every 11 has Delta S=g/3. Generic prefix cap and zeta^2<136/135 give
# Delta S < (3/8)*(136/135)=17/45. Fifteen are therefore <17/3.
assert F(3,8)*F(136,135) == F(17,45)
assert 15*F(17,45) == F(17,3)
# Since S_final >17/3 and each contribution is strictly <17/45, >=16 11s.

# A maximal all-00 run has mass <17/15 (twice its last zero cap).
# Four runs cannot carry >45/8; hence at least five runs.
assert 4*F(17,15) < F(45,8)

print('RL59 final synchronized-tail forcing verifier: PASS')
print('M00_final > 45/8 =', float(F(45,8)))
print('S11_final  >', S_LOWER_RELAX, '=', float(S_LOWER_RELAX), '> 17/3')
print('forced final-tail events: #00 >=10, #11 >=16, total columns >=26')
print('forced maximal aligned 00-runs: >=5')
