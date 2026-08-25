#!/usr/bin/env python3
from fractions import Fraction
from math import ceil
from itertools import combinations
C=42150931628
DW,RW=5000030,7000000
DM,RM=7500032,3675000
DD,RD=10000032,2000000
DU,RU=15000038,335000
mu=Fraction(1,RW+1)
lam=Fraction(RW-RD,(RW+1)*(DM+1))
assert mu==Fraction(1,7000001)
assert lam==Fraction(5000000,52500238500033)
corners=[('A',0,RW+1),('B',DW+1,RM+1),('C',DM+1,RD+1),('D',DD+1,RU+1),('E',DU+1,0)]
vals=[lam*d+mu*r for _,d,r in corners]
assert vals[0]==1 and vals[2]==1 and all(v>=1 for v in vals)
assert vals[1]==Fraction(5840309308337,5833359833337)
assert vals[3]==Fraction(52512683555033,52500238500033)
assert vals[4]==Fraction(2777785000000,1944453277779)
assert (lam*C).numerator//(lam*C).denominator==4014
# exact feasible two-corner supports at final staircase
feasible=[]
for (n1,d1,r1),(n2,d2,r2) in combinations(corners,2):
    det=d1*r2-d2*r1
    if not det: continue
    l=Fraction(r2-r1,det); m=Fraction(d1-d2,det)
    if l<0 or m<0: continue
    vv=[l*d+m*r for _,d,r in corners]
    if min(vv)>=1: feasible.append((n1+n2,l,m))
assert [x[0] for x in feasible]==['AC','CD','DE'],feasible
# current and next-step coupling thresholds for A-C line
def req(rd):
    rm=ceil(Fraction(RW+1,1)-Fraction((RW-rd)*(DW+1),DM+1))-1
    ru=ceil(Fraction(RW+1,1)-Fraction((RW-rd)*(DD+1),DM+1))-1
    return rm,ru
assert req(RD)==(3666661,333341)
assert req(2025000)==(3683328,366674)
axis=Fraction(RW,1)-Fraction((RW+1)*(DM+1),DU+1)
assert axis.numerator//axis.denominator==3499993
print('RL94 four-tier geometry verifier: PASS')
print('lambda =',lam,'mu =',mu)
print('support corner values =',*vals)
print('feasible pair supports =',*[x[0] for x in feasible])
print('b-monotonic weighted decrement floor =',4014)
print('current minimum middle radius = 3666661 current minimum ultra radius = 333341')
print('for R_d=2025000: minimum middle radius = 3683328 minimum ultra radius = 366674')
print('ultra depth-axis remains nonbinding through deep radius floor =',axis.numerator//axis.denominator)
