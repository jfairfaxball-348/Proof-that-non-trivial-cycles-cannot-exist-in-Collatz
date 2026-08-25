#!/usr/bin/env python3
from fractions import Fraction
from math import ceil
C=42150931628
DW,RW=5000030,7000000
DM,RM=7500032,3525000
DD,RD=10000032,1775000
DU,RU=15000038,35000
mu=Fraction(1,RW+1)
lam=Fraction(RW-RD,(RW+1)*(DM+1))
assert mu==Fraction(1,7000001)
assert lam==Fraction(5225000,52500238500033)
corners=[(0,RW+1),(DW+1,RM+1),(DM+1,RD+1),(DD+1,RU+1),(DU+1,0)]
vals=[lam*d+mu*r for d,r in corners]
assert vals[0]==1 and vals[2]==1 and all(v>=1 for v in vals)
assert (lam*C).numerator//(lam*C).denominator==4195
rm_req=ceil(Fraction(RW+1,1)-Fraction((RW-RD)*(DW+1),DM+1))-1
ru_req=ceil(Fraction(RW+1,1)-Fraction((RW-RD)*(DD+1),DM+1))-1
assert rm_req==3516661
assert ru_req==33341
RD2=1800000
rm2=ceil(Fraction(RW+1,1)-Fraction((RW-RD2)*(DW+1),DM+1))-1
ru2=ceil(Fraction(RW+1,1)-Fraction((RW-RD2)*(DD+1),DM+1))-1
assert rm2==3533328 and ru2==66675
axis=Fraction(RW,1)-Fraction((RW+1)*(DM+1),DU+1)
assert axis.numerator//axis.denominator==3499993
print('RL93 four-tier geometry verifier: PASS')
print('lambda =',lam,'mu =',mu)
print('support corner values =',*vals)
print('b-monotonic weighted decrement floor =',4195)
print('current minimum middle radius =',rm_req,'current minimum ultra radius =',ru_req)
print('for R_d=1800000: minimum middle radius =',rm2,'minimum ultra radius =',ru2)
print('ultra depth-axis remains nonbinding through deep radius floor =',axis.numerator//axis.denominator)
