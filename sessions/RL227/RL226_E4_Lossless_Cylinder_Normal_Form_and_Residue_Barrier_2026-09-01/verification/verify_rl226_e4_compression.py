#!/usr/bin/env python3
from math import gcd
from collections import Counter

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
EXPECTED_HEIGHT_SURV_43=3_856_662_074
EXPECTED_COMBINED=3_856_660_232

def b(i): return A*i//L
B36=b(36)
def count_cong(r,m):
    first=KMIN+((r-KMIN)%m)
    return 0 if first>KMAX else (KMAX-first)//m+1

def solve_div(gu,gv,power):
    M=1<<power
    g=gcd(abs(gu),M)
    if gv%g: return None
    Md=M//g
    if Md==1: return (0,0)
    rr=(-(gv//g)*pow((gu//g)%Md,-1,Md))%Md
    return rr,Md.bit_length()-1

def v2(n): return (n & -n).bit_length()-1

pow3=[1]
for _ in range(80): pow3.append(pow3[-1]*3)

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

# Lossless compressed state: (phase, residue r mod 2^m, precision m, intercept v).
# The slope and height are derived, not stored:
#   u_i = U36 * 3^(i-36)
#   h_i = H36 + b(i)-b(36)-m.
stack=[(36,0,0,V36)]
fails=Counter(); state_counts=Counter(); examples={}
leaf43_surv=0; fail43=0
while stack:
    i,r,m,v=stack.pop()
    u=U36*pow3[i-36]
    h=H36+b(i)-B36-m
    assert h>=0 and (v&1)==1 and v2(u)==1
    state_counts[i]+=1
    if i==43:
        c=count_cong(r,1<<m)
        leaf43_surv += c
        cap=b(44)-b(43)+h
        gu=3*u; gv=3*v+1
        sf=solve_div(gu,gv,cap+1)
        assert sf is not None and sf[1]==cap
        rf,df=sf; fm=m+df; fr=(r+(1<<m)*rf)%(1<<fm)
        fail43 += count_cong(fr,1<<fm)
        if m==30 and c in (3,4): examples.setdefault(c,(r,v,h))
        continue
    cap=b(i+1)-b(i)+h
    gu=3*u; gv=3*v+1
    # Failure a>cap is one exact extension class modulo 2^cap in local t.
    sf=solve_div(gu,gv,cap+1)
    assert sf is not None and sf[1]==cap
    rf,df=sf; fm=m+df; fr=(r+(1<<m)*rf)%(1<<fm)
    fails[i]+=count_cong(fr,1<<fm)
    # Because v2(u)=1 and v is odd, exact valuation a is exactly one local
    # residue class modulo 2^a. Hence precision rises by a and child slope is 3u.
    for a in range(1,cap+1):
        sa=solve_div(gu,gv,a); sb=solve_div(gu,gv,a+1)
        assert sa is not None and sb is not None
        ra,da=sa; rb,db=sb
        assert da==a-1 and db==a
        lo=ra%(1<<a); hi=(ra+(1<<(a-1)))%(1<<a)
        rt=lo if hi==rb%(1<<a) else hi
        assert rt!=rb%(1<<a)
        nm=m+a; nr=(r+(1<<m)*rt)%(1<<nm)
        if count_cong(nr,1<<nm):
            nv=(gu*rt+gv)//(1<<a)
            assert nv&1
            stack.append((i+1,nr,nm,nv))

assert dict(state_counts)==EXPECTED_STATES,(state_counts,EXPECTED_STATES)
for i in range(36,43): assert fails[i]==EXPECTED_FAIL[i],(i,fails[i])
assert fail43==EXPECTED_FAIL[43],fail43
assert leaf43_surv==3_860_091_166,leaf43_surv
height_surv=leaf43_surv-fail43
assert height_surv==EXPECTED_HEIGHT_SURV_43,height_surv
# Same structural (i,m,h,u) state can have different exact finite-window counts.
assert 3 in examples and 4 in examples and examples[3][0]!=examples[4][0]
# Terminal-Hensel coupling remains disjoint through transition 43.
term_count=0
for rr in TERM_R:
    k=KMIN+((rr-KMIN)%MOD22)
    while k<=KMAX:
        term_count+=1
        assert terminal_fail_phase(k,43) is None
        k+=MOD22
assert term_count==1842
assert height_surv-term_count==EXPECTED_COMBINED
print('RL226 E4 LOSSLESS COMPRESSION / TRANSITION-43 CERTIFICATE: PASS')
print('compressed_state=(phase,residue,precision,intercept); slope,height derived exactly')
print('state_counts', ' '.join(f'{i}:{state_counts[i]}' for i in range(36,44)))
print('new_fail transition42',EXPECTED_FAIL[42],'transition43',EXPECTED_FAIL[43])
print('height_survivors_through_43',height_surv)
print('terminal_hensel_overlap_through_43 0')
print('combined_survivors',EXPECTED_COMBINED)
print('residue_barrier_example_counts 3_and_4_at_same_phase43_precision30')
