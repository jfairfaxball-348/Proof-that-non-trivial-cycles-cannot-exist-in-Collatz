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
K_LO=128_081_997_553
CLEAN=10_075_174_499
N35=7_559_400_754
N36=7_238_318_174
N37=7_052_720_272
U=Fraction(1,2**25)

assert A*p-L*u==1

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

@lru_cache(maxsize=None)
def exp_hi_at_rank(r):
    q=(p*r)//L
    xhi=r*s_hi+q*d_hi
    return exp_bounds_pos(xhi)[1]

def local_budget_U(T,H,rhi):
    generic=Fraction(2**(24-H),1)
    corridor=Fraction(K_LO*(2**25),T)
    rank_endpoint=Fraction(2**(25-H),1)/exp_hi_at_rank(rhi)
    return max(generic,corridor,rank_endpoint)

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

core_by_key_tau={}
for (T,H),rs in rows.items():
    terminal=Fraction(T,2**H)
    dct=defaultdict(list)
    for rr in rs:
        dct[rr[0]].extend(full_prefix_core(rr[-2],rr[-1],rr[0],terminal))
    md={}
    for tau,cs in dct.items():
        merged=[]
        for a,b in sorted(cs):
            if merged and a<=merged[-1][1]+1:
                merged[-1]=(merged[-1][0],max(merged[-1][1],b))
            else:
                merged.append((a,b))
        md[tau]=merged
    core_by_key_tau[(T,H)]=md

cells=[]
for (T,H),md in core_by_key_tau.items():
    points={0,L}
    for cs in md.values():
        for a,b in cs:
            points.add(a)
            points.add(b+1)
    ss=sorted(points)
    for a,b1 in zip(ss,ss[1:]):
        b=b1-1
        if a>b:
            continue
        owners=tuple(sorted(t for t,cs in md.items() if any(x<=a and b<=y for x,y in cs)))
        if owners:
            cells.append((T,H,a,b,owners))
cells=sorted(cells)
assert len(cells)==7531

def overlap_core(sep,lo,hi):
    sh=(sep*B)%L
    out=[]
    for k in range(-2,3):
        a=max(lo,lo-sh+k*L)
        b=min(hi,hi-sh+k*L)
        if a<=b:
            out.append((a,b))
    return out

def atom_params_fast(lo,hi,n):
    """Exact carry-word atom partition with lazy suffix powers-of-two updates.

    For a word c_0,...,c_{n-1}, the universal radius numerator is
      2 * sum_j 3^(n-1-j) * 2^(S_j),
    where S_j is the prefix carry sum before c_j.
    When x crosses one carry boundary only one c_j changes by +/-1, so
    every term after j is multiplied/divided by 2. A lazy segment tree
    updates that exact suffix and exposes the exact radius at its root.
    """
    if n==0:
        return [(lo,hi,0,0)]

    bits=[cbit((lo+j*B)%L) for j in range(n)]
    totalS=sum(bits)

    terms=[]
    pref=0
    p3=3**(n-1)
    for j in range(n):
        terms.append((2*p3) << pref)
        pref += bits[j]
        if j<n-1:
            p3//=3
    assert pref==totalS

    size=1
    while size<n:
        size*=2
    tree=[0]*(2*size)
    lazy=[0]*(2*size)
    for i,v in enumerate(terms):
        tree[size+i]=v
    for i in range(size-1,0,-1):
        tree[i]=tree[2*i]+tree[2*i+1]

    def apply(idx,delta):
        if delta>0:
            tree[idx] <<= delta
        elif delta<0:
            div=1<<(-delta)
            assert tree[idx] % div==0
            tree[idx] >>= -delta
        lazy[idx]+=delta

    def push(idx):
        d=lazy[idx]
        if d:
            apply(2*idx,d)
            apply(2*idx+1,d)
            lazy[idx]=0

    def range_shift(ql,qr,delta,idx=1,l=0,r=None):
        if r is None:
            r=size
        if qr<=l or r<=ql:
            return
        if ql<=l and r<=qr:
            apply(idx,delta)
            return
        push(idx)
        m=(l+r)//2
        range_shift(ql,qr,delta,2*idx,l,m)
        range_shift(ql,qr,delta,2*idx+1,m,r)
        tree[idx]=tree[2*idx]+tree[2*idx+1]

    events=defaultdict(list)
    for j in range(n):
        sh=(j*B)%L
        for q in (0,R):
            x=(q-sh)%L
            if lo<x<=hi:
                events[x].append(j)

    out=[]
    cur=lo
    for x in sorted(events):
        if cur<=x-1:
            out.append((cur,x-1,tree[1],totalS))
        for j in events[x]:
            newbit=cbit((x+j*B)%L)
            delta=newbit-bits[j]
            if delta:
                if j+1<n:
                    range_shift(j+1,n,delta)
                totalS += delta
                bits[j]=newbit
        cur=x
    if cur<=hi:
        out.append((cur,hi,tree[1],totalS))
    return out

def recurrence_scan(T,H,fam,core,start_sep,end_sep,expected_atoms,expected_nonempty):
    lo,hi=core
    tau=max(fam)
    rs=rows[(T,H)]
    targets=sorted(set(int(Fraction(rr[2],2**rr[1])) for rr in rs if rr[0]==tau))
    assert targets
    atoms=0
    nonempty=0
    for sep in range(start_sep,end_sep+1):
        ovs=overlap_core(sep,lo,hi)
        if not ovs:
            continue
        nonempty+=1
        n=sep-tau
        cnum=T*(3**n)
        for a,b in ovs:
            for x,y,radnum,S in atom_params_fast(a,b,n):
                denexp=H+S
                for target in targets:
                    distnum=abs(cnum-target*(1<<denexp))
                    rhs=radnum*(1<<H)
                    assert distnum>rhs
                atoms+=1
    assert atoms==expected_atoms
    assert nonempty==expected_nonempty
    return atoms,nonempty

