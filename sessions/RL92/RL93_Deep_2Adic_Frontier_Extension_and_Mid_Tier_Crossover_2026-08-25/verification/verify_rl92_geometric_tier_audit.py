#!/usr/bin/env python3
from fractions import Fraction
from pathlib import Path
import re
C=42_150_931_628
DW=5_000_030; RW=7_000_000
DD=10_000_032; RD=1_100_000
DU=15_000_046; RU=1_000
LAM=Fraction(RW-RD,(RW+1)*(DW+1))
MU=Fraction(1,RW+1)
# Ultra-deep complement corners after adding the exploratory tier.
corners=[(0,RW+1),(DW+1,RD+1),(DD+1,RU+1),(DU+1,0)]
vals=[LAM*d+MU*r for d,r in corners]
assert vals[0]==1 and vals[1]==1
assert vals[2]>=1 and vals[3]>=1
# Deep depth-axis activation threshold.
thr=Fraction(RW,1)-Fraction((RW+1)*(DW+1),DD+1)
ceil_thr=-(-thr.numerator//thr.denominator)
assert ceil_thr==3_499_990
# Exact exploratory raw certificate.
raw=(Path(__file__).parent/'raw'/'ultra_probe_15000056_0_1000.txt').read_text().strip()
assert raw=='N=15000056 chunk=0..1000 min_bits=15000048 at_r=88'
# Local consequence from bit length B: d<=B-2; successor<=N-3.
assert 15_000_048-2==DU
assert 15_000_056-3==15_000_053
print('RL92 geometric tier audit: PASS')
print('current deep-axis support value =',LAM*(DD+1))
print('ultra tier remains non-load-bearing in the current one-line cover')
print('deep-frontier activation threshold >=',ceil_thr)
