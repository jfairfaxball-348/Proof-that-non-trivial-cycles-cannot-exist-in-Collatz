#!/usr/bin/env python3
from fractions import Fraction as Q
from functools import lru_cache
from math import log
import json

A=217_976_794_617
L=137_528_045_312
B=A-L
p=65_470_613_321
z=L-p
K0=2**37
DLO,DHI=25_583_192_106,41_775_866_136
N0=2**24
SUBDIV=64
OLD_DELETIONS={
26_058_127_773,26_058_127_774,28_746_802_249,28_746_802_250,
31_435_476_726,34_124_151_202,36_398_517_184,36_398_517_185,
36_812_825_678,39_087_191_660,39_087_191_661,41_775_866_136,
}
ANCHOR_DELETIONS={26_058_127_775,28_746_802_251,36_398_517_186,39_087_191_662}
INHERITED_COUNT=16_188_727_234
EXPECTED_NEW=2_765_120_323
EXPECTED_REMAINING=13_423_606_911

@lru_cache(maxsize=None)
def ln_bounds(x, terms=110):
    x=Q(x); assert x>0
    t=(x-1)/(x+1); t2=t*t; term=t; partial=Q(0)
    for j in range(terms):
        partial += term/(2*j+1); term *= t2
    partial *= 2
    tail=2*abs(term)/((2*terms+1)*(1-t2))
    return (partial,partial+tail) if t>=0 else (partial-tail,partial)

def mul(c,b):
    lo,hi=b
    return (c*lo,c*hi) if c>=0 else (c*hi,c*lo)

LN2=ln_bounds(2); LN3=ln_bounds(3); LN87=ln_bounds(Q(8,7))

def log_k_over_u_exact(r,u):
    i=p*r%L
    n=(A*i-r)//L
    assert A*i==n*L+r
    U=ln_bounds(Q(u)/K0)
    pieces=(mul(n-55,LN2),mul(35-i,LN3),(-LN87[1],-LN87[0]),(-U[1],-U[0]))
    return sum(v[0] for v in pieces),sum(v[1] for v in pieces)

def log_k_over_u_float(r,u):
    i=p*r%L
    n=(A*i-r)//L
    return (n-55)*log(2.0)+(35-i)*log(3.0)-log(8.0/7.0)-log(float(Q(u)/K0))

def first_below(u):
    lo,hi=DLO,DHI+1
    while lo<hi:
        mid=(lo+hi)//2
        a,b=log_k_over_u_exact(mid,u)
        if b<0:
            hi=mid
        elif a>0:
            lo=mid+1
        else:
            raise AssertionError("log enclosure straddles zero")
    c=lo
    if c>DLO:
        a,b=log_k_over_u_exact(c-1,u); assert a>0
    if c<=DHI:
        a,b=log_k_over_u_exact(c,u); assert b<0
    return c

def safe_band(N):
    low=Q(K0)-Q(N,3)
    high=Q(K0+1)+Q(N,3)
    assert low>0
    return first_below(high), first_below(low)-1

