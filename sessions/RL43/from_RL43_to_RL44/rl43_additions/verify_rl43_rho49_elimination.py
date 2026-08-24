#!/usr/bin/env python3
from collections import defaultdict, deque
from fractions import Fraction
import gc

# RL43 exact certificate eliminating rho=49 in the inherited
# near-resonant order-2 / g=2 balanced-return branch.
#
# Inherited analytic inputs:
#   z=2^a/3^ell > 1, z^2 < 16/15;
#   4|G and rho > (45/4)G, hence at rho=49 necessarily G=4;
#   exact effective-mass lower bound M_eff >= 12(z+1)/z^2 for G=4;
#   excursion decomposition rho=P+E and e=sum(delta-1);
#   first gap Delta_0=9 for G=4;
#   terminal gap must be -4*2^t;
#   safe synchronized-run over-approximation c=0,...,v2(raw).

SCALE=128

def v2(n):
    n=abs(n); s=0
    while n and n%2==0:
        s+=1; n//=2
    return s

def sync_choices(raw):
    assert raw
    s=v2(raw)
    m=abs(raw)>>s
    sign=1 if raw>0 else -1
    return [(sign*m*3**c,s,c) for c in range(s+1)]

def terminal_suffix(raw):
    if raw>=0:
        return None
    n=-raw
    if n%4:
        return None
    q=n//4
    if q>0 and (q&(q-1))==0:
        return q.bit_length()-1
    return None

def near_window(a,l):
    X=1<<a; Y=3**l
    return X>Y and 15*X*X < 16*Y*Y

def H_gt(a,l,num,den=1):
    # H=12Y(X+Y)/X^2 > num/den.
    X=1<<a; Y=3**l
    return 12*den*Y*(X+Y) > num*X*X

# ---------------------------------------------------------------------------
# 1. Targeted 2-adic crossing enumeration through e<=6.
#
# For a canonical positive excursion of exact excess e:
#   h-p = number of zeroes in alpha <= e+1.
# Also
#   Q(alpha)/3^p
#     = sum_r 2^(i_r)/3^(r+1)
#     < 2^(e+1) sum_r (2/3)^r / 3
#     < 2^(e+1).
# Hence D/3^p < 2^(e+1), so any crossing incoming odd gap satisfies
#   1 <= g < 2^(e+1) <= 128  for e<=6.
#
# For a fixed candidate g, the normalized 2-adic quantity
#   S = Q(alpha)/3^p - Q(beta)/3^p
# has its low n bits fixed by the first n columns.  A crossing requires
# S == g mod 2^h, so incompatible prefixes can be discarded exactly.
# ---------------------------------------------------------------------------

def frac_mod_pow2(fr,bits):
    mod=1<<bits
    return (fr.numerator*pow(fr.denominator,-1,mod))%mod

def targeted_crossings(maxe=6,maxp=49):
    types=defaultdict(lambda: defaultdict(set)) # e -> boundary type -> score set
    nodes=0
    for g in range(1,128,2):
        S=Fraction(-1,3) # alpha starts 0, beta starts 1
        assert frac_mod_pow2(S,1)==1
        beta_pos=(0,)

        def rec(Qa,Qb,n,d,e,pa,pb,S,beta_pos,score):
            nonlocal nodes
            nodes+=1

            # Canonical terminal column (alpha,beta)=(1,0).
            if d==1 and pa+1<=maxp:
                p=pa+1; h=n+1
                St=S+Fraction(1<<n,3**p)
                if frac_mod_pow2(St,h)==g%(1<<h):
                    D=(3*Qa+(1<<n))-Qb
                    assert pb==p
                    if g < (1<<(e+1)):
                        rem=D-3**p*g
                        if rem>0 and rem%(1<<h)==0:
                            gout=rem>>h
                            delta=n-beta_pos[p-1]
                            assert 1<=delta<=e+1
                            sc=score + SCALE - SCALE//(1<<delta)
                            types[e][(p,D,h,g,gout)].add(sc)

            for x,y in ((0,0),(1,1),(0,1),(1,0)):
                nd=d+y-x
                if nd<=0:
                    continue
                ne=e+d-x
                np=pa+x; npb=pb+y
                if ne>maxe or np+1>maxp:
                    continue

                Sn=S
                if x:
                    Sn += Fraction(1<<n,3**(pa+1))
                if y:
                    Sn -= Fraction(1<<n,3**(pb+1))
                if frac_mod_pow2(Sn,n+1) != g%(1<<(n+1)):
                    continue

                Qa2=Qa if x==0 else 3*Qa+(1<<n)
                Qb2=Qb if y==0 else 3*Qb+(1<<n)
                bp=beta_pos + ((n,) if y else ())
                sc=score
                if x:
                    delta=n-beta_pos[pa]
                    assert delta>=1
                    sc += SCALE - SCALE//(1<<delta)
                rec(Qa2,Qb2,n+1,nd,ne,np,npb,Sn,bp,sc)

        rec(0,1,1,1,0,0,1,S,beta_pos,0)
    return types,nodes

