from collections import defaultdict, deque

# RL42 exact/superset certificate eliminating rho=28.
# Inputs from earlier analytic notes:
#   * P_+ > (45/8) G, 4|G;
#   * exact z-dependent P_+ > 3(z+1)G/z^2;
#   * P = sum excursion odd weights;
#   * rho = P + sum e_E, e_E=r_E-p_E >=0;
#   * common prefix for G=4 is 11, hence first excursion gap = 9;
#   * terminal synchronized suffix has zero common odd weight.


def Qword(w):
    L=sum(w); p=0; q=0
    for i,b in enumerate(w):
        if b:
            q += (1<<i)*3**(L-1-p)
            p += 1
    return q


def gen_by_excess(maxe,maxp):
    """Stream every canonical positive excursion with e<=maxe,p<=maxp."""
    def rec(alpha,beta,d,e,palpha):
        if d==1 and palpha+1<=maxp:
            yield alpha+(1,),beta+(0,),palpha+1,e
        for x,y in ((0,0),(1,1),(0,1),(1,0)):
            nd=d+y-x
            if nd<=0:
                continue
            ne=e+d-x
            np=palpha+x
            if ne<=maxe and np+1<=maxp:
                yield from rec(alpha+(x,),beta+(y,),nd,ne,np)
    yield from rec((0,),(1,),1,0,0)


def crossing_gap(D,h,p):
    mod=1<<h
    g0=(D*pow(3**p,-1,mod))%mod
    if g0==0:
        g0=mod
    maxg=(D-1)//3**p
    if g0<=maxg and (g0&1):
        n=D-3**p*g0
        assert n>0 and n%mod==0
        return g0,n//mod
    return None


def v2(n):
    n=abs(n); s=0
    while n and n%2==0:
        s+=1; n//=2
    return s


def sync_choices(raw):
    """Safe synchronized-run over-approximation.

    If |raw|=2^s m, m odd, the next excursion is allowed to start at
    sign(raw)*m*3^c for every 0<=c<=s.  Actual parity dynamics may realize
    fewer c values; admitting all of them can only create false survivors.
    Returns (next_gap, synchronized_length s, common_odd_count c).
    """
    assert raw!=0
    s=v2(raw)
    m=abs(raw)>>s
    sign=1 if raw>0 else -1
    return [(sign*m*3**c,s,c) for c in range(s+1)]


def terminal_suffix(raw):
    """For G=4, terminal suffix is all-even: raw=-4*2^s."""
    if raw>=0:
        return None
    n=-raw
    if n%4:
        return None
    q=n//4
    if q>0 and (q&(q-1))==0:
        return q.bit_length()-1
    return None


def local_raw(g,p,D,h,sigma):
    # sigma=+1 positive prefix-count excursion: (3^p g-D)/2^h
    # sigma=-1 negative prefix-count excursion: (3^p g+D)/2^h
    num=3**p*g-sigma*D
    den=1<<h
    if num%den:
        return None
    return num//den


def near_window(a,l):
    X=1<<a; Y=3**l
    return X>Y and 15*X*X < 16*Y*Y


def resonance_forces_24(a,l):
    # For G=4: P_+ > 12(z+1)/z^2 = 12 Y(X+Y)/X^2.
    X=1<<a; Y=3**l
    return 12*Y*(X+Y) > 23*X*X


# ---------------------------------------------------------------------------
# Local data needed for rho=28.
# ---------------------------------------------------------------------------
e0=defaultdict(set)
e1=defaultdict(set)
cross4=defaultdict(set)
cross5=defaultdict(set)
word_counts=defaultdict(int)

for alpha,beta,p,e in gen_by_excess(5,24):
    word_counts[e]+=1
    if e not in (0,1,4,5):
        continue
    D=Qword(alpha)-Qword(beta)
    h=len(alpha)
    assert D>0
    if e==0:
        e0[p].add((D,h))
    elif e==1:
        e1[p].add((D,h))
    else:
        c=crossing_gap(D,h,p)
        if c is not None:
            g,gout=c
            (cross4 if e==4 else cross5)[p].add((D,h,g,gout))

assert dict(word_counts)=={0:24,1:300,2:2876,3:22403,4:149709,5:886240}
assert sum(len(v) for v in e0.values())==24
assert sum(len(v) for v in e1.values())==300
assert sum(len(v) for v in cross4.values())==20
assert sum(len(v) for v in cross5.values())==42

# Every e=4/e=5 crossing relevant to rho=28 requires incoming physical gap 1.
for table in (cross4,cross5):
    for p,vals in table.items():
        for D,h,g,gout in vals:
            assert g==1
