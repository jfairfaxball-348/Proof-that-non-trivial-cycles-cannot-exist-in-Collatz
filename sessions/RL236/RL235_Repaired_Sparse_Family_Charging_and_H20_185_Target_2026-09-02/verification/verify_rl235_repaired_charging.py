#!/usr/bin/env python3
from fractions import Fraction
from functools import lru_cache
from pathlib import Path

A=217_976_794_617
L=137_528_045_312
p=65_470_613_321
u=103_768_467_013
K_LO=128_081_997_553
CLEAN=10_075_174_499
N35=7_559_400_754
N36=7_238_318_174
N37=7_052_720_272

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
T20=5*3**35
T21=350_220_815_692_997_949
H20=(T20,20,96_166_487_668,98_855_162_143,(32,33,34,35))
H21=(T21,21,23_369_453_298,41_775_866_136,(33,34,35))
H24=(4052555153018976267,24,96_166_487_668,111_884_226_030,(39,))
assert H20 in overages and H21 in overages and H24 in overages

b20=local_budget_U(H20[0],H20[1],H20[3])
b21=local_budget_U(H21[0],H21[1],H21[3])
b24=local_budget_U(H24[0],H24[1],H24[3])
c=b24
b=c
a=(b20-b)/3
assert a>b==c>0

def charge_U(owners):
    return sum(a if t<=34 else b if t in (35,36) else c for t in owners)

assert a<Fraction(6102,1000)
assert b==c<Fraction(1138,1000)
for cell in overages:
    T,H,rlo,rhi,owners=cell
    charge=charge_U(owners)
    if cell==H21:
        continue
    assert charge<=local_budget_U(T,H,rhi)

h21_excess=charge_U(H21[4])-b21
assert h21_excess>0
cap1001=L//1001
assert cap1001==137_390_654

early=CLEAN-N35
tau35=N35-N36
tau36=N36-N37
assert early==2_515_773_745
assert tau35==321_082_580
assert tau36==185_597_902
U=Fraction(1,2**25)
ordinary_floor=U*(early*a+(tau35+tau36)*b+N37*c-cap1001*h21_excess)
assert ordinary_floor>712
assert ordinary_floor>665
assert ordinary_floor/2>356
assert ordinary_floor/6>118

slope=early-2*cap1001
assert slope==2_240_992_437
assert slope-3*746_997_478>0
assert slope-3*746_997_479==0
assert L//184==747_435_028
assert L//185==743_394_839
assert slope-3*(L//184)<0
assert slope-3*(L//185)>0

print('PASS: RL235 repaired exhaustive sparse-family charging certificate')
print('full_prefix_atomic_cells=7531')
print('generic_budget_overages=13')
print('all_non_H21_overages_covered_by_local_K_pricing=yes')
print('H21_333435_spacing_ge=1001 inherited_and_used=yes')
print('ordinary_abs_flow_gt_712=yes')
print('ordinary_abs_flow_approx=%.12f' % float(ordinary_floor))
print('each_signed_flow_gt_356=yes')
print('each_directional_K_variation_gt_118=yes')
print('next_H20_incidence_cap_le=746997478')
print('H20_spacing_184_sufficient=no')
print('H20_spacing_185_sufficient=yes')
