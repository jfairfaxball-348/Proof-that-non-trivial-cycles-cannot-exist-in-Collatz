#!/usr/bin/env python3
from fractions import Fraction
from itertools import product


def vp(n: int, p: int) -> int:
    c = 0
    while n % p == 0:
        n //= p
        c += 1
    return c


def v2(n: int) -> int:
    return vp(n, 2)


def v3(n: int) -> int:
    return vp(n, 3)


def step(x: int):
    n = 3 * x + 1
    a = v2(n)
    return n >> a, a


def xi(y: int) -> int:
    m = v3(y + 1)
    return (1 << m) * ((y + 1) // (3**m))


def plateau_data(y: int):
    assert y > 0 and y % 2 == 1
    s = v2(y + 1)
    mu = v3(y + 1)
    q = (y + 1) // ((1 << s) * (3**mu))
    assert q % 2 == 1 and q % 3 != 0
    n = s + mu
    W = (1 << n) * q
    u = W - 1
    t = v2((3**n) * q - 1)
    z = ((3**n) * q - 1) >> t
    mu_next = v3(z + 1)
    W_next = xi(z)
    u_next = W_next - 1
    r = v3((1 << t) - 1)
    return dict(s=s, mu=mu, q=q, n=n, W=W, u=u, t=t, z=z,
                mu_next=mu_next, W_next=W_next, u_next=u_next, r=r)


# RL-L31: anchor normalization and deterministic induced map.
anchor_checks = 0
induced_consistency_checks = 0
for y in range(1, 100000, 2):
    if y % 3 == 0:
        continue
    d = plateau_data(y)
    s, mu, q, n, W, u, t, z = d['s'], d['mu'], d['q'], d['n'], d['W'], d['u'], d['t'], d['z']

    assert u + 1 == (1 << n) * q
    assert v3(u + 1) == 0
    assert xi(y) == u + 1

    # From anchor u, exactly mu exponent-1 steps reach y.
    cur = u
    for _ in range(mu):
        nxt, a = step(cur)
        assert a == 1
        cur = nxt
    assert cur == y

    # The anchor's full neutral run has n-1 exponent-1 moves and the same exit z.
    cur = u
    for _ in range(n - 1):
        nxt, a = step(cur)
        assert a == 1
        cur = nxt
    nxt, a = step(cur)
    assert a == t + 1
    assert nxt == z

    # Starting at physical plateau y only the final s-1 one-steps remain.
    cur = y
    for _ in range(s - 1):
        nxt, a = step(cur)
        assert a == 1
        cur = nxt
    nxt, a = step(cur)
    assert a == t + 1
    assert nxt == z

    assert d['u_next'] == xi(z) - 1
    anchor_checks += 1

# Same anchor, wherever sampled along its neutral run, gives same induced successor.
for u in range(1, 40000, 2):
    if (u + 1) % 3 == 0:
        continue
    n = v2(u + 1)
    if n == 0:
        continue
    base = plateau_data(u)
    cur = u
    for j in range(n):
        dj = plateau_data(cur)
        assert dj['u'] == u
        assert dj['u_next'] == base['u_next']
        induced_consistency_checks += 1
        if j < n - 1:
            cur, a = step(cur)
            assert a == 1


# RL-L32: exact next-mu law, parity reset, and saturated-exit cost.
valuation_checks = 0
parity_reset_checks = 0
saturation_checks = 0
cancellation_checks = 0
for y in range(1, 150000, 2):
    if y % 3 == 0:
        continue
    d = plateau_data(y)
    n, q, t, r, mu_next = d['n'], d['q'], d['t'], d['r'], d['mu_next']

    if r < n:
        assert mu_next == r
    elif r > n:
        assert mu_next == n
    else:
        hunit = ((1 << t) - 1) // (3**n)
        assert hunit % 3 != 0
        assert mu_next == n + v3(q + hunit)
        cancellation_checks += 1

    # LTE specialization.
    if t % 2 == 1:
        assert r == 0
        assert mu_next == 0
    else:
        assert r == 1 + v3(t // 2)
        assert mu_next >= 1
    assert (mu_next == 0) == (t % 2 == 1)
    parity_reset_checks += 1

    if r >= n:
        assert t % 2 == 0
        assert t % (2 * (3 ** (n - 1))) == 0
        assert t >= 2 * (3 ** (n - 1))
        saturation_checks += 1
    valuation_checks += 1


# RL-L33: unit-width xi-direction grammar.
# Let h=n-mu_next. Exact ratio:
# W'/W=(3/2)^h * 2^-t * (1+eta), 0<eta<1.
# h<=0 => descent.
# h>0 and 2^(h+t)<3^h => rise.
# h>0 and 2^(h+t-1)>3^h => descent.
# Remaining strip: 2^(h+t-1)<3^h<2^(h+t), exactly one integer t.
ratio_checks = 0
forced_rise_checks = 0
forced_descent_checks = 0
critical_checks = 0
for y in range(1, 180000, 2):
    if y % 3 == 0:
        continue
    d = plateau_data(y)
    n, q, t, mu_next = d['n'], d['q'], d['t'], d['mu_next']
    W, W_next = d['W'], d['W_next']
    h = n - mu_next

    eta = Fraction((1 << t) - 1, (3**n) * q)
    assert 0 < eta < 1
    scale = (Fraction(3, 2) ** h) * Fraction(1, 1 << t) if h >= 0 else (Fraction(2, 3) ** (-h)) * Fraction(1, 1 << t)
    assert Fraction(W_next, W) == scale * (1 + eta)
    ratio_checks += 1

    if h <= 0:
        assert W_next < W
        forced_descent_checks += 1
        continue

    low = (1 << (h + t)) < 3**h
    superhigh = (1 << (h + t - 1)) > 3**h
    if low:
        assert W_next > W
        forced_rise_checks += 1
    elif superhigh:
        assert W_next < W
        forced_descent_checks += 1
    else:
        # No equality between powers 2 and 3; this is the unique critical strip.
        assert (1 << (h + t - 1)) < 3**h < (1 << (h + t))
        # Exact sign formula in the critical strip.
        M = (3**mu_next) * ((1 << (h + t)) - 3**h)
        lhs = (1 << t) - 1
        if lhs > M * q:
            assert W_next > W
        elif lhs < M * q:
            assert W_next < W
        else:
            assert W_next == W
        critical_checks += 1


# RL-L34 local arithmetic: exact exit cylinder for q.
# v2(3^n q-1)=t iff q == 3^{-n}(1+2^t) mod 2^(t+1).
cylinder_checks = 0
for n in range(1, 18):
    for t in range(1, 18):
        mod = 1 << (t + 1)
        residue = (pow(pow(3, n, mod), -1, mod) * (1 + (1 << t))) % mod
        assert residue % 2 == 1
        for k in range(0, 16):
            q = residue + k * mod
            if q <= 0 or q % 3 == 0:
                continue
            assert v2((3**n) * q - 1) == t
            cylinder_checks += 1


# RL-L34b: local Haar cost of saturated exits and 3-adic cancellation depth.
# Conditional on odd q, exact t has normalized 2-adic mass 2^-t.
# Saturation r(t)>=n iff M_n=2*3^(n-1) divides t, hence total mass 1/(2^M_n-1).
saturation_mass_checks = 0
cancellation_mass_checks = 0
for n in range(1, 6):
    M = 2 * (3 ** (n - 1))
    # Partial geometric sum plus exact tail equals the closed form.
    partial = sum((Fraction(1, 2**(j * M)) for j in range(1, 8)), Fraction(0, 1))
    tail = Fraction(1, 2**(8 * M)) / (1 - Fraction(1, 2**M))
    assert partial + tail == Fraction(1, (1 << M) - 1)
    saturation_mass_checks += 1

# If r=n, write hunit=(2^t-1)/3^n.  For q a 3-adic unit,
# c=v3(q+hunit) has P(c=0)=1/2 and P(c=ell)=3^-ell, ell>=1.
# Audit exactly modulo 3^(ell_max+1).
for ell_max in range(1, 6):
    mod = 3 ** (ell_max + 1)
    # choose any hunit that is a 3-unit; translation by a unit is all that matters
    hunit = 1
    units = [q for q in range(mod) if q % 3 != 0]
    counts = {c: 0 for c in range(ell_max + 1)}
    overflow = 0
    for q in units:
        c = v3(q + hunit) if q + hunit else ell_max + 1
        if c > ell_max:
            overflow += 1
        else:
            counts[c] += 1
    total = len(units)
    assert Fraction(counts[0], total) == Fraction(1, 2)
    for ell in range(1, ell_max + 1):
        if ell < ell_max + 1:
            # exact c=ell has mass 3^-ell, except the finite-modulus top level
            # where residues divisible by 3^(ell_max+1) are in overflow.
            if ell <= ell_max:
                expected = Fraction(1, 3**ell)
                if ell == ell_max:
                    # At this modulus, exact ell is still resolved; overflow is >=ell+1.
                    pass
                assert Fraction(counts[ell], total) == expected
    assert Fraction(overflow, total) == Fraction(1, 2 * (3**ell_max))
    cancellation_mass_checks += 1


# RL-L34c: universal half-depth cost for any non-rise.
# Analytically: if 2t<n then n>=2t+1.  With r=v3(2^t-1),
# one proves t < (7/12)(n-r) < log2(3/2)(n-r), hence forced rise.
half_depth_checks = 0
half_depth_mass_checks = 0
assert 3**12 > 2**19  # log2(3/2) > 7/12
for y in range(1, 180000, 2):
    if y % 3 == 0:
        continue
    d = plateau_data(y)
    if d['W_next'] <= d['W']:
        assert 2 * d['t'] >= d['n']
        half_depth_checks += 1
for n in range(1, 30):
    t0 = (n + 1) // 2
    mass = sum((Fraction(1, 2**t) for t in range(t0, t0 + 80)), Fraction(0, 1))
    tail = Fraction(1, 2**(t0 + 80 - 1))  # sum from t0+80 onward
    assert mass + tail == Fraction(1, 2**(t0 - 1))
    half_depth_mass_checks += 1


# RL-L35: final-return/root-side probe realization.
# For any chosen root R == 1 mod 3 and odd t, n=v3(2^t R+1), q=(...)/3^n,
# the canonical anchor u=2^n q-1 has physical exit R whenever t is exactly
# the 2-adic exit valuation of that anchor. This is automatic from q being odd,
# which follows because 2^t R+1 is even? Careful: for t>=1, numerator odd? 2^t R even +1 odd,
# so q is odd. Check exact construction and xi side-probe identity.
return_probe_checks = 0
return_high_checks = 0
for R in range(1, 5000, 2):
    if R % 3 != 1:
        continue
    for t in range(1, 20, 2):
        N = (1 << t) * R + 1
        n = v3(N)
        assert n >= 1
        q = N // (3**n)
        assert q % 2 == 1 and q % 3 != 0
        u = (1 << n) * q - 1
        # Its canonical exit parameter is exactly t, because
        # 3^n q - 1 = 2^t R and R is odd.
        assert v2((3**n) * q - 1) == t
        z = ((3**n) * q - 1) >> t
        assert z == R
        assert xi(z) == R + 1  # root has mu=0 because R == 1 mod3
        # This anchor is exactly the normalized xi-probe value.
        # Side predecessor p_{t+1}(R) is integral since t+1 is even and R==1 mod3.
        pnum = (1 << (t + 1)) * R - 1
        assert pnum % 3 == 0
        p = pnum // 3
        assert xi(p) == u + 1
        return_probe_checks += 1
        if u > R:
            # Strict anchor descent to R forces the exact high coefficient.
            assert (1 << (n + t)) > 3**n
            return_high_checks += 1


# RL-L35b: exact discrete-log address of the final-return exponent.
# ord_{3^n}(2)=2*3^(n-1); an exact valuation n occupies two of the
# three lifts of the level-n discrete-log class to modulus 2*3^n.
dlog_checks = 0
dlog_lift_checks = 0
mod9_return_checks = 0
for R in range(1, 4000, 2):
    if R % 3 != 1:
        continue
    for t in range(1, 30, 2):
        n = v3((1 << t) * R + 1)
        if n < 1 or n > 7:
            continue
        M = 2 * (3 ** (n - 1))
        lam = t % M
        assert (pow(2, lam, 3**n) * (R % (3**n)) + 1) % (3**n) == 0
        # uniqueness of the level-n logarithm class
        sols = [e for e in range(M) if (pow(2, e, 3**n) * (R % (3**n)) + 1) % (3**n) == 0]
        assert sols == [lam]
        # exact valuation excludes the unique lift that solves one level deeper
        Mnext = 3 * M
        lifts = [lam + j * M for j in range(3)]
        deep = [e for e in lifts if (pow(2, e, 3**(n + 1)) * (R % (3**(n + 1))) + 1) % (3**(n + 1)) == 0]
        assert len(deep) == 1
        assert (t % Mnext) in lifts
        assert (t % Mnext) != deep[0]
        dlog_checks += 1
        dlog_lift_checks += 1
        if n >= 2:
            if R % 9 == 1:
                assert t % 6 == 3
            elif R % 9 == 7:
                assert t % 6 == 5
            elif R % 9 == 4:
                # RL-F6 excludes this root class in the k=0 branch; general arithmetic gives t == 1 mod6.
                assert t % 6 == 1
            else:
                raise AssertionError((R % 9, n, t))
            mod9_return_checks += 1


# RL-L36: repeated-crossing rigidity bound audit with exact rational products.
# If all states are >=R then each correction factor differs from 1 by at most
# delta_R=log2((3+1/R)/3). We cannot compare logs exactly, but the stronger
# multiplicative implication for an integer cumulative gap C>=1 is:
# if ((3R+1)/(3R))^h < 2, then ratio has sign matching C.
rigidity_checks = 0
root_horizon_checks = 0
for R in range(1, 250):
    assert (3 * R + 1) ** (2 * R) < 2 * (3 * R) ** (2 * R)
    root_horizon_checks += 1
for R in range(3, 80, 2):
    # exact horizon condition ((3R+1)/(3R))^h < 2
    for h in range(1, 5):
        rigid = (3 * R + 1) ** h < 2 * (3 * R) ** h
        if not rigid:
            continue
        # Build pairs of legal same-endpoint inverse paths, retaining only states >=R.
        for endpoint in range(R, min(R + 50, 130), 2):
            if endpoint % 3 == 0:
                continue
            paths = []
            for word in product(range(1, 6), repeat=h):
                cur = endpoint
                states = [cur]
                ok = True
                for d in word:
                    num = (1 << d) * cur - 1
                    if num % 3:
                        ok = False
                        break
                    cur = num // 3
                    if cur < R or cur <= 0 or cur % 2 == 0:
                        ok = False
                        break
                    states.append(cur)
                if ok:
                    paths.append((word, states))
                if len(paths) >= 20:
                    break
            for wa, xa in paths:
                for wb, xb in paths:
                    C = sum(wa) - sum(wb)
                    if C >= 1:
                        assert xa[h] > xb[h]
                    elif C <= -1:
                        assert xa[h] < xb[h]
                    rigidity_checks += 1



# RL-L38: exact multiplicative-ceiling form and integer affine transition.
# With h=n-mu_next,
#   W_next = a W + e,
#   a=(3/2)^h 2^-t,
#   e=(2/3)^mu_next (1-2^-t),  0<e<1.
# Hence W_next=ceil(aW).  Clearing denominators gives
#   d W_next = ell W + c
# where ell=2^mu' 3^n, c=2^(n+mu')(2^t-1), d=2^(n+t)3^mu'.
ceiling_checks = 0
affine_checks = 0
for y in range(1, 180000, 2):
    if y % 3 == 0:
        continue
    d0 = plateau_data(y)
    n, t, mup = d0['n'], d0['t'], d0['mu_next']
    W, Wp = d0['W'], d0['W_next']
    h = n - mup
    a = (Fraction(3, 2) ** h) * Fraction(1, 1 << t)
    e = (Fraction(2, 3) ** mup) * (1 - Fraction(1, 1 << t))
    assert 0 < e < 1
    assert Fraction(Wp, 1) == a * W + e
    aw = a * W
    assert aw.denominator != 1
    assert Wp == (aw.numerator + aw.denominator - 1) // aw.denominator
    ell = (1 << mup) * (3 ** n)
    c = (1 << (n + mup)) * ((1 << t) - 1)
    den = (1 << (n + t)) * (3 ** mup)
    assert den * Wp == ell * W + c
    ceiling_checks += 1
    affine_checks += 1


def transition_coeff(n, t, mup):
    ell = (1 << mup) * (3 ** n)
    c = (1 << (n + mup)) * ((1 << t) - 1)
    den = (1 << (n + t)) * (3 ** mup)
    return ell, c, den


def compose_rotation(word, start=0):
    """Return (Lin,C,Den) for Den*W_after = Lin*W_start + C."""
    P = len(word)
    Lin, C, Den = 1, 0, 1
    for k in range(P):
        n, t, mup = word[(start + k) % P]
        ell, c, den = transition_coeff(n, t, mup)
        C = ell * C + c * Den
        Lin *= ell
        Den *= den
    return Lin, C, Den


# RL-L39: compressed common denominator / all-rotation signature.
# For a cyclic word, put mu_j=mu_next of the previous transition,
# s_j=n_j-mu_j, M=sum mu_j, L=sum s_j, A=L+sum t_j, D=2^A-3^L.
# Then every rotation has Den-Lin=6^M D.  A closed orbit must obey
# C_r=6^M D W_r, so each discrete word has at most one rational anchor
# candidate at every rotation.  Integer/valuation/local-transition checks are
# therefore an exact all-rotation obstruction.
common_denominator_checks = 0
rotation_signature_checks = 0
finite_word_checks = 0
finite_word_survivors = 0
finite_nontrivial_survivors = 0

# Algebraic product audit on a broad finite family of cyclic discrete words.
for P in (1, 2, 3):
    for seed in range(1, 1800):
        word = []
        mus = []
        # Deterministic pseudo-variety without random dependencies.
        for j in range(P):
            n = 1 + ((7 * seed + 5 * j) % 7)
            t = 1 + ((11 * seed + 3 * j) % 8)
            r = v3((1 << t) - 1)
            if r < n:
                mup = r
            elif r > n:
                mup = n
            else:
                # Include shallow cancellation candidates in the symbolic audit.
                mup = n + ((seed + j) % 3)
            word.append((n, t, mup))
        mus = [word[(j - 1) % P][2] for j in range(P)]
        if any(word[j][0] <= mus[j] for j in range(P)):
            continue
        M = sum(mus)
        L = sum(word[j][0] - mus[j] for j in range(P))
        A = L + sum(t for n, t, mup in word)
        D = (1 << A) - 3 ** L
        for r0 in range(P):
            Lin, C, Den = compose_rotation(word, r0)
            assert Den - Lin == (6 ** M) * D
            common_denominator_checks += 1

# Exact finite candidate sieve: P<=3, n,t<=6, and cancellation depth<=2.
# This is only a diagnostic domain, not a proof for arbitrary cycles.
def local_mu_options(n, t):
    r = v3((1 << t) - 1)
    if r < n:
        return [r]
    if r > n:
        return [n]
    return [n, n + 1, n + 2]

triples = []
for n in range(1, 7):
    for t in range(1, 7):
        for mup in local_mu_options(n, t):
            triples.append((n, t, mup))

for P in (1, 2, 3):
    for word in product(triples, repeat=P):
        finite_word_checks += 1
        mus = [word[(j - 1) % P][2] for j in range(P)]
        if any(word[j][0] <= mus[j] for j in range(P)):
            continue
        M = sum(mus)
        L = sum(word[j][0] - mus[j] for j in range(P))
        A = L + sum(t for n, t, mup in word)
        D = (1 << A) - 3 ** L
        if D <= 0:
            continue

        Ws = []
        ok = True
        for r0 in range(P):
            Lin, C, Den = compose_rotation(word, r0)
            defect = Den - Lin
            assert defect == (6 ** M) * D
            if C % defect:
                ok = False
                break
            W = C // defect
            n, t, mup = word[r0]
            if W <= 0 or v2(W) != n or W % 3 == 0:
                ok = False
                break
            q = W >> n
            if q % 2 == 0 or q % 3 == 0:
                ok = False
                break
            # All-rotation numerator signature.
            assert C == (6 ** M) * D * W
            assert v2(C) == M + n
            assert v3(C) == M
            rotation_signature_checks += 1
            # Exact local cylinder and next-mu must also be realized by this q.
            x = (3 ** n) * q - 1
            if v2(x) != t:
                ok = False
                break
            z = x >> t
            if v3(z + 1) != mup:
                ok = False
                break
            Ws.append(W)
        if not ok:
            continue

        # Check actual anchor successor around every edge.
        for j, W in enumerate(Ws):
            n, t, mup = word[j]
            q = W >> n
            z = ((3 ** n) * q - 1) >> t
            if xi(z) != Ws[(j + 1) % P]:
                ok = False
                break
        if not ok:
            continue
        finite_word_survivors += 1
        # The only survivor in this declared domain is a repetition of W=2,
        # i.e. repeated traversals of the trivial 1-cycle anchor.
        if not all(W == 2 for W in Ws):
            finite_nontrivial_survivors += 1

assert finite_nontrivial_survivors == 0


# RL-L40: valuation-triangularity of the composed numerator.
# Expand C=sum_i c_i prod_{k<i} d_k prod_{k>i} ell_k.
# For rotation start 0 and cyclic mu_j=mu_next of transition j-1,
# the first term has v2=M+n_0, while term i>=1 is higher by exactly
#   sum_{k=1}^i s_k + sum_{k=0}^{i-1} t_k >= 2i.
# Hence v2(C)=M+n_0 is automatic for every valid cyclic discrete word.
# For p=3, put r_i=v3(2^t_i-1), a_i=r_i-mu_{i+1}, h_i=n_i-mu_{i+1}.
# Then v3(T_i)-M=a_i+sum_{k>i}h_k.  If no r_i=n_i boundary occurs,
# local valuation law gives either (a_i,h_i)=(0,positive) or
# (positive,0). Since sum h_i=L>0, the last positive-h position is the
# unique minimum 0, so v3(C)=M is also automatic.  Thus nontrivial
# 3-adic numerator cancellation is confined to exact saturation boundaries.
v2_triangular_checks = 0
generic_v3_checks = 0
boundary_localization_checks = 0


def composed_terms(word):
    P = len(word)
    out = []
    for i, (n, t, mup) in enumerate(word):
        ell, c, den = transition_coeff(n, t, mup)
        term = c
        for k in range(i):
            term *= transition_coeff(*word[k])[2]
        for k in range(i + 1, P):
            term *= transition_coeff(*word[k])[0]
        out.append(term)
    return out

# Audit v2 triangularity on the symbolic word family already used above.
for P in (1, 2, 3, 4):
    for seed in range(1, 900):
        word = []
        for j in range(P):
            n = 1 + ((5 * seed + 7 * j) % 8)
            t = 1 + ((13 * seed + 5 * j) % 9)
            r = v3((1 << t) - 1)
            if r < n:
                mup = r
            elif r > n:
                mup = n
            else:
                mup = n + ((seed + 2 * j) % 3)
            word.append((n, t, mup))
        mus = [word[(j - 1) % P][2] for j in range(P)]
        if any(word[j][0] <= mus[j] for j in range(P)):
            continue
        M = sum(mus)
        terms = composed_terms(word)
        vals2 = [v2(x) for x in terms]
        assert vals2[0] == M + word[0][0]
        for i in range(1, P):
            expected_gap = sum(word[k][0] - mus[k] for k in range(1, i + 1)) + sum(word[k][1] for k in range(i))
            assert vals2[i] - vals2[0] == expected_gap
            assert expected_gap >= 2 * i
        assert v2(sum(terms)) == M + word[0][0]
        v2_triangular_checks += 1

# Generic 3-adic uniqueness when no r_i=n_i boundary is present.
for P in (1, 2, 3, 4, 5):
    for seed in range(1, 1400):
        word = []
        boundary = False
        for j in range(P):
            n = 1 + ((11 * seed + 3 * j) % 7)
            t = 1 + ((17 * seed + 7 * j) % 12)
            r = v3((1 << t) - 1)
            if r == n:
                boundary = True
                break
            mup = r if r < n else n
            word.append((n, t, mup))
        if boundary:
            boundary_localization_checks += 1
            continue
        mus = [word[(j - 1) % P][2] for j in range(P)]
        if any(word[j][0] <= mus[j] for j in range(P)):
            continue
        M = sum(mus)
        L = sum(word[j][0] - mus[j] for j in range(P))
        assert L > 0
        terms = composed_terms(word)
        vals3 = [v3(x) - M for x in terms]
        # Formula a_i + suffix h.
        for i, (n, t, mup) in enumerate(word):
            r = v3((1 << t) - 1)
            a = r - mup
            suffix_h = sum(word[k][0] - word[k][2] for k in range(i + 1, P))
            assert vals3[i] == a + suffix_h
        assert min(vals3) == 0
        assert vals3.count(0) == 1
        assert v3(sum(terms)) == M
        generic_v3_checks += 1



# RL-L41: generic one-rotation denominator criterion.
# A generic admissible cyclic word has r_i!=n_i and mu_{i+1} fixed by RL-L32.
# Then RL-L40 makes 6^M | C_r with exact v2/v3 at every rotation. Since
# D=2^A-3^L is coprime to 6 and the rotation numerators satisfy
#   d_i C_{i+1} = ell_i C_i + c_i K,  K=6^M D,
# D-divisibility propagates through all rotations. Therefore D|C_0 is
# necessary and sufficient for all rational anchor candidates to be positive
# integers with the prescribed n_i. The affine equation then forces the
# declared t_i and mu_{i+1} to be the exact Collatz exit valuations.
generic_criterion_words = 0
generic_D_divisible_words = 0
generic_realization_checks = 0
generic_nontrivial_realizations = 0

generic_triples = []
for n in range(1, 9):
    for t in range(1, 9):
        r = v3((1 << t) - 1)
        if r == n:
            continue
        mup = r if r < n else n
        generic_triples.append((n, t, mup))

for P in (1, 2, 3):
    for word in product(generic_triples, repeat=P):
        mus = [word[(j - 1) % P][2] for j in range(P)]
        if any(word[j][0] <= mus[j] for j in range(P)):
            continue
        M = sum(mus)
        L = sum(word[j][0] - mus[j] for j in range(P))
        A = L + sum(t for n, t, mup in word)
        D = (1 << A) - 3 ** L
        if D <= 0:
            continue
        assert D % 2 == 1 and D % 3 != 0
        K = (6 ** M) * D
        Lin0, C0, Den0 = compose_rotation(word, 0)
        assert Den0 - Lin0 == K
        generic_criterion_words += 1

        # Exact rotation-numerator transport identity and D propagation.
        Cs = [compose_rotation(word, r0)[1] for r0 in range(P)]
        for j in range(P):
            ell, c, den = transition_coeff(*word[j])
            assert den * Cs[(j + 1) % P] == ell * Cs[j] + c * K
            assert (Cs[j] % D == 0) == (Cs[(j + 1) % P] % D == 0)

        if C0 % D:
            continue
        generic_D_divisible_words += 1

        Ws = []
        for r0 in range(P):
            Cr = Cs[r0]
            assert Cr % K == 0
            W = Cr // K
            n, t, mup = word[r0]
            assert W > 0 and v2(W) == n and W % 3 != 0
            Ws.append(W)

        # The affine identity plus v2(W_next)=n_next>mu_next forces exact t;
        # then it also forces v3(z+1)=mu_next and xi(z)=W_next.
        for j, W in enumerate(Ws):
            n, t, mup = word[j]
            Wnext = Ws[(j + 1) % P]
            nnext = word[(j + 1) % P][0]
            assert nnext > mup
            q = W >> n
            X = (3 ** n) * q - 1
            # From the affine relation, X+2^t has t+s_next twos, hence >t.
            assert v2(X + (1 << t)) == t + (nnext - mup)
            assert v2(X) == t
            z = X >> t
            assert v3(z + 1) == mup
            assert xi(z) == Wnext
            generic_realization_checks += 1

        if not all(W == 2 for W in Ws):
            generic_nontrivial_realizations += 1

assert generic_nontrivial_realizations == 0

print('RL-5 anchor / exit grammar verifier: PASS')
print('anchor-normalization checks:', anchor_checks)
print('induced-map consistency checks:', induced_consistency_checks)
print('valuation-law checks:', valuation_checks)
print('parity-reset checks:', parity_reset_checks)
print('saturated-exit checks:', saturation_checks)
print('cancellation checks:', cancellation_checks)
print('exact xi-ratio checks:', ratio_checks)
print('forced-rise checks:', forced_rise_checks)
print('forced-descent checks:', forced_descent_checks)
print('critical-strip checks:', critical_checks)
print('exact 2-adic exit-cylinder checks:', cylinder_checks)
print('saturated-exit Haar-mass checks:', saturation_mass_checks)
print('cancellation-depth Haar-mass checks:', cancellation_mass_checks)
print('half-depth non-rise checks:', half_depth_checks)
print('half-depth mass-bound checks:', half_depth_mass_checks)
print('final-return/root-probe checks:', return_probe_checks)
print('strict final-return high checks:', return_high_checks)
print('final-return discrete-log checks:', dlog_checks)
print('exact-valuation lift checks:', dlog_lift_checks)
print('mod-9 return residue checks:', mod9_return_checks)
print('2R rigidity-horizon checks:', root_horizon_checks)
print('finite rigidity checks:', rigidity_checks)
print('multiplicative-ceiling checks:', ceiling_checks)
print('integer affine-transition checks:', affine_checks)
print('common-denominator product checks:', common_denominator_checks)
print('all-rotation numerator-signature checks:', rotation_signature_checks)
print('finite compressed-word candidates checked:', finite_word_checks)
print('finite compressed-word survivors:', finite_word_survivors)
print('finite nontrivial compressed-word survivors:', finite_nontrivial_survivors)
print('2-adic numerator-triangularity checks:', v2_triangular_checks)
print('generic 3-adic unique-minimum checks:', generic_v3_checks)
print('sampled exact-boundary localizations:', boundary_localization_checks)
print('generic scalar-criterion words checked:', generic_criterion_words)
print('generic D-divisible words:', generic_D_divisible_words)
print('generic exact-realization edge checks:', generic_realization_checks)
print('generic nontrivial realizations in domain:', generic_nontrivial_realizations)
print('scope: exact finite audits of analytic statements; Hercher m>=92 is an external input and is not re-proved here')
