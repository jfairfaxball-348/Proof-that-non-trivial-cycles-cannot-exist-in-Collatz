#!/usr/bin/env python3
from fractions import Fraction
from collections import defaultdict
from functools import lru_cache

A=217_976_794_617
L=137_528_045_312
p=65_470_613_321
u=103_768_467_013
B=A-L
R=L-B
GAP_LOWER=128_081_997_553
GAP_UPPER=293_591_818_782
K0=2**37
K_LO=128_081_997_553
K_HI=146_795_909_391
W_UPPER=28_070_867_755
CLEAN=10_075_174_499
N35=7_559_400_754
N36=7_238_318_174
N37=7_052_720_272

assert A*p-L*u==1
assert B==80_448_749_305
assert R==57_079_296_007
assert K0-K_LO==K_HI-K0==9_356_955_919
assert 3*(K0-K_LO)==28_070_867_757==W_UPPER+2

def ceil_div(a,b): return (a+b-1)//b
def v2(x): return (x & -x).bit_length()-1
def cbit(r): return 1 if r<R else 2

def ln_bounds_int(x,N=100):
    x=Fraction(x)
    z=(x-1)/(x+1)
    z2=z*z
    term=z
    s=Fraction(0)
    for n in range(N):
        s += term/Fraction(2*n+1)
        term *= z2
    lo=2*s
    tail=2*term/Fraction(2*N+1)/(1-z2)
    return lo,lo+tail

@lru_cache(maxsize=None)
def exp_bounds_pos(x,N=50):
    assert 0<=x<1
    term=Fraction(1)
    s=term
    for k in range(1,N+1):
        term=term*x/k
        s += term
    nxt=term*x/Fraction(N+1)
    tail=nxt/(1-x/Fraction(N+2))
    return s,s+tail

l2_lo,l2_hi=ln_bounds_int(2)
l3_lo,l3_hi=ln_bounds_int(3)
d_lo=A*l2_lo-L*l3_hi
d_hi=A*l2_hi-L*l3_lo
s_lo=p*l3_lo-u*l2_hi
s_hi=p*l3_hi-u*l2_lo
assert 0<d_lo<d_hi<Fraction(1,1000)
assert 0<s_lo<s_hi<Fraction(1,1000)

_,eds_hi=exp_bounds_pos(d_hi+s_hi)
_,ed_hi=exp_bounds_pos(d_hi)
Nminus_hi=eds_hi*W_UPPER
F2_hi=3*K0*(ed_hi-1)
Nplus_hi=Nminus_hi+F2_hi
assert Nminus_hi < W_UPPER+Fraction(1,6)
assert F2_hi < Fraction(3,8)
assert Nplus_hi < W_UPPER+Fraction(13,24)