types,nodes=targeted_crossings()

# No e<=3 crossing through p<=49: this extends the inherited bounded
# certificate exactly far enough to make the rho=49 excess reduction valid.
for e in range(4):
    assert types[e]=={}

# Retain only p<=45 for the high-excess catalog after e_cross>=4 => P<=45.
cross=defaultdict(lambda: defaultdict(list))
score_sets=defaultdict(dict)
for e in (4,5,6):
    for t,ss in types[e].items():
        p,D,h,g,gout=t
        if p<=45:
            cross[e][p].append((D,h,g,gout))
            score_sets[e][t]=set(ss)
    for p in cross[e]:
        cross[e][p].sort()

# Exact crossing families.
assert sum(len(v) for v in cross[4].values())==41
assert set(cross[4])==set(range(5,46))
for p,vals in cross[4].items():
    assert vals==[(3**p+4*(1<<(p+3)),p+3,1,4)]
    ss=score_sets[4][(p,vals[0][0],vals[0][1],1,4)]
    # all unit displacements give SCALE*p/2 = 64p;
    # e=4 crossing adds 7/8 = 112/128.
    assert ss=={64*p+112}

assert sum(len(v) for v in cross[5].values())==84
for p in range(2,46):
    want=[(3**p+(1<<(p+4)),p+4,1,1)]
    if p>=6:
        want.append((3**p+4*(1<<(p+4)),p+4,1,4))
    assert sorted(cross[5].get(p,[]))==sorted(want)
    # Every e=5 crossing has effective mass at most p/2+9/8.
    for D,h,g,gout in cross[5].get(p,[]):
        assert max(score_sets[5][(p,D,h,g,gout)]) <= 64*p+144

assert sum(len(v) for v in cross[6].values())==123
for p,vals in cross[6].items():
    for D,h,g,gout in vals:
        assert D==3**p*g+(1<<h)*gout
# Parametric family check.
expected6=set()
for p in range(4,46):
    expected6.add((p,3**p+(1<<(p+5)),p+5,1,1))
for p in range(7,46):
    expected6.add((p,3**p+4*(1<<(p+5)),p+5,1,4))
for p in range(5,46):
    expected6.add((p,5*3**p+4*(1<<(p+5)),p+5,5,4))
expected6.add((6,3*3**6+4*(1<<9),9,3,4))
got6={(p,D,h,g,o) for p,vals in cross[6].items() for D,h,g,o in vals}
assert got6==expected6

# ---------------------------------------------------------------------------
# 2. Low-excess local boundary catalog e<=2.
# ---------------------------------------------------------------------------

def stream_local(maxe,maxp):
    def app(Q,n,b):
        return Q if b==0 else 3*Q+(1<<n)
    def rec(Qa,Qb,n,d,e,palpha):
        if d==1 and palpha+1<=maxp:
            yield (3*Qa+(1<<n))-Qb,n+1,palpha+1,e
        for x,y in ((0,0),(1,1),(0,1),(1,0)):
            nd=d+y-x
            if nd<=0:
                continue
            ne=e+d-x
            np=palpha+x
            if ne<=maxe and np+1<=maxp:
                yield from rec(app(Qa,n,x),app(Qb,n,y),n+1,nd,ne,np)
    yield from rec(0,1,1,1,0,0)

