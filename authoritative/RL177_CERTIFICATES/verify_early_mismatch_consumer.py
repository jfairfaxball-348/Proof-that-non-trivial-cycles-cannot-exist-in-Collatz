#!/usr/bin/env python3
from fractions import Fraction

A=217_976_794_617
L=137_528_045_312
p=65_470_613_321
u=103_768_467_013
assert A*p-L*u == 1
assert p+37 < L

def B(j):
    return (A*j)//L

C=[B(j+1)-B(j) for j in range(37)]
assert set(C) <= {1,2}

# Common-height automaton before the first mismatch.  States are identified
# by height only; this certificate counts identified mismatch tuples, not full
# prefix histories.
reach={0:{0}}
for j in range(37):
    nxt=set()
    for h in reach[j]:
        for a in range(1,h+C[j]+1):
            h2=h+C[j]-a
            assert h2>=0
            nxt.add(h2)
    reach[j+1]=nxt

types=[]
for J in range(1,37):
    for H in reach[J]:
        top=H+C[J]
        for a in range(1,top+1):
            for b in range(1,top+1):
                if a==b:
                    continue
                d=b-a
                v=B(J)-H+min(a,b)
                if v<=37:
                    types.append((J,H,a,b,d,v))

assert len(types)==15_872
assert sorted({x[5] for x in types})==list(range(2,38))
for v in range(2,38):
    assert {1 if x[4]>0 else -1 for x in types if x[5]==v}=={-1,1}
assert max(abs(x[4]) for x in types)==21

# Exact first-flow quantum lower bound.
def term_abs(x):
    J,H,a,b,d,v=x
    return Fraction((2**abs(d)-1)*2**v,3**(J+1))

min_all=min(term_abs(x) for x in types)
assert min_all==Fraction(2**37,3**37)
assert min_all > Fraction(3,10_000_000)

zero=[x for x in types if x[1]==0]
zero_js=[1,3,5,6,8,10,11,13,15,17,18,20,22,23]
assert len(zero)==28
assert sorted({x[0] for x in zero})==zero_js
for J,H,a,b,d,v in zero:
    assert C[J]==2
    assert {a,b}=={1,2}
    assert abs(d)==1
    assert v==B(J)+1
    # The created height-one phase is a component start; exact arithmetic
    # checks rho_(J+1)>2/3 and therefore |T|=rho/2>1/3.
    assert 3*(2**B(J+1)) > 2*(3**(J+1))
    assert term_abs((J,H,a,b,d,v)) > Fraction(1,3)

min_zero=min(term_abs(x) for x in zero)
assert min_zero==Fraction(134_217_728,387_420_489)
assert min_zero > Fraction(1,3)

v36=[x for x in types if x[5]==36]
assert v36 and all(x[1]>=1 for x in v36)

v37_zero=[x for x in zero if x[5]==37]
assert {(x[0],x[4]) for x in v37_zero}=={(23,-1),(23,1)}
assert all(term_abs(x)==Fraction(2**37,3**24) for x in v37_zero)

# The analytic positive-height support-loss floor is minimized at H=1, |d|=1.
loss_min=Fraction(3,2)-Fraction(1,2)-Fraction(1,4)
assert loss_min==Fraction(3,4)

print('PASS: RL177 early-mismatch finite certificate completed successfully.')
print(f'identified local mismatch tuples = {len(types):,}')
print('valuations 2..37: both signs locally feasible')
print('max |d| = 21')
print('zero-height signed types = 28 across 14 indices')
print(f'min zero-height |T| = {min_zero.numerator}/{min_zero.denominator} > 1/3')
print(f'global min |T| = 2^37/3^37 > 3/10^7')
print('v=36: H>=1; v=37,H=0: J=23, d=+/-1 only')
