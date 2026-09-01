#!/usr/bin/env python3
from fractions import Fraction
import json
from pathlib import Path

root=Path(__file__).resolve().parents[1]
c=json.loads((root/'certificates/rl229_h21_rank_blind_charge_barrier.json').read_text())

DLO=23_369_453_298
DHI=41_775_866_136
R16=34_124_151_203
R4=31_435_476_727
assert DHI-DLO+1==18_406_412_839
assert DLO<=R16<=DHI and DLO<=R4<=DHI
assert c['current_rank_checks']['e16_excluded'] is True
assert c['current_rank_checks']['e4_excluded'] is False
assert c['current_rank_checks']['e4_combined_arithmetic_survivors_through_transition_43']==3_856_660_232

CLEAN=10_075_174_499
N35=9_168_536_354
N36=7_238_318_174
a=CLEAN-N35
b=N35-N36
assert a==906_638_145
assert b==1_930_218_180
assert 2*b-a==2_953_798_215>0

C=Fraction(1,2**22)
flat=Fraction(1,3*(2**22))
assert flat==C/3
assert 2*flat+flat==C
assert a-2*b<0

# On active y=C-2x, x>=y is x>=C/3. Since slope a-2b is negative,
# objective a*x+b*y is maximized at x=C/3, hence y=C/3.
x=C/3
y=C-2*x
assert x==y==flat

# Exact duplicate-constraint lemma: the rank coordinate is absent.
# Any positive number of identical rows gives the same max LHS / feasible test.
def h21_ok(x,y,n_rows):
    if n_rows<=0:
        return True
    return 2*x+y<=C
for n in (1,2,14,1_000_000):
    assert h21_ok(flat,flat,n)
    assert not h21_ok(flat+Fraction(1,2**30),flat,n)
assert h21_ok(flat+Fraction(1,2**30),flat,0)

assert c['physical_incidence_inherited']['clean_40_edge_corridors_min']==CLEAN
assert c['physical_incidence_inherited']['distinct_nonzero_defect_phases_min']==251_879_363
assert c['physical_incidence_inherited']['forces_h21_height21'] is False
assert c['barrier']['isolated_rank_deletion_relaxes_current_charge_polytope'] is False

print('RL229 H21 RANK-BLIND CHARGE / PHYSICAL-INCIDENCE BARRIER: PASS')
print('dangerous_H21_rank_core',DLO,DHI,'size',DHI-DLO+1)
print('e16_deleted_inside_core',R16,'e4_live_inside_core',R4)
print('two_level_populations',a,b,'2b-a',2*b-a)
print('charge_optimum x=y=1/(3*2^22); rank_rows_duplicate')
print('isolated_rank_deletion_charge_relaxation=0 while dangerous support nonempty')
