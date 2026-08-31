#!/usr/bin/env python3
"""RL195 exact moment-to-chronological-zero-edge checks.

Actual constants are rigorously enclosed. The toy domain below is only an
algebraic regression, never an actual high-branch phase certificate.
"""
from fractions import Fraction as F
from itertools import product

A=217976794617
L=137528045312
B=A-L
R=L-B
p=65470613321
u0=103768467013
z=L-p
K0=2**37

def ln_bounds(n, terms=96):
    t=F(n-1,n+1)
    term=t
    total=F(0)
    for k in range(terms):
        total+=term/(2*k+1)
        term*=t*t
    lo=2*total
    return lo,lo+2*term/((2*terms+1)*(1-t*t))

def expm1_bounds(lo,hi):
    assert 0<lo<hi<1
    return lo+lo*lo/2, hi+hi*hi/(2*(1-hi/3))

assert A*p-u0*L==1
assert 0<R<B<2*R<L
assert (p*B)%L==1
assert ((p-1)*B)%L==R+1<2*R
assert ((L-1)*B)%L==R<2*R
assert ((R-1)*p)%L==z-1
assert ((2*R-1)*p)%L==z-2
assert ((z-1)*B)%L==R-1
assert ((z-2)*B)%L==2*R-1
assert ((z)*B)%L==L-1

l2,h2=ln_bounds(2)
l3,h3=ln_bounds(3)
delta_lo=A*l2-L*h3
delta_hi=A*h2-L*l3
assert 0<delta_lo<delta_hi<F(1,2**40)
e_lo,e_hi=expm1_bounds(delta_lo,delta_hi)
eta_lo,eta_hi=expm1_bounds((l2-p*delta_hi)/L,(h2-p*delta_lo)/L)
theta_lo,theta_hi=expm1_bounds((l2+(L-p)*delta_lo)/L,(h2+(L-p)*delta_hi)/L)
assert 0<eta_hi<theta_lo
flow_lo,flow_hi=3*K0*e_lo,3*K0*e_hi
M_lo=2*flow_lo-F(1,2)-3*theta_hi/2
C_hi=3*(1+theta_hi)/16
assert M_lo>C_hi>0
threshold_lo=(2*flow_lo-F(11,16))/theta_hi-F(27,16)
threshold_hi=(2*flow_hi-F(11,16))/theta_lo-F(27,16)
assert F(9719139551)<threshold_lo<threshold_hi<F(9719139552)
J_floor=9719139553
assert J_floor==9719139551+2
assert J_floor<L

def toy_checks():
    a,length,shift,bezout=8,5,2,3
    b=a-length
    rr=length-b
    carry=length-shift
    assert 0<rr<b<2*rr<length
    lam=F(2**a,3**length)
    alpha=F(3**shift,2**bezout)
    eta=alpha-1
    theta=lam*alpha-1
    assert 0<eta<theta
    rho=[F(2**(a*i//length),3**i) for i in range(length)]
    rank=[(i*b)%length for i in range(length)]
    phase=[(r*shift)%length for r in range(length)]
    w=[rho[i] for i in phase]
    d=[F(0)]+[w[r-1]-w[r] for r in range(1,length)]
    c=[a*(i+1)//length-a*i//length for i in range(length)]
    assert c[0]==1
    assert rho[carry]==lam*alpha/2
    for r in range(1,length):
        i=phase[r]
        assert d[r]==(theta if i<shift else eta)*w[r]
        assert 0<d[r]<theta
    for r in range(rr):
        assert rank[(phase[r]+1)%length]==r+b
    for r in range(1,rr):
        assert d[r+b]==F(2,3)*d[r]
    for r in range(2*rr,length):
        assert rank[(phase[r]+1)%length]==r-rr
        assert d[r-rr]==F(4,3)*d[r]
    low=set(range(rr))
    doubles=set(range(2*rr,length))|set(range(rr,b))
    single=set(range(b,2*rr))
    assert not(low&doubles or low&single or doubles&single)
    assert low|doubles|single==set(range(length))
    base=sum(d[rr:2*rr],F(0))
    assert base==w[rr-1]-w[2*rr-1]==3*(1+theta)/16
    total_arrays=0
    admissible_arrays=0
    strict_cases=0
    for tail in product(range(4),repeat=length-1):
        total_arrays+=1
        h=(0,)+tail
        exponent=[h[i]+c[i]-h[(i+1)%length] for i in range(length)]
        if min(exponent)<1:
            continue
        admissible_arrays+=1
        assert sum(exponent)==a
        v=[F(1,2**hh) for hh in h]
        x=[int(h[i]==0) for i in phase]
        edge=[int(h[i]==h[(i+1)%length]==0) for i in range(length)]
        J=sum(edge)
        assert edge[0]==1
        for r in low:
            assert x[r]<=x[r+b]
        zero_mass=sum((d[r]*x[r] for r in range(1,length)),F(0))
        charge_low=sum((d[r]*edge[phase[r]] for r in range(1,rr)),F(0))
        charge_double=sum((d[r]*edge[phase[r]] for r in range(2*rr,length)),F(0))
        charged_edges=sum(edge[phase[r]] for r in list(range(1,rr))+list(range(2*rr,length)))
        assert charged_edges<=J-1
        assert zero_mass<=base+charge_low+charge_double
        for r in range(2*rr,length):
            assert d[r]*x[r]+d[r-rr]*x[r-rr]<=d[r-rr]+d[r]*x[r]*x[r-rr]
        errors=[v[(i+shift)%length]-v[i]+int(i==carry) for i in range(length)]
        flow=sum((rho[i]*errors[i] for i in range(length)),F(0))
        assert flow==theta+sum((d[r]*v[phase[r]] for r in range(1,length)),F(0))
        M=2*flow-3*rho[carry]+1
        assert M<=zero_mass
        if M>base:
            strict_cases+=1
            assert charged_edges>0
            assert M<=zero_mass<base+theta*(J-1)
            assert J-1>(2*flow-F(11,16))/theta-F(27,16)
    assert total_arrays==256
    assert admissible_arrays>0 and strict_cases>0
    return total_arrays,admissible_arrays,strict_cases

counts=toy_checks()
print('PASS exact RL195 moment-to-chronological-zero-edge constants and geometry')
print('actual_zero_zero_edge_floor_J>=9719139553 (conditional on physical high branch)')
print('strict_integer_threshold_for_J_minus_one in (9719139551,9719139552)')
print('toy_arrays_total_admissible_strict=',counts)
print('no actual-phase scan; toy arrays are algebraic regression only')
print('no H21 ownership/count, p-shifted zero-pair count, spacing or branch/global closure claim')
