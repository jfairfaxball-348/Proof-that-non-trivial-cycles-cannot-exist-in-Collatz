#!/usr/bin/env python3
"""Exact/rational verifier for RL135 multiplicity defect and state ceilings."""
from fractions import Fraction
from math import gcd, isqrt

A = 217_976_794_617
L = 137_528_045_312
R0 = 1 << 71
BASE_HEAD = "528465486fa9bd6d09bf0df08dc2d269ff71cc29"

CF_EXPECTED = [1,1,1,2,2,3,1,5,2,23,2,2,1,1,55,1,4,3,1,1,15,1,9,2,5,7,1,1,4,8]
U = (103_768_467_013, 65_470_613_321)      # det -1
V = (10_439_860_591, 6_586_818_670)        # det +2
W = (114_208_327_604, 72_057_431_991)      # det +1
VM2 = (207_536_934_026, 130_941_226_642)   # det -2

GSTAR = 771_316_334_039
G75 = 28_000_000_000

EXPECTED_GENERIC = {
    2:(0,352_686_524,6_741_665_312),
    3:(0,529_029_786,10_112_497_968),
    4:(0,705_373_047,13_483_330_624),
    5:(0,881_716_309,16_854_163_279),
    6:(0,1_058_059_571,20_224_995_935),
    7:(1,1_234_402_831,23_595_828_590),
    8:(2,1_410_746_092,26_966_661_245),
    9:(3,1_587_089_353,30_337_493_899),
    10:(4,1_763_432_613,33_708_326_554),
    11:(5,1_939_775_874,37_079_159_209),
    12:(7,2_116_119_133,40_449_991_862),
    13:(9,2_292_462_393,43_820_824_516),
    14:(11,2_468_805_653,47_191_657_170),
    15:(13,2_645_148_912,50_562_489_823),
    16:(15,2_821_492_172,53_933_322_477),
}

def ln_interval(x: Fraction, N=260):
    """atanh-series enclosure: log((1+x)/(1-x))."""
    x2 = x*x
    term = x
    s = Fraction(0)
    for k in range(N):
        s += term/(2*k+1)
        term *= x2
    lo = 2*s
    tail = 2*term/(2*N+1)/(1-x2)
    return lo, lo + tail

def cf_interval(lo: Fraction, hi: Fraction, terms=30):
    out=[]
    for _ in range(terms):
        a0=lo.numerator//lo.denominator
        a1=hi.numerator//hi.denominator
        assert a0==a1
        out.append(a0)
        lo-=a0; hi-=a0
        assert lo>0
        lo,hi=1/hi,1/lo
    return out

ln2_lo, ln2_hi = ln_interval(Fraction(1,3))
ln3_lo, ln3_hi = ln_interval(Fraction(1,2))
beta_lo = ln3_lo/ln2_hi
beta_hi = ln3_hi/ln2_lo
assert cf_interval(beta_lo,beta_hi) == CF_EXPECTED

# CF neighborhood and determinant bases.
pm2,pm1=0,1
qm2,qm1=1,0
conv=[]
for a in CF_EXPECTED:
    p=a*pm1+pm2
    q=a*qm1+qm2
    conv.append((p,q))
    pm2,pm1=pm1,p
    qm2,qm1=qm1,q
assert conv[21] == V
assert conv[22] == U
assert conv[23] == (A,L)
assert W == (U[0]+V[0], U[1]+V[1])
assert VM2 == (2*U[0], 2*U[1])
assert gcd(A,L)==1
assert U[0]*L-U[1]*A == -1
assert W[0]*L-W[1]*A == 1
assert V[0]*L-V[1]*A == 2
assert VM2[0]*L-VM2[1]*A == -2

# Rigorous discrepancy / theta.
delta_lo = A*ln2_lo - L*ln3_hi
delta_hi = A*ln2_hi - L*ln3_lo
assert delta_lo > 0
theta_lo = L*delta_lo/ln2_hi
theta_hi = L*delta_hi/ln2_lo
assert 5*theta_hi < 1
assert 11*theta_hi < 2 < 12*theta_lo
assert 16*theta_hi < 3 < 17*theta_lo

# RL135.1 one-defect endpoint.
assert GSTAR*delta_hi < ln2_lo
assert (GSTAR+1)*delta_hi >= ln2_lo

# Inherited one-period rho envelope from RL134.
x_lo = ln2_lo/L
x_hi = ln2_hi/L
exp1_up = 1/(1-delta_hi)
den_lo = x_lo-x_lo*x_lo/2
geom_up = 1/(2*den_lo)
rho_sum_up = 1 + exp1_up*(geom_up-1)
rho_sum_ceil = (rho_sum_up.numerator+rho_sum_up.denominator-1)//rho_sum_up.denominator
assert rho_sum_ceil == 99_205_514_478
m_rl134_up = rho_sum_up/(3*delta_lo)
assert m_rl134_up < (1<<75)

