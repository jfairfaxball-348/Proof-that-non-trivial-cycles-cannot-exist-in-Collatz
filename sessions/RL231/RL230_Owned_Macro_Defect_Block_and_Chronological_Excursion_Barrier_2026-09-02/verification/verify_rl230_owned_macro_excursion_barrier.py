#!/usr/bin/env python3
from fractions import Fraction
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
c=json.loads((ROOT/'certificates/rl230_owned_macro_excursion_barrier.json').read_text())

L=137_528_045_312
E={1:10_075_174_578,2:25_683_594_700,3:32_081_399_276,4:35_000_224_336}
expected_clean={1:10_075_174_499,2:25_683_594_619,3:32_081_399_193,4:35_000_224_251}
expected_distinct={1:251_879_363,2:626_429_138,3:763_842_838,4:813_958_704}

assert c['L']==L
assert c['normalized_gap_upper'] < 2**39

for k in range(1,5):
    n=k+38
    clean=E[k]-1-2*n
    distinct=(clean+(n+1)-1)//(n+1)
    assert clean==expected_clean[k]
    assert distinct==expected_distinct[k]
    assert c['n_by_k'][str(k)]==n
    assert c['clean_corridor_floors'][str(k)]==clean
    assert c['distinct_nonzero_defect_floors'][str(k)]==distinct

Klo=128_081_997_553
Khi=146_795_909_391
width=Khi-Klo
assert width==18_713_911_838
flow=3*width
assert flow==56_141_735_514
need=flow+1
assert need==56_141_735_515

N=(L+need+1)//2
assert N==96_834_890_414
assert 2*N-L >= need
assert 2*(N-1)-L < need
M=L-N
assert M==40_693_154_898

# Exact location and weight inequalities used by the method barrier.
assert 10*N > 7*L
assert 128*5**10 > 8**10   # equivalent to 2^(7/10) > 8/5
W=28_070_867_755
assert 5*M < 8*W

assert c['K_width']==width
assert c['arbitrary_boundary_flow_width']==flow
assert c['minimum_nearly_unit_same_sign_defects']==need
assert c['required_shallow_population_optimistic']==N
assert c['remaining_high_population']==M
assert c['W_upper']==W
assert c['five_eighths_high_mass_numerator']==5*M
assert c['eight_W_upper']==8*W
assert c['status']=='PASS'

print('RL230 OWNED MACRO / EXCURSION BARRIER: PASS')
print('clean corridors k1..k4:', *(expected_clean[k] for k in range(1,5)))
print('distinct nonzero defects k1..k4:', *(expected_distinct[k] for k in range(1,5)))
print('K width:', width)
print('arbitrary-boundary corrected-flow threshold: >', flow)
print('minimum nearly-unit same-sign defects:', need)
print('optimistic required shallow population:', N)
print('remaining high phases at that population:', M)
print('5M < 8W:', 5*M, '<', 8*W)
