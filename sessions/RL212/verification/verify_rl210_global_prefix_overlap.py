#!/usr/bin/env python3
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
A=217_976_794_617
L=137_528_045_312
B=80_448_749_305
p=65_470_613_321
u=103_768_467_013
z=L-p
assert A*p-u*L==1
assert (p*B)%L==1

def b(i): return (A*i)//L

# Exact no-carry boundary and first-divergence index bounds.
assert z==72_057_431_991
assert ((z*B)%L)==L-1
for t in [0,1,2,23,24,37,55,56,10**6,z-1]:
    assert b(p+t)==u+b(t)
assert b(23)==36 and b(24)==38 and b(56)==88

# Current small-offset necessary frontier. RL208/RL209 layer cuts are only inside
# the first/last 2^35 terminal phases; these phases are strictly central.
lo,hi=25_583_192_106,41_775_866_136
isolated={
26_058_127_773,26_058_127_774,28_746_802_249,28_746_802_250,
31_435_476_726,34_124_151_202,36_398_517_184,36_398_517_185,
36_812_825_678,39_087_191_660,39_087_191_661,41_775_866_136}
anchors={26_058_127_775,28_746_802_251,36_398_517_186,39_087_191_662}
small=[]
for e in range(1,56):
    i=p+e+34
    assert (1<<35) < i < L-(1<<35)
    r=(i*B)%L
    if lo<=r<=hi and r not in isolated and r not in anchors:
        small.append({'e':e,'terminal_phase':i,'terminal_rank':r,'n_e':b(e)-1})
expected=[
 {'e':4,'terminal_phase':65_470_613_359,'terminal_rank':31_435_476_727,'n_e':5},
 {'e':16,'terminal_phase':65_470_613_371,'terminal_rank':34_124_151_203,'n_e':24},
 {'e':28,'terminal_phase':65_470_613_383,'terminal_rank':36_812_825_679,'n_e':43},
 {'e':33,'terminal_phase':65_470_613_388,'terminal_rank':26_472_436_268,'n_e':51},
 {'e':40,'terminal_phase':65_470_613_395,'terminal_rank':39_501_500_155,'n_e':62},
 {'e':45,'terminal_phase':65_470_613_400,'terminal_rank':29_161_110_744,'n_e':70},
]
assert small==expected
locked=[]
for row in small:
    e,n=row['e'],row['n_e']
    if n<37 and b(e-1)<n:
        locked.append(e)
assert locked==[4,16]

# Exact finite m=24 orientation certificate modulo 2^40. Exponents >=40 are
# collapsed to a sentinel because they contribute zero. We exhaust all strictly
# increasing continuations bounded by b_t.
N=40
MOD=1<<N
target=(-3*(1<<37))%MOD
coeff=[pow(pow(3,t,MOD),-1,MOD) for t in range(N)]

def choices(prev, upper):
    if prev==N:
        # Sentinel means an actual exponent >=N. Since b_t strictly grows on this
        # tiny range, a further strictly larger actual exponent remains feasible.
        return [N]
    out=list(range(prev+1,min(upper,N-1)+1))
    if upper>=N:
        out.append(N)
    return out

def residues_for_orientation(root24,shift24):
    def pow2(x): return 0 if x==N else (1<<x)
    states={(root24,shift24,((pow2(shift24)-pow2(root24))*coeff[24])%MOD)}
    for t in range(25,N):
        nxt=set()
        for xr,xs,res in states:
            for yr in choices(xr,b(t)):
                for ys in choices(xs,b(t)):
                    rr=(res+(pow2(ys)-pow2(yr))*coeff[t])%MOD
                    nxt.add((yr,ys,rr))
        states=nxt
    return sorted({res for _,_,res in states})

root_smaller=residues_for_orientation(37,38)
shift_smaller=residues_for_orientation(38,37)
assert target not in root_smaller
assert target in shift_smaller
assert sorted(r>>37 for r in root_smaller)==[1,3,7]
assert sorted(r>>37 for r in shift_smaller)==[1,5,7]

out={
 'status':'PASS',
 'global_overlap_modulus_bits':56,
 'required_difference_valuation':37,
 'first_mismatch_min_index':24,
 'first_mismatch_max_index':37,
 'm24_root_smaller_orientation_possible':False,
 'm24_shift_smaller_orientation_not_excluded':True,
 'small_offset_current_necessary_sources':small,
 'small_offset_count':len(small),
 'locked_offsets':[4,16],
 'current_total_count':13_415_865_871,
 'current_above_p_count':7_091_831_284,
 'current_below_p_count':6_324_034_587,
 'above_p_e_ge_56_count':7_091_831_284-len(small),
 'new_rank_exclusions':0,
}
cert=ROOT/'certificates/verify_rl210_global_prefix_overlap_output.json'
cert.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print('PASS RL210 global p-shift prefix overlap')
print('- first mismatch m: 24..37 with smaller exponent exactly 37')
print('- m=24 root-smaller orientation: EXCLUDED')
print('- exact current above-p sources with e<56: 6')
print('- exact locked short offsets: e=4,16')
print('- current necessary frontier unchanged: 13,415,865,871')
