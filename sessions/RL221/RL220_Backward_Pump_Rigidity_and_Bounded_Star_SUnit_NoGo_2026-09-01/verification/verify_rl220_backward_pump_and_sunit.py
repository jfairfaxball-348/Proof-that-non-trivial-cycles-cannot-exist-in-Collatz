#!/usr/bin/env python3
import json
from collections import Counter
from fractions import Fraction
from itertools import product
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
A0=217_976_794_617
L=137_528_045_312
p=65_470_613_321
u=103_768_467_013
z=L-p
K0=1<<37
DELETED_Q=43_013_953
RMIN=24_913_843_845_551_577_787_381
RMAX=31_285_589_992_934_194_300_574

def b(i): return A0*i//L

def v2(n):
    n=abs(n)
    return (n & -n).bit_length()-1

assert A0*p-u*L==1
assert z==72_057_431_991

# Reconstruct the inherited e=16 root-prefix family exactly.
bs=[b(i) for i in range(17)]
assert bs==[0,1,3,4,6,7,9,11,12,14,15,17,19,20,22,23,25]
c=[bs[i+1]-bs[i] for i in range(16)]
states={(0,1)}
for i in range(1,16):
    nxt=set()
    for h,Q in states:
        S=bs[i]-h
        for hn in range(h+c[i]):
            a=c[i]+h-hn
            assert a>=1
            nxt.add((hn,3*Q+(1<<S)))
    states=nxt
terminal=sorted(Q for h,Q in states if h==1)
assert len(terminal)==108_950

S=24
gap=3**16 * 2**13
mod16=3**16
mod17=3**17
inv16=pow(1<<(S+34),-1,mod16)
rows=[]
for Q in terminal:
    eta0=((1<<S)+Q)*inv16 % mod16
    if eta0%9 not in (0,8):
        continue
    y16=(1<<34)*eta0-1-gap
    num=(1<<S)*y16-Q
    assert num%mod16==0
    y0base=num//mod16
    valid=[]
    for t in range(3):
        y0=y0base+(1<<(S+34))*t
        if y0%3 and (y0+K0)%3:
            valid.append((t,y0))
    assert len(valid)==1
    t,y0=valid[0]
    rows.append((Q,eta0+t*mod16,y0))
assert len(rows)==45_046
assert rows[0][0]==DELETED_Q

U=sum(Fraction(2,(2*n+1)*3**(2*n+1)) for n in range(7))
U+=Fraction(1,20*3**14)
W=U+Fraction(z,1<<40)
LB=Fraction(K0)*(L-W)/W
step=3*(1<<58)
CAPNUM=48*L*K0
M=1<<22
forbidden=pow(pow(3,34,M),-1,M)
r_odd=forbidden
r_even=(forbidden-21)%M
invN22=pow(mod17,-1,M)
records=[]
post_hensel=0
for Q,eta,y0 in rows:
    kmax=(CAPNUM-1-29*y0)//(29*step)
    num=LB.numerator-LB.denominator*y0
    kmin=0 if num<0 else num//(LB.denominator*step)+1
    bad=set()
    for rr in (r_odd,r_even):
        k=((rr-eta)*invN22)%M
        if kmin<=k<=kmax:
            bad.add(k)
    records.append((Q,eta,y0,kmin,kmax,tuple(sorted(bad))))
    post_hensel += (kmax-kmin+1)-len(bad)
assert post_hensel==331_935_285
assert records[0][5]==()
assert post_hensel-(records[0][4]-records[0][3]+1)==331_927_916

live=records[1:]
assert len(live)==45_045

# RL220-C1: exact first accelerated-step screen.
mod4=Counter()
vcounts=Counter()
for Q,eta,y0,lo,hi,bad in live:
    mod4[y0%4]+=1
    e=v2(3*y0+1)
    assert e<58
    vcounts[e]+=1
    # The step is divisible by 2^58, so e<58 is constant for the whole progression.
    assert v2(3*(y0+step)+1)==e
assert mod4==Counter({3:45_045})
assert vcounts==Counter({1:45_045})

# Stable external interval cannot be reached in one accelerated odd step.
external=1<<71
min_first=(3*RMIN+1)//2
assert min_first>external

# RL220-C2: exact same-integer screen for b_38.
b38=((1<<76)-1)//3
assert RMIN<=b38<=RMAX
matches=[]
for idx,(Q,eta,y0,lo,hi,bad) in enumerate(live, start=1):
    d=b38-y0
    if d%step:
        continue
    k=d//step
    if lo<=k<=hi and k not in bad:
        matches.append((idx,Q,eta,y0,k))
assert matches==[]

# Analytic-theorem sanity: exact raw-block affine constant and defect identity.
def block_data(word):
    n=len(word)
    h=0
    C=0
    for i,ch in enumerate(word, start=1):
        if ch=="O":
            C += (1<<(n-i))*(3**h)
            h += 1
    return 1<<n,3**h,C,h

words_checked=0
identity_checks=0
for n in range(1,9):
    for bits in product("DO", repeat=n):
        w="".join(bits)
        AA,BB,C,h=block_data(w)
        if h==0:
            assert C==0 and BB==1
            continue
        words_checked+=1
        assert C>0 and AA!=BB
        for x in (-17,-1,0,1,2,19):
            # Cross-multiplied identity:
            # B*Delta(F(x)) = A*Delta(x), avoiding any integrality assumption.
            # B*F(x)=A*x-C.
            D=AA-BB
            lhs = D*(AA*x-C) - BB*C
            rhs = AA*(D*x-C)
            assert lhs==rhs
            identity_checks+=1
assert words_checked==502
assert identity_checks==3012

# RL220-T4 sanity: recurrence unroll for fixed odd count and variable gap exponents.
unroll_cases=0
for h in range(1,6):
    for es in product((1,2,3), repeat=h):
        E=sum(es)
        Q=0
        for j,e in enumerate(es, start=1):
            Q=(1<<e)*Q+3**(j-1)
        Qu=sum(3**(i-1)*(1<<sum(es[i:])) for i in range(1,h+1))
        assert Q==Qu
        for s in (1,5,17):
            lhs=(1<<E)*s-Q
            rhs=(1<<E)*s-sum(3**(i-1)*(1<<sum(es[i:])) for i in range(1,h+1))
            assert lhs==rhs
            unroll_cases+=1
assert unroll_cases==1089

result={
  "status":"PASS",
  "live_prefixes_checked":45045,
  "pre_phase51_live_candidates_after_hensel":331927916,
  "root_base_mod4_counts":{"3":45045},
  "root_first_accelerated_v2_counts":{"1":45045},
  "one_step_external_interval_deletions":0,
  "b38_value":b38,
  "b38_in_root_band":True,
  "b38_pre_phase51_exact_matches":0,
  "fixed_non_dyadic_blocks_sanity_checked":words_checked,
  "fixed_block_defect_identity_checks":identity_checks,
  "odd_only_recurrence_unroll_cases":unroll_cases,
  "new_candidate_deletions":0,
  "new_prefix_deletions":0,
  "new_rank_exclusions":0,
  "frontier":13415865871
}
frozen=json.loads((ROOT/"certificates/verify_rl220_backward_pump_and_sunit_output.json").read_text())
assert frozen==result
print("PASS RL220 backward pump rigidity / bounded-star support verifier")
print("live_prefixes=45045 all_root_v2_3y_plus_1=1")
print(f"b38={b38} exact_live_window_matches=0")
print("new_candidate_deletions=0 new_rank_exclusions=0 frontier=13415865871")
