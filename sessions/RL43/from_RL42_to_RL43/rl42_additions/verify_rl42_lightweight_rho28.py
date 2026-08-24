from collections import defaultdict

# RL42 lightweight reconstruction of the rho>=28 checkpoint.
# This certificate intentionally avoids the transient RL41 area-26/27 tables.


def Qword(w):
    L = sum(w)
    p = 0
    q = 0
    for i,b in enumerate(w):
        if b:
            q += (1 << i) * 3**(L-1-p)
            p += 1
    return q


def area_pair(alpha,beta):
    d = 0
    area = 0
    for x,y in zip(alpha,beta):
        area += abs(d)
        d += y-x
    assert d == 0
    return area


def gen_by_excess(maxe,maxp):
    """Enumerate every canonical positive excursion with e=r-p<=maxe,
    common odd weight p<=maxp.

    The recurrence charges d-x for each interior appended pair.  This is
    exactly the increment of e=r-p after the initial/final cancellation.
    The only zero-cost interior move is 11 at d=1; maxp bounds its repetitions.
    """
    out = []
    def rec(alpha,beta,d,e,palpha):
        if d == 1 and palpha+1 <= maxp:
            aa = alpha+(1,)
            bb = beta+(0,)
            r = area_pair(aa,bb)
            p = sum(aa)
            assert p == sum(bb)
            assert r-p == e
            out.append((aa,bb,r,p,e))
        for x,y in ((0,0),(1,1),(0,1),(1,0)):
            nd = d+y-x
            if nd <= 0:
                continue
            ne = e + d-x
            np = palpha+x
            if ne <= maxe and np+1 <= maxp:
                rec(alpha+(x,),beta+(y,),nd,ne,np)
    rec((0,),(1,),1,0,0)
    return out


def crossing_gap(D,h,p):
    """Unique positive odd crossing input, if one exists.

    D-3^p g = 2^h g_out > 0.
    Since 3^p is invertible mod 2^h, g is one residue class mod 2^h.
    """
    mod = 1 << h
    g0 = (D * pow(3**p,-1,mod)) % mod
    if g0 == 0:
        g0 = mod
    maxg = (D-1)//(3**p)
    if g0 <= maxg and (g0 & 1):
        n = D-3**p*g0
        assert n > 0 and n % mod == 0
        return g0,n//mod
    return None


def reduce_zero_cost_11(alpha,beta):
    """Delete every interior common 11 occurring while prefix gap d=1."""
    aa=[]; bb=[]; d=0; n=len(alpha)
    for j,(x,y) in enumerate(zip(alpha,beta)):
        if j not in (0,n-1) and d == 1 and (x,y) == (1,1):
            continue
        aa.append(x); bb.append(y)
        d += y-x
    return ''.join(map(str,aa)),''.join(map(str,bb))


# ---------------------------------------------------------------------------
# 1. Low-excess crossing floor over the complete range needed for rho<=28.
# ---------------------------------------------------------------------------
low = gen_by_excess(3,28)
counts = defaultdict(int)
for alpha,beta,r,p,e in low:
    counts[e] += 1
    D = Qword(alpha)-Qword(beta)
    h = len(alpha)
    assert D > 0
    # Any excursion appearing in a putative rho<=28 return has p<=28.
    # The complete low-excess list contains no integer sign-changing excursion.
    assert crossing_gap(D,h,p) is None

assert dict(counts) == {0:28,1:406,2:4438,3:39124}

skeletons = sorted(set(reduce_zero_cost_11(a,b) for a,b,r,p,e in low))
expected_skeletons = sorted([
    ('01','10'),
    ('001','100'),
    ('0001','1000'),('0011','1100'),
    ('00001','10000'),('00011','10100'),
    ('00101','11000'),('00111','11100'),
])
assert skeletons == expected_skeletons

# Thus, in any rho<=28 candidate, the mandatory first physical crossing has
# excess e_cross >= 4. Combined with the analytic moved-mass theorem P>=23,
# rho = P + sum_E (r_E-p_E) gives rho>=27.
P_MIN = 23
assert P_MIN + 4 == 27


# ---------------------------------------------------------------------------
# 2. Equality rho=27 is rigid: P=23, total excess=4, all moved ranks positive.
#    Therefore there is one e=4 crossing and all pre-crossing excursions have e=0.
# ---------------------------------------------------------------------------
small = gen_by_excess(4,23)
by_e = defaultdict(list)
for rec in small:
    by_e[rec[4]].append(rec)
