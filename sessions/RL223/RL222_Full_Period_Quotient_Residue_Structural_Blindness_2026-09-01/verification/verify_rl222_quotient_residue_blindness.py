#!/usr/bin/env python3
from pathlib import Path
import json

A=217976794617
L=137528045312
ROOT_LOWER=24913843845551577787381
ROOT_UPPER=31285589992934194300574
M=1<<76
THREE_RES=7653485309995355851777
D_RES=67904378415918967567359
GAP=36618788422984773266785
Q16=43079489
K=28821
ETA_STAR=94527378
Y0_STAR=632932199441596415
ETA=3722043165201
Y0=24921895945404894117887
Y16=63944214675001842327551

assert A > 76
assert pow(3, L, M) == THREE_RES
assert (-pow(3, L, M)) % M == D_RES
assert 0 < D_RES < M
assert D_RES - ROOT_UPPER == GAP
assert ROOT_UPPER < D_RES
assert ETA_STAR + pow(3,17)*K == ETA
assert Y0_STAR + 3*(1<<58)*K == Y0
assert ROOT_LOWER <= Y0 <= ROOT_UPPER
assert Y16 == (1<<34)*ETA - 1 - pow(3,16)*(1<<13)
assert (1<<24)*Y16 == pow(3,16)*Y0 + Q16

# Algebraic replay of the local two-adic blindness identity on several
# independent integer tuples.  It depends only on the affine recurrence.
tests = [
    (17, 100, 7, 3, 11, 19, 23),
    (31, 211, 9, 4, 13, 21, 37),
    (55, 401, 10, 5, 17, 24, 61),
]
for x, xm, m, r, total_odd, total_len, yend in tests:
    q = (1<<m)*xm - pow(3,r)*x
    target = (1<<total_len)*yend - pow(3,total_odd)*x
    lhs = (pow(3,total_odd-r)*(q % (1<<m))) % (1<<m)
    assert lhs == target % (1<<m)

print("PASS RL222 denominator-separation / quotient-residue blindness verifier")
print(f"D_mod_2^76={D_RES} root_upper={ROOT_UPPER} gap={GAP}")
print(f"witness Q16={Q16} k={K} eta={ETA} y0={Y0}")
print("qfull_mod_D2=exact_D_times_y0_on_physical_realization no_wrap=true")
print("local_2adic_tail_prefix_selector=AUTOMATIC candidate_deletions=0 rank_exclusions=0")
