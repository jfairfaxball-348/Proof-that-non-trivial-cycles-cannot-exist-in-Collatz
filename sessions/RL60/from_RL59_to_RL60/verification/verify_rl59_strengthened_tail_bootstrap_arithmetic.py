#!/usr/bin/env python3
from fractions import Fraction as F

# Inherited / RL59 facts used here:
#   1 < zeta < 136/135; K >= 25 odd.
#   At every positive terminal-embeddable d=1 state: J*g <= (27/2) zeta.
#   After the final 10 return, J0 is positive odd and the rest is synchronized.
#   J0=1 cannot support a nontrivial synchronized terminal tail to K>=25, hence J0>=3.
#   Psi=(g(J+1))/2 at d=1, and each 00 contributes exactly Delta Psi=g while 11 contributes 0.
#   Psi_end=(27/4) zeta (1+2^-K).

ZETA_UP = F(136,135)

# J0>=3 and J0*g0 <= (3/2)zeta imply g0 <= zeta/2 and Psi0<=zeta.
assert F(3,2)/3 == F(1,2)
assert (F(3,2)+F(1,2))/2 == 1
# Therefore M_final = Psi_end-Psi0 > (27/4 -1)*1 = 23/4.
MLOW = F(23,4)
assert F(27,4)-1 == MLOW

# Exact finite-search boundary for any admissible odd K>=25 terminal predecessor.
N25 = 11_184_810
J25 = 2*N25 + 1
assert J25 == 22_369_621
# At d=1, g <= (27/2)*zeta/J < (68/5)/J because zeta<136/135.
assert F(27,2)*ZETA_UP == F(68,5)
WMAX25 = F(68, 5*J25)
# Need A*wmax > 23/4, hence A > 115*J/272.
def forced_zeros(J):
    x = F(115*J,272)
    return x.numerator//x.denominator + 1, x

A25, raw25 = forced_zeros(J25)
assert A25 == 9_457_745
# Total internal x-zero count is z-1; z is odd.
z_raw = A25 + 1
z_odd = z_raw if z_raw % 2 else z_raw + 1
assert z_odd == 9_457_747

# Reproduced exploratory exact finite-search boundaries for higher K minima.
N27 = 13_256_071
J27 = 2*N27 + 1
A27, raw27 = forced_zeros(J27)
assert J27 == 26_512_143
assert A27 == 11_209_179  # corrected from an earlier arithmetic slip in prose

N29 = 125_687_199
J29 = 2*N29 + 1
A29, raw29 = forced_zeros(J29)
assert J29 == 251_374_399
assert A29 == 106_279_618

print('RL59 strengthened terminal-tail/bootstrap arithmetic: PASS')
print('M_final > 23/4 =', float(MLOW))
print('K>=25 boundary: n_min=',N25,'J_min=',J25,'forced_00>=',A25,'odd z>=',z_odd)
print('K>=27 boundary: n_min=',N27,'J_min=',J27,'forced_00>=',A27,'[finite boundary reproduced; independent audit still recommended]')
print('K>=29 boundary: n_min=',N29,'J_min=',J29,'forced_00>=',A29,'[finite boundary reproduced; independent audit still recommended]')