assert {e:len(by_e[e]) for e in range(5)} == {
    0:23,1:276,2:2553,3:19229,4:124456
}

e4_types = set()
e4_cross = []
for alpha,beta,r,p,e in by_e[4]:
    D = Qword(alpha)-Qword(beta)
    h = len(alpha)
    e4_types.add((p,D,h))
    c = crossing_gap(D,h,p)
    if c is not None:
        e4_cross.append((p,D,h,c,alpha,beta))
assert len(e4_types) == 124225

# Exact e=4 crossing classification through p<=23: one type for each p=5..23,
# always incoming gap 1 and outgoing magnitude 4.
assert len(e4_cross) == 19
assert [x[0] for x in e4_cross] == list(range(5,24))
for p,D,h,(g,gout),alpha,beta in e4_cross:
    assert h == p+3
    assert (g,gout) == (1,4)
    assert D == 3**p + 4*(1<<h)

# e=0 family is explicit: alpha=0 1^p, beta=1^p 0,
# D=3^p-2^p, h=p+1.
e0 = {}
for alpha,beta,r,p,e in by_e[0]:
    D = Qword(alpha)-Qword(beta)
    h = len(alpha)
    assert ''.join(map(str,alpha)) == '0'+'1'*p
    assert ''.join(map(str,beta)) == '1'*p+'0'
    assert D == 3**p-2**p and h == p+1 and r == p
    e0[p] = (D,h)
assert set(e0) == set(range(1,24))


def v2(n):
    n=abs(n); s=0
    while n and n%2 == 0:
        s += 1
        n //= 2
    return s


def sync_next_gaps(delta):
    """Safe over-approximation after a synchronized run.

    If |delta|=2^s m, m odd, the next excursion starts at sign*m*3^c,
    0<=c<=s.  Every c is allowed here, even if not dynamically realized.
    """
    assert delta != 0
    sign = 1 if delta>0 else -1
    n=abs(delta)
    s=v2(n)
    m=n >> s
    return {sign*m*3**c for c in range(s+1)}

# For rho=27, G=4 is forced by rho>(45/8)G, and the inherited exact prefix
# theorem gives common prefix 11, hence first-excursion physical gap 9.
first_gap = 9

# Reach every possible positive odd pre-crossing gap using only e=0 positive
# excursions, charging their odd mass. Leave at least one unit for the crossing.
reachable = defaultdict(set)
reachable[0].add(first_gap)
edge_count = 0
for spent in range(23):
    for g in tuple(sorted(reachable[spent])):
        for p,(D,h) in e0.items():
            ns = spent+p
            if ns > 22:
                continue
            num = 3**p*g-D
            den = 1 << h
            if num <= 0 or num % den:
                continue
            gout = num//den
            for gn in sync_next_gaps(gout):
                if gn > 0:
                    if gn not in reachable[ns]:
                        edge_count += 1
                    reachable[ns].add(gn)

reachable_gaps = set().union(*reachable.values())
assert 1 not in reachable_gaps

# Since every e=4 crossing in the allowed p-range requires incoming gap 1,
# none can be the unique crossing of a rho=27 equality candidate.
for p,D,h,(g,gout),alpha,beta in e4_cross:
    assert g not in reachable_gaps

# A direct redundant scan of every reachable gap against all 124225 local e=4
# types certifies zero crossing transitions under the remaining p budget.
for spent,gaps in reachable.items():
    maxp = 23-spent
    for g in gaps:
        for p,D,h in e4_types:
            if p > maxp:
                continue
            n = D-3**p*g
            assert not (n > 0 and n % (1<<h) == 0)

print('RL42 lightweight rho>=28 verifier: PASS')
print('complete e<=3 excursions checked for p<=28 =',sum(counts.values()))
print('reduced e<=3 skeletons =',len(skeletons),'(correct count: eight)')
print('e=4 words checked for p<=23 =',len(by_e[4]))
print('distinct e=4 (p,D,h) types =',len(e4_types))
print('crossing-capable e=4 types =',len(e4_cross),'all require gap 1 -> -4')
print('pre-crossing e=0 reachable odd gaps =',len(reachable_gaps))
print('new reachable-state insertions =',edge_count)
print('certified consequence from analytic P>=23 + bounded certificate: rho >= 28')
