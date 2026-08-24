#!/usr/bin/env python3
from fractions import Fraction

# Exact analytic reduction for the next odd case z=33.
# This is NOT an elimination certificate. It reduces the live terminal search
# to a suffix with <=6 x-zero and <=16 y-zero edges after u_26.

A=123139092617126647266
ELL=77692117359936589403
Q=A-ELL
Z=33
S=Z-1
K=Q-Z+3
CAP=Fraction(17,30)
R=Fraction(143,12)
ECAP=Fraction(5,3)


def weight(j,p):
    return Fraction(2**(p+j-1),3**p)

p=0; ps=[]; ws=[]
for j in range(1,27):
    while weight(j,p)>CAP:
        p+=1
    ps.append(p); ws.append(weight(j,p))
M15=sum(ws[:15],Fraction(0))
M25=sum(ws[:25],Fraction(0))
assert ps[-1]==45


def future_max(P):
    p=P; total=Fraction(0)
    for j in range(27,S+1):
        while weight(j,p)>CAP:
            p+=1
        total+=weight(j,p)
    return total

# p26<=56: at P=57 even greedy-maximal prefix/future cannot reach R.
RELAX57=M25+weight(26,57)+future_max(57)
assert RELAX57 <= R
PMAX=56

# If at least 11 of y_1..y_26 occur after u_26, they are indices 16..26.
# For P=p26, the same correction identity as z=31 gives
# E > R - M15 - F_27..32(P) - C_11(P).
def correction(P):
    factor=Fraction(2**(P+11),3**(P+11))
    return sum(Fraction(2**(j-1))*factor for j in range(16,27))

lbs=[]
for P in range(45,PMAX+1):
    lb=R-M15-future_max(P)-correction(P)
    lbs.append((lb,P))
    assert lb>ECAP
MIN_LB,MIN_P=min(lbs,key=lambda t:t[0])

# Therefore at most ten of first 26 y-zeros are after u26. Six later x-zero
# indices force six later matching y-zeros, giving suffix budgets <=6 x-zero,
# <=16 y-zero. Also u26<=56+25=81.
assert PMAX+25==81

print('RL51 z=33 reduced frontier certificate: PASS')
print('relaxed maximum at p_26=57 =',float(RELAX57),'<=',float(R))
print('therefore p_26<=56 and u_26<=81')
print('minimum 11-delayed defect lower bound =',float(MIN_LB),'at p_26 =',MIN_P)
print('therefore at most 10 of y_1..y_26 lie after u_26')
print('LIVE REDUCED TARGET: terminal suffix with <=6 x-zero and <=16 y-zero edges')
print('This verifier does not eliminate z=33.')
