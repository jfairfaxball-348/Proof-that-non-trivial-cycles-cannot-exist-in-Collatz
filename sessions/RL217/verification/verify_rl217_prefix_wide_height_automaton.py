#!/usr/bin/env python3
import bisect
import hashlib
import json
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
A=217_976_794_617
L=137_528_045_312
p=65_470_613_321
u=103_768_467_013
z=L-p
K0=1<<37
HORIZON=51
DELETED_Q=43_013_953

def b(i): return A*i//L
def v2(n):
    n=abs(n)
    return (n & -n).bit_length()-1

def cyclic_count(vals,mod,start,length):
    if length<=0:
        return 0
    end=start+length
    if end<=mod:
        return bisect.bisect_left(vals,end)-bisect.bisect_left(vals,start)
    return (len(vals)-bisect.bisect_left(vals,start))+bisect.bisect_left(vals,end-mod)

assert A*p-u*L==1
assert z==72_057_431_991

# Reconstruct the complete inherited RL212/RL215 e=16 prefix family.
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
    rows.append((Q,eta,y0))
assert len(rows)==45_046
assert rows[0][0]==DELETED_Q

# Reconstruct the inherited two-sided k windows and terminal Hensel filter.
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
pre_hensel=0
post_hensel=0
hensel_removed=0
for Q,eta,y0 in rows:
    kmax=(CAPNUM-1-29*y0)//(29*step)
    num=LB.numerator-LB.denominator*y0
    kmin=0 if num<0 else num//(LB.denominator*step)+1
    n=kmax-kmin+1
    bad=set()
    for rr in (r_odd,r_even):
        k=((rr-eta)*invN22)%M
        if kmin<=k<=kmax:
            bad.add(k)
    records.append((Q,eta,y0,kmin,kmax,tuple(sorted(bad))))
    pre_hensel+=n
    post_hensel+=n-len(bad)
    hensel_removed+=len(bad)
assert pre_hensel==331_935_455
assert post_hensel==331_935_285
assert hensel_removed==170
assert records[0][3:5]==(28_812,36_180)
assert records[0][5]==()
assert post_hensel-(records[0][4]-records[0][3]+1)==331_927_916

