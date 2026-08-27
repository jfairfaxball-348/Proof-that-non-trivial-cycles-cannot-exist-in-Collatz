#!/usr/bin/env python3
from fractions import Fraction

R0 = 1 << 71
def ln_interval(x, N=220):
    x2=x*x; term=x; s=Fraction()
    for k in range(N):
        s += term/(2*k+1); term *= x2
    return 2*s, 2*s + 2*term/(2*N+1)/(1-x2)

l2lo,l2hi=ln_interval(Fraction(1,3))
l3lo,l3hi=ln_interval(Fraction(1,2))
cf=[1,1,1,2,2,3,1,5,2,23,2,2,1,1,55,1,4,3,1,1,15,1,9,2,5,7,1,1,4,8]
pm2,pm1=0,1; qm2,qm1=1,0; rows=[]
for i,a in enumerate(cf):
    p=a*pm1+pm2; q=a*qm1+qm2
    dlo=p*l2lo-q*l3hi; dhi=p*l2hi-q*l3lo
    if q>49_547_666_543 and len(rows)<2:
        rows.append((p,q,dlo>0,dlo>Fraction(q,3*R0)))
    pm2,pm1=pm1,p; qm2,qm1=qm1,q
assert rows == [(103768467013,65470613321,False,False),(217976794617,137528045312,True,False)]
print('RL132 CF-survivor verifier: PASS')
print('first_beyond_below=',rows[0][:3])
print('first_above_survives_external_product_inequality=',rows[1][:3])