def floor_sum(n,m,a,b):
    assert n>=0 and m>0 and a>=0 and b>=0
    ans=0
    if a>=m:
        ans+=(n-1)*n*(a//m)//2; a%=m
    if b>=m:
        ans+=n*(b//m); b%=m
    while True:
        y=a*n+b
        if y<m: return ans
        n=y//m; b=y%m; m,a=a,m
        if a>=m:
            ans+=(n-1)*n*(a//m)//2; a%=m
        if b>=m:
            ans+=n*(b//m); b%=m

def count_mod_less(start,n,y):
    if y<=0:return 0
    if y>=L:return n
    b=B*start
    ge=floor_sum(n,L,B,b+L-y)-floor_sum(n,L,B,b)
    return n-ge

def count_mod_interval(start,n,lo,hi):
    if lo>hi:return 0
    return count_mod_less(start,n,hi+1)-count_mod_less(start,n,lo)

def count_residue_less_generic(start,n,mult,y):
    if y<=0:return 0
    if y>=L:return n
    bb=mult*start
    ge=floor_sum(n,L,mult,bb+L-y)-floor_sum(n,L,mult,bb)
    return n-ge

def count_rank_interval_in_phase(a,b,istart,iend):
    # Independent coordinate-swapped rectangle count: iterate ranks and use i=p*r mod L.
    n=b-a+1
    return (count_residue_less_generic(a,n,p,iend)
            -count_residue_less_generic(a,n,p,istart))

def outside_parts(slo,shi):
    out=[]
    if DLO<=slo-1:out.append((DLO,min(DHI,slo-1)))
    if shi+1<=DHI:out.append((max(DLO,shi+1),DHI))
    return out

def in_parts(r,parts): return any(a<=r<=b for a,b in parts)

def main():
    assert A*p-103_768_467_013*L==1
    assert p*B%L==1
    assert z==72_057_431_991
    assert N0 < z and N0 < p-1
    delta_lo=A*LN2[0]-L*LN3[1]
    delta_hi=A*LN2[1]-L*LN3[0]
    assert 0<delta_lo<delta_hi<Q(1,2**40)
    assert LN2[0] > L*delta_hi  # inherited strict K_H21 reverse-rank ordering
    # floor-sum regression against brute on a small independent modulus
    mm,aa=101,37
    for start in range(7):
        for n in range(15):
            for y in (0,1,17,50,100,101):
                brute=sum(1 for i in range(start,start+n) if (aa*i)%mm<y)
                # local generic formula
                def fs(nn,m,a,b):
                    ans=0
                    if a>=m: ans+=(nn-1)*nn*(a//m)//2; a%=m
                    if b>=m: ans+=nn*(b//m); b%=m
                    while True:
                        yy=a*nn+b
                        if yy<m:return ans
                        nn=yy//m;b=yy%m;m,a=a,m
                        if a>=m: ans+=(nn-1)*nn*(a//m)//2;a%=m
                        if b>=m: ans+=nn*(b//m);b%=m
                bb=aa*start
                got=n-(fs(n,mm,aa,bb+mm-y)-fs(n,mm,aa,bb)) if 0<y<mm else (0 if y<=0 else n)
                assert got==brute
    prev=N0
    total_f=total_b=0
    octaves=[]
    all_discrete_hits=[]
    first_band=None; last_nontrivial=None
    for k in range(24,35):
        base=2**k; step=base//SUBDIV
        of=ob=0
        for j in range(1,SUBDIV+1):
            N=base+j*step
            assert N<=2**35 < p-1 < z+1
            slo,shi=safe_band(N)
            if first_band is None:first_band=(N,slo,shi)
            parts=outside_parts(slo,shi)
            if parts:last_nontrivial=(N,slo,shi)
            n=N-prev
            fstart=prev; bstart=L-N
            f=sum(count_mod_interval(fstart,n,a,b) for a,b in parts)
            b=sum(count_mod_interval(bstart,n,a,b) for a,b in parts)
            # Coordinate-swapped independent rectangle recount.
            f_alt=sum(count_rank_interval_in_phase(a,b,fstart,fstart+n) for a,b in parts)
            b_alt=sum(count_rank_interval_in_phase(a,b,bstart,bstart+n) for a,b in parts)
            assert (f,b)==(f_alt,b_alt)
            hits=[]
            for r in OLD_DELETIONS|ANCHOR_DELETIONS:
                i=p*r%L
                if ((fstart<=i<fstart+n) or (bstart<=i<bstart+n)) and in_parts(r,parts): hits.append(r)
            all_discrete_hits.extend(hits)
            of+=f;ob+=b;prev=N
        total_f+=of;total_b+=ob
        octaves.append({"outer_power":k+1,"forward_exclusions":of,"backward_exclusions":ob,"total":of+ob})
    assert prev==2**35
    assert all_discrete_hits==[]
    total=total_f+total_b
    assert total==EXPECTED_NEW
    assert INHERITED_COUNT-total==EXPECTED_REMAINING

    # Exact source-side split for the successor target.  A tau34 source is a=(i-34) mod L,
    # so a>p exactly when terminal i lies in [0,34) U [p+35,L).
    SAFE0_LO,SAFE0_HI=38_643_145_224,38_659_291_956
    above_domains=((0,34),(p+35,L))
    base_above=sum(count_mod_interval(s,e-s,DLO,DHI) for s,e in above_domains)
    discrete=OLD_DELETIONS|ANCHOR_DELETIONS
    disc_above={r for r in discrete if any(s <= (p*r%L) < e for s,e in above_domains)}
    old_root_parts=((DLO,SAFE0_LO-1),(SAFE0_HI+1,DHI))
    old_root_out_above=0
    for rs,re in ((0,N0),(L-N0,L)):
        for ds,de in above_domains:
            ss=max(rs,ds); ee=min(re,de)
            if ss<ee:
                old_root_out_above += sum(count_mod_interval(ss,ee-ss,a,b) for a,b in old_root_parts)
    old_root_disc_above={r for r in disc_above
        if ((p*r%L)<N0 or (p*r%L)>=L-N0) and not (SAFE0_LO<=r<=SAFE0_HI)}
    current_above=base_above-len(disc_above)-old_root_out_above+len(old_root_disc_above)
    assert current_above==8_482_132_546
    # All new backward layers are above-p source phases; all forward layers are below-p.
    assert L-2**35 > p+35 and 2**35 < p+35
    above_remaining=current_above-total_b
    below_current=INHERITED_COUNT-current_above
    below_remaining=below_current-total_f
    assert above_remaining==7_099_572_324
    assert below_remaining==6_324_034_587
    assert above_remaining+below_remaining==EXPECTED_REMAINING

    # By 2^35 the common cone admits the entire inherited rank core, so coarser/larger
    # common-radius layers cannot delete anything else by this consumer.
    slo,shi=safe_band(2**35)
    assert (slo,shi)==(DLO,DHI)
    out={
      "status":"PASS",
      "classification":"exact finite rank-exclusion certificate using inherited analytic speed cone and monotone H21 law",
      "subdivisions_per_dyadic_octave":SUBDIV,
      "layer_count":11*SUBDIV,
      "phase_domain_forward":[N0,2**35],
      "phase_domain_backward":[L-2**35,L-N0],
      "carry_free":True,
      "first_layer_outer_band":{"N":first_band[0],"safe_lo":first_band[1],"safe_hi":first_band[2]},
      "last_nontrivial_outer_band":{"N":last_nontrivial[0],"safe_lo":last_nontrivial[1],"safe_hi":last_nontrivial[2]},
      "octaves":octaves,
      "forward_new_exclusions":total_f,
      "backward_new_exclusions":total_b,
      "new_rank_exclusions":total,
      "inherited_necessary_rank_count":INHERITED_COUNT,
      "remaining_necessary_rank_count":EXPECTED_REMAINING,
      "above_p_source_necessary_before":current_above,
      "above_p_source_necessary_after":above_remaining,
      "below_p_source_necessary_after":below_remaining,
      "discrete_preexisting_deletion_hits_in_new_layers":0,
      "coordinate_swapped_rectangle_recount":"PASS",
      "eta_classes_removed":0,
      "physical_realization_claimed":False,
      "h21_charge_claimed":False,
      "gate_closure_claimed":False,
      "common_radius_saturation_at_N":2**35,
      "common_radius_saturation_band":[slo,shi]
    }
    print(json.dumps(out,indent=2))

if __name__=='__main__': main()
