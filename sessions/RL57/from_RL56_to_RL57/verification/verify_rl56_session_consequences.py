#!/usr/bin/env python3
from fractions import Fraction

# Pure arithmetic consequences; this does NOT independently validate the 33/4 search.
REQ = Fraction(143,12)
PREFIX = Fraction(33,4)
LATE = REQ-PREFIX
assert LATE == Fraction(11,3)

# Conservative cap used by the K>=25 scripts.
PSI_END = Fraction(27,4)*(1+Fraction(1,2**25)) + Fraction(1,10**18)
PSI_CUT = PSI_END-LATE
assert PSI_CUT < Fraction(771,250)  # 3.084

# Defect localization.
E_CAP = Fraction(5,3)
COST_R2 = Fraction(5,9)
M_GE2_CAP = E_CAP/COST_R2
assert M_GE2_CAP == 3
M_LE1_LOWER = LATE-M_GE2_CAP
assert M_LE1_LOWER == Fraction(2,3)
assert Fraction(17,30) < Fraction(2,3)

print('RL56 session arithmetic consequences: PASS')
print('late mass lower bound =', LATE, '=', float(LATE))
print('conservative Psi_end(K>=25) =', float(PSI_END))
print('Psi_cut upper bound =', float(PSI_CUT), '< 3.084')
print('r>=2 mass <', M_GE2_CAP)
print('therefore r<=1 mass >', M_LE1_LOWER)
print('single x-zero cap 17/30 < 2/3, so at least two r<=1 late x-zeros are required')
