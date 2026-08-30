#!/usr/bin/env python3
from fractions import Fraction
from functools import lru_cache

A=217_976_794_617
L=137_528_045_312
p=65_470_613_321
u=103_768_467_013
t=L-p
assert A*p-L*u==1

# Frozen RL180/RL181 inputs for the surviving (37,0,23,-1) branch.
W_UPPER=28_070_867_755
GAP_UPPER=293_591_818_782
SHALLOW={
    1:73_801_609_945,
    2:81_605_820_006,
    3:84_804_722_294,
    4:86_264_134_824,
}
EDGES={k:2*n-L for k,n in SHALLOW.items()}
assert EDGES=={
    1:10_075_174_578,
    2:25_683_594_700,
    3:32_081_399_276,
    4:35_000_224_336,
}

def ln_bounds_int(x,N=80):
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
def exp_bounds_pos(x,N=36):
    assert 0<=x<1
    term=Fraction(1)
    s=term
    for k in range(1,N+1):
        term=term*x/k
        s += term
    nxt=term*x/Fraction(N+1)
    tail=nxt/(1-x/Fraction(N+2))
    return s,s+tail

def exp_interval(lo,hi):
    assert 0<=lo<=hi<1
    elo,_=exp_bounds_pos(lo)
    _,ehi=exp_bounds_pos(hi)
    return elo,ehi

def exp_neg_interval(lo,hi):
    assert 0<=lo<=hi<1
    elo_lo,ehi_lo=exp_bounds_pos(lo)
    elo_hi,ehi_hi=exp_bounds_pos(hi)
    return Fraction(1,ehi_hi),Fraction(1,elo_lo)

l2_lo,l2_hi=ln_bounds_int(2)
l3_lo,l3_hi=ln_bounds_int(3)
d_lo=A*l2_lo-L*l3_hi
d_hi=A*l2_hi-L*l3_lo
s_lo=p*l3_lo-u*l2_hi
s_hi=p*l3_hi-u*l2_lo
assert 0<d_lo<d_hi<Fraction(1,1000)
assert 0<s_lo<s_hi<Fraction(1,1000)

ed_lo,ed_hi=exp_interval(d_lo,d_hi)
es_lo,es_hi=exp_interval(s_lo,s_hi)
eds_lo,eds_hi=exp_interval(d_lo+s_lo,d_hi+s_hi)
lam1_lo=ed_lo-1
lam1_hi=ed_hi-1
es1_lo=es_lo-1
es1_hi=es_hi-1
eds1_lo=eds_lo-1
eds1_hi=eds_hi-1

# Recompute the frozen RL180 mass corridor with rigorous rational enclosures.
rho_t_lo=eds_lo/2
rho_t_hi=eds_hi/2
F2_lo=3*(2**37)*lam1_lo
F2_hi=3*(2**37)*lam1_hi
D_lo=rho_t_lo-F2_hi
D_hi=rho_t_hi-F2_lo
W_lo=D_lo/eds1_hi
W_hi=D_hi/es1_lo
assert W_lo>23_493_381_795
assert W_hi<W_UPPER

x_lo=l2_lo/L
x_hi=l2_hi/L
q_lo,q_hi=exp_neg_interval(x_lo,x_hi)
R_lo=Fraction(1,2*(1-q_lo))
R_hi=ed_hi*Fraction(1,2*(1-q_hi))
Q_lo=R_lo-W_hi
Q_hi=R_hi-W_lo

m_lo=Q_lo/(3*lam1_hi)
m_hi=Q_hi/(3*lam1_lo)
M_LO=26_385_000_000_000_000_000_000
M_HI=28_084_000_000_000_000_000_000
assert m_lo>M_LO
assert m_hi<M_HI
assert Q_lo>71_134_646_723

def first_base_sum_upper(n):
    qnl,qnh=exp_neg_interval(n*x_lo,n*x_lo)
    return (1-qnl)/(1-q_hi)

# Any t-element base-period phase subset has q-mass no larger than the t
# largest mechanical weights. Wrapped periodic q terms are larger by lambda,
# so the cyclic base-period replacement is conservative for a p-window lower bound.
top_t_rho_hi=ed_hi*first_base_sum_upper(t)
assert top_t_rho_hi<60_422_815_771
P_LO=10_711_830_952
assert Q_lo-top_t_rho_hi>P_LO
TAIL_LO=3_570_610_317
assert Fraction(P_LO,3)>TAIL_LO

# RL182.2: the strict shallow numerator ceiling is below these ternary moduli.
DEPTH={1:25,2:26,3:26,4:27}
for k,n in DEPTH.items():
    assert (2**k)*GAP_UPPER < 3**n

# Fixed-defect populations after removing the possible carry edge.
ordinary={k:e-1 for k,e in EDGES.items()}
repeated={k:(ordinary[k]+2*k)//(2*k+1) for k in ordinary}
assert repeated=={
    1:3_358_391_526,
    2:5_136_718_940,
    3:4_583_057_040,
    4:3_888_913_815,
}

# RL182.4: affine-tail width occupancy.
# delta_r > exp(sr)((exp(s)-1)m+T).  For E arbitrary selected ranks, the
# minimum lower-envelope sum uses ranks 0..E-1.
OCCUPANCY={
    1:Fraction(25,512),
    2:Fraction(33,256),
    3:Fraction(167,1024),
    4:Fraction(23,128),
}
for k,E in EDGES.items():
    ey_lo,ey_hi=exp_interval(E*s_lo,E*s_hi)
    geometric_count_lo=(ey_lo-1)/(es_hi-1)
    fraction_lo=(ey_lo-1)+Fraction(TAIL_LO)*geometric_count_lo/M_HI
    assert fraction_lo>OCCUPANCY[k]

print('PASS: RL182 numerator ownership and affine-tail certificate')
print('m_lower_gt=',M_LO)
print('m_upper_lt=',M_HI)
print('Q_lower_gt=71134646723')
print('p_window_q_mass_gt=',P_LO)
print('affine_tail_gt=',TAIL_LO)
print('ownership_depth_h_le_1=25')
print('ownership_depth_h_le_2=26')
print('ownership_depth_h_le_3=26')
print('ownership_depth_h_le_4=27')
for k in sorted(repeated):
    print(f'h_le_{k}_fixed_G_repeat_lower={repeated[k]}')
print('occupancy_h_le_1_gt=25/512')
print('occupancy_h_le_2_gt=33/256')
print('occupancy_h_le_3_gt=167/1024')
print('occupancy_h_le_4_gt=23/128')
