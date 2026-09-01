#!/usr/bin/env python3
import hashlib, json
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

assert A*p-u*L==1
assert z==72_057_431_991

# Exact rational ln2 upper bound used by the analytic theorem:
# partial n=0..6 of 2*sum 1/((2n+1)3^(2n+1)),
# plus tail <= 1/(20*3^14).
U=sum(Fraction(2,(2*n+1)*3**(2*n+1)) for n in range(7))
U+=Fraction(1,20*3**14)
assert U==Fraction(13_274_467_117,19_151_007_876)

W=U+Fraction(z,1<<40)
LB=Fraction(K0)*(L-W)/W
LB_INT=LB.numerator//LB.denominator+1
assert LB==Fraction(
    99_502_176_389_773_321_825_857_103_001_223_487_471_747_072,
    3_993_850_848_813_907_800_727
)
assert LB_INT==24_913_843_845_551_577_787_381

# Reconstruct the complete RL212/RL214 e=16 prefix domain.
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
step=3*(1<<58)

rows=[]
prefix_states=Counter()
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
    prefix_states[eta%9]+=1

assert len(rows)==45_046
assert prefix_states==Counter({0:29_286,8:15_760})

# Inherited RL214 upper cap.
CAPNUM=48*L*K0
CAP=(CAPNUM-1)//29
assert CAP==31_285_589_992_934_194_300_574

# Terminal Hensel setup.
M=1<<22
forbidden=pow(pow(3,34,M),-1,M)
assert forbidden==1_893_305
r_odd=forbidden
r_even=(forbidden-21)%M
invN=pow(mod17,-1,M)

kmins=Counter()
joint=Counter()
bad_distribution=Counter()
mod18=Counter()
state_counts=Counter()
reachable2187=set()
before=0
bad_total=0
min_good=10**18
max_good=0
digest_lines=[]

for Q,eta0,t,eta,y0 in rows:
    kmax=(CAPNUM-1-29*y0)//(29*step)
    num=LB.numerator-LB.denominator*y0
    kmin=0 if num<0 else num//(LB.denominator*step)+1
    assert kmin<=kmax
    kmins[kmin]+=1
    joint[(kmin,kmax)]+=1
    n=kmax-kmin+1
    before+=n

    badks=set()
    for r in (r_odd,r_even):
        k=((r-eta)*invN)%M
        if kmin<=k<=kmax:
            etak=eta+k*mod17
            s=etak if etak&1 else etak+21
            assert v2(3**34*s-1)>=22
            badks.add(k)

    bad_total+=len(badks)
    bad_distribution[len(badks)]+=1
    good=n-len(badks)
    min_good=min(min_good,good)
    max_good=max(max_good,good)

    for parity in (0,1):
        first=kmin if kmin%2==parity else kmin+1
        if first<=kmax:
            count=(kmax-first)//2+1
            mod18[(eta+first*mod17)%18]+=count
    for k in badks:
        mod18[(eta+k*mod17)%18]-=1

    state_counts[eta%9]+=good
    reachable2187.add(eta%2187)
    digest_lines.append(
        f"{Q},{eta0},{t},{eta},{y0},{kmin},{kmax},{','.join(map(str,sorted(badks)))}\n"
    )

assert kmins==Counter({28_812:26_133,28_813:18_913})
assert joint==Counter({
    (28_812,36_180):26_133,
    (28_813,36_180):8_519,
    (28_813,36_181):10_394,
})
assert before==331_935_455
assert bad_total==170
assert bad_distribution==Counter({0:44_876,1:170})
after=before-bad_total
assert after==331_935_285
assert min_good==7_367 and max_good==7_369
assert mod18==Counter({0:107_901_476,9:107_901_377,8:58_066_202,17:58_066_230})
assert state_counts==Counter({0:215_802_853,8:116_132_432})
assert len(reachable2187)==469

digest=hashlib.sha256("".join(digest_lines).encode()).hexdigest()
assert digest=="f059976b3627bde3b97e009b2f7ae6dd055d23eee7e5a641704fa61663962fe7"

out=json.loads((ROOT/"certificates/verify_rl215_arc_sandwich_output.json").read_text())
assert out["status"]=="PASS"
assert out["root_lower_bound_integer"]==LB_INT
assert out["two_sided_candidates_before_terminal_filter"]==before
assert out["terminal_hensel_removed_inside_window"]==bad_total
assert out["two_sided_candidates_after_terminal_filter"]==after
assert out["witness_digest_sha256"]==digest
assert out["new_rank_exclusions"]==0
assert out["frontier"]==13_415_865_871

print("PASS RL215 complementary-arc sandwich certificate")
print("root_lower=24913843845551577787381 root_upper=31285589992934194300574")
print("kmin=28812_or_28813 candidates_before_terminal=331935455")
print("terminal_hensel_removed=170 candidates_after_terminal=331935285")
print("prefixes_deleted=0 states011_111_survive mod18=0,8,9,17 eta_mod2187=469")
print("rank_deletions=0 frontier=13415865871")
