#!/usr/bin/env python3
from fractions import Fraction
from collections import defaultdict
from functools import lru_cache
import json
from pathlib import Path

A=217_976_794_617
L=137_528_045_312
B=A-L
R=L-B
p=65_470_613_321
u=103_768_467_013
GAP_LOWER=128_081_997_553
GAP_UPPER=293_591_818_782
K_LO=128_081_997_553
CLEAN=10_075_174_499
N35=7_559_400_754
N36=7_238_318_174
N37=7_052_720_272

assert A*p-L*u==1
def ceil_div(a,b): return (a+b-1)//b
def v2(x): return (x & -x).bit_length()-1
def cbit(r): return 1 if r<R else 2

late_max={j:(0 if j==0 else ceil_div(j*B,L)) for j in range(40)}
height_envelope={j:1+late_max[j] for j in range(40)}
rows=defaultdict(list)
for tau in range(26,40):
    ell0=(tau*B)//L
    ell1=ceil_div(tau*B,L)
    for h0 in (0,1):
        lo=GAP_LOWER*(2**h0)
        hi=GAP_UPPER*(2**h0)
        step=2**tau
        for k in range(lo//step+1,(hi-1)//step+1):
            C0=k*step
            vv=v2(C0)
            odd=C0>>vv
            T=(3**tau)*odd
            for ell in sorted({ell0,ell1}):
                H=h0+tau+ell-vv
                if H<1 or H>height_envelope[tau]: continue
                if not (GAP_LOWER*(2**H)<T<GAP_UPPER*(2**H)): continue
                rlo=max(0,tau*B-ell*L)
                rhi=min(L-1,tau*B-(ell-1)*L-1)
                if rlo<=rhi:
                    rows[(T,H)].append((tau,h0,C0,vv,odd,ell,rlo,rhi))

def overlap_core(sep,lo,hi):
    sh=(sep*B)%L
    out=[]
    for k in range(-2,3):
        a=max(lo,lo-sh+k*L)
        b=min(hi,hi-sh+k*L)
        if a<=b: out.append((a,b))
    return out

def atom_intervals(lo,hi,n):
    bounds={lo,hi+1}
    for j in range(n):
        shift=(j*B)%L
        for q in (0,R):
            x=(q-shift)%L
            if lo<x<=hi: bounds.add(x)
    bounds=sorted(bounds)
    return [(a,b-1) for a,b in zip(bounds,bounds[1:]) if a<=b-1]

def universal_params(word):
    radnum=0
    S=0
    for c in word:
        radnum=3*radnum+2*(1<<S)
        S+=c
    return radnum,S

T20=250_157_725_494_998_535
H20=20
FAM=(32,33,34,35)
CORE=(96_166_487_668,98_855_162_143)
tau=max(FAM)
targets=sorted(set(int(Fraction(rr[2],2**rr[1])) for rr in rows[(T20,H20)] if rr[0]==tau))
assert targets==[171_798_691_840]

atoms=0
nonempty=0
min_margin=None
for sep in range(36,3032):
    ovs=overlap_core(sep,*CORE)
    if ovs: nonempty+=1
    n=sep-tau
    p3=3**n
    for a,b in ovs:
        for x,y in atom_intervals(a,b,n):
            w=tuple(cbit((x+j*B)%L) for j in range(n))
            assert tuple(cbit((y+j*B)%L) for j in range(n))==w
            radnum,S=universal_params(w)
            denexp=H20+S
            cnum=T20*p3
            for target in targets:
                distnum=abs(cnum-target*(1<<denexp))
                rhs=radnum*(1<<H20)
                assert distnum>rhs
                margin=Fraction(distnum-rhs,1<<denexp)
                min_margin=margin if min_margin is None or margin<min_margin else min_margin
            atoms+=1
assert atoms==1829
assert nonempty==118
assert min_margin>0
cap3032=L//3032
assert cap3032==45_358_853

def ln_bounds_int(x,N=100):
    x=Fraction(x)
    z=(x-1)/(x+1)
    z2=z*z
    term=z
    s=Fraction(0)
    for n in range(N):
        s += term/Fraction(2*n+1)
        term *= z2
    lo=2*s
    tail=2*term/Fraction(2*N+1)/(1-z2)
    return lo,lo+tail

@lru_cache(maxsize=None)
def exp_bounds_pos(x,N=50):
    assert 0<=x<1
    term=Fraction(1)
    s=term
    for k in range(1,N+1):
        term=term*x/k
        s += term
    nxt=term*x/Fraction(N+1)
    tail=nxt/(1-x/Fraction(N+2))
    return s,s+tail

l2_lo,l2_hi=ln_bounds_int(2)
l3_lo,l3_hi=ln_bounds_int(3)
d_lo=A*l2_lo-L*l3_hi
d_hi=A*l2_hi-L*l3_lo
s_lo=p*l3_lo-u*l2_hi
s_hi=p*l3_hi-u*l2_lo
assert 0<d_lo<d_hi<Fraction(1,1000)
assert 0<s_lo<s_hi<Fraction(1,1000)

@lru_cache(maxsize=None)
def exp_hi_at_rank(r):
    q=(p*r)//L
    xhi=r*s_hi+q*d_hi
    return exp_bounds_pos(xhi)[1]

def local_budget_U(T,H,rhi):
    generic=Fraction(2**(24-H),1)
    corridor=Fraction(K_LO*(2**25),T)
    rank_endpoint=Fraction(2**(25-H),1)/exp_hi_at_rank(rhi)
    return max(generic,corridor,rank_endpoint)

overages=[
(138976514163888075,20,0,13029063886,(31,32,33)),
(150094635296999121,20,0,18406412838,(31,32,33,34,35,36)),
(150094635296999121,20,18406412839,23369453297,(32,33,34,35,36)),
(161212756430110167,20,5377348952,18406412838,(31,32,33)),
(183448998696332259,20,28746802250,62456644958,(32,33,34)),
(216803362095665397,20,62456644959,96166487667,(32,33,34)),
(250157725494998535,20,96166487668,98855162143,(32,33,34,35)),
(283512088894331673,21,0,13029063886,(33,34)),
(316866452293664811,21,5377348952,36398517184,(33,34)),
(350220815692997949,21,23369453298,41775866136,(33,34,35)),
(450283905890997363,21,72797034370,103818202602,(34,35,36,37)),
(1350851717672992089,23,15717738363,46738906595,(37,38)),
(4052555153018976267,24,96166487668,111884226030,(39,)),
]
H20four=overages[6]
H21a=overages[9]
H21b=overages[10]
H24=overages[12]
binding=overages[5]

b=c=local_budget_U(H24[0],H24[1],H24[3])
a=local_budget_U(binding[0],binding[1],binding[3])/3
assert Fraction(6607,1000)<a<Fraction(6608,1000)
assert Fraction(1137,1000)<b<Fraction(1139,1000)

def charge_U(owners):
    return sum(a if t<=34 else b if t in (35,36) else c for t in owners)

active=[]
bindings=[]
for cell in overages:
    q=charge_U(cell[4])
    bud=local_budget_U(cell[0],cell[1],cell[3])
    if q>bud: active.append(cell)
    if q==bud: bindings.append(cell)

assert active==[H20four,H21a,H21b]
assert binding in bindings and H24 in bindings

cap1001=L//1001
assert cap1001==137_390_654
def excess(cell):
    return charge_U(cell[4])-local_budget_U(cell[0],cell[1],cell[3])
assert excess(H20four)>0 and excess(H21a)>0 and excess(H21b)>0

early=CLEAN-N35
mid=(N35-N36)+(N36-N37)
U=Fraction(1,2**25)
penalty=cap3032*excess(H20four)+cap1001*excess(H21a)+cap1001*excess(H21b)
ordinary=U*(early*a+mid*b+N37*c-penalty)
assert ordinary>742
assert ordinary/2>371
assert ordinary/6>123

slope=early-3*cap3032-3*cap1001
assert slope==1_967_525_224
assert slope-3*655_841_741>0
assert slope-3*655_841_742<0
assert L//209==658_028_924
assert L//210==654_895_453
assert slope-3*(L//209)<0
assert slope-3*(L//210)>0

print("PASS: RL236 exact H20 four-owner recurrence and repaired charging")
print("H20_32333435_spacing_ge=3032")
print("H20_32333435_occurrence_cap=45358853")
print("recurrence_atoms=1829 nonempty_separations=118")
print("ordinary_abs_flow_gt_742=yes")
print("ordinary_abs_flow_approx=%.12f" % float(ordinary))
print("each_signed_flow_gt_371=yes")
print("each_directional_K_variation_gt_123=yes")
print("next_H20_323334_incidence_cap_le=655841741")
print("next_spacing_209_sufficient=no")
print("next_spacing_210_sufficient=yes")