for p,vals in cross4.items():
    for D,h,g,gout in vals:
        assert gout==4 and h==p+3 and D==3**p+4*(1<<h)

# rho=28 and rho>(45/8)G with 4|G force G=4, hence first gap 9.
assert 28*8 < 45*8  # G=8 already impossible; all larger multiples are too.
FIRST_GAP=9


def finish_record(A,B,raw,tag):
    sf=terminal_suffix(raw)
    if sf is None:
        return None
    # Common prefix 11 contributes length 2 and odd weight 2.
    return (2+A+sf,2+B,tag)


# ---------------------------------------------------------------------------
# Case I: P=24, total excess=4.
# The unique crossing is e=4; every other excursion is e=0.
# P_+>=23 permits either all positive excursions or exactly one negative
# excursion, necessarily e=0,p=1.
# ---------------------------------------------------------------------------
def search_case_I():
    # states at excursion starts: (P,neg_used,crossed,g,A,B)
    start=(0,0,0,FIRST_GAP,0,0)
    seen={start}; q=deque([start]); endpoints=set()
    while q:
        P,neg,crossed,g,A,B=q.popleft()
        rem=24-P

        # Positive e=0 excursion.
        for p,vals in e0.items():
            if p>rem: continue
            for D,h in vals:
                raw=local_raw(g,p,D,h,+1)
                if raw is None or raw==0: continue
                # e=0 cannot be a physical sign-changing excursion here.
                if (g>0)!=(raw>0): continue
                P2=P+p; A2=A+h; B2=B+p
                if P2==24:
                    if crossed:
                        rec=finish_record(A2,B2,raw,('I',neg))
                        if rec: endpoints.add(rec)
                    continue
                for gn,s,c in sync_choices(raw):
                    st=(P2,neg,crossed,gn,A2+s,B2+c)
                    if st not in seen:
                        seen.add(st); q.append(st)

        # The only allowed negative-prefix mass is one p=1 e=0 excursion.
        if not neg and rem>=1:
            for D,h in e0[1]:
                raw=local_raw(g,1,D,h,-1)
                if raw is None or raw==0: continue
                if (g>0)!=(raw>0): continue
                P2=P+1; A2=A+h; B2=B+1
                if P2==24:
                    if crossed:
                        rec=finish_record(A2,B2,raw,('I',1))
                        if rec: endpoints.add(rec)
                    continue
                for gn,s,c in sync_choices(raw):
                    st=(P2,1,crossed,gn,A2+s,B2+c)
                    if st not in seen:
                        seen.add(st); q.append(st)

        # Unique e=4 crossing.
        if not crossed and g>0:
            for p,vals in cross4.items():
                if p>rem: continue
                for D,h,greq,gout in vals:
                    if g!=greq: continue
                    raw=-gout
                    assert local_raw(g,p,D,h,+1)==raw
                    P2=P+p; A2=A+h; B2=B+p
                    if P2==24:
                        rec=finish_record(A2,B2,raw,('I',neg))
                        if rec: endpoints.add(rec)
                        continue
                    for gn,s,c in sync_choices(raw):
                        st=(P2,neg,1,gn,A2+s,B2+c)
                        if st not in seen:
                            seen.add(st); q.append(st)
    return seen,endpoints


# ---------------------------------------------------------------------------
# Case IIa: P=23,total excess=5, all excursions positive, unique e=5 crossing.
# ---------------------------------------------------------------------------
def search_case_IIa():
    start=(0,0,FIRST_GAP,0,0) # P,crossed,g,A,B
    seen={start}; q=deque([start]); endpoints=set()
    while q:
        P,crossed,g,A,B=q.popleft()
        rem=23-P
        for p,vals in e0.items():
            if p>rem: continue
            for D,h in vals:
                raw=local_raw(g,p,D,h,+1)
                if raw is None or raw==0: continue
                if (g>0)!=(raw>0): continue
                P2=P+p; A2=A+h; B2=B+p
                if P2==23:
                    if crossed:
                        rec=finish_record(A2,B2,raw,('IIa',))
                        if rec: endpoints.add(rec)
                    continue
                for gn,s,c in sync_choices(raw):
                    st=(P2,crossed,gn,A2+s,B2+c)
                    if st not in seen:
                        seen.add(st); q.append(st)
        if not crossed and g>0:
            for p,vals in cross5.items():
                if p>rem: continue
                for D,h,greq,gout in vals:
                    if g!=greq: continue
                    raw=-gout
                    assert local_raw(g,p,D,h,+1)==raw
                    P2=P+p; A2=A+h; B2=B+p
                    if P2==23:
                        rec=finish_record(A2,B2,raw,('IIa',))
                        if rec: endpoints.add(rec)
                        continue
                    for gn,s,c in sync_choices(raw):
                        st=(P2,1,gn,A2+s,B2+c)
                        if st not in seen:
                            seen.add(st); q.append(st)
    return seen,endpoints


