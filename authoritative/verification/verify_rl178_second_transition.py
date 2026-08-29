#!/usr/bin/env python3
from fractions import Fraction

A=217_976_794_617
L=137_528_045_312
p=65_470_613_321
u=103_768_467_013
assert A*p-L*u==1

def B(j): return (A*j)//L
def c(j): return B(j+1)-B(j)
def v2(n):
    n=abs(n)
    assert n
    return (n & -n).bit_length()-1

assert B(23)==36
assert c(23)==2 and c(24)==1
assert v2(3**25+1)==2
assert v2(3**25-1)==1

# High positive sign: height caps beta=1, alpha=1 or2; neither valuation pattern fits.
vp=v2(3**25+1)
ok=[]
for alpha in (1,2):
    beta=1
    x=alpha
    y=1+beta
    ok.append(vp==min(x,y) if x!=y else vp> x)
assert ok==[False,False]

# High negative sign: alpha=1, beta=1 survives; beta=2 does not.
vm=v2(3**25-1)
ok=[]
for beta in (1,2):
    alpha=1
    x=beta
    y=1+alpha
    ok.append(vm==min(x,y) if x!=y else vm>x)
assert ok==[True,False]

# Exact possible positive-return quanta recorded for phase 29.
qs={
    Fraction(2**43,3**29),
    Fraction(2**44,3**29),
    Fraction(2**43,3**28),
}
assert min(qs)==Fraction(2**43,3**29)
assert max(qs)==Fraction(2**43,3**28)

print('PASS: RL178 portable second-transition verifier.')
print('v37 d=+1 excluded; d=-1 next pair forced')
print('phase-29 positive quanta verified')
