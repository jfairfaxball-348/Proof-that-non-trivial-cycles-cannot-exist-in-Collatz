#!/usr/bin/env python3
from fractions import Fraction
from pathlib import Path

DELTA0 = 13_201_833_154_443_526_323
C = 42_150_931_628
LOGM_UP = Fraction(42_150_931_628_751_333, 1_000_000)
SSTAR_EXPECTED = 26_594_276_905
K0 = 2_921_406_841
LAST = 2_921_630_973
NEXT = LAST + 2
EXPECTED_COUNT = 112_067
EXPECTED_LAST_MARGIN = 586
EXPECTED_NEXT_MARGIN = -23_150

D_WIDE=5_000_030
R_WIDE=7_000_000
L_WIDE=5_000_053
D_DEEP=10_000_035
R_DEEP=300_000
L_DEEP=10_000_053
# Conservative common short-successor ceiling for every block in the union.
SHORT=L_DEEP

# Supporting line through the integer uncovered corner
# (D_WIDE+1,R_DEEP+1) and the r-axis corner (0,R_WIDE+1).
MU=Fraction(1,R_WIDE+1)
LAM=Fraction(R_WIDE-R_DEEP,(R_WIDE+1)*(D_WIDE+1))

def ceil_frac(x: Fraction) -> int:
    return -(-x.numerator // x.denominator)

def log_interval_int(x: int, terms: int = 260):
    y=Fraction(x-1,x+1); y2=y*y; s=Fraction(0); yp=y
    for n in range(terms):
        s += yp/(2*n+1); yp *= y2
    lo=2*s
    tail=2*yp/((2*terms+1)*(1-y2))
    return lo,lo+tail

l2,u2=log_interval_int(2); l3,u3=log_interval_int(3)
beta_lo=l3/u2; beta_hi=u3/l2
gamma=2*beta_hi-3
assert gamma>0
SSTAR=(LOGM_UP.numerator*beta_lo.denominator)//(LOGM_UP.denominator*beta_lo.numerator)
assert SSTAR==SSTAR_EXPECTED

def q_lower(k:int)->int:
    num=beta_hi*(DELTA0-2*k+4)-3*LOGM_UP-(4*beta_hi+3)*(k-1)
    return ceil_frac(num/gamma)

def rsum_upper(k:int,b:int,q:int)->int:
    U=Fraction(k-1,1)+b*SSTAR+(LOGM_UP+b-q)/beta_hi
    return ceil_frac(U)-1

def top_margin(k:int):
    b=k-1; q=q_lower(k); D=C*b-q; Ru=rsum_upper(k,b,q)
    weighted=LAM*D+MU*Ru
    bad=weighted.numerator//weighted.denominator
    good=b-bad
    short_cap=D//(C-SHORT)
    margin=good-short_cap
    return q,D,Ru,bad,good,short_cap,margin

# Staircase complement proof: every block outside
# U={(d<=D_DEEP,r<=R_DEEP) or (d<=D_WIDE,r<=R_WIDE)}
# has LAM*d+MU*r>=1.  It suffices to check the integer corners.
assert LAM*(D_WIDE+1)+MU*(R_DEEP+1)==1
assert LAM*(D_DEEP+1)>=1
assert MU*(R_WIDE+1)==1

# Top-stratum monotonicity.  For fixed k, D rises by exactly C when b rises by one;
# R^max is nondecreasing.  Hence the weighted bad-block floor rises by at least
# floor(LAM*C)=8068, while the explicit 2b contribution rises only by 2 and the
# short-successor capacity is nondecreasing.
assert (LAM*C).numerator//(LAM*C).denominator==8068
assert 2-8068<0

cert=Path(__file__).with_name("RL91_MULTISCALE_2ADIC_SCAN.txt").read_text()
for s in [
    "r_range=0..7000000",
    "global_min_balanced_bitlen=5000032 at_r=2595446",
    "consequence: d<=5000030 and r<=7000000 under minimal reset => n_next<=5000053",
    "r_range=0..300000",
    "global_min_balanced_bitlen=10000037 at_r=33524",
    "consequence: d<=10000035 and r<=300000 under minimal reset => n_next<=10000053",
    "RL91 multiscale scan certificate: PASS",
]: assert s in cert,s

count=0; worst=None; worst_k=None
for k in range(K0,LAST+1,2):
    st=top_margin(k); assert st[-1]>0,(k,st)
    count+=1
    if worst is None or st[-1]<worst: worst=st[-1]; worst_k=k
assert count==EXPECTED_COUNT
assert worst_k==LAST and worst==EXPECTED_LAST_MARGIN
nxt=top_margin(NEXT)
assert nxt[-1]==EXPECTED_NEXT_MARGIN and nxt[-1]<=0

assert top_margin(LAST)==(
    123_139_091_657_869_683_283,
    10_375_685_149_499_133,
    6_546_360_238_723_941,
    2_921_384_173,
    246_799,
    246_213,
    586,
)
assert top_margin(NEXT)==(
    123_139_091_657_869_683_136,
    10_375_769_451_362_536,
    6_546_413_427_277_847,
    2_921_407_909,
    223_065,
    246_215,
    -23_150,
)

print("RL91 multiscale interval verifier: PASS")
print("SSTAR =",SSTAR)
print("wide tier: d<=5000030, r<=7000000 => next<=5000053")
print("deep tier: d<=10000035, r<=300000 => next<=10000053")
print("supporting weights lambda =",LAM,"mu =",MU)
print("b-monotonic weighted decrement floor =",(LAM*C).numerator//(LAM*C).denominator)
print("odd values eliminated =",count)
print("eliminated odd interval =",K0,"through",LAST)
print("last margin =",worst)
print("next odd =",NEXT,"multiscale margin =",nxt[-1])
print("new surviving odd lower endpoint >=",NEXT)
