#!/usr/bin/env python3
from fractions import Fraction
from functools import lru_cache

# Exact follow-on probe after z=27 elimination.
# For z=29, prove a sharp bound on the terminal all-x-one suffix and quantify
# exactly why forcing only the last one (or two) x-zeros to be terminal-small
# does not yet close the phase zero-mass inequality.

A=123139092617126647266
ELL=77692117359936589403
QGAP=A-ELL
Z=29
S=Z-1
K=QGAP-Z+3       # q-26
CAP=Fraction(17,30)
ZX_REQ=Fraction(143,12)

# Exact residue BFS for the all-x-one backward grammar.  We only need to
# disprove a chain of length 68.  Starting with 69 ternary digits is enough,
# because each backward 11 division loses one digit and a length-68 chain can
# lose at most 68.
TARGET=68
PREC0=TARGET+1
mods=[1]
for _ in range(PREC0):
    mods.append(mods[-1]*3)
q0=(pow(2,K,mods[PREC0])+1) % mods[PREC0]
states={(0,q0,PREC0)}
layer_counts=[1]
for depth in range(1,TARGET+1):
    nxt=set()
    for yzeros,Q,prec in states:
        mod=mods[prec]
        if Q%3==0:
            assert prec>=2
            nxt.add((yzeros,(2*(Q//3))%mods[prec-1],prec-1))
        if yzeros<S:
            nxt.add((yzeros+1,(2*Q+1)%mod,prec))
    states=nxt
    layer_counts.append(len(states))
    if not states:
        break
TAILMAX=next(i-1 for i,c in enumerate(layer_counts) if i>0 and c==0)
assert TAILMAX==67

# Sequential-cap greedy maxima for n zero weights. These are exact because
# increasing the number of x-ones before any zero decreases that zero and can
# only constrain all later zeros further.
def weight(j,p):
    return Fraction(2**(p+j-1),3**p)

def greedy_mass(n):
    p=0
    total=Fraction(0)
    for j in range(1,n+1):
        while weight(j,p)>CAP:
            p+=1
        total += weight(j,p)
    return total

M25=greedy_mass(25)
M26=greedy_mass(26)
M27=greedy_mass(27)
assert M25 < ZX_REQ < M26 < M27

# Terminal proximity makes the last x-zero utterly negligible. If c is the
# number of all-x-one columns after it, c<=67 and
#   w_last = (g_end/2)*(3/2)^c,
# with g_end=27*zeta/2^(K+1). The very weak zeta<2 and huge K already give
# w_last < 2^-1000, so numerical size is not the obstruction.
assert K>2000
# 27*(3/2)^67 / 2^(K+1) < 2^-1000 follows from 27*3^67 < 2^(K+68-1000).
assert (27*(3**67)).bit_length() <= K+68-1000

print('RL51 z=29 terminal-proximity/barrier certificate: PASS')
print('maximum all-x-one terminal suffix length at z=29 =',TAILMAX)
print('therefore the final x-zero lies within 68 columns of terminal')
print('its weight is < 2^-1000 (very conservative bound)')
print('max zero mass with 27 unrestricted earlier zeros =',float(M27))
print('max zero mass with 26 unrestricted earlier zeros =',float(M26))
print('max zero mass with 25 unrestricted earlier zeros =',float(M25))
print('required stable survivor mass Zx > 143/12 =',float(ZX_REQ))
print('BARRIER: forcing only 1 or 2 terminal-negligible x-zeros is insufficient')
print('NEXT TARGET: force the last 3 x-zeros terminal-near; equivalently bound a terminal suffix containing <=2 x-zero edges')