# ---------------------------------------------------------------------------
# Case IIb: P=23,total excess=5, all excursions positive, one e=4 crossing
# and exactly one e=1 noncrossing excursion; all remaining excursions e=0.
# ---------------------------------------------------------------------------
def search_case_IIb():
    start=(0,0,0,FIRST_GAP,0,0) # P,crossed,e1_used,g,A,B
    seen={start}; q=deque([start]); endpoints=set()
    while q:
        P,crossed,u1,g,A,B=q.popleft()
        rem=23-P

        for p,vals in e0.items():
            if p>rem: continue
            for D,h in vals:
                raw=local_raw(g,p,D,h,+1)
                if raw is None or raw==0: continue
                if (g>0)!=(raw>0): continue
                P2=P+p; A2=A+h; B2=B+p
                if P2==23:
                    if crossed and u1:
                        rec=finish_record(A2,B2,raw,('IIb',))
                        if rec: endpoints.add(rec)
                    continue
                for gn,s,c in sync_choices(raw):
                    st=(P2,crossed,u1,gn,A2+s,B2+c)
                    if st not in seen:
                        seen.add(st); q.append(st)

        if not u1:
            for p,vals in e1.items():
                if p>rem: continue
                for D,h in vals:
                    raw=local_raw(g,p,D,h,+1)
                    if raw is None or raw==0: continue
                    # e=1 cannot cross in the bounded range.
                    if (g>0)!=(raw>0): continue
                    P2=P+p; A2=A+h; B2=B+p
                    if P2==23:
                        if crossed:
                            rec=finish_record(A2,B2,raw,('IIb',))
                            if rec: endpoints.add(rec)
                        continue
                    for gn,s,c in sync_choices(raw):
                        st=(P2,crossed,1,gn,A2+s,B2+c)
                        if st not in seen:
                            seen.add(st); q.append(st)

        if not crossed and g>0:
            for p,vals in cross4.items():
                if p>rem: continue
                for D,h,greq,gout in vals:
                    if g!=greq: continue
                    raw=-gout
                    assert local_raw(g,p,D,h,+1)==raw
                    P2=P+p; A2=A+h; B2=B+p
                    if P2==23:
                        if u1:
                            rec=finish_record(A2,B2,raw,('IIb',))
                            if rec: endpoints.add(rec)
                        continue
                    for gn,s,c in sync_choices(raw):
                        st=(P2,1,u1,gn,A2+s,B2+c)
                        if st not in seen:
                            seen.add(st); q.append(st)
    return seen,endpoints


seenI,endI=search_case_I()
seenIIa,endIIa=search_case_IIa()
seenIIb,endIIb=search_case_IIb()

nearI={(a,l,tag) for a,l,tag in endI if near_window(a,l)}
nearIIa={(a,l,tag) for a,l,tag in endIIa if near_window(a,l)}
nearIIb={(a,l,tag) for a,l,tag in endIIb if near_window(a,l)}

# The over-approximation leaves only the two inherited convergent resonances.
assert {(a,l) for a,l,tag in nearI} == {(46,29),(65,41)}
assert all(tag==('I',1) for a,l,tag in nearI)  # every survivor used p=1 negative mass
assert nearIIa == set()
assert {(a,l) for a,l,tag in nearIIb} == {(46,29)}

# At every surviving resonance the exact z-dependent G=4 bound is >23,
# so P_+>=24. Case I survivors have P_+=24-1=23; Case IIb has P_+=P=23.
for a,l in {(46,29),(65,41)}:
    assert near_window(a,l)
    assert resonance_forces_24(a,l)

print('RL42 rho=28 excess-DP elimination verifier: PASS')
print('local words streamed through e<=5,p<=24 =',sum(word_counts.values()))
print('e=4 crossing types =',sum(len(v) for v in cross4.values()),'all require incoming gap 1')
print('e=5 crossing types =',sum(len(v) for v in cross5.values()),'all require incoming gap 1')
print('Case I states/endpoints =',len(seenI),len(endI),'near pairs =',sorted({(a,l) for a,l,t in nearI}),'all P+=23')
print('Case IIa states/endpoints =',len(seenIIa),len(endIIa),'near pairs = none')
print('Case IIb states/endpoints =',len(seenIIb),len(endIIb),'near pairs =',sorted({(a,l) for a,l,t in nearIIb}),'with P+=23')
print('exact resonance bound forces P+>=24 at (46,29) and (65,41)')
print('certified consequence: rho != 28, hence together with rho>=28, rho >= 29')