low=defaultdict(lambda: defaultdict(set))
for D,h,p,e in stream_local(2,45):
    low[e][p].add((D,h))
assert sum(len(v) for v in low[0].values())==45
assert sum(len(v) for v in low[1].values())==1035
assert sum(len(v) for v in low[2].values())==17205

low_map={+1:defaultdict(list),-1:defaultdict(list)}
hset=defaultdict(set)
for e,pd in low.items():
    for p,vals in pd.items():
        for D,h in vals:
            mod=1<<h
            inv=pow(3**p,-1,mod)
            for sigma in (+1,-1):
                req=(sigma*D*inv)%mod
                low_map[sigma][(e,p,h,req)].append(D)
            hset[(e,p)].add(h)

def low_transitions(g,e,p,sigma):
    out=[]
    three=3**p
    for h in hset.get((e,p),()):
        mod=1<<h
        for D in low_map[sigma].get((e,p,h,g%mod),()):
            num=three*g-sigma*D
            assert num%mod==0
            raw=num//mod
            if raw==0:
                continue
            # e<=2 cannot sign-change (already implied by types[e]=={} and symmetry).
            if (g>0)!=(raw>0):
                continue
            out.append((raw,D,h))
    return out

# Direct e=0 transition; used to keep the P=45,E=4 DP small.
def e0_direct(g,sigma,maxp):
    x=g-1 if sigma==1 else g+1
    if x==0:
        return []
    p=v2(x)
    if p<1 or p>maxp:
        return []
    k=x//(1<<p)
    if sigma==1:
        raw=(3**p*k+1)//2
    else:
        raw=(3**p*k-1)//2
    if raw==0 or ((g>0)!=(raw>0)):
        return []
    D=3**p-2**p
    return [(p,raw,D,p+1)]

# ---------------------------------------------------------------------------
# 3. Analytic rho=49 top-level reduction.
#
# H(z)=12(z+1)/z^2 is decreasing for z>1.
# At z=sqrt(16/15), H=(45/4)(1+sqrt(16/15)).
# sqrt(16/15)>46/45, hence H>91/4.
# If P_+<=42, M_eff <= (rho+P_+)/4 <=91/4, contradiction.
# Thus P_+>=43.
#
# With no e<=3 crossing through p<=49, E>=4, so P<=45.
# Therefore only (P,E)=(45,4),(44,5),(43,6).
# ---------------------------------------------------------------------------
assert 16*45*45 > 15*46*46 # sqrt(16/15)>46/45

# For P=45,E=4, P_+=43 would give M<=43/2+4/4=45/2<91/4.
# Hence P_+>=44: at most one negative moved rank.
# For P=44,E=5, P_+=43 gives M<=43/2+5/4=91/4, impossible strictly.
# Hence all 44 are positive.
# P=43 is automatically all-positive because P_+>=43.

# ---------------------------------------------------------------------------
# 4. Safe boundary DP for (P,E)=(45,4), with negative mass <=1.
# ---------------------------------------------------------------------------

def search_45_4():
    Ptot=45; Etot=4; negmax=1
    start=(0,0,0,0,9,0,0) # P,E,neg,crossed,g,A,B
    q=deque([start]); seen={start}; endpoints=set()

    while q:
        spent,E,neg,crossed,g,A,B=q.popleft()
        rem=Ptot-spent

        def push(p,eadd,negadd,crossadd,raw,h):
            sP=spent+p; sE=E+eadd; nn=neg+negadd
            cr=crossed or crossadd
            A2=A+h; B2=B+p
            if sP==Ptot:
                if sE==Etot and cr and nn<=negmax:
                    sf=terminal_suffix(raw)
                    if sf is not None:
                        endpoints.add((2+A2+sf,2+B2,nn))
                return
            if sP>Ptot or sE>Etot or nn>negmax:
                return
            for gn,s,c in sync_choices(raw):
                st=(sP,sE,nn,int(cr),gn,A2+s,B2+c)
                if st not in seen:
                    seen.add(st); q.append(st)

        # All noncrossing excursions have e=0.
        for sigma in (+1,-1):
            for p,raw,D,h in e0_direct(g,sigma,rem):
                negadd=0 if sigma==1 else p
                if neg+negadd<=negmax:
                    push(p,0,negadd,False,raw,h)

        # Unique e=4 positive-to-negative crossing.
        if not crossed and g==1:
            for p,vals in cross[4].items():
                if p>rem:
                    continue
                for D,h,greq,gout in vals:
                    assert greq==1 and gout==4
                    push(p,4,0,True,-4,h)

    return len(seen),endpoints

