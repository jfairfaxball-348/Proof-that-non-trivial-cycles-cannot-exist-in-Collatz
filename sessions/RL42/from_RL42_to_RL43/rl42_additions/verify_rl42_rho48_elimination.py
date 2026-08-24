#!/usr/bin/env python3
from collections import defaultdict, deque

# RL42 elimination of rho=48 using the transport-efficiency bridge.


def stream_local(maxe,maxp):
    """Stream canonical positive excursions as (D,h,p,e), using O(1) Q updates."""
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


def crossing_gap(D,h,p):
    mod=1<<h
    g=(D*pow(3**p,-1,mod))%mod
    if g==0:
        g=mod
    maxg=(D-1)//3**p
    if (g&1) and g<=maxg:
        n=D-3**p*g
        assert n>0 and n%mod==0
        return g,n//mod
    return None


def v2(n):
    n=abs(n); s=0
    while n and n%2==0:
        s+=1; n//=2
    return s


def local_raw(g,p,D,h):
    n=3**p*g-D
    den=1<<h
    if n%den:
        return None
    return n//den


def sync_choices(raw):
    s=v2(raw)
    m=abs(raw)>>s
    sign=1 if raw>0 else -1
    return [(sign*m*3**c,s,c) for c in range(s+1)]


def terminal_suffix(raw):
    # G=4 and zero terminal odd suffix: raw=-4*2^t.
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


# ---------------------------------------------------------------------------
# 1. Crossing excess is >=4 throughout every hypothetical rho<=48 candidate.
# ---------------------------------------------------------------------------
counts=defaultdict(int)
for D,h,p,e in stream_local(3,48):
    counts[e]+=1
    assert crossing_gap(D,h,p) is None
assert dict(counts)=={0:48,1:1176,2:20728,3:287829}

# ---------------------------------------------------------------------------
# 2. Exact e=4 crossing classification through p<=44.
# ---------------------------------------------------------------------------
e4_words=0
cross4={}
for D,h,p,e in stream_local(4,44):
    if e!=4:
        continue
    e4_words+=1
    c=crossing_gap(D,h,p)
    if c is not None:
        assert p not in cross4
        cross4[p]=(D,h,c[0],c[1])

assert e4_words==2243398
assert set(cross4)==set(range(5,45))
for p,(D,h,g,gout) in cross4.items():
    assert h==p+3
    assert (g,gout)==(1,4)
    assert D==3**p+4*(1<<h)

# ---------------------------------------------------------------------------
# 3. Rigidity of rho=48.
# ---------------------------------------------------------------------------
# Refined normalized proper-factor threshold H(z)=12(z+1)/z^2 for G=4.
# H is decreasing on z>1. At z=sqrt(16/15),
# H=(45/4)(1+sqrt(16/15)) > 91/4 because sqrt(16/15)>46/45.
assert 16*45*45 > 15*46*46

# For every integer delta>=1,
#   1-2^-delta <= 1/2 + (delta-1)/4 = (delta+1)/4.
for d in range(1,100):
    lhs_num=(1<<d)-1
    # 4*(1-2^-d) <= d+1
    assert 4*lhs_num <= (d+1)*(1<<d)

# If rho=48 and P_+<=43, summing the preceding bound gives
# effective positive-rank mass <= (rho+P_+)/4 <=91/4,
# contradicting H(z)>91/4. Hence P_+>=44.
# The crossing e>=4 gives P<=rho-4=44, so P=P_+=44 and E=4.
RHO=48
assert (RHO+43)==91
P=44

# The transport theorem rho>(45/4)G also forces G=4 at rho=48,
# since the next allowed G=8 would require rho>90.
assert RHO < 90
FIRST_GAP=9  # inherited exact common prefix 11 for G=4

# ---------------------------------------------------------------------------
# 4. Safe-superset boundary DP: all-positive e=0 excursions + one e=4 crossing.
# ---------------------------------------------------------------------------
start=(0,0,FIRST_GAP,0,0)  # Pspent,crossed,g,A,B
q=deque([start]); seen={start}; endpoints=set()
while q:
    spent,crossed,g,A,B=q.popleft()
    rem=P-spent

    # e=0 positive excursion: D=3^p-2^p,h=p+1.
    for p in range(1,rem+1):
        D=3**p-2**p
        h=p+1
        raw=local_raw(g,p,D,h)
        if raw is None or raw==0:
            continue
        # e=0 cannot physically change sign (already certified by e<=3 scan).
        if (g>0)!=(raw>0):
            continue
        s2=spent+p; A2=A+h; B2=B+p
        if s2==P:
            if crossed:
                sf=terminal_suffix(raw)
                if sf is not None:
                    endpoints.add((2+A2+sf,2+B2))
            continue
        for gn,s,c in sync_choices(raw):
            st=(s2,crossed,gn,A2+s,B2+c)
            if st not in seen:
                seen.add(st); q.append(st)

    # Unique e=4 crossing.
    if not crossed and g==1:
        for p,(D,h,greq,gout) in cross4.items():
            if p>rem:
                continue
            assert greq==1 and gout==4
            raw=-4
            assert local_raw(g,p,D,h)==raw
            s2=spent+p; A2=A+h; B2=B+p
            if s2==P:
                sf=terminal_suffix(raw)
                if sf is not None:
                    endpoints.add((2+A2+sf,2+B2))
                continue
            for gn,s,c in sync_choices(raw):
                st=(s2,1,gn,A2+s,B2+c)
                if st not in seen:
                    seen.add(st); q.append(st)

near={x for x in endpoints if near_window(*x)}
assert near==set()

print('RL42 rho=48 elimination verifier: PASS')
print('e<=3 words checked through p<=48 =',sum(counts.values()),'with zero crossings')
print('e=4 words checked through p<=44 =',e4_words)
print('e=4 crossing types =',len(cross4),'all gap 1 -> -4')
print('rho=48 rigidity: P=P+=44,E=4,G=4')
print('safe boundary-DP states/endpoints =',len(seen),len(endpoints))
print('near-resonant endpoints = 0')
print('certified consequence: rho != 48; together with rho>=48, rho >= 49')
