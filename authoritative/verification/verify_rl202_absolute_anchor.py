#!/usr/bin/env python3
"""RL202 exact H21 root-anchor speed-cone and height-collision certificate.

Only integer/Fraction arithmetic is used for promoted boundary claims.  Large
exclusion sets are certified by exact modular interval counts rather than an
ordering-sensitive materialized-list digest.
"""
from fractions import Fraction as Q
from functools import lru_cache

A = 217_976_794_617
L = 137_528_045_312
B = A - L
R = 2*L - A
p = 65_470_613_321
u0 = 103_768_467_013
z = L - p
T = 7*3**35
K0 = 2**37
DLO, DHI = 25_583_192_106, 41_775_866_136
N = 2**24
SAFE_LO, SAFE_HI = 38_643_145_224, 38_659_291_956
OLD_DELETIONS = {
    26_058_127_773, 26_058_127_774, 28_746_802_249, 28_746_802_250,
    31_435_476_726, 34_124_151_202, 36_398_517_184, 36_398_517_185,
    36_812_825_678, 39_087_191_660, 39_087_191_661, 41_775_866_136,
}
NEW_ANCHOR = {26_058_127_775, 28_746_802_251, 36_398_517_186, 39_087_191_662}

@lru_cache(maxsize=None)
def ln_bounds(x, terms=110):
    x = Q(x)
    assert x > 0 and terms > 0
    t = (x-1)/(x+1)
    t2 = t*t
    term = t
    partial = Q(0)
    for j in range(terms):
        partial += term/(2*j+1)
        term *= t2
    partial *= 2
    tail = 2*abs(term)/((2*terms+1)*(1-t2))
    return (partial, partial+tail) if t >= 0 else (partial-tail, partial)

def mul(c, bounds):
    lo, hi = bounds
    return (c*lo, c*hi) if c >= 0 else (c*hi, c*lo)

LN2 = ln_bounds(2)
LN3 = ln_bounds(3)
LN87 = ln_bounds(Q(8, 7))

@lru_cache(maxsize=None)
def log_k_over_u(r, u):
    """Enclose ln[(rho(I(r))*T/2^21)/u]."""
    i = p*r % L
    n = (A*i-r)//L
    assert 0 <= r < L and A*i == n*L+r
    ulog = ln_bounds(Q(u)/K0)
    # 7*3^35/2^21 divided by 2^37 = 3^35*2^-55/(8/7).
    pieces = [mul(n-55, LN2), mul(35-i, LN3),
              (-LN87[1], -LN87[0]), (-ulog[1], -ulog[0])]
    return sum(x[0] for x in pieces), sum(x[1] for x in pieces)