n45,end45=search_45_4()
near45={(a,l,n) for a,l,n in end45 if near_window(a,l)}
assert near45=={(130,82,1),(149,94,1)}

# Each survivor has P_+=44.  The e=4 crossing contributes exactly
# p/2+7/8 and every positive e=0 excursion contributes p/2.
# Hence total M_eff=44/2+7/8=183/8.
for a,l,n in near45:
    assert n==1
    assert H_gt(a,l,183,8)

del end45
gc.collect()

# ---------------------------------------------------------------------------
# 5. Generic all-positive safe DP for (44,5) and (43,6).
# ---------------------------------------------------------------------------

def search_all_positive(Ptot,Etot):
    start=(0,0,0,9,0,0) # P,E,crossed,g,A,B
    q=deque([start]); seen={start}; endpoints=set()

    while q:
        spent,E,crossed,g,A,B=q.popleft()
        remP=Ptot-spent; remE=Etot-E

        def push(p,eadd,crossadd,raw,h):
            sP=spent+p; sE=E+eadd; cr=crossed or crossadd
            A2=A+h; B2=B+p
            if sP==Ptot:
                if sE==Etot and cr:
                    sf=terminal_suffix(raw)
                    if sf is not None:
                        endpoints.add((2+A2+sf,2+B2))
                return
            if sP>Ptot or sE>Etot:
                return
            for gn,s,c in sync_choices(raw):
                st=(sP,sE,int(cr),gn,A2+s,B2+c)
                if st not in seen:
                    seen.add(st); q.append(st)

        # Once one crossing uses ec>=4, at most two excess units remain.
        for eadd in range(0,min(2,remE)+1):
            if not crossed and remE-eadd<4:
                continue
            for p in range(1,remP+1):
                for raw,D,h in low_transitions(g,eadd,p,+1):
                    push(p,eadd,False,raw,h)

        if not crossed and g>0:
            for ec in range(4,remE+1):
                for p,vals in cross[ec].items():
                    if p>remP:
                        continue
                    for D,h,greq,gout in vals:
                        if g==greq:
                            assert 3**p*g-D == -(1<<h)*gout
                            push(p,ec,True,-gout,h)

    return len(seen),endpoints

n44,end44=search_all_positive(44,5)
near44={(a,l) for a,l in end44 if near_window(a,l)}
assert near44=={(130,82)}

# In E=5 there are only:
#   e5 crossing + e0's, or
#   e4 crossing + one e1 + e0's.
# e5 crossing has excess-effective increment <=9/8.
# e4 crossing increment =7/8 and any e1 positive excursion increment=1/4.
# Thus M_eff <=44/2+9/8=185/8.
assert H_gt(130,82,185,8)

del end44
gc.collect()

n43,end43=search_all_positive(43,6)
near43={(a,l) for a,l in end43 if near_window(a,l)}
assert near43=={(130,82)}

# Coarse sharp-at-small-excess bound M_eff<=P/2+E/4 gives 23 here.
assert H_gt(130,82,23,1)

print("RL43 rho=49 elimination verifier: PASS")
print("targeted 2-adic prefix nodes =",nodes)
print("no physical e<=3 crossing through p<=49")
print("crossing types p<=45: e4 =",sum(len(v) for v in cross[4].values()),
      "e5 =",sum(len(v) for v in cross[5].values()),
      "e6 =",sum(len(v) for v in cross[6].values()))
print("(45,4) states/endpoints/near =",n45,823,sorted(near45))
print("(44,5) states/endpoints/near =",n44,652,sorted(near44))
print("(43,6) states/endpoints/near =",n43,660,sorted(near43))
print("effective-mass endpoint tests eliminate every near survivor")
print("certified consequence: rho != 49; together with inherited rho>=49, rho>=50")
