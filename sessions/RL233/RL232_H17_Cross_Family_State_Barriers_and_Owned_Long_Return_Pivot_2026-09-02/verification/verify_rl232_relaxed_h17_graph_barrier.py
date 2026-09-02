#!/usr/bin/env python3
from fractions import Fraction
from functools import lru_cache

A=217_976_794_617
L=137_528_045_312
B=A-L
p=65_470_613_321
u=103_768_467_013

K_LO=128_081_997_553
K_HI=146_795_909_391

# H17-B: offsets {27,...,33}
H=17
TAU=33
T=27_795_302_832_777_615       # 5*3^33
TERMINAL=Fraction(T, 2**H)
START=171_798_691_840           # 5*2^35
CORE_LO=72_797_034_370
CORE_HI=103_818_202_602

# Concrete relaxed self-return.
SEP=190_537
N=SEP-TAU
REM=(N*A) % L
Q=(N*A)//L
S=Q+1
SHIFT=(SEP*B) % L

assert N == 190_504
assert REM == 95_752_166_376
assert Q == 301_941
assert S == 301_942
assert L-REM == 41_775_878_936
assert CORE_LO > L-REM                 # exponent-sum branch e=1 throughout H17-B core
assert SHIFT == L-12_799               # terminal rank maps r -> r-12,799

# For H17-B, zero-prefix propagation gives:
#   TERMINAL = START * 3^33 / 2^52.
# Hence for this return
#   centre/START = exp(-x),
#   x=(12,799 ln2 + SEP*delta)/L,
# where delta=A ln2-L ln3 and inherited RL192 has 0<delta<2^-40.
#
# Using ln2<1 and SEP<2^18:
#   x < 12,800/L,
# so START-centre < START*12,800/L < 16,000.
assert SEP < 2**18
assert 4*START < 5*L                    # equivalent to START*12,800/L < 16,000
MISS_UPPER=16_000

# Uniform lower bound for the RL191 universal relaxed ball.
# For any suffix of m<=L mechanical transitions, its exponent sum C_m obeys
# C_m <= ceil(mA/L). With delta<2^-40<1/4,
# exp(delta)<1/(1-delta)<4/3, hence
# 2^C_m < (8/3) 3^m.
# Each |epsilon|<2 coordinate therefore contributes radius >1/4.
# Thus total radius > N/4.
RADIUS_LOWER=Fraction(N,4)
assert RADIUS_LOWER == 47_626
assert RADIUS_LOWER > MISS_UPPER

# Therefore the target START lies inside the positive side of the relaxed ball.
# Because the centre is below START, the correction may be chosen with
# 0<=epsilon_i<2, so K is nondecreasing across each relaxed return.

# Build a long chain: q edges fit in less than one base period.
EDGES=L//SEP
EVENTS=EDGES+1
PHASE_SPAN=EDGES*SEP
RANK_DRIFT=EDGES*12_799

assert EDGES == 721_791
assert EVENTS == 721_792
assert PHASE_SPAN == 137_527_891_767 < L
assert RANK_DRIFT == 9_238_203_009

# Choose a corridor-interior starting rank and follow r -> r-12,799.
R0=99_000_000_000
R1=R0-RANK_DRIFT
assert CORE_LO <= R1 < R0 <= CORE_HI
assert R1 == 89_761_796_991

# Exact inherited rho/K endpoint certification using the same rational
# atanh/exponential machinery as RL231.
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
delta_lo=A*l2_lo-L*l3_hi
delta_hi=A*l2_hi-L*l3_lo
small_lo=p*l3_lo-u*l2_hi
small_hi=p*l3_hi-u*l2_lo

assert 0 < delta_lo < delta_hi < Fraction(1,2**40)
assert 0 < small_lo < small_hi < Fraction(1,1000)

def K_bounds(r):
    q=(p*r)//L
    xlo=r*small_lo+q*delta_lo
    xhi=r*small_hi+q*delta_hi
    elo,_=exp_bounds_pos(xlo)
    _,ehi=exp_bounds_pos(xhi)
    return TERMINAL/ehi, TERMINAL/elo

r0_lo,r0_hi=K_bounds(R0)
r1_lo,r1_hi=K_bounds(R1)

assert r0_lo > 128_754_994_844
assert r0_hi < 128_754_994_845
assert r1_lo > 134_891_704_635
assert r1_hi < 134_891_704_637
assert K_LO < r0_lo < r0_hi < K_HI
assert K_LO < r1_lo < r1_hi < K_HI

# With nonnegative relaxed epsilons, K is nondecreasing on every return.
# Event ranks decrease monotonically, so terminal K endpoints increase
# monotonically from the certified R0 value to the certified R1 value.
# Hence the entire constructed relaxed chain can remain inside the K corridor.
assert EVENTS > 1_615

print("PASS: RL232 relaxed H17-B graph barrier")
print("H17_B_relaxed_return_separation=190537")
print("rank_shift_per_return=-12799")
print("zero_error_target_miss_lt=16000")
print("universal_relaxed_radius_gt=47626")
print("relaxed_events_within_one_period=721792")
print("phase_span=137527891767")
print("rank_start=99000000000")
print("rank_end=89761796991")
print("endpoint_K_start_between=128754994844,128754994845")
print("endpoint_K_end_between=134891704635,134891704637")
print("required_physical_H17_incidence_cap=1615")
print("classification=METHOD_BARRIER")
