#!/usr/bin/env python3
from itertools import combinations
from collections import defaultdict

# Exact finite sanity certificate for the analytic RL43 defect-support bridge.
# Exhausts all equal-weight binary word pairs through half-length 9.

MAX_N = 9


def Q(bits):
    p = sum(bits)
    r = 0
    out = 0
    for i,b in enumerate(bits):
        if b:
            r += 1
            out += (3 ** (p-r)) * (1 << i)
    return out


def q_run_terms(bits):
    """Return Q(bits) as a signed dictionary of pure 2^i 3^j monomials,
    using maximal 1-run compression. Keys are (i,j), values integer coeffs."""
    p = sum(bits)
    terms = defaultdict(int)
    rank_before = 0
    i = 0
    while i < len(bits):
        if bits[i] == 0:
            i += 1
            continue
        t = i
        k = 0
        while i < len(bits) and bits[i] == 1:
            k += 1
            i += 1
        m0 = rank_before + 1
        # run contribution:
        # 2^t 3^(p-m0-k+1) (3^k-2^k)
        terms[(t, p-m0+1)] += 1
        terms[(t+k, p-m0-k+1)] -= 1
        rank_before += k
    assert rank_before == p
    return {k:v for k,v in terms.items() if v}


def eval_terms(terms):
    return sum(c * (1 << i) * (3 ** j) for (i,j),c in terms.items())


def add_shifted(dst, terms, shift2, shift3, sign):
    for (i,j),c in terms.items():
        dst[(i+shift2,j+shift3)] += sign*c


def decompose(u,v):
    n=len(u)
    assert len(v)==n and sum(u)==sum(v)
    d=[0]
    pu=pv=0
    for x,y in zip(u,v):
        pu += x; pv += y
        d.append(pv-pu)

    excursions=[]
    s=0
    while s<n:
        if d[s] != 0:
            raise AssertionError("decomposition must start synchronized")
        t=s+1
        if t<=n and d[t]==0:
            s=t
            continue
        if t>n:
            break
        sign=1 if d[t]>0 else -1
        while t<n and d[t]!=0:
            assert (d[t]>0)==(sign>0)
            t += 1
        assert d[t]==0
        # local segment columns s,...,t-1; local prefix-flow internal values d[s+1:t]
        au=u[s:t]; bv=v[s:t]
        p=sum(au)
        assert p==sum(bv) and p>=1
        r=sum(abs(x) for x in d[s+1:t])
        e=r-p
        z=(t-s)-p
        assert e>=0
        assert z<=e+1
        # departure/return orientation
        if sign>0:
            assert au[0]==0 and bv[0]==1 and au[-1]==1 and bv[-1]==0
        else:
            assert au[0]==1 and bv[0]==0 and au[-1]==0 and bv[-1]==1
        excursions.append((s,t,sign,p,r,e,z,au,bv))
        s=t
    return d,excursions


def bits_from_positions(n,pos):
    s=set(pos)
    return tuple(1 if i in s else 0 for i in range(n))


def verify_pair(u,v):
    ell=sum(u)
    U=Q(u); V=Q(v)
    d,ex=decompose(u,v)
    poly=defaultdict(int)
    E=0
    N=len(ex)
    pre_support=0

    # common prefix rank count at each column
    pu=0; pv=0
    prefix_u=[0]
    prefix_v=[0]
    for x,y in zip(u,v):
        pu+=x; pv+=y
        prefix_u.append(pu); prefix_v.append(pv)

    for s,t,sign,p,r,e,z,au,bv in ex:
        E += e
        c=prefix_u[s]
        assert c==prefix_v[s]
        q=ell-c-p
        tu=q_run_terms(au)
        tv=q_run_terms(bv)
        assert eval_terms(tu)==Q(au)
        assert eval_terms(tv)==Q(bv)
        runs_u=sum(1 for i,b in enumerate(au) if b and (i==0 or au[i-1]==0))
        runs_v=sum(1 for i,b in enumerate(bv) if b and (i==0 or bv[i-1]==0))
        assert runs_u<=z and runs_v<=z
        local_pre=2*(runs_u+runs_v)
        assert local_pre<=4*z<=4*(e+1)
        pre_support += local_pre
        add_shifted(poly,tu,s,q,+1)
        add_shifted(poly,tv,s,q,-1)

    poly={k:v for k,v in poly.items() if v}
    assert eval_terms(poly)==U-V
    assert pre_support<=4*(E+N)
    assert len(poly)<=pre_support
    return E,N,len(poly),pre_support


pairs=0
max_ratio=0
worst=None
for n in range(1,MAX_N+1):
    for ell in range(0,n+1):
        words=[bits_from_positions(n,c) for c in combinations(range(n),ell)]
        for u in words:
            for v in words:
                E,N,supp,pre=verify_pair(u,v)
                pairs+=1
                if E+N:
                    ratio=supp/(E+N)
                    if ratio>max_ratio:
                        max_ratio=ratio; worst=(n,ell,u,v,E,N,supp,pre)

# Retained RL21 gap-factor countermodel: one enormous excursion, showing why
# the new parameter is not just raw transport/moved-rank count.
u=tuple(map(int,"11011011010110110110101101110011011100110110110101110101011011100"))
v=tuple(map(int,"11111111110111000111110011011011110101010111110011101000011100000"))
d,ex=decompose(u,v)
assert len(ex)==1
assert ex[0][3]==39 and ex[0][4]==170 and ex[0][5]==131
E,N,supp,pre=verify_pair(u,v)
assert (E,N)==(131,1)

print("RL43 defect-support / radius-3 bridge verifier: PASS")
print("equal-weight word pairs exhausted through n =",MAX_N)
print("pairs checked =",pairs)
print("analytic support inequality sanity: support <= 4(E+N)")
print("max observed support/(E+N) =",max_ratio)
print("RL21 gap-factor countermodel excursion: p=39, rho=170, e=131, N=1")
print("countermodel compressed support =",supp,"pre-collection bound =",pre)
