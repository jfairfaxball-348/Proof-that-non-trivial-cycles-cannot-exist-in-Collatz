#!/usr/bin/env python3
from fractions import Fraction
from math import floor

R0 = 1 << 71
C = Fraction(398,45)

# Exact atanh-series interval for log(x), x rational >0.
def log_interval_int(x:int, terms:int=260):
    y = Fraction(x-1, x+1)
    y2 = y*y
    s = Fraction(0)
    yp = y
    for n in range(terms):
        s += yp / (2*n+1)
        yp *= y2
    lo = 2*s
    # Tail <= 2*y^(2N+1)/((2N+1)*(1-y^2)), where yp=y^(2N+1)
    tail = 2*yp / ((2*terms+1)*(1-y2))
    hi = lo + tail
    return lo,hi

def ratio_interval(nlo,nhi,dlo,dhi):
    assert 0 < dlo <= dhi
    return nlo/dhi, nhi/dlo

def cf_prefix_interval(lo,hi,max_terms=80):
    out=[]
    for _ in range(max_terms):
        a_lo=lo.numerator//lo.denominator
        a_hi=hi.numerator//hi.denominator
        if a_lo != a_hi:
            break
        a=a_lo
        out.append(a)
        lo2=lo-a; hi2=hi-a
        if lo2 <= 0:
            break
        lo,hi = 1/hi2, 1/lo2
    return out

def convergents(cf):
    pm2,pm1=0,1
    qm2,qm1=1,0
    for i,a in enumerate(cf):
        p=a*pm1+pm2
        q=a*qm1+qm2
        yield i,p,q
        pm2,pm1=pm1,p
        qm2,qm1=qm1,q

def linform_interval(p,q,l2,u2,l3,u3):
    return p*l2-q*u3, p*u2-q*l3

l2,u2=log_interval_int(2)
l3,u3=log_interval_int(3)
blo,bhi=ratio_interval(l3,u3,l2,u2)
cf=cf_prefix_interval(blo,bhi,80)
assert len(cf) >= 44, len(cf)

# Necessary phase-resonance bound from analytic theorem.
phase_bound = C / R0

# Legendre range: C/(R0*ell*log2) < 1/(2 ell^2)
# sufficient if ell < R0*log2/(2C); use rigorous lower log2.
legendre_floor = Fraction(R0,1)*l2/(2*C)
Qmax = legendre_floor.numerator // legendre_floor.denominator

survivors=[]
excluded=[]
for i,p,q in convergents(cf):
    dlo,dhi=linform_interval(p,q,l2,u2,l3,u3)
    if dlo > 0: # above beta
        # If log(zeta)=linear form already exceeds phase_bound, zeta-1 does too.
        if dlo >= phase_bound:
            excluded.append((i,p,q))
        else:
            survivors.append((i,p,q,dlo,dhi))

# Below the Legendre range, every admissible reduced a/ell is an above-beta convergent.
# Check the unique surviving above-beta convergent with q <= Qmax.
small_survivors=[x for x in survivors if x[2] <= Qmax]
assert len(small_survivors)==1, [(x[0],x[2]) for x in small_survivors]
i,p,q,dlo,dhi=small_survivors[0]
assert i==41
assert p==123139092617126647266
assert q==77692117359936589403

# Previous above-beta convergent is rigorously excluded.
assert any(i0==39 for i0,_,_ in excluded)
# Next above-beta denominator is beyond Legendre gate.
next_above=[(i0,p0,q0) for i0,p0,q0 in convergents(cf) if i0>i and linform_interval(p0,q0,l2,u2,l3,u3)[0] > 0]
assert next_above and next_above[0][0]==43
assert next_above[0][2] > Qmax

print('RL49 phase-resonance squeeze verifier: PASS')
print('analytic constant C = 398/45')
print('phase bound zeta-1 < C/2^71 =', phase_bound)
print('rigorous Legendre denominator gate Qmax =', Qmax)
print('unique above-beta convergent surviving below gate:')
print(' index=',i,'a=',p,'ell=',q,'q=a-ell=',p-q)
print('next above-beta convergent index/ell =',next_above[0][0],next_above[0][2])
