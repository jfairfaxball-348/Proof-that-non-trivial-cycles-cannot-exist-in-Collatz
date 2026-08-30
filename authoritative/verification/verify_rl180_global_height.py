#!/usr/bin/env python3
from fractions import Fraction
from functools import lru_cache

A=217_976_794_617
L=137_528_045_312
p=65_470_613_321
u0=103_768_467_013
t=L-p
assert A*p-L*u0==1

# Exact rational logarithm enclosure, same atanh-series method as RL179.
def ln_bounds_int(x, N=80):
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
    return lo, lo+tail

# Rigorous exp enclosure for 0 <= x < 1 using a positive Taylor series.
@lru_cache(maxsize=None)
def exp_bounds_pos(x, N=36):
    assert 0 <= x < 1
    term=Fraction(1)
    s=term
    for k in range(1,N+1):
        term = term*x/k
        s += term
    nxt=term*x/Fraction(N+1)
    # After the first omitted term, successive ratios are <= x/(N+2).
    tail=nxt/(1-x/Fraction(N+2))
    return s, s+tail

def exp_interval(lo,hi):
    assert 0 <= lo <= hi < 1
    elo,_=exp_bounds_pos(lo)
    _,ehi=exp_bounds_pos(hi)
    return elo,ehi

def exp_neg_interval(lo,hi):
    assert 0 <= lo <= hi < 1
    elo_lo,ehi_lo=exp_bounds_pos(lo)
    elo_hi,ehi_hi=exp_bounds_pos(hi)
    # e^-x decreases with x.
    return Fraction(1,ehi_hi), Fraction(1,elo_lo)

l2_lo,l2_hi=ln_bounds_int(2)
l3_lo,l3_hi=ln_bounds_int(3)
d_lo=A*l2_lo-L*l3_hi
d_hi=A*l2_hi-L*l3_lo
s_lo=p*l3_lo-u0*l2_hi
s_hi=p*l3_hi-u0*l2_lo
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

rho_t_lo=eds_lo/2
rho_t_hi=eds_hi/2
F2_lo=3*(2**37)*lam1_lo
F2_hi=3*(2**37)*lam1_hi
D_lo=rho_t_lo-F2_hi
D_hi=rho_t_hi-F2_lo
assert D_lo>Fraction(0)

# RL178 deficit-to-mechanical-loss splice:
# D/(e^(s+Delta)-1) < R-Q < D/(e^s-1).
W_lo=D_lo/eds1_hi
W_hi=D_hi/es1_lo
assert W_lo>23_493_381_795
assert W_hi<Fraction(28_070_867_755)

# Mechanical residue envelope:
# g_r=2^(-r/L) <= omega_r < e^Delta g_r.
x_lo=l2_lo/L
x_hi=l2_hi/L
q_lo,q_hi=exp_neg_interval(x_lo,x_hi)
G_lo=Fraction(1,2*(1-q_lo))
G_hi=Fraction(1,2*(1-q_hi))
R_lo=G_lo
R_hi=ed_hi*G_hi
Q_lo=R_lo-W_hi
Q_hi=R_hi-W_lo
assert Q_lo>0

m_lo=Q_lo/(3*lam1_hi)
m_hi=Q_hi/(3*lam1_lo)
assert m_lo>2**74
assert m_hi<3*(2**73)

# Upper support bound. With N positive heights, W >= half the sum of the N
# smallest mechanical weights.  The base g_r is decreasing and omega_r>=g_r.
N_upper_forbidden=88_981_261_497
ylo=Fraction(L-N_upper_forbidden,L)*l2_lo
yhi=Fraction(L-N_upper_forbidden,L)*l2_hi
ey_lo,ey_hi=exp_neg_interval(ylo,yhi)
# sum_{r=L-N}^{L-1} 2^(-r/L) = (2^(-(L-N)/L)-1/2)/(1-2^(-1/L)).
lastN_lo=(ey_lo-Fraction(1,2))/(1-q_lo)
assert lastN_lo/2 > W_hi
SUPPORT_UPPER=N_upper_forbidden-1
assert SUPPORT_UPPER==88_981_261_496

