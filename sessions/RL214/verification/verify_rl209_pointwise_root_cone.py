#!/usr/bin/env python3
from decimal import Decimal, getcontext
from functools import lru_cache
import json

A=217_976_794_617
L=137_528_045_312
B=A-L
p=65_470_613_321
z=L-p
K0=2**37
DLO,DHI=25_583_192_106,41_775_866_136
N0=2**24
M=2**35
FINE=4096
COARSE=64
SAFE0_LO,SAFE0_HI=38_643_145_224,38_659_291_956
CURRENT_TOTAL=13_423_606_911
CURRENT_ABOVE=7_099_572_324
CURRENT_BELOW=6_324_034_587
EXPECTED_ROOT=983
EXPECTED_ROOT_REMAIN=986
EXPECTED_OCTAVES=[13,63,241,970,3893,15517,62044,248182,740166,1925308,4743660]
EXPECTED_NEW=7_741_040
EXPECTED_ABOVE=7_091_831_284
EXPECTED_TOTAL=13_415_865_871
OLD_DELETIONS={
26_058_127_773,26_058_127_774,28_746_802_249,28_746_802_250,
31_435_476_726,34_124_151_202,36_398_517_184,36_398_517_185,
36_812_825_678,39_087_191_660,39_087_191_661,41_775_866_136,
}
ANCHOR_DELETIONS={26_058_127_775,28_746_802_251,36_398_517_186,39_087_191_662}
DISCRETE=OLD_DELETIONS|ANCHOR_DELETIONS

# Rigorous fixed-point logarithm enclosures.  SCALE is deliberately much finer
# than any crossing margin; every sign used below is certified by integer bounds.
SCALE=1<<192

def _floor_div(a,b): return a//b