# RL135.3 broad m<2^76.
m76_envelope = Fraction(2*L*L,3)/theta_lo
assert m76_envelope < (1<<76)

def exp_g_up(g):
    assert g*delta_hi < 1
    return 1/(1-g*delta_hi)

def refined_m_up(g):
    # Baseline one-period cancellation plus worst h=-1 shell excess.
    return m_rl134_up + Fraction(g)*theta_hi*exp_g_up(g)/(6*delta_lo)

assert refined_m_up(G75) < (1<<75)
# Method threshold only: the same coarse envelope does not certify 29b.
assert refined_m_up(29_000_000_000) >= (1<<75)

# Canonical-contact gap at g<=6.
gap_up = 5*delta_hi/(1-5*delta_hi)*(1<<75)
gap_ceil = (gap_up.numerator+gap_up.denominator-1)//gap_up.denominator
assert gap_ceil == 169_751_105_674

# Determinant +/-2 discrepancy windows.
def discrepancy_interval(pair):
    s,t=pair
    return s*ln2_lo-t*ln3_hi, s*ln2_hi-t*ln3_lo

v_lo,v_hi = discrepancy_interval(V)
vm_lo,vm_hi = discrepancy_interval(VM2)
assert v_lo > 11*delta_hi
assert v_hi < 12*delta_lo
assert vm_lo > -11*delta_hi
assert vm_hi < -10*delta_lo

# Check RL134 translate parametrization.
qinv = U[1]
assert (qinv*A) % L == 1
def base_for_det(r):
    jr=(-r*qinv) % L
    num=jr*A+r
    assert num%L==0
    sr=num//L
    assert sr*L-jr*A==r
    return sr,jr
assert base_for_det(-2)==VM2
assert base_for_det(-1)==U
assert base_for_det(1)==W
assert base_for_det(2)==V

def p_exc(g):
    if g<=6:
        return 0
    if g<=11:
        return g-6
    if g<=16:
        return 2*g-17
    raise ValueError

def geom_blocks_up(g):
    # e^(t Delta) <= 1/(1-t Delta_hi)
    return sum((1/(1-t*delta_hi) for t in range(g)), Fraction(0))

def generic_shallow_floor(g,k):
    M=1<<(k+1)
    E=exp_g_up(g)
    totalrho=rho_sum_up*geom_blocks_up(g)
    lower=3*R0*g*delta_lo
    rem=lower-totalrho/Fraction(M)-p_exc(g)*E
    assert rem>0
    denom=Fraction(M-1,M)*E
    x=rem/denom
    return (x.numerator+x.denominator-1)//x.denominator

for g,(p,n3,n4) in EXPECTED_GENERIC.items():
    assert p_exc(g)==p
    assert generic_shallow_floor(g,3)==n3
    assert generic_shallow_floor(g,4)==n4

# Retain the stronger RL134 g=1 exact top-rho optimization.
def top_rho_upper(N):
    if N==0:
        return Fraction(0)
    if N==1:
        return Fraction(1)
    n=N-1
    y=n*x_hi
    assert y<1
    num_up=y-y*y/2+y*y*y/6
    return Fraction(1)+exp1_up*(num_up/den_lo)

def rl134_shallow_min(k):
    M=1<<(k+1)
    lower=3*R0*delta_lo
    lo,hi=0,L
    while lo<hi:
        mid=(lo+hi)//2
        cap=rho_sum_up/Fraction(M)+Fraction(M-1,M)*top_rho_upper(mid)
        if cap>=lower:
            hi=mid
        else:
            lo=mid+1
    return lo
assert rl134_shallow_min(3)==176_421_674
assert rl134_shallow_min(4)==3_399_794_205

# Absolute physical windows through g=16.
for g in range(1,17):
    E=exp_g_up(g)
    m_up=refined_m_up(g)
    assert 16*E*m_up < (1<<79)
    assert 32*E*m_up < (1<<80)

print("RL135 multiplicity-defect verifier: PASS")
print(f"base_head={BASE_HEAD}")
print(f"survivor_A={A} survivor_L={L} gcd={gcd(A,L)}")
print(f"one_defect_endpoint_g={GSTAR}")
print(f"m_lt_2^75_through_g={G75}")
print(f"m_lt_2^76_through_g={GSTAR}")
print("nonnegative_defect_g_le_6=PASS")
print("det_pm2_windows=11Delta<d+2<12Delta and -11Delta<d-2<-10Delta")
print("det_shell_stop=16theta<3<17theta")
print(f"canonical_contact_gap_upper={gap_ceil}")
print("conditional_population_table_g_1_to_16=PASS")
print("absolute_state_windows_g_1_to_16=PASS")
print("scope=no multiplicity exclusion; no frontier advance; Gate A/B open; Collatz not proved")
