#!/usr/bin/env python3
from fractions import Fraction
from pathlib import Path
import re, sys

DELTA0 = 13_201_833_154_443_526_323
C = 42_150_931_628
LOGM_UP = Fraction(42_150_931_628_751_333, 1_000_000)
K0 = 2_921_384_819
K1 = K0 + 2
EXPECTED_Q0 = 123_139_091_657_887_804_990
EXPECTED_Q1 = 123_139_091_657_887_804_843
EXPECTED_B0 = 2_921_384_817
EXPECTED_FIXED_B0_LAST = 3_527_154_083
EXPECTED_FIXED_B1_LAST = 3_116_403_917


def ceil_frac(x: Fraction) -> int:
    return -(-x.numerator // x.denominator)

def log_interval_int(x: int, terms: int = 260):
    y = Fraction(x - 1, x + 1)
    y2 = y * y
    s = Fraction(0)
    yp = y
    for n in range(terms):
        s += yp / (2 * n + 1)
        yp *= y2
    lo = 2 * s
    tail = 2 * yp / ((2 * terms + 1) * (1 - y2))
    return lo, lo + tail

l2,u2=log_interval_int(2)
l3,u3=log_interval_int(3)
beta_hi=u3/l2
gamma=2*beta_hi-3
assert gamma>0

def q_lower(k:int)->int:
    num=(beta_hi*(DELTA0-2*k+4)-3*LOGM_UP-(4*beta_hi+3)*(k-1))
    return ceil_frac(num/gamma)

# Incoming RL88 arithmetic reproduction.
q0=q_lower(K0)
q1=q_lower(K1)
assert q0==EXPECTED_Q0
assert q1==EXPECTED_Q1
B0=(q0+C-1)//C
assert B0==EXPECTED_B0
assert (q1+C-1)//C==B0

# Exact excursion grammar spot audit. Height is pre-column d, area is sum(d-1).
COLS=((0,0),(0,1),(1,0),(1,1))
from itertools import product
small=[]
for L in range(2,9):
    for w in product(COLS, repeat=L):
        if w[0]!=(0,1) or w[-1]!=(1,0):
            continue
        h=1; area=0; tens=0; valid=True
        for j,(x,y) in enumerate(w):
            area += h-1
            tens += (x,y)==(1,0)
            h += y-x
            if j<L-1 and h<=1:
                valid=False; break
        if valid and h==1:
            excess=area-tens
            if excess<=1:
                small.append((excess,w))
expected={
    (0,((0,1),(1,0))),
    (1,((0,1),(0,0),(1,0))),
    (1,((0,1),(1,1),(1,0))),
}
assert set(small)==expected

# Parse exact C discrete-log scan.
scan_path=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name('RL89_DLOG64_SCAN.txt')
text=scan_path.read_text()
mc=re.search(r'candidate_count=(\d+)',text)
assert mc and int(mc.group(1))==2
pairs=[]
for m,a in re.findall(r'candidate m=(-?\d+) a=(\d+)',text):
    pairs.append((int(m),int(a)))
assert pairs==[(101_319_985,27_039_197_284),(303_959_955,27_039_197_283)]
# Both are the same product after one factor of 3 and have exact 2-adic valuation 65.
for m,a in pairs:
    assert (pow(3,a,1<<65)*m-1)%(1<<65)==0
    assert (pow(3,a,1<<66)*m-1)%(1<<66)!=0
assert pairs[1][0]==3*pairs[0][0] and pairs[1][1]+1==pairs[0][1]

# Therefore all signed odd 0<|m|<2^29 and 1<=a<=C+1 have v2(3^a m-1)<=65,
# and any minimal reset from a block of deficit <=28 has next length <=63.
SHORT=63
DTH=28
BAD=DTH+1

def stats(k,b):
    q=q_lower(k)
    D=C*b-q
    assert D>=0
    good=max(0,b-D//BAD)
    short_cap=D//(C-SHORT)
    exceptions=(k-1)-b
    margin=good-exceptions-short_cap
    return D,good,short_cap,exceptions,margin

# Endpoint: b is between B0 and k0-1, i.e. exactly two cases, both impossible.
s0=stats(K0,B0)
s1=stats(K0,B0+1)
assert s0==(22_556_487_086,2_143_574_918,0,1,2_143_574_917)
assert s1==(64_707_418_714,690_094_518,1,0,690_094_517)
assert s0[-1]>0 and s1[-1]>0

# Next odd: the two low-b cases are also impossible; survivor must have b>=k-2.
t0=stats(K1,B0)
t1=stats(K1,B0+1)
assert t0==(22_556_487_233,2_143_574_913,0,3,2_143_574_910)
assert t1==(64_707_418_861,690_094_513,1,2,690_094_510)
assert t0[-1]>0 and t1[-1]>0
assert B0+2==K1-2

# General fixed-b exclusion intervals from the same necessary inequality.
def margin(k,b):
    return stats(k,b)[-1]

def first_nonexcluded(b,lo=K0,hi=42_150_931_559):
    while lo<hi:
        mid=(lo+hi)//2
        if margin(mid,b)>0:
            lo=mid+1
        else:
            hi=mid
    return lo
f0=first_nonexcluded(B0)
f1=first_nonexcluded(B0+1)
assert f0-1==EXPECTED_FIXED_B0_LAST
assert f1-1==EXPECTED_FIXED_B1_LAST
assert margin(f0-1,B0)>0 and margin(f0,B0)<=0
assert margin(f1-1,B0+1)>0 and margin(f1,B0+1)<=0

print('RL89 near-capacity verifier: PASS')
print('q_lower(k0) =',q0)
print('q_lower(k0+2) =',q1)
print('minimum block count B0 =',B0)
print('dlog64 candidates below 2^29 =',pairs)
print('certified minimal-reset implication: deficit <=28 => next block length <=63')
print('k0 b=B0 margin =',s0[-1])
print('k0 b=B0+1 margin =',s1[-1])
print('k0 eliminated; next odd lower endpoint >=',K1)
print('at next odd, b >=',K1-2,'= k-2')
print('fixed b=B0 excluded through k =',f0-1)
print('fixed b=B0+1 excluded through k =',f1-1)
