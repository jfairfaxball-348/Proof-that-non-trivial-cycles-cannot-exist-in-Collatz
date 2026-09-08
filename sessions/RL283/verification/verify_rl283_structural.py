#!/usr/bin/env python3
"""Portable RL283 closeout regression verifier.

This script checks only compact algebraic/regression consequences of the
promoted RL283 analytic results. It is not a replacement for the inherited
RL282 H<=22 exact checkpoint certificate.
"""

from fractions import Fraction
from itertools import product

def v2(n):
    n=abs(n)
    assert n
    c=0
    while n%2==0:
        n//=2; c+=1
    return c

def q_word(bits):
    r=sum(bits)
    out=0
    seen=0
    for i,b in enumerate(bits):
        if b:
            seen += 1
            out += (2**i) * (3**(r-seen))
    return out

def collatz_affine(bits,z):
    return Fraction((3**sum(bits))*z + q_word(bits), 2**len(bits))

def j_transition_fraction(d,J,x,y):
    # Formal pair-column recurrence, valid algebraically before parity legality.
    if (x,y)==(0,0):
        return d, (J + 3**d - 2**d)/2
    if (x,y)==(1,1):
        return d, (3*J + 2**d - 1)/2
    if (x,y)==(1,0):
        return d-1, J/2
    if (x,y)==(0,1):
        return d+1, (3*J + 3**(d+1) - 2**d - 1)/2
    raise AssertionError

def exact_step(d,J,H,x):
    K=J+2**d-1
    if K%2==0:
        if x==1:
            d2=d; K2=3*K//2; y=1
        else:
            d2=d; K2=(K+3**d-1)//2; y=0
    else:
        if x==1:
            if d<=1:
                return None
            d2=d-1; K2=(K-1)//2; y=0
        else:
            d2=d+1; K2=3*(K+3**d)//2; y=1
    J2=K2-2**d2+1
    return d2,J2,H+d-1,y

def xi_from_ranks(m,A,B):
    r=len(A)
    return (2**m - 14*3**r
            + sum(3**(r-j-1)*(3*2**A[j]-2**B[j])
                  for j in range(r)))

# 1. Two-shadow identity on every exact prefix through length 10.
states=[(1,-13,0,(),())]
shadow_checks=0
for n in range(11):
    for d,J,H,xw,yw in states:
        T=J-3**d+2**d
        rhs=3**d*collatz_affine(xw,-7)-collatz_affine(yw,-7)
        assert rhs.denominator==1 and rhs.numerator==T
        shadow_checks += 1
    if n==10:
        break
    nxt=[]
    for d,J,H,xw,yw in states:
        for x in (0,1):
            st=exact_step(d,J,H,x)
            if st is not None:
                d2,J2,H2,y=st
                nxt.append((d2,J2,H2,xw+(x,),yw+(y,)))
    states=nxt

# 2. High-divisibility -> prefix-integrality regression on all noncrossing,
# equal-weight pair words through length 8.
hd_checks=0
for m in range(1,9):
    for xw in product((0,1), repeat=m):
        for yw in product((0,1), repeat=m):
            if sum(xw)!=sum(yw):
                continue
            d=1
            ok=True
            for x,y in zip(xw,yw):
                d += y-x
                if d<1:
                    ok=False; break
            if not ok or d!=1:
                continue
            d=1
            J=Fraction(-13,1)
            prefixes=[]
            for x,y in zip(xw,yw):
                d,J=j_transition_fraction(d,J,x,y)
                prefixes.append(J)
            if J.denominator==1:
                assert all(z.denominator==1 for z in prefixes)
                hd_checks += 1

# 3. Sharp adjacent-swap barrier.
A=(2,6,7,8,9); B=(1,5,6,8,9)
Aminus=(1,6,7,8,9)
xi=xi_from_ranks(10,A,B)
xim=xi_from_ranks(10,Aminus,B)
assert xi==8192 and v2(xi)==13
assert xim==7706 and v2(xim)==1
assert xi-xim==486

# 4. Exact terminal stress regression: enumerate all genuine canonical
# terminals whose extended bridge length L=m+k+1 is <=16.
states=[(1,-13,0,(),())]
terminal_count=0
gate_violations=0
for m in range(16):
    for d,J,H,xw,yw in states:
        if d==1 and J>0 and (J&(J-1))==0:
            k=J.bit_length()-1
            L=m+k+1
            if L<=16:
                terminal_count += 1
                if H<k:
                    gate_violations += 1
                # Extended-rank identity and single final reversal.
                X=xw+(1,)+(0,)*k
                Y=yw+(0,)*k+(1,)
                assert len(X)==len(Y)==L and sum(X)==sum(Y)
                ax=tuple(i for i,b in enumerate(X) if b)
                by=tuple(i for i,b in enumerate(Y) if b)
                assert all(b<=a for a,b in zip(ax[:-1],by[:-1]))
                assert ax[-1]==m and by[-1]==m+k
                assert sum(a-b for a,b in zip(ax[:-1],by[:-1]))==H
                assert 3*q_word(X)-q_word(Y)==14*3**sum(X)+2**L
    nxt=[]
    for d,J,H,xw,yw in states:
        for x in (0,1):
            st=exact_step(d,J,H,x)
            if st is not None:
                d2,J2,H2,y=st
                nxt.append((d2,J2,H2,xw+(x,),yw+(y,)))
    states=nxt
assert terminal_count==379
assert gate_violations==0

# 5. Strengthened noncrossing rank-relaxation barrier arithmetic.
assert 3**72 < 5*2**112
assert 3**7 > 2**11
# At zeta=1, (219/8) zeta^2 - [14+(837/64)zeta] = 19/64 > 0.
assert Fraction(219,8)-14-Fraction(837,64)==Fraction(19,64)
# Seven cap increments in {1,2} totaling >=11 force >=4 increments of size 2.
for inc in product((1,2), repeat=7):
    if sum(inc)>=11:
        assert sum(v==2 for v in inc)>=4

print("RL283 portable structural regression: PASS")
print(f"two_shadow_prefix_checks={shadow_checks}")
print(f"high_divisibility_prefix_cases={hd_checks}")
print("adjacent_swap_xi=8192,7706")
print("adjacent_swap_v2=13,1")
print(f"extended_terminal_L_le_16={terminal_count}")
print(f"extended_terminal_gate_violations={gate_violations}")
print("noncrossing_barrier_core_inequalities=PASS")
print("inherited_RL282_H22_certificate=NOT_RERUN_VERIFICATION_ECONOMY")
