#!/usr/bin/env python3
from fractions import Fraction

# This verifier starts from two already-certified clean consequences for the sole
# safe sub-Legendre CF survivor:
#     S > 45/4,  E < 5/3,
# plus the RL50 prefix caps.  It checks the exact local-energy localization and
# the initial negative-cycle macro bounds used in the analytic note.

SLOW=Fraction(45,4)
EUP=Fraction(5,3)

# From epsilon formulas in the monotone-J verifier:
# - every y=1 edge except height-one 11 has epsilon >= 2 DeltaS;
# - every x=0 edge except height-one 00 has epsilon >= (2/3) g.
# Since sum epsilon=2E:
#   S_nonfree <= E,
#   Zx_nonfree <= 3E.
# Hence with Zx=S-1+g_end+E and g_end>0:
F11_LO=SLOW-EUP
F00_LO=SLOW-1-2*EUP
assert F11_LO==Fraction(115,12)
assert F00_LO==Fraction(83,12)

# Verify the local coefficient inequalities for many d; their displayed closed
# forms establish them algebraically for every d>=1.
def eps(d,x,y):
    if (x,y)==(0,0): return 2-Fraction(2**d,3**(d-1))
    if (x,y)==(1,1): return Fraction(2**d-2,3**d)
    if (x,y)==(0,1): return 2-Fraction(2**d+2,3**d)
    if (x,y)==(1,0): return Fraction(0)
    raise AssertionError

for d in range(1,100):
    # normalized g=1
    # nonfree y=1: 01 at every d, plus 11 at d>=2
    assert eps(d,0,1) >= 2*Fraction(1,3**d)
    if d>=2:
        assert eps(d,1,1) >= 2*Fraction(1,3**d)
    # nonfree x-zero: 01 every d, plus 00 at d>=2
    assert eps(d,0,1) >= Fraction(2,3)
    if d>=2:
        assert eps(d,0,0) >= Fraction(2,3)

# Before the first positive-energy edge, the path is forced to remain at d=1
# on zero-energy 00/11 edges.  Starting J=-13, the odd-preserving grammar is
# the exact 3-step negative cycle.  One full macro (starting weight g) has
# S_11=7g/9, Z_00=2g/3 and scales g by 8/9.
# After r full macros let h=(8/9)^r.  There are exactly three possible phases
# at which to choose the alternative same-bit even exit before the forced 01.
for r in range(0,400):
    h=Fraction(8,9)**r
    baseS=7*(1-h)
    baseZ=6*(1-h)
    # exit A: alternative 00 at J=-13
    SA=baseS; ZA=baseZ+h
    # exit B: preserve 11 at J=-13, then alternative 11 at J=-19
    SB=baseS+h/3+2*h/9; ZB=baseZ
    # exit C: preserve 11, preserve 00, then alternative 00 at J=-9
    SC=baseS+h/3; ZC=baseZ+2*h/3+4*h/3
    for s,z in [(SA,ZA),(SB,ZB),(SC,ZC)]:
        assert s<7 and z<6

# Therefore the certified total free masses force this much free height-one
# mass strictly after the first positive-energy 01.
POST11_LO=F11_LO-7
POST00_LO=F00_LO-6
assert POST11_LO==Fraction(31,12)
assert POST00_LO==Fraction(11,12)

# Safe prefix cap: zeta^2<136/135.
# Height-one 11 has S increment g/3 with g<17/15.
# Height-one 00 is an x-zero and has the sharper g<17/30.
assert 6*Fraction(17,45) < POST11_LO
assert 7*Fraction(17,45) > POST11_LO
assert Fraction(17,30) < POST00_LO
assert 2*Fraction(17,30) > POST00_LO

print('RL50 defect-energy localization verifier: PASS')
print('safe survivor forces free height-one 11 S-mass >',F11_LO,'and free 00 g-mass >',F00_LO)
print('before first paid 01, exact negative-cycle grammar has S_11<7 and Z_00<6')
print('therefore after first paid 01: S_11 >',POST11_LO,'and Z_00 >',POST00_LO)
print('prefix caps force at least 7 post-exit height-one 11 columns and 2 post-exit height-one 00 columns')
print('NEW STRUCTURAL CONSEQUENCE: sole safe survivor must return to height one and execute >=9 free synchronized columns after its first genuine excursion departure')
