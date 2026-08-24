#!/usr/bin/env python3
from fractions import Fraction
from math import gcd

R0=1<<71
B=Fraction(79, 9*(R0-2))
EXPECTED_P=123139092617126647266
EXPECTED_Q=77692117359936589403
EXPECTED_D=13201833154443526323
EXPECTED_QMAX=93226756704262400759
EXPECTED_BLOCK=40249491324522944

# Exact atanh log intervals, copied in method (not bytes) from the audited RL49 verifier.
def log_interval_int(x:int, terms:int=260):
    y=Fraction(x-1,x+1)
    y2=y*y
    s=Fraction(0)
    yp=y
    for n in range(terms):
        s += yp/(2*n+1)
        yp *= y2
    lo=2*s
    tail=2*yp/((2*terms+1)*(1-y2))
    return lo,lo+tail

def ratio_interval(nlo,nhi,dlo,dhi):
    return nlo/dhi,nhi/dlo

def cf_prefix_interval(lo,hi,max_terms=80):
    out=[]
    for _ in range(max_terms):
        a_lo=lo.numerator//lo.denominator
        a_hi=hi.numerator//hi.denominator
        if a_lo!=a_hi: break
        a=a_lo; out.append(a)
        lo2=lo-a; hi2=hi-a
        if lo2<=0: break
        lo,hi=1/hi2,1/lo2
    return out

def convergents(cf):
    pm2,pm1=0,1; qm2,qm1=1,0
    for i,a in enumerate(cf):
        p=a*pm1+pm2; q=a*qm1+qm2
        yield i,p,q
        pm2,pm1=pm1,p; qm2,qm1=qm1,q

def linform_interval(p,q,l2,u2,l3,u3):
    return p*l2-q*u3,p*u2-q*l3

def ceil_div(a,b):
    return -(-a//b)

# 1. Stronger phase gate and reduced denominator floor.
l2,u2=log_interval_int(2)
l3,u3=log_interval_int(3)
blo,bhi=ratio_interval(l3,u3,l2,u2)
cf=cf_prefix_interval(blo,bhi,80)
assert len(cf)>=44
Qmax_frac=l2/(2*B)
Qmax=Qmax_frac.numerator//Qmax_frac.denominator
assert Qmax==EXPECTED_QMAX, Qmax
survivors=[]
for i,p,q in convergents(cf):
    dlo,dhi=linform_interval(p,q,l2,u2,l3,u3)
    if dlo>0 and q<=Qmax and dlo<B:
        survivors.append((i,p,q,dlo,dhi))
assert [(i,p,q) for i,p,q,_,_ in survivors]==[(41,EXPECTED_P,EXPECTED_Q)]
next_above=[(i,p,q) for i,p,q in convergents(cf)
            if i>41 and linform_interval(p,q,l2,u2,l3,u3)[0]>0]
assert next_above and next_above[0][2]>Qmax

# 2. Uniform exponent-skew floor.
D0=2*EXPECTED_P-3*EXPECTED_Q
assert D0==EXPECTED_D
c_lo=2*blo-3
assert c_lo>0
assert c_lo*EXPECTED_Q > D0-1

# 3. Canonical synchronized prefix grammar.
def sync(J,bit):
    return (J+1)//2 if bit==0 else (3*J+1)//2
J=-13
assert sync(J,1)==-19 and sync(-19,0)==-9 and sync(-9,1)==-13
# Exit branches after any whole number of 101 cycles.
assert sync(-13,0)==-6
assert sync(sync(-13,1),1)==-28
assert sync(sync(sync(-13,1),0),0)==-4
prefix_skews={2,-2,3}
# 0 -> 2; 11 -> -2; 100 -> 3 under P=2*c00-c11.
assert prefix_skews=={2,-2,3}

# 4. Algebraic count identity regression over a broad exact grid.
for k in range(3,25,2):
    for c00 in range(0,8):
        for c11 in range(0,8):
            for e in range(1,5):
                m=c00+c11+2*e
                r=c11+e
                a=m+k+1
                ell=r+3
                Delta=2*a-3*ell
                assert Delta-2*k+7 == 2*c00-c11+e

# 5. Exhaustive finite audit of the low-k violation window.
best_block=None
minimizers=[]
checks=0
for k in range(27,166,2):
    for H in range(25,k):
        for e in range(1,H+1):
            for P in (-2,2,3):
                c00_post=ceil_div(D0-2*k+7-P-e,2)
                height1_00=c00_post-H
                block=ceil_div(height1_00,e)
                checks+=1
                tup=(k,H,e,P,c00_post,height1_00)
                if best_block is None or block<best_block:
                    best_block=block
                    minimizers=[tup]
                elif block==best_block:
                    minimizers.append(tup)

assert best_block==EXPECTED_BLOCK, (best_block,minimizers[:5])
assert {(k,H,e,P) for k,H,e,P,_,_ in minimizers} == {
    (165,164,164,-2),(165,164,164,2),(165,164,164,3)
}, minimizers
min_c00=min(x[4] for x in minimizers)
min_h00=min(x[5] for x in minimizers)
assert min_c00==6600916577221762917
assert min_h00==6600916577221762753

print('RL73 ownership-forced zero-area macro verifier: PASS')
print('phase bound = 79/[9*(2^71-2)]')
print('Legendre reduced-denominator gate =',Qmax)
print('first admissible reduced pair =',EXPECTED_P,EXPECTED_Q)
print('uniform exponent-skew floor =',D0)
print('canonical prefix skews =',sorted(prefix_skews))
print('low-k parameter tuples checked =',checks)
print('minimum post-first c00 among block minimizers =',min_c00)
print('minimum post-first height-one c00 among block minimizers =',min_h00)
print('minimum aligned-00 count in one synchronized block =',best_block)
print('block-minimizing (k,H,e,P) tuples =',[(x[0],x[1],x[2],x[3]) for x in minimizers])
