#!/usr/bin/env python3
from collections import Counter, defaultdict

A=217_976_794_617
L=137_528_045_312
KMIN=15_106_005_985
KMAX=18_969_385_559
N=3_863_379_575
U36=900_567_811_781_994_726
V36=692_103_040_536_162_613
H36=19
TERM_R=(801_774,1_785_623)
MOD22=1<<22
EXPECTED_FAIL={36:3684,37:18422,38:105924,39:203794,40:713558,41:943078,42:1299949,43:3429092}
EXPECTED_STATES={36:1,37:20,38:230,39:1770,40:12395,41:65524,42:361277,43:1906336}
EXPECTED_ALL_STATES_44=7_743_281
EXPECTED_HEIGHT_SURV_43=3_856_662_074
EXPECTED_COMBINED_43=3_856_660_232

def b(i): return A*i//L
B36=b(36)
def E(i): return H36+b(i)-B36

def count_cong(r,mod):
    first=KMIN+((r-KMIN)%mod)
    return 0 if first>KMAX else (KMAX-first)//mod+1

def v2(n): return (n & -n).bit_length()-1

# Independent precision-only DP. Since E_44=31 and N>2^31, every admissible
# phase-44 cylinder intersects the finite window, so this gives the exact
# phase-44 live-state count without residue enumeration.
dp={0:1}; totals={36:1}
for i in range(36,44):
    lim=E(i+1)
    nd={}
    running=0
    for mp in range(1,lim+1):
        running += dp.get(mp-1,0)
        nd[mp]=running
    dp=nd
    totals[i+1]=sum(dp.values())
for i,x in EXPECTED_STATES.items(): assert totals[i]==x,(i,totals[i],x)
assert totals[44]==EXPECTED_ALL_STATES_44,totals[44]
assert E(43)==30 and E(44)==31 and E(45)==33
assert (1<<31)<N<(1<<32)<(1<<33)
assert N//(1<<E(45))==0

# Optimized exact RL226 replay through transition 43.
pow3=[1]
for _ in range(10): pow3.append(pow3[-1]*3)
q_phase={i:(3*(U36*pow3[i-36]))//2 for i in range(36,44)}
inv_cache={}
def inv_q(i,cap):
    key=(i,cap)
    if key not in inv_cache:
        inv_cache[key]=pow(q_phase[i],-1,1<<cap)
    return inv_cache[key]

stack=[(36,0,0,V36)]
states=Counter(); fails=Counter(); leaf43=0
while stack:
    i,r,m,v=stack.pop()
    states[i]+=1
    h=E(i)-m
    assert h>=0 and (v&1)==1
    cnt=count_cong(r,1<<m)
    cap=E(i+1)-m
    assert cap==b(i+1)-b(i)+h and cap>=1
    q=q_phase[i]
    c=(3*v+1)//2
    z=(-c*inv_q(i,cap))%(1<<cap)
    fm=m+cap
    assert fm==E(i+1)
    fr=(r+(1<<m)*z)%(1<<fm)
    fails[i]+=count_cong(fr,1<<fm)
    if i==43:
        leaf43 += cnt
        continue
    for a in range(1,cap+1):
        j=a-1
        rt=(z&((1<<j)-1)) | ((1-((z>>j)&1))<<j)
        nm=m+a
        nr=(r+(1<<m)*rt)%(1<<nm)
        if count_cong(nr,1<<nm):
            nv=(q*rt+c)>>j
            assert nv&1
            stack.append((i+1,nr,nm,nv))

assert dict(states)==EXPECTED_STATES,(states,EXPECTED_STATES)
assert dict(fails)==EXPECTED_FAIL,(fails,EXPECTED_FAIL)
assert leaf43==3_860_091_166,leaf43
height43=leaf43-fails[43]
assert height43==EXPECTED_HEIGHT_SURV_43,height43

# Terminal-Hensel coupling remains disjoint through transition 43.
def terminal_fail_phase(k,maxp=43):
    eta=207+243*k
    y4=(1<<34)*eta-1-81*(1<<32)
    y=((1<<5)*y4-85)//81
    h=0
    for i in range(maxp+1):
        a=v2(3*y+1)
        nh=b(i+1)-b(i)+h-a
        if nh<0: return i
        y=(3*y+1)>>a
        h=nh
    return None
term_count=0
for rr in TERM_R:
    k=KMIN+((rr-KMIN)%MOD22)
    while k<=KMAX:
        term_count+=1
        assert terminal_fail_phase(k,43) is None
        k+=MOD22
assert term_count==1842
assert height43-term_count==EXPECTED_COMBINED_43

# Exact same-cardinality/opposite-future witness at phase 44.
def replay_witness(k, expected_vals, expected_next):
    y=U36*k+V36
    m=0
    vals=[]
    for i in range(36,44):
        a=v2(3*y+1); vals.append(a); m+=a
        assert E(i+1)-m>=0
        y=(3*y+1)>>a
    assert vals==expected_vals,(vals,expected_vals)
    assert m==31 and E(44)-m==0
    cap=E(45)-m
    a44=v2(3*y+1)
    assert cap==2 and a44==expected_next
    return a44>cap

kA=16_903_549_360
kB=17_239_093_680
assert KMIN<=kA<=KMAX and KMIN<=kB<=KMAX
assert kA%(1<<31)==1_871_163_824
assert kB%(1<<31)==59_224_496
assert count_cong(1_871_163_824,1<<31)==1
assert count_cong(59_224_496,1<<31)==1
assert replay_witness(kA,[20,2,1,2,1,2,1,2],1) is False
assert replay_witness(kB,[20,2,1,2,1,1,3,1],4) is True

print('RL228 E4 DYADIC BULK/FRINGE ENDPOINT BARRIER: PASS')
print('RL226 reproduction through transition43 PASS')
print('state_counts_through_43', ' '.join(f'{i}:{states[i]}' for i in range(36,44)))
print('phase44_exact_state_count',EXPECTED_ALL_STATES_44)
print('E44 31 E45 33; transition44_bulk_coefficient 0')
print('same_precision_height_cardinality_opposite_future_witness PASS')
print('combined_survivors_certified_through_43',EXPECTED_COMBINED_43)