def floor_sum(n, m, a, b):
    """sum_{0<=i<n} floor((a*i+b)/m), exact nonnegative AtCoder form."""
    assert n >= 0 and m > 0 and a >= 0 and b >= 0
    ans = 0
    if a >= m:
        ans += (n-1)*n*(a//m)//2
        a %= m
    if b >= m:
        ans += n*(b//m)
        b %= m
    while True:
        y = a*n+b
        if y < m:
            return ans
        n = y//m
        b = y % m
        m, a = a, m
        if a >= m:
            ans += (n-1)*n*(a//m)//2
            a %= m
        if b >= m:
            ans += n*(b//m)
            b %= m

def count_mod_less(start, n, y):
    """# start<=i<start+n with (B*i mod L)<y."""
    if y <= 0:
        return 0
    if y >= L:
        return n
    b = B*start
    ge = floor_sum(n, L, B, b+L-y)-floor_sum(n, L, B, b)
    return n-ge

def count_mod_interval(start, n, lo, hi):
    assert 0 <= lo <= hi < L
    return count_mod_less(start, n, hi+1)-count_mod_less(start, n, lo)

def in_root_window(i):
    return 0 <= i < N or L-N <= i < L

def main():
    assert A*p-u0*L == 1
    assert p*B % L == 1
    assert z == 72_057_431_991
    assert N < z < L-N
    assert T == 350_220_815_692_997_949
    assert len(OLD_DELETIONS) == 12
    assert DHI-DLO+1-len(OLD_DELETIONS) == 16_192_674_019

    # Re-certify inherited tiny defect and the lifted-root displacement bound.
    delta_lo = A*LN2[0]-L*LN3[1]
    delta_hi = A*LN2[1]-L*LN3[0]
    assert 0 < delta_lo < delta_hi < Q(1, 2**40)
    # exp(x)-1 < x/(1-x), so (lambda-1)K0 < K0/(2^40-1) < 1.
    assert Q(K0, 2**40-1) < 1

    # Strict reverse-rank ordering of K_H21 is inherited and re-certified.
    assert LN2[0] > L*delta_hi

    lower_wall = Q(K0)-Q(N, 3)
    upper_wall = Q(K0+1)+Q(N, 3)
    assert lower_wall > 0

    # Exact rank boundaries for the common conservative root-anchor cone.
    assert log_k_over_u(SAFE_LO-1, upper_wall)[0] > 0
    assert log_k_over_u(SAFE_LO, upper_wall)[1] < 0
    assert log_k_over_u(SAFE_HI, lower_wall)[0] > 0
    assert log_k_over_u(SAFE_HI+1, lower_wall)[1] < 0
    assert DLO < SAFE_LO <= SAFE_HI < DHI

    # Exact modular counts in the two length-N chronological windows.
    ranges = ((DLO, SAFE_LO-1), (SAFE_HI+1, DHI))
    fwd_core = count_mod_interval(0, N, DLO, DHI)
    fwd_safe = count_mod_interval(0, N, SAFE_LO, SAFE_HI)
    fwd_out = sum(count_mod_interval(0, N, a, b) for a, b in ranges)
    back_core = count_mod_interval(L-N, N, DLO, DHI)
    back_safe = count_mod_interval(L-N, N, SAFE_LO, SAFE_HI)
    back_out = sum(count_mod_interval(L-N, N, a, b) for a, b in ranges)
    assert (fwd_core, fwd_safe, fwd_out) == (1_975_360, 1_969, 1_973_391)
    assert (back_core, back_safe, back_out) == (1_975_366, 1_969, 1_973_397)
    assert fwd_core-fwd_safe == fwd_out and back_core-back_safe == back_out

    old_in_fwd_out = {
        r for r in OLD_DELETIONS
        if (p*r) % L < N and not (SAFE_LO <= r <= SAFE_HI)
    }
    old_in_back_out = {
        r for r in OLD_DELETIONS
        if (p*r) % L >= L-N and not (SAFE_LO <= r <= SAFE_HI)
    }
    assert old_in_fwd_out == {
        26_058_127_774, 28_746_802_250, 31_435_476_726,
        34_124_151_202, 36_398_517_185, 36_812_825_678,
        39_087_191_661,
    }
    assert old_in_back_out == set()
    fwd_new = fwd_out-len(old_in_fwd_out)
    back_new = back_out-len(old_in_back_out)
    root_new = fwd_new+back_new
    assert (fwd_new, back_new, root_new) == (1_973_384, 1_973_397, 3_946_781)

    # Absolute-height collision: tau34 starts at height 1 and the next 33
    # acceleration exponents are 1, so c>=1 makes all 34 displayed heights
    # positive.  They cannot hit any inherited zero-height anchor 0,1,p,p+1.
    anchors = (0, 1, p, p+1)
    collision_pairs = []
    for k in anchors:
        for t in range(34):
            r = ((k+34-t)*B) % L
            if DLO <= r <= DHI:
                collision_pairs.append((r, k, t))
    collision_ranks = {r for r, _, _ in collision_pairs}
    assert len(collision_pairs) == 16
    assert collision_ranks == {
        26_058_127_774, 26_058_127_775,
        28_746_802_250, 28_746_802_251,
        36_398_517_185, 36_398_517_186,
        39_087_191_661, 39_087_191_662,
    }
    assert collision_ranks & OLD_DELETIONS == {
        26_058_127_774, 28_746_802_250, 36_398_517_185, 39_087_191_661,
    }
    assert collision_ranks-OLD_DELETIONS == NEW_ANCHOR
    assert all(not in_root_window((p*r) % L) for r in NEW_ANCHOR)

    remaining = 16_192_674_019-root_new-len(NEW_ANCHOR)
    assert remaining == 16_188_727_234

    print("PASS RL202 exact H21 absolute-root anchor certificate")
    print(f"root_phase_windows=[0,{N}) U [{L-N},{L}); each_length={N}")
    print(f"conservative_K_band=({lower_wall},{upper_wall})")
    print(f"necessary_rank_band_inside_root_windows=[{SAFE_LO},{SAFE_HI}]")
    print("forward_window_core=1975360; safe_band=1969; new_exclusions=1973384")
    print("backward_window_core=1975366; safe_band=1969; new_exclusions=1973397")
    print("root_anchor_new_rank_exclusions=3946781")
    print("new_zero_height_anchor_collisions=26058127775,28746802251,36398517186,39087191662")
    print("combined_new_rank_exclusions=3946785")
    print("remaining_necessary_ranks=16188727234")
    print("eta_mod18_classes_removed=0; state_selected=no; terminal_sign_selected=no")
    print("digest_dependency=removed; exact_interval_counts=yes")

if __name__ == "__main__":
    main()
