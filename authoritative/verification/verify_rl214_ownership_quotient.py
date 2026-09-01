#!/usr/bin/env python3
import hashlib, json
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
A=217_976_794_617
L=137_528_045_312
p=65_470_613_321
u=103_768_467_013
K0=1<<37

def b(i): return A*i//L
def v2(n): return (n & -n).bit_length()-1

# RL212 exact e=16 root-prefix enumeration.
bs=[b(i) for i in range(17)]
assert bs == [0,1,3,4,6,7,9,11,12,14,15,17,19,20,22,23,25]
c=[bs[i+1]-bs[i] for i in range(16)]
assert c == [1,2,1,2,1,2,2,1,2,1,2,2,1,2,1,2]

states={(0,1)}
for i in range(1,16):
    nxt=set()
    for h,Q in states:
        S=bs[i]-h
        for hn in range(h+c[i]):
            a=c[i]+h-hn
            assert a>=1
            assert S+a == bs[i+1]-hn
            nxt.add((hn,3*Q+(1<<S)))
    states=nxt

terminal=sorted(Q for h,Q in states if h==1)
assert len(terminal)==108_950
assert len(set(terminal))==108_950
S=24
assert bs[16]-1==S

gap=3**16 * 2**13
mod16=3**16
mod17=3**17
inv16=pow(1<<(S+34),-1,mod16)
lift_step_y0=3*(1<<58)

rows=[]
state_prefix_counts=Counter()
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
        yp=y0+K0
        if y0%3 and yp%3:
            valid.append((t,y0))
    assert len(valid)==1
    t,y0=valid[0]
    eta=eta0+t*mod16
    assert 0<=eta<mod17
    assert 0<y0<lift_step_y0
    assert y0&1 and (y0+K0)&1
    rows.append((Q,eta0,t,eta,y0))
    state_prefix_counts[eta%9]+=1

assert len(rows)==45_046
assert state_prefix_counts==Counter({0:29_286,8:15_760})
assert min(r[3] for r in rows)==4_167
assert max(r[3] for r in rows)==129_137_967
assert min(r[4] for r in rows)==27_763_779_757_799
assert max(r[4] for r in rows)==864_676_287_134_182_727

# RL214 analytic p-arc bound is:
#   29*y0 < 48*L*K0.
# It follows from 2^u*K0=(3^p-2^u)y0+P_p with P_p>0,
# Ap-uL=1, 0<ln(lambda)<2^-40, p<2^36 and ln2>2/3.
CAPNUM=48*L*K0
CAP_FLOOR=(CAPNUM-1)//29
assert CAP_FLOOR==31_285_589_992_934_194_300_574

# Every exact eta lift is eta=eta_*+k*3^17 and hence
# y0=y0_*+3*2^58*k. Positivity forces k>=0 because 0<y0_*<step.
kmax_counts=Counter()
total_bounded=0
kmax_by_row=[]
for Q,eta0,t,eta,y0 in rows:
    kmax=(CAPNUM-1-29*y0)//(29*lift_step_y0)
    assert kmax in (36_180,36_181)
    kmax_counts[kmax]+=1
    total_bounded+=kmax+1
    kmax_by_row.append(kmax)

assert kmax_counts==Counter({36_180:34_652,36_181:10_394})
assert total_bounded==1_629_819_720

# Combine the finite root window with the inherited physical terminal valuation.
# nu>=22 iff the odd parameter s is one forbidden residue mod 2^22.
M=1<<22
g=pow(3,34,M)
forbidden_s=pow(g,-1,M)
assert forbidden_s==1_893_305
r_odd=forbidden_s
r_even=(forbidden_s-21)%M
N=mod17
invN=pow(N,-1,M)

bad_prefix_distribution=Counter()
total_bad=0
mod18_counts=Counter()
min_good=10**18
max_good=0
reachable2187=set()

digest_lines=[]
for (Q,eta0,t,eta,y0),kmax in zip(rows,kmax_by_row):
    n=kmax+1
    # Count parity / mod18 candidates before the Hensel removal.
    even_k=(n+1)//2
    odd_k=n//2
    mod18_counts[eta%18]+=even_k
    mod18_counts[(eta+9)%18]+=odd_k  # 3^17 == 9 mod 18

    badks=set()
    for r in (r_odd,r_even):
        k=((r-eta)*invN)%M
        if k<=kmax:
            etak=eta+k*N
            s=etak if etak&1 else etak+21
            assert v2(3**34*s-1)>=22
            badks.add(k)
    for k in badks:
        mod18_counts[(eta+k*N)%18]-=1

    total_bad+=len(badks)
    bad_prefix_distribution[len(badks)]+=1
    good=n-len(badks)
    min_good=min(min_good,good)
    max_good=max(max_good,good)
    reachable2187.add(eta%2187)
    digest_lines.append(f"{Q},{eta0},{t},{eta},{y0},{kmax},{','.join(map(str,sorted(badks)))}\n")

assert bad_prefix_distribution==Counter({0:44_257,1:789})
assert total_bad==789
assert min_good==36_180
assert max_good==36_182
assert sum(mod18_counts.values())==1_629_818_931
assert mod18_counts==Counter({
    0:529_801_527,
    9:529_801_531,
    8:285_107_835,
    17:285_108_038,
})
assert len(reachable2187)==469
assert set(mod18_counts)=={0,8,9,17}

digest=hashlib.sha256("".join(digest_lines).encode()).hexdigest()
assert digest=="cd0f9235a557a8f70c8fed89a802da95222fcc5bc80b7644e6dba57f71346136"

out={
  "status":"PASS",
  "offset_e":16,
  "root_prefix_count":108950,
  "h21_prefix_count":45046,
  "state011_prefix_count":29286,
  "state111_prefix_count":15760,
  "canonical_eta_range":[4167,129137967],
  "canonical_y0_range":[27763779757799,864676287134182727],
  "root_lift_step_y0":lift_step_y0,
  "root_cap_strict":"29*y0 < 48*L*K0",
  "root_cap_integer_max":CAP_FLOOR,
  "kmax_distribution":{"36180":34652,"36181":10394},
  "bounded_root_candidates_before_terminal_filter":total_bounded,
  "terminal_hensel_removed_candidates":total_bad,
  "bounded_root_candidates_after_terminal_filter":sum(mod18_counts.values()),
  "prefixes_deleted_by_terminal_filter":0,
  "minimum_candidates_per_prefix_after_terminal_filter":min_good,
  "maximum_candidates_per_prefix_after_terminal_filter":max_good,
  "surviving_mod18_candidate_counts":{str(k):mod18_counts[k] for k in (0,8,9,17)},
  "reachable_eta_mod2187":len(reachable2187),
  "witness_digest_sha256":digest,
  "new_rank_exclusions":0,
  "frontier":13_415_865_871
}
(ROOT/"certificates/verify_rl214_ownership_quotient_output.json").write_text(
    json.dumps(out,indent=2,sort_keys=True)+"\n"
)
print("PASS RL214 discrete ownership-quotient bridge/root-cap certificate")
print("root_prefixes=108950 h21_prefixes=45046 states011_111=29286_15760")
print("root_bridge=y0=Q(full_word)/(2^A-3^L)")
print("root_cap=29*y0<48*L*K0 integer_max=31285589992934194300574")
print("kmax=36180_or_36181 bounded_candidates=1629819720")
print("terminal_hensel_removed=789 prefixes_deleted=0")
print("mod18_survivors=0,8,9,17 eta_mod2187_reachable=469")
print("rank_deletions=0 frontier=13415865871")