late_max={j:(0 if j==0 else ceil_div(j*B,L)) for j in range(40)}
height_envelope={j:1+late_max[j] for j in range(40)}
rows=defaultdict(list)
for tau in range(26,40):
    ell0=(tau*B)//L
    ell1=ceil_div(tau*B,L)
    for h0 in (0,1):
        lo=GAP_LOWER*(2**h0)
        hi=GAP_UPPER*(2**h0)
        step=2**tau
        for k in range(lo//step+1,(hi-1)//step+1):
            C0=k*step
            vv=v2(C0)
            odd=C0>>vv
            T=(3**tau)*odd
            for ell in sorted({ell0,ell1}):
                H=h0+tau+ell-vv
                if H<1 or H>height_envelope[tau]:
                    continue
                if not (GAP_LOWER*(2**H)<T<GAP_UPPER*(2**H)):
                    continue
                rlo=max(0,tau*B-ell*L)
                rhi=min(L-1,tau*B-(ell-1)*L-1)
                if rlo<=rhi:
                    rows[(T,H)].append((tau,h0,C0,vv,odd,ell,rlo,rhi))

def maximal_sets_for_height(H):
    seen=set()
    for (T,H0),rs in rows.items():
        if H0!=H:
            continue
        points={0}
        for rr in rs:
            points.add(rr[-2])
            if rr[-1]+1<L:
                points.add(rr[-1]+1)
        for r in points:
            S=frozenset(rr[0] for rr in rs if rr[-2]<=r<=rr[-1])
            if S:
                seen.add(S)
    return {tuple(sorted(s)) for s in seen if not any(s<t for t in seen)}

assert maximal_sets_for_height(17)=={
    (26,27,28,29,30,31,32),
    (27,28,29,30,31,32,33),
}
assert maximal_sets_for_height(18)=={(28,29,30,31,32,33,34,35)}
assert maximal_sets_for_height(19)=={
    (30,31,32,33,34),
    (31,32,33,34,35,36),
}
assert maximal_sets_for_height(20)=={(31,32,33,34,35,36)}
assert maximal_sets_for_height(21)=={
    (33,34,35),
    (34,35,36,37),
}

def word_before_terminal(r_terminal,n):
    return tuple(cbit((r_terminal-(n-j)*B)%L) for j in range(n))

def backward_gaps(word,terminal):
    ds=[None]*(len(word)+1)
    ds[-1]=terminal
    for j in range(len(word)-1,-1,-1):
        ds[j]=ds[j+1]*(2**word[j])/3
    return tuple(ds)

def full_prefix_core(rawlo,rawhi,tau,terminal):
    bounds={rawlo,rawhi+1}
    for j in range(tau):
        shift=(tau-j)*B
        for threshold in (0,R):
            q=(threshold+shift)%L
            if rawlo<q<=rawhi:
                bounds.add(q)
    bounds=sorted(bounds)
    good=[]
    for x,y in zip(bounds,bounds[1:]):
        lo,hi=x,y-1
        if lo>hi:
            continue
        w=word_before_terminal(lo,tau)
        assert word_before_terminal(hi,tau)==w
        ds=backward_gaps(w,terminal)
        if all(Fraction(GAP_LOWER)<d<Fraction(GAP_UPPER) for d in ds):
            good.append((lo,hi))
    merged=[]
    for lo,hi in good:
        if merged and merged[-1][1]+1==lo:
            merged[-1]=(merged[-1][0],hi)
        else:
            merged.append((lo,hi))
    return merged

def family_candidate(H,fam):
    candidates=[]
    for (T,H0),rs in rows.items():
        if H0!=H:
            continue
        if not set(fam)<=set(rr[0] for rr in rs):
            continue
        intervals=[]
        for tau in fam:
            tr=[rr for rr in rs if rr[0]==tau]
            intervals.append((min(rr[-2] for rr in tr),max(rr[-1] for rr in tr)))
        rawlo=max(a for a,b in intervals)
        rawhi=min(b for a,b in intervals)
        if rawlo<=rawhi:
            candidates.append((T,rs))
    assert len(candidates)==1
    T,rs=candidates[0]
    terminal=Fraction(T,2**H)
    tau_cores=[]
    for tau in fam:
        cs=[]
        for rr in rs:
            if rr[0]==tau:
                cs.extend(full_prefix_core(rr[-2],rr[-1],tau,terminal))
        cs.sort()
        merged=[]
        for a,b in cs:
            if merged and a<=merged[-1][1]+1:
                merged[-1]=(merged[-1][0],max(merged[-1][1],b))
            else:
                merged.append((a,b))
        tau_cores.append(merged)
    points={0,L}
    for cs in tau_cores:
        for a,b in cs:
            points.add(a); points.add(b+1)
    common=[]
    ss=sorted(points)
    for a,b in zip(ss,ss[1:]):
        hi=b-1
        if a<=hi and all(any(x<=a and hi<=y for x,y in cs) for cs in tau_cores):
            common.append((a,hi))
    merged=[]
    for a,b in common:
        if merged and a<=merged[-1][1]+1:
            merged[-1]=(merged[-1][0],b)
        else:
            merged.append((a,b))
    return T,merged

specs={
"H21_333435":(21,(33,34,35),350_220_815_692_997_949,(23_369_453_298,41_775_866_136)),
"H21_34353637":(21,(34,35,36,37),450_283_905_890_997_363,(72_797_034_370,103_818_202_602)),
"H20_3136":(20,(31,32,33,34,35,36),150_094_635_296_999_121,(0,18_406_412_838)),
"H19_3034":(19,(30,31,32,33,34),83_385_908_498_332_845,(15_717_738_363,46_738_906_595)),
"H19_3136":(19,(31,32,33,34,35,36),150_094_635_296_999_121,(129_876_330_377,137_528_045_311)),
"H18_2835":(18,(28,29,30,31,32,33,34,35),50_031_545_098_999_707,(49_427_581_072,52_116_255_547)),
"H17_A":(17,(26,27,28,29,30,31,32),20_383_222_077_370_251,(5_377_348_952,28_746_802_249)),
"H17_B":(17,(27,28,29,30,31,32,33),27_795_302_832_777_615,(72_797_034_370,103_818_202_602)),
}
for name,(H,fam,T_expected,core_expected) in specs.items():
    T,core=family_candidate(H,fam)
    assert T==T_expected
    assert core==[core_expected]

rD=41_775_866_136
qD=(p*rD)//L
xD_hi=rD*s_hi+qD*d_hi
_,exD_hi=exp_bounds_pos(xD_hi)
deltaD=Fraction(350_220_815_692_997_949,2**21)
Kstar=2**37-2**31
assert deltaD/exD_hi > Kstar

r20=18_406_412_838
q20=(p*r20)//L
x20_hi=r20*s_hi+q20*d_hi
_,ex20_hi=exp_bounds_pos(x20_hi)
delta20=Fraction(150_094_635_296_999_121,2**20)
assert delta20/ex20_hi > 130_459_631_616

def overlap_core(sep,lo,hi):
    sh=(sep*B)%L
    out=[]
    for k in range(-2,3):
        a=max(lo,lo-sh+k*L)
        b=min(hi,hi-sh+k*L)
        if a<=b:
            out.append((a,b))
    return out

def atom_intervals(lo,hi,n):
    bounds={lo,hi+1}
    for j in range(n):
        shift=(j*B)%L
        for q in (0,R):
            x=(q-shift)%L
            if lo<x<=hi:
                bounds.add(x)
    bounds=sorted(bounds)
    return [(a,b-1) for a,b in zip(bounds,bounds[1:]) if a<=b-1]

def universal_params(word):
    radnum=0
    S=0
    for c in word:
        radnum=3*radnum+2*(1<<S)
        S+=c
    return radnum,S

def recurrence_scan(key,start_sep,end_sep,expected_atoms,expected_nonempty,margin_floor):
    H,fam,T,core=specs[key]
    lo,hi=core
    tau=max(fam)
    rs=rows[(T,H)]
    targets=sorted(set(int(Fraction(rr[2],2**rr[1])) for rr in rs if rr[0]==tau))
    atoms=0
    nonempty=0
    min_margin=None
    worst=None
    for sep in range(start_sep,end_sep+1):
        ovs=overlap_core(sep,lo,hi)
        if ovs:
            nonempty+=1
        n=sep-tau
        p3=3**n
        for a,b in ovs:
            for x,y in atom_intervals(a,b,n):
                w=tuple(cbit((x+j*B)%L) for j in range(n))
                assert tuple(cbit((y+j*B)%L) for j in range(n))==w
                radnum,S=universal_params(w)
                denexp=H+S
                cnum=T*p3
                for target in targets:
                    distnum=abs(cnum-target*(1<<denexp))
                    rhs=radnum*(1<<H)
                    assert distnum>rhs
                    margin=Fraction(distnum-rhs,1<<denexp)
                    if min_margin is None or margin<min_margin:
                        min_margin=margin
                        worst=(sep,x,y,target,S)
                atoms+=1
    assert atoms==expected_atoms
    assert nonempty==expected_nonempty
    assert min_margin>margin_floor
    return min_margin,worst

m21a,w21a=recurrence_scan("H21_333435",36,1000,8610,258,10_499_297)
m20,w20=recurrence_scan("H20_3136",37,1000,8609,257,5_999_587)
m19a,w19a=recurrence_scan("H19_3034",35,1000,24178,436,7_499_467)
m19b,w19b=recurrence_scan("H19_3136",37,1000,1556,108,11_999_231)
m18,w18=recurrence_scan("H18_2835",36,3031,1829,118,11_999_245)
m21b,w21b=recurrence_scan("H21_34353637",46,1000,24173,432,5_999_580)

U=Fraction(1,2**25)
x=Fraction(128,7)*U
y=Fraction(4,3)*U
wlong=U
early=CLEAN-N35
tau35=N35-N36
tau36=N36-N37
assert early==2_515_773_745
assert tau35==321_082_580
assert tau36==185_597_902
cap1001=L//1001
cap3032=L//3032
assert cap1001==137_390_654
assert cap3032==45_358_853

def charge(t):
    if t<=34: return x
    if t in (35,36): return y
    return wlong

expected_tail={
28:(7,8,9,10,11,12,13,14,15,16,17,18),
29:(8,9,10,11,12,13,14,15,16,17,18),
30:(10,12,13,14,15,16,17,18,19),
31:(12,13,14,15,16,17,18,19,20),
32:(13,15,16,17,18,19,20),
33:(15,16,17,18,19,20,21),
34:(16,18,19,20,21),
35:(18,19,20,21,22),
36:(19,20,21,22),
37:(21,23),38:(23,),39:(24,),
}
allowed={}
for t in range(40):
    allowed[t]=tuple(range(1,height_envelope[t]+1)) if t<28 else expected_tail[t]
for H in range(1,17):
    assert sum(charge(t) for t in range(40) if H in allowed[t]) <= Fraction(1,2**(H+1))

assert 7*x==Fraction(1,2**18)

joint={
"H18_2835":(18,(28,29,30,31,32,33,34,35),cap3032),
"H19_3034":(19,(30,31,32,33,34),cap1001),
"H19_3136":(19,(31,32,33,34,35,36),cap1001),
"H20_3136":(20,(31,32,33,34,35,36),cap1001),
"H21_333435":(21,(33,34,35),cap1001),
"H21_34353637":(21,(34,35,36,37),cap1001),
}
penalty=Fraction(0)
for key,(H,fam,cap) in joint.items():
    lhs=sum(charge(t) for t in fam)
    budget=Fraction(1,2**(H+1))
    assert lhs>budget
    penalty += (lhs-budget)*cap

assert 2*y <= Fraction(1,2**23)
assert 2*wlong <= Fraction(1,2**24)
assert wlong <= Fraction(1,2**25)

nominal=early*x+tau35*y+tau36*y+N37*wlong
ordinary_floor=nominal-penalty
assert ordinary_floor==Fraction(234_578_279_671,352_321_536)
assert ordinary_floor>665
signed_floor=ordinary_floor/2
kdir_floor=ordinary_floor/6
assert signed_floor>332
assert kdir_floor>110

slope=early-(7*cap3032+(5+4+4+2+1)*cap1001)
assert slope==11_310
assert slope-7*1615>0
assert slope-7*1616<0
min_combined_spacing_for_1615=L//1616+1
assert min_combined_spacing_for_1615==85_103_989

print("PASS: RL231 chronological renewal / sparse-blocker verifier")
print("fixed_origin_sign_order_escape_impossible=yes")
print("H21_D_K_gt=135291469824")
print("H21_333435_spacing_ge=1001")
print("H20_3136_spacing_ge=1001")
print("H19_3034_spacing_ge=1001")
print("H19_3136_spacing_ge=1001")
print("H18_2835_spacing_ge=3032")
print("H17_exact_maximal_families=2")
print("ordinary_abs_flow_gt=234578279671/352321536")
print("ordinary_abs_flow_gt_665=yes")
print("each_signed_flow_gt=234578279671/704643072")
print("each_directional_K_variation_gt=234578279671/2113929216")
print("further_uniform_charge_requires_combined_H17_incidence_le=1615")
print("spacing_only_combined_H17_requirement_ge=85103989")