def _ceil_div(a,b): return -((-a)//b)

@lru_cache(maxsize=None)
def ln_scaled(num,den,terms=24):
    assert num>0 and den>0
    # ln(x)=2*atanh(t), t=(x-1)/(x+1).
    tn=num-den; td=num+den
    neg=tn<0
    an=abs(tn)
    if an==0: return (0,0)
    # Exact rational partial sum, accumulated as conservative scaled floors/ceilings.
    lo=hi=0
    npow=an
    dpow=td
    n2=an*an; d2=td*td
    for k in range(terms):
        qden=dpow*(2*k+1)
        qnum=2*npow*SCALE
        tlo=_floor_div(qnum,qden)
        thi=_ceil_div(qnum,qden)
        lo += tlo; hi += thi
        npow*=n2; dpow*=d2
    # Tail <= 2*t^(2m+1)/((2m+1)*(1-t^2)); add outward.
    m=terms
    tail_num=2*npow*d2*SCALE
    tail_den=(2*m+1)*dpow*(d2-n2)
    tail=_ceil_div(tail_num,tail_den)
    hi += tail
    if neg:
        return (-hi,-lo)
    return (lo,hi)

LN2=ln_scaled(2,1,90)
LN3=ln_scaled(3,1,130)
LN87=ln_scaled(8,7,40)

def mul_interval(c,iv):
    a,b=iv
    return (c*a,c*b) if c>=0 else (c*b,c*a)

def add_intervals(*ivs):
    return sum(x[0] for x in ivs),sum(x[1] for x in ivs)

@lru_cache(maxsize=None)
def log_k_over_u_scaled(r,u_num,u_den=1):
    i=p*r%L
    n=(A*i-r)//L
    assert A*i==n*L+r
    U=ln_scaled(u_num,u_den*K0,24)
    return add_intervals(
        mul_interval(n-55,LN2),
        mul_interval(35-i,LN3),
        (-LN87[1],-LN87[0]),
        (-U[1],-U[0]),
    )

getcontext().prec=75
D2=Decimal(2).ln(); D3=Decimal(3).ln(); D87=(Decimal(8)/Decimal(7)).ln()

def dec_log_k_over_u(r,u_num,u_den=1):
    i=p*r%L
    n=(A*i-r)//L
    u=Decimal(u_num)/Decimal(u_den)
    return Decimal(n-55)*D2+Decimal(35-i)*D3-D87-(u/Decimal(K0)).ln()

def certified_first_below(u_num,u_den=1):
    # Decimal only proposes the monotone crossing; fixed-point intervals certify it.
    du=(Decimal(u_num)/Decimal(u_den*K0)).ln()
    lo,hi=DLO,DHI+1
    while lo<hi:
        mid=(lo+hi)//2
        i=p*mid%L
        n=(A*i-mid)//L
        v=Decimal(n-55)*D2+Decimal(35-i)*D3-D87-du
        if v<0: hi=mid
        else: lo=mid+1
    c=lo
    if c>DLO:
        a,b=log_k_over_u_scaled(c-1,u_num,u_den); assert a>0
    if c<=DHI:
        a,b=log_k_over_u_scaled(c,u_num,u_den); assert b<0
    return c

@lru_cache(maxsize=None)
def safe_band_common(N):
    # RL208 inherited common-radius band: (K0-N/3, K0+1+N/3).
    low_num=3*K0-N; high_num=3*(K0+1)+N
    return certified_first_below(high_num,3), certified_first_below(low_num,3)-1

@lru_cache(maxsize=None)
def safe_band_tight(N):
    # RL209 theorem: K0+1/9-N/3 < K_i < K0+1/8+N/3.
    low_num=9*K0+1-3*N
    high_num=24*K0+3+8*N
    assert low_num>0
    return certified_first_below(high_num,24), certified_first_below(low_num,9)-1

def floor_sum(n,m,a,b):
    assert n>=0 and m>0 and a>=0 and b>=0
    ans=0
    if a>=m:
        ans+=(n-1)*n*(a//m)//2; a%=m
    if b>=m:
        ans+=n*(b//m); b%=m
    while True:
        y=a*n+b
        if y<m:return ans
        n=y//m;b=y%m;m,a=a,m
        if a>=m:
            ans+=(n-1)*n*(a//m)//2;a%=m
        if b>=m:
            ans+=n*(b//m);b%=m

def count_mod_less(start,n,y):
    if y<=0:return 0
    if y>=L:return n
    bb=B*start
    ge=floor_sum(n,L,B,bb+L-y)-floor_sum(n,L,B,bb)
    return n-ge

def count_mod_interval(start,n,lo,hi):
    if lo>hi:return 0
    return count_mod_less(start,n,hi+1)-count_mod_less(start,n,lo)

def coarse_band_for_fine_outer(k,N):
    base=1<<k; step=base//COARSE
    j=(N-base+step-1)//step
    assert 1<=j<=COARSE
    Nc=base+j*step
    return safe_band_common(Nc)

def excluded_parts(cur_lo,cur_hi,new_lo,new_hi):
    out=[]
    if cur_lo<=min(cur_hi,new_lo-1):out.append((cur_lo,min(cur_hi,new_lo-1)))
    if max(cur_lo,new_hi+1)<=cur_hi:out.append((max(cur_lo,new_hi+1),cur_hi))
    return out

def discrete_hits(start,n,parts):
    hits=[]
    for r in DISCRETE:
        if any(a<=r<=b for a,b in parts):
            i=p*r%L
            if start<=i<start+n:hits.append(r)
    return hits

def main():
    assert A*p-103_768_467_013*L==1
    assert p*B%L==1 and z==72_057_431_991
    # Strict lambda anchor bracket K0+1/9 < K_L < K0+1/8.
    delta_lo=A*LN2[0]-L*LN3[1]
    delta_hi=A*LN2[1]-L*LN3[0]
    l9=ln_scaled(9*K0+1,9*K0,24)
    l8=ln_scaled(8*K0+1,8*K0,24)
    assert l9[1] < delta_lo < delta_hi < l8[0]
    assert 0<delta_lo

    # RL209 exact pointwise consumption inside the inherited backward root window.
    root_survivors=root_deleted=0
    root_remaining=[]
    i=p*SAFE0_LO%L
    for r in range(SAFE0_LO,SAFE0_HI+1):
        if i>=L-N0 and r not in DISCRETE:
            root_survivors+=1
            d=L-i
            low_num=9*K0+1-3*d
            high_num=24*K0+3+8*d
            # Outside if K<=lower or K>=upper; strict crossing intervals certify signs.
            up=log_k_over_u_scaled(r,high_num,24)
            low=log_k_over_u_scaled(r,low_num,9)
            if up[0]>0 or low[1]<0:
                root_deleted+=1
            else:
                assert up[1]<0 and low[0]>0
                root_remaining.append((r,i,d))
        i+=p
        if i>=L:i-=L
    assert root_survivors==1969
    assert root_deleted==EXPECTED_ROOT
    assert len(root_remaining)==EXPECTED_ROOT_REMAIN

    # Independent signed-successor red team on the exact pointwise root survivors.
    # K_(i+1)=K_i*(1+sigma*(2^nu-1)/(3T)); every one of the 42 inherited
    # sign/valuation pairs remains inside the independently anchored next-phase corridor.
    T=7*3**35
    mult={}
    for sig in (-1,1):
        for nu in range(1,22):
            num=3*T + sig*(2**nu-1)
            mult[(sig,nu)]=ln_scaled(num,3*T,16)
    successor_pairs_checked=0
    for r,i,d in root_remaining:
        base=log_k_over_u_scaled(r,K0,1)
        low_num=9*K0+1-3*(d-1)
        high_num=24*K0+3+8*(d-1)
        ll=ln_scaled(low_num,9*K0,24)
        uu=ln_scaled(high_num,24*K0,24)
        for sig in (-1,1):
            for nu in range(1,22):
                mm=mult[(sig,nu)]
                v=(base[0]+mm[0],base[1]+mm[1])
                assert v[0]>ll[1] and v[1]<uu[0]
                successor_pairs_checked+=1
    assert successor_pairs_checked==EXPECTED_ROOT_REMAIN*42

    octave_counts=[]
    total=root_deleted
    all_discrete=[]
    # 4096-way refinement of every RL208 backward dyadic band.  The fine outer
    # radius gives a valid pointwise consequence and each interval is disjoint.
    for k in range(24,35):
        base=1<<k; step=base//FINE; prev=base; subtotal=0
        for j in range(1,FINE+1):
            N=base+j*step
            cur_lo,cur_hi=coarse_band_for_fine_outer(k,N)
            new_lo,new_hi=safe_band_tight(N)
            assert new_lo>=cur_lo and new_hi<=cur_hi
            parts=excluded_parts(cur_lo,cur_hi,new_lo,new_hi)
            start=L-N; n=N-prev
            hits=discrete_hits(start,n,parts)
            all_discrete.extend(hits)
            cnt=sum(count_mod_interval(start,n,a,b) for a,b in parts)-len(hits)
            subtotal+=cnt
            prev=N
        octave_counts.append(subtotal); total+=subtotal
    assert all_discrete==[]
    assert octave_counts==EXPECTED_OCTAVES
    assert total==EXPECTED_NEW
    assert CURRENT_ABOVE-total==EXPECTED_ABOVE
    assert CURRENT_TOTAL-total==EXPECTED_TOTAL
    assert EXPECTED_TOTAL==EXPECTED_ABOVE+CURRENT_BELOW

    out={
      "status":"PASS",
      "classification":"exact finite above-p rank-exclusion certificate from RL209 pointwise root-anchor theorem",
      "lambda_K0_lower_increment":"1/9",
      "lambda_K0_upper_increment":"1/8",
      "old_backward_root_current_survivors":root_survivors,
      "old_backward_root_pointwise_exclusions":root_deleted,
      "old_backward_root_pointwise_remaining":len(root_remaining),
      "signed_successor_pairs_checked_on_root_remaining":successor_pairs_checked,
      "signed_successor_root_selector":"NONE: all 42 sign/valuation pairs survive each pointwise root survivor",
      "fine_subdivisions_per_rl208_octave":FINE,
      "fine_layer_count":11*FINE,
      "octave_new_exclusions":octave_counts,
      "new_above_p_rank_exclusions":total,
      "incoming_above_p_count":CURRENT_ABOVE,
      "remaining_above_p_count":EXPECTED_ABOVE,
      "below_p_count_unchanged":CURRENT_BELOW,
      "incoming_total_count":CURRENT_TOTAL,
      "remaining_total_count":EXPECTED_TOTAL,
      "preexisting_discrete_deletion_hits":len(all_discrete),
      "eta_classes_removed":0,
      "sign_or_valuation_selected":False,
      "physical_realization_claimed":False,
      "h21_charge_claimed":False,
      "gate_closure_claimed":False,
    }
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
