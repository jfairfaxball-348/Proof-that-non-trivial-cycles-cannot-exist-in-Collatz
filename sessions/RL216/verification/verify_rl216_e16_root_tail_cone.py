#!/usr/bin/env python3
import hashlib
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
A=217_976_794_617
L=137_528_045_312
p=65_470_613_321
u=103_768_467_013
z=L-p
K0=1<<37

def b(i): return A*i//L
def v2(n): return (n & -n).bit_length()-1

def count_class(lo,hi,r,m):
    mod=1<<m
    first=lo+((r-lo)%mod)
    if first>hi: return 0
    return (hi-first)//mod+1

assert A*p-u*L==1
assert z==72_057_431_991

# Reconstruct the complete RL212/RL215 e=16 prefix family.
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
    eta=eta0+t*mod16
    rows.append((Q,eta0,t,eta,y0))
assert len(rows)==45_046

# Canonical target: the unique minimum-Q H21-compatible e=16 prefix.
Q,eta0,t,eta,y0=rows[0]
assert Q==43_013_953
assert eta0==33_322_841
assert t==2
assert eta==119_416_283
assert y0==799_582_255_090_532_351
assert all(r[0]>Q for r in rows[1:])
assert eta%9==8 and eta%18==17 and eta%2187==1709
assert sum(1 for r in rows[1:] if r[3]%2187==eta%2187)==11

# Exact RL215 two-sided k-window for this prefix.
U=sum(Fraction(2,(2*n+1)*3**(2*n+1)) for n in range(7))
U+=Fraction(1,20*3**14)
W=U+Fraction(z,1<<40)
LB=Fraction(K0)*(L-W)/W
step=3*(1<<58)
CAPNUM=48*L*K0
kmax=(CAPNUM-1-29*y0)//(29*step)
num=LB.numerator-LB.denominator*y0
kmin=0 if num<0 else num//(LB.denominator*step)+1
assert (kmin,kmax)==(28_812,36_180)
assert kmax-kmin+1==7_369

# The inherited Hensel filter removes no candidate from this particular prefix.
M=1<<22
forbidden=pow(pow(3,34,M),-1,M)
r_odd=forbidden
r_even=(forbidden-21)%M
invN=pow(mod17,-1,M)
badks=set()
for r in (r_odd,r_even):
    k=((r-eta)*invN)%M
    if kmin<=k<=kmax:
        badks.add(k)
assert badks==set()

# Exact modular/range-counting height-cone sieve.
# A branch k == r (mod 2^m) is written k=r+2^m*t and carries y_i=A_i*t+B_i.
# If v2(3*B_i+1) < v2(A_i), the acceleration exponent is fixed on the branch.
# Otherwise t parity is split, raising m by one. If every value on a branch has
# a_i > h_i+c_i, then h_(i+1)<0 for the whole branch and that residue class is dead.
initial_A=(1<<34)*mod17
initial_B=(1<<34)*eta-1-gap
stack=[(16,1,0,0,initial_A,initial_B)]
fails=[]
survivors=[]
while stack:
    i,h,m,r,Acoef,Bconst=stack.pop()
    cnt=count_class(kmin,kmax,r,m)
    if not cnt:
        continue
    if i>174:
        survivors.append((m,r,cnt))
        continue
    ci=b(i+1)-b(i)
    maxa=ci+h
    Nconst=3*Bconst+1
    va=v2(abs(Acoef))
    vb=v2(abs(Nconst))
    if min(va,vb)>maxa:
        fails.append((m,r,i,cnt,">",maxa,va,vb))
        continue
    if vb<va:
        a=vb
        assert a>=1
        if a>maxa:
            fails.append((m,r,i,cnt,a,maxa,va,vb))
            continue
        den=1<<a
        assert Acoef%den==0 and Nconst%den==0
        stack.append((i+1,ci+h-a,m,r,3*Acoef//den,Nconst//den))
        continue

    # valuation depends on the next 2-adic digit of t; split exactly by parity.
    for bit in (0,1):
        nr=r+(bit<<m)
        nA=2*Acoef
        nB=Acoef*bit+Bconst
        stack.append((i,h,m+1,nr,nA,nB))

assert survivors==[]
assert len(fails)==6_219
assert sum(x[3] for x in fails)==7_369
assert max(x[2] for x in fails)==174
phase_counts=Counter()
for m,r,i,cnt,*rest in fails:
    phase_counts[i]+=cnt
assert phase_counts[39]==116
assert phase_counts[40]==344
assert phase_counts[43]==500
assert phase_counts[45]==515
assert phase_counts[174]==1

canonical=sorted((m,r,i,cnt,str(a),maxa,va,vb) for m,r,i,cnt,a,maxa,va,vb in fails)
digest=hashlib.sha256(
    "".join(",".join(map(str,row))+"\n" for row in canonical).encode()
).hexdigest()
assert digest=="b7f03ca354275de4e4d9aaa0698ab6e39d088232331a3f2f9b111a01df96d972"

# Exact population consequence of deleting only this certified prefix.
deleted_mod18=Counter()
for parity in (0,1):
    first=kmin if kmin%2==parity else kmin+1
    if first<=kmax:
        count=(kmax-first)//2+1
        deleted_mod18[(eta+first*mod17)%18]+=count
assert deleted_mod18==Counter({17:3685,8:3684})

result={
    "status":"PASS",
    "offset_e":16,
    "canonical_prefix_Q":Q,
    "canonical_prefix_eta_base_mod_3pow17":eta,
    "canonical_prefix_eta_mod2187":eta%2187,
    "canonical_prefix_kmin":kmin,
    "canonical_prefix_kmax":kmax,
    "canonical_prefix_candidates_after_terminal_filter":7369,
    "terminal_hensel_removed_in_canonical_prefix":0,
    "height_cone_last_failure_phase":174,
    "modular_failure_residue_classes":len(fails),
    "modular_failure_class_digest_sha256":digest,
    "deleted_mod18_candidate_counts":{"8":3684,"17":3685},
    "prefixes_deleted":1,
    "e16_h21_prefixes_remaining":45045,
    "arithmetic_candidates_removed_vs_rl215":7369,
    "two_sided_candidates_after_rl216_targeted_deletion":331_927_916,
    "reachable_eta_mod2187_remaining":469,
    "new_rank_exclusions":0,
    "frontier":13_415_865_871,
}
out=json.loads((ROOT/"certificates/verify_rl216_e16_root_tail_cone_output.json").read_text())
assert out==result

print("PASS RL216 e=16 root-tail height-cone certificate")
print("canonical_Q=43013953 k=28812..36180 deleted_candidates=7369 prefixes_deleted=1")
print("modular_classes=6219 latest_negative_height_phase=174 eta_mod2187=1709_still_represented")
print("remaining_e16_prefixes=45045 targeted_candidates_remaining=331927916")
print("rank_deletions=0 frontier=13415865871")