# RL217-T1: after phase 16 every prefix enters one universal state in x=eta+3^17 k:
# y_16 = 2^34 x - 1 - 3^16*2^13, h_16=1.
# Build that universal 2-adic automaton once, not once per arithmetic candidate.
stack=[(16,1,0,0,1<<34,-1-gap)]
live=defaultdict(list)
processed=0
failure_classes=0
failure_phase=Counter()
while stack:
    i,h,m,r,Acoef,Bconst=stack.pop()
    processed+=1
    if i>HORIZON:
        live[m].append(r)
        continue
    ci=b(i+1)-b(i)
    maxa=ci+h
    Nconst=3*Bconst+1
    va=v2(Acoef)
    vb=v2(Nconst)
    if min(va,vb)>maxa:
        failure_classes+=1
        failure_phase[i]+=1
        continue
    if vb<va:
        a=vb
        if a>maxa:
            failure_classes+=1
            failure_phase[i]+=1
            continue
        den=1<<a
        assert Acoef%den==0 and Nconst%den==0
        stack.append((i+1,ci+h-a,m,r,3*Acoef//den,Nconst//den))
        continue
    for bit in (0,1):
        stack.append((i,h,m+1,r+(bit<<m),2*Acoef,Acoef*bit+Bconst))

live_count=sum(map(len,live.values()))
assert processed==14_514_513
assert failure_classes==1_705_547
assert live_count==3_132_617
assert max(live)==25
assert failure_phase[48]==59_166
assert failure_phase[49]==143_295
assert failure_phase[50]==445_260
assert failure_phase[51]==1_030_718
assert sorted((m,len(v)) for m,v in live.items())==[
    (13,1),(14,13),(15,91),(16,455),(17,1820),(18,6188),(19,18557),
    (20,50282),(21,124823),(22,283493),(23,585458),(24,1030718),(25,1030718)
]

# Pin the exact disjoint phase-51 survivor cylinders.
digest=hashlib.sha256()
for m in sorted(live):
    live[m].sort()
    assert len(live[m])==len(set(live[m]))
    for r in live[m]:
        digest.update(f"{m},{r}\n".encode())
assert digest.hexdigest()=="abf94388354f55d34ae35370e3bcbcd2086da2f6053035840c0a9f68665e8d05"

# Transform x-residue cylinders to a prefix-independent coordinate s=(3^17)^(-1)x.
# A prefix with base eta samples s=a+k, a=(3^17)^(-1)eta. Count each short
# finite k interval by cyclic range arithmetic. No candidate enumeration occurs here.
trans={}
trans_parity={}
for m,rs in live.items():
    mod=1<<m
    inv=pow(mod17,-1,mod)
    ss=sorted((r*inv)%mod for r in rs)
    assert len(ss)==len(set(ss))
    trans[m]=ss
    trans_parity[m]=(ss[0::1],)  # temporary; replaced below without retaining rs
# parity partitions are used only for exact mod18 population accounting.
for m,ss in trans.items():
    trans_parity[m]=([s for s in ss if not (s&1)],[s for s in ss if s&1])
# release the original x-residue lists before the prefix sweep.
live.clear()

def count_prefix(eta,lo,hi):
    n=hi-lo+1
    total=0
    par=[0,0]
    for m,ss in trans.items():
        mod=1<<m
        q,rem=divmod(n,mod)
        # All current k intervals are shorter than 2^13, but keep exact general form.
        total+=q*len(ss)
        if q:
            ev,od=trans_parity[m]
            # full modulus contains equally well-defined parity counts of cylinder residues;
            # convert s parity to k parity using a below.
        inv=pow(mod17,-1,mod)
        a=(eta*inv)%mod
        if q:
            ev,od=trans_parity[m]
            par[(a)&1]+=q*len(ev)
            par[(a^1)&1]+=q*len(od)
        if rem:
            start=(a+lo)%mod
            total+=cyclic_count(ss,mod,start,rem)
            ev,od=trans_parity[m]
            par[0]+=cyclic_count((ev,od)[a&1],mod,start,rem)
            par[1]+=cyclic_count((ev,od)[(a^1)&1],mod,start,rem)
    assert total==sum(par)
    return total,par

def survives_direct(eta,k):
    x=eta+mod17*k
    y=(1<<34)*x-1-gap
    h=1
    for i in range(16,HORIZON+1):
        ci=b(i+1)-b(i)
        a=v2(3*y+1)
        if a>ci+h:
            return False
        h=ci+h-a
        y=(3*y+1)//(1<<a)
    return True

survivors=[]
state_counts=Counter()
mod18_counts=Counter()
eta2187_counts=Counter()
hensel_survivors_removed=0
for idx,(Q,eta,y0,lo,hi,badks) in enumerate(records):
    total,par=count_prefix(eta,lo,hi)
    for k in badks:
        if survives_direct(eta,k):
            total-=1
            par[k&1]-=1
            hensel_survivors_removed+=1
    assert total==sum(par)
    survivors.append(total)
    if idx==0:  # RL216 already deleted this complete prefix; do not reintroduce it.
        continue
    state_counts["011" if eta%9==0 else "111"]+=total
    for kp,cnt in enumerate(par):
        mod18_counts[(eta+(mod17%18)*kp)%18]+=cnt
    eta2187_counts[eta%2187]+=total

assert hensel_survivors_removed==88
assert len(survivors)==45_046
assert sum(survivors[1:])==139_581_280
assert 331_927_916-sum(survivors[1:])==192_346_636
assert min(survivors[1:])==2_995
assert max(survivors[1:])==3_235
assert all(x>0 for x in survivors[1:])
assert state_counts==Counter({"011":90_749_885,"111":48_831_395})
assert mod18_counts==Counter({0:35_622_831,8:19_167_422,9:55_127_054,17:29_663_973})
assert len(eta2187_counts)==469
assert min(eta2187_counts.values())==3_043
assert max(eta2187_counts.values())==1_664_633

# Independent red-team projection: direct replay a small deterministic cross-section,
# including terminal-Hensel-hit prefixes, and require agreement with modular counts.
sample=[1,2,17,101,261,497,1000,5000,10000,20000,30000,40000,45045]
for idx in sample:
    Q,eta,y0,lo,hi,badks=records[idx]
    bad=set(badks)
    direct=sum(1 for k in range(lo,hi+1) if k not in bad and survives_direct(eta,k))
    assert direct==survivors[idx], (idx,Q,direct,survivors[idx])

result={
    "status":"PASS",
    "offset_e":16,
    "height_horizon":51,
    "universal_processed_states":processed,
    "universal_failure_cylinders":failure_classes,
    "universal_live_cylinders":live_count,
    "universal_max_2adic_precision_bits":25,
    "universal_survivor_cylinder_digest_sha256":digest.hexdigest(),
    "inherited_rl216_prefixes":45_045,
    "inherited_rl216_candidates":331_927_916,
    "rl217_candidates_removed_through_phase51":192_346_636,
    "rl217_candidates_surviving_through_phase51":139_581_280,
    "rl217_prefixes_deleted":0,
    "rl217_prefixes_remaining":45_045,
    "per_prefix_survivor_min":2_995,
    "per_prefix_survivor_max":3_235,
    "state011_survivors":90_749_885,
    "state111_survivors":48_831_395,
    "mod18_survivors":{"0":35_622_831,"8":19_167_422,"9":55_127_054,"17":29_663_973},
    "reachable_eta_mod2187_remaining":469,
    "eta_mod2187_survivor_min":3_043,
    "eta_mod2187_survivor_max":1_664_633,
    "terminal_hensel_removed_in_narrowed_window":170,
    "terminal_hensel_candidates_that_would_survive_height51":88,
    "new_rank_exclusions":0,
    "e16_terminal_rank":34_124_151_203,
    "frontier":13_415_865_871,
}
out=json.loads((ROOT/"certificates/verify_rl217_prefix_wide_height_automaton_output.json").read_text())
assert out==result

print("PASS RL217 prefix-wide universal height automaton certificate")
print("horizon=51 live_cylinders=3132617 max_2adic_bits=25")
print("removed_vs_rl216=192346636 survivors=139581280 prefixes_remaining=45045")
print("state011=90749885 state111=48831395 eta_mod2187=469")
print("rank_deletions=0 frontier=13415865871")