H20_323334=(216_803_362_095_665_397,20,(32,33,34),(62_456_644_959,96_166_487_667))
H20_3136=(150_094_635_296_999_121,20,(31,32,33,34,35,36),(0,18_406_412_838))
H21_3435=(550_346_996_088_996_777,21,(34,35),(109_195_551_555,122_224_615_441))

for T,H,fam,core in (H20_323334,H20_3136,H21_3435):
    assert (T,H,core[0],core[1],fam) in cells

recurrence_scan(*H20_323334,35,209,1014,85)
recurrence_scan(*H20_3136,37,5596,278049,1486)
recurrence_scan(*H21_3435,36,3031,41039,569)

cap210=L//210
cap5597=L//5597
cap3032=L//3032
cap1001=L//1001
assert cap210==654_895_453
assert cap5597==24_571_742
assert cap3032==45_358_853
assert cap1001==137_390_654

target=(216_803_362_095_665_397,20,62_456_644_959,96_166_487_667,(32,33,34))
h20six=(150_094_635_296_999_121,20,0,18_406_412_838,(31,32,33,34,35,36))
h20four=(250_157_725_494_998_535,20,96_166_487_668,98_855_162_143,(32,33,34,35))
h21a=(350_220_815_692_997_949,21,23_369_453_298,41_775_866_136,(33,34,35))
h21b=(450_283_905_890_997_363,21,72_797_034_370,103_818_202_602,(34,35,36,37))
newh21=(550_346_996_088_996_777,21,109_195_551_555,122_224_615_441,(34,35))
h24=(4_052_555_153_018_976_267,24,96_166_487_668,111_884_226_030,(39,))
for c0 in (target,h20six,h20four,h21a,h21b,newh21,h24):
    assert c0 in cells

c=local_budget_U(h24[0],h24[1],h24[3])
a=local_budget_U(target[0],target[1],target[3])/3
b_corner=(local_budget_U(h20six[0],h20six[1],h20six[3])-4*a)/2
b=local_budget_U(newh21[0],newh21[1],newh21[3])-a
assert b>b_corner>c>0
assert 4*a+2*b_corner==local_budget_U(h20six[0],h20six[1],h20six[3])
assert a+b==local_budget_U(newh21[0],newh21[1],newh21[3])

def charge_U(owners):
    return sum(a if t<=34 else b if t in (35,36) else c for t in owners)

# First discharge every cell whose exact charge is within the generic
# height budget. Only the remaining generic-overage candidates require
# the more expensive exact local K-priced budget.
generic_over=[]
for cell in cells:
    T,H,rlo,rhi,owners=cell
    if charge_U(owners)>Fraction(2**(24-H),1):
        generic_over.append(cell)
assert len(generic_over)==17

over=[]
binding=[]
for cell in generic_over:
    T,H,rlo,rhi,owners=cell
    ch=charge_U(owners)
    bud=local_budget_U(T,H,rhi)
    if ch>bud:
        over.append(cell)
    elif ch==bud:
        binding.append(cell)

expected_over=[h20six,h20four,h21a,h21b]
expected_binding=[target,newh21,h24]
assert over==sorted(expected_over)
assert binding==sorted(expected_binding)

caps={
    h20six:cap5597,
    h20four:cap3032,
    h21a:cap1001,
    h21b:cap1001,
}
penalty=Fraction(0)
for cell in over:
    T,H,rlo,rhi,owners=cell
    penalty += (charge_U(owners)-local_budget_U(T,H,rhi))*caps[cell]

early=CLEAN-N35
middle=(N35-N36)+(N36-N37)
late=N37
assert early==2_515_773_745
assert middle==506_680_482
assert late==7_052_720_272

ordinary=U*(early*a+middle*b+late*c-penalty)
assert ordinary>Fraction(7_424_232,10_000)
assert ordinary/2>Fraction(3_712_116,10_000)
assert ordinary/6>Fraction(1_237_372,10_000)

slope_b=middle-cap3032-2*cap5597-cap1001-2*cap1001
assert slope_b==6183
assert slope_b-6182>0
assert slope_b-6183==0
threshold=L//6183+1
assert threshold==22_242_932
assert L//(threshold-1)==6183
assert L//threshold==6182

# The final H21 returnability scan is promoted only as a spacing theorem.
# Its cap is far too large to reopen the saturated b-direction.
assert cap3032>6182

print("PASS: RL237 recurrence, full-cell charging and saturation certificate")
print("full_prefix_atomic_cells=7531")
print("H20_323334_spacing_ge=210 cap=654895453 atoms=1014 nonempty=85")
print("H20_3136_spacing_ge=5597 cap=24571742 atoms=278049 nonempty=1486")
print("H21_3435_spacing_ge=3032 cap=45358853 atoms=41039 nonempty=569")
print("final_overbudget_cells=4 final_binding_cells=3")
print("final_early_charge_U_approx=%.12f" % float(a))
print("final_middle_charge_U_approx=%.12f" % float(b))
print("final_late_charge_U_approx=%.12f" % float(c))
print("ordinary_abs_flow_approx=%.12f" % float(ordinary))
print("ordinary_abs_flow_gt_742_4232=yes")
print("each_signed_flow_gt_371_2116=yes")
print("each_directional_K_variation_gt_123_7372=yes")
print("uncapped_H21_3435_crossing_slope_before_cap=6183")
print("H21_3435_cap_needed_le=6182")
print("H21_3435_spacing_needed_for_further_charge=22242932")
print("charging_program_frozen_for_RL238_pivot=yes")
