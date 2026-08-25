#!/usr/bin/env python3
from fractions import Fraction
from math import ceil
from itertools import combinations

C=42150931628
DW,RW=5000030,7000000
DM,RM=7500032,3800000
DD,RD=10000032,2200000
DU,RU=15000035,605000

mu=Fraction(1,RW+1)
lam=Fraction(RW-RD,(RW+1)*(DM+1))
assert mu==Fraction(1,7000001)
assert lam==Fraction(1600000,17500079500011)

corners=[
    ('A',0,RW+1),
    ('B',DW+1,RM+1),
    ('C',DM+1,RD+1),
    ('D',DD+1,RU+1),
    ('E',DU+1,0),
]
vals=[lam*d+mu*r for _,d,r in corners]
assert vals[0]==1 and vals[2]==1
assert vals[1]==Fraction(1944454877779,1944453277779)
assert vals[3]==Fraction(17512561955011,17500079500011)
assert vals[4]==Fraction(8000019200000,5833359833337)
assert all(v>=1 for v in vals)

feasible=[]
for (n1,d1,r1),(n2,d2,r2) in combinations(corners,2):
    det=d1*r2-d2*r1
    if not det:
        continue
    l=Fraction(r2-r1,det)
    m=Fraction(d1-d2,det)
    if l<0 or m<0:
        continue
    vv=[l*d+m*r for _,d,r in corners]
    if min(vv)>=1:
        feasible.append((n1+n2,l,m))

assert [x[0] for x in feasible]==['AC','CD','DE'],feasible
assert (lam*C).numerator//(lam*C).denominator==3853

def req(rd):
    rm=ceil(Fraction(RW+1,1)-Fraction((RW-rd)*(DW+1),DM+1))-1
    ru=ceil(Fraction(RW+1,1)-Fraction((RW-rd)*(DD+1),DM+1))-1
    return rm,ru

assert req(RD)==(3799995,600008)
assert req(2225000)==(3816661,633341)

axis=Fraction(RW,1)-Fraction((RW+1)*(DM+1),DU+1)
assert axis.numerator//axis.denominator==3499992

# E-axis robustness for the active AC support:
# AC remains valid at E as long as lambda*(D_u+1)>=1.
min_du_for_e=ceil(Fraction(1,1)/lam)-1
assert min_du_for_e==10937549
assert DU-min_du_for_e==4062486

print('RL95 four-tier geometry verifier: PASS')
print('lambda =',lam,'mu =',mu)
print('support corner values =',*vals)
print('feasible pair supports =',*[x[0] for x in feasible])
print('b-monotonic weighted decrement floor =',3853)
print('current minimum middle radius = 3799995 current minimum ultra radius = 600008')
print('for R_d=2225000: minimum middle radius = 3816661 minimum ultra radius = 633341')
print('ultra depth-axis remains nonbinding through deep radius floor =',axis.numerator//axis.denominator)
print('AC E-axis minimum D_u =',min_du_for_e,'current depth reserve =',DU-min_du_for_e)
