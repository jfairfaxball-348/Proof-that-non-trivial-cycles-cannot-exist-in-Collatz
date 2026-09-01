#!/usr/bin/env python3
from math import gcd
from collections import Counter
A=217_976_794_617
L=137_528_045_312
LO=24_913_843_845_551_577_787_381
HI=31_285_589_992_934_194_300_574
BASE=1_267_492_570_907
STEP=1_649_267_441_664
KMIN=15_106_005_985
KMAX=18_969_385_559
N=3_863_379_575
MOD22=1<<22
TERM_R=(801_774,1_785_623)
EXPECTED_FAIL={36:3684,37:18422,38:105924,39:203794,40:713558,41:943078}
EXPECTED_SURV={36:3863375891,37:3863357469,38:3863251545,39:3863047751,40:3862334193,41:3861391115}

def b(i): return A*i//L
def v2(n): return (n & -n).bit_length()-1

def count_cong(r,m):
    first=KMIN+((r-KMIN)%m)
    return 0 if first>KMAX else (KMAX-first)//m+1

def sol(gu,gv,power):
    M=1<<power; g=gcd(abs(gu),M)
    if gv%g: return None
    Md=M//g
    if Md==1:return (0,0)
    rr=(-(gv//g)*pow((gu//g)%Md,-1,Md))%Md
    return rr,Md.bit_length()-1

def trans(st):
    i,r,m,u,v,h=st; c=b(i+1)-b(i); cap=c+h
    gu=3*u; gv=3*v+1; out=[]
    for a in range(1,cap+1):
        sa=sol(gu,gv,a); sb=sol(gu,gv,a+1)
        if sa is None: continue
        ra,da=sa
        if sb is None: ex=((ra,da),)
        else:
            rb,db=sb
            if da==db: ex=()
            else:
                ex=[]
                for x in range(1<<(db-da)):
                    rr=(ra+(x<<da))%(1<<db)
                    if rr!=rb%(1<<db): ex.append((rr,db))
        for rt,dt in ex:
            nm=m+dt; nr=r+(1<<m)*rt
            if nm:nr%=1<<nm
            if count_cong(nr,1<<nm if nm else 1):
                out.append((i+1,nr,nm,(gu*(1<<dt))//(1<<a),(gu*rt+gv)//(1<<a),cap-a))
    sf=sol(gu,gv,cap+1); fail=0
    if sf is not None:
        rf,df=sf; fm=m+df; fr=r+(1<<m)*rf
        if fm: fr%=1<<fm
        fail=count_cong(fr,1<<fm if fm else 1)
    return out,fail

# exact RL211 affine bridge
assert STEP==3*(1<<39)
assert (LO-BASE+STEP-1)//STEP==KMIN
assert (HI-BASE)//STEP==KMAX
assert KMAX-KMIN+1==N
assert BASE+STEP*KMIN==24_913_843_845_909_514_929_947
assert BASE+STEP*KMAX==31_285_589_992_097_449_101_083
# terminal hensel
inv=pow(3**34,-1,MOD22); assert inv==1_893_305
assert ((inv-207)*pow(243,-1,MOD22))%MOD22==TERM_R[0]
assert ((inv-21-207)*pow(243,-1,MOD22))%MOD22==TERM_R[1]
assert sum(count_cong(r,MOD22) for r in TERM_R)==1842
# fixed trajectory to phase 36
u=STEP; v=BASE; h=0
fixed=[]
for i in range(36):
    eu=3*u; ev=3*v+1; qv=v2(ev); qu=v2(eu)
    assert qv<qu
    a=qv; fixed.append(a); h=b(i+1)-b(i)+h-a; assert h>=0
    u=eu>>a; v=ev>>a
assert fixed[:4]==[1,2,1,1]
assert fixed[4:35]==[1]*31
assert fixed[35]==2
assert h==19 and u==900_567_811_781_994_726 and v==692_103_040_536_162_613
states=[(36,0,0,u,v,h)]
for phase in range(36,42):
    ns=[]; fail=0
    for st in states:
        ch,ff=trans(st); ns.extend(ch); fail+=ff
    states=ns
    surv=sum(count_cong(st[1],1<<st[2] if st[2] else 1) for st in states)
    assert fail==EXPECTED_FAIL[phase],(phase,fail)
    assert surv==EXPECTED_SURV[phase],(phase,surv)
# terminal bad candidates are disjoint from height failures through 41
def fail_phase(k,maxp=41):
    eta=207+243*k
    y4=(1<<34)*eta-1-81*(1<<32)
    y=((1<<5)*y4-85)//81
    hh=0
    for i in range(maxp+1):
        a=v2(3*y+1); nh=b(i+1)-b(i)+hh-a
        if nh<0:return i
        y=(3*y+1)>>a; hh=nh
    return None
for rr in TERM_R:
    k=KMIN+((rr-KMIN)%MOD22)
    while k<=KMAX:
        assert fail_phase(k) is None
        k+=MOD22
assert N-1_988_460-1_842==3_861_389_273
print('RL225 e4 transfer verifier: PASS')
print('raw candidates',N)
print('terminal Hensel deletions',1842)
print('height deletions through transition 41',1_988_460)
print('combined survivors',3_861_389_273)