# Lower support bound. Split residue gaps into the two exact p-shift species.
# kth large-gap coefficient <= C_L exp(-k a_L),
# kth small-gap coefficient <= C_S exp(-(k-1) a_S).
# For the claimed N-1, maximize the sum of these two decreasing geometric
# majorants.  The discrete maximum is certified by adjacent marginal signs.
SUPPORT_LOWER=26_724_850_253
N=SUPPORT_LOWER-1
aL_lo=Fraction(L,p)*s_lo+d_lo
aL_hi=Fraction(L,p)*s_hi+d_hi
aS_lo=Fraction(L,t)*s_lo+Fraction(p,t)*d_lo
aS_hi=Fraction(L,t)*s_hi+Fraction(p,t)*d_hi
CL_lo=eds1_lo
CL_hi=eds1_hi
CS_lo=ed_lo*es1_lo
CS_hi=ed_hi*es1_hi
n0=21_532_148_254
assert 0<n0<N

def eneg_at(xlo,xhi):
    return exp_neg_interval(xlo,xhi)

def large_term_bounds(k):
    lo,hi=eneg_at(k*aL_lo,k*aL_hi)
    return CL_lo*lo, CL_hi*hi

def small_term_bounds(k):
    # small sequence starts at exponent (k-1)aS
    lo,hi=eneg_at((k-1)*aS_lo,(k-1)*aS_hi)
    return CS_lo*lo, CS_hi*hi

# F(n+1)-F(n)=L_(n+1)-S_(N-n).
Ll,Lu=large_term_bounds(n0)
Sl,Su=small_term_bounds(N-(n0-1))
assert Ll>Su
Ll,Lu=large_term_bounds(n0+1)
Sl,Su=small_term_bounds(N-n0)
assert Lu<Sl

# Upper sums at the maximizing n0, using the fixed safe upper geometric
# sequences CL_hi*exp(-k*aL_lo), CS_hi*exp(-(k-1)*aS_lo).
def large_sum_upper(n):
    ql,qh=eneg_at(aL_lo,aL_lo)
    qnl,qnh=eneg_at((n+1)*aL_lo,(n+1)*aL_lo)
    # sum k=1..n q^k = (q-q^(n+1))/(1-q)
    return CL_hi*(qh-qnl)/(1-qh)

def small_sum_upper(n):
    ql,qh=eneg_at(aS_lo,aS_lo)
    qnl,qnh=eneg_at(n*aS_lo,n*aS_lo)
    # sum k=1..n q^(k-1)=(1-q^n)/(1-q)
    return CS_hi*(1-qnl)/(1-qh)

cap=large_sum_upper(n0)+small_sum_upper(N-n0)
assert cap<D_lo

# Internal shallow populations. If only n phases have h<=k, the q-mass is at
# most R/M plus (1-1/M) times the n largest mechanical weights.
SHALLOW={
    1:73_801_609_945,
    2:81_605_820_006,
    3:84_804_722_294,
    4:86_264_134_824,
}

def first_base_sum_upper(n):
    # sum r=0..n-1 exp(-r*x), x>=x_lo.
    qnl,qnh=eneg_at(n*x_lo,n*x_lo)
    return (1-qnl)/(1-q_hi)

for k,needed in SHALLOW.items():
    n=needed-1
    M=2**(k+1)
    top_rho_hi=ed_hi*first_base_sum_upper(n)
    capq=R_hi/Fraction(M)+Fraction(M-1,M)*top_rho_hi
    assert capq<Q_lo

print('PASS: RL180 rigorous global height certificate')
print('support_lower=',SUPPORT_LOWER)
print('support_upper=',SUPPORT_UPPER)
print('zero_height_lower=',L-SUPPORT_UPPER)
print('m_floor_gt_2^74=PASS')
print('m_ceiling_lt_3*2^73=PASS')
for k,n in SHALLOW.items():
    print(f'h_le_{k}_lower={n}')
