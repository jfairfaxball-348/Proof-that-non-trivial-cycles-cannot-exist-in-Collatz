#!/usr/bin/env python3
from fractions import Fraction
from itertools import product


def Q(w):
    ell=sum(w); rank=0; out=0
    for i,b in enumerate(w):
        if b:
            rank += 1
            out += (1<<i)*3**(ell-rank)
    return out


def q_repeat(c,q):
    P=1<<len(c); R=3**sum(c); C=Q(c)
    if q==0: return 0
    assert R != P
    return C*(R**q-P**q)//(R-P)


def pump_coeff(A,c,B):
    LA=len(A); wB=sum(B)
    P=1<<len(c); R=3**sum(c); C=Q(c); delta=R-P
    X0=1<<(len(A)+len(B)); Y0=3**(sum(A)+sum(B))
    AA=delta*3**wB*Q(A)+(1<<LA)*3**wB*C+4*delta*Y0
    BB=delta*(1<<LA)*Q(B)-(1<<LA)*3**wB*C
    return P,R,delta,X0,Y0,AA,BB

# Concatenation and repeat identity.
concat_checks=0
for la in range(4):
  for lb in range(4):
    for A in product([0,1], repeat=la):
      for B in product([0,1], repeat=lb):
        assert Q(A+B)==3**sum(B)*Q(A)+(1<<len(A))*Q(B)
        concat_checks += 1

repeat_checks=0
for c in [(1,0,1),(1,0),(0,),(1,1,0),(0,1,1)]:
    for q in range(8):
        assert Q(c*q)==q_repeat(c,q)
        repeat_checks += 1

# Exact pump/Mobius law on bounded contexts.
pump_checks=0
for A in [(),(1,),(1,1,1),(1,0,1)]:
  for c in [(1,0,1),(1,0),(0,1,1)]:
    for B in [(),(0,0),(1,0),(1,1,0,0),(0,1,0)]:
      P,R,delta,X0,Y0,AA,BB=pump_coeff(A,c,B)
      for q in range(7):
        v=A+c*q+B
        ell=sum(v)
        lhs=delta*(Q(v)+4*3**ell)
        rhs=AA*R**q+BB*P**q
        assert lhs==rhs
        M=X0*P**q-Y0*R**q
        if M:
            N1=Fraction(Q(v)+4*3**ell,M)
            N2=Fraction(AA*R**q+BB*P**q,delta*M)
            assert N1==N2
        pump_checks += 1

# Height-one canonical dynamics and fixed-area family.
def step(d,J,H,e,g):
    x,y=map(int,e)
    if J&1:
        assert e in ('00','11')
        if e=='00': J2=(J+3**d-2**d)//2
        else: J2=(3*J+2**d-1)//2
    else:
        assert e in ('01','10')
        if e=='01': J2=(3*J+3**(d+1)-2**d-1)//2
        else:
            assert d>1
            J2=J//2
    d2=d+y-x
    H2=H+d-1
    g2=g*Fraction(2,3 if x else 1)
    return d2,J2,H2,g2

# Closed synchronized cycles.
def sync_step(J,b):
    assert J&1
    return ((3 if b else 1)*J+1)//2
for J,c in [(-13,(1,0,1)),(3,(1,0))]:
    cur=J
    for b in c:
        cur=sync_step(cur,b)
        assert cur&1
    assert cur==J

family_checks=0
cap_checks=0
psi_checks=0
for q in range(61):
    p=3*q+15
    edges=['11','00','11']*p+['11','00','00']+['01','00','00','11','10']+['11','00']*q+['00']
    d,J,H,g=1,-13,0,Fraction(2)
    pump_index=3*p+3+5
    g_ent=None
    zero_mass=Fraction(0)
    psi_ent=None
    positive_cap_ok=True
    for idx,e in enumerate(edges):
        if idx==pump_index:
            assert (d,J,H)==(1,3,4)
            g_ent=g
            psi_ent=g*Fraction(J+1,2)
        # audit inherited stronger zeta=1 cap at every positive pre-state
        if J>0:
            assert J*g <= Fraction(9,2)*3**d
            cap_checks += 1
        if idx>=pump_index and e=='00':
            zero_mass += g
        d,J,H,g=step(d,J,H,e,g)
    assert (d,J,H)==(1,2,4)
    assert g_ent==Fraction(512,27)*Fraction(8,9)**p
    assert g==2*g_ent*Fraction(4,3)**q
    assert zero_mass==g_ent*(3*Fraction(4,3)**q-2)
    psi_out=g*Fraction(J+1,2)
    assert psi_out-psi_ent==zero_mass
    assert zero_mass < 10
    family_checks += 1
    psi_checks += 1

# Canonical-prefix specialization of the full-phase numerator.
special_checks=0
A=(1,1,1); c=(1,0,1)
for y in [(),(0,),(1,),(1,0,1),(0,1,1,0),(1,1,0,1)]:
  for t in range(4):
    B=y+(0,)*(t+1)
    r=sum(y); Qy=Q(y)
    for q in range(7):
      v=A+c*q+B
      Vq=Q(v)
      assert Vq==75*3**r*9**q+(8*Qy-56*3**r)*8**q
      full=Vq+4*3**(r+3+2*q)
      assert full==183*3**r*9**q+(8*Qy-56*3**r)*8**q
      special_checks += 1

print('RL74 synchronized-pump verifier: PASS')
print('concat checks =',concat_checks)
print('repeat checks =',repeat_checks)
print('pump/Mobius checks =',pump_checks)
print('canonical fixed-area family checks =',family_checks)
print('positive corrected-cap state checks =',cap_checks)
print('Psi telescope checks =',psi_checks)
print('canonical-prefix specialization checks =',special_checks)
