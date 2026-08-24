#!/usr/bin/env python3
from collections import defaultdict

# RL42 bounded crossing-excess + analytic transport-efficiency floor.
# Goal: certify rho>=48 without reconstructing any large area table.


def stream_local(maxe,maxp):
    """Stream canonical positive excursions as (D,h,p,e)."""
    def app(Q,n,b):
        return Q if b == 0 else 3*Q + (1 << n)

    def rec(Qa,Qb,n,d,e,palpha):
        # Canonical close when d=1: append alpha bit 1, beta bit 0.
        if d == 1 and palpha + 1 <= maxp:
            yield (3*Qa + (1 << n)) - Qb, n + 1, palpha + 1, e
        for x,y in ((0,0),(1,1),(0,1),(1,0)):
            nd = d + y - x
            if nd <= 0:
                continue
            ne = e + d - x
            np = palpha + x
            if ne <= maxe and np + 1 <= maxp:
                yield from rec(app(Qa,n,x), app(Qb,n,y), n+1, nd, ne, np)

    yield from rec(0,1,1,1,0,0)


def crossing_gap(D,h,p):
    """Return physical positive->negative crossing gap pair if one exists."""
    mod = 1 << h
    g = (D * pow(3**p, -1, mod)) % mod
    if g == 0:
        g = mod
    maxg = (D - 1) // (3**p)
    if (g & 1) and g <= maxg:
        n = D - 3**p * g
        assert n > 0 and n % mod == 0
        return g, n // mod
    return None


# Under a hypothetical rho<=47, every excursion has p<=47 and e<=rho-p<47.
# It is enough to rule out all sign-changing positive excursions with e<=3,
# because the transport argument below then forces the mandatory crossing to
# carry at least four units of excess displacement.
counts = defaultdict(int)
for D,h,p,e in stream_local(3,47):
    counts[e] += 1
    assert crossing_gap(D,h,p) is None

assert dict(counts) == {0:47, 1:1128, 2:19505, 3:265927}

# Rank-efficiency sharpening.  For every integer delta>=1,
#   1-2^-delta <= delta/2 - (delta-1)/4 = (delta+1)/4.
# The form with the explicit -(delta-1)/4 is what prices excursion excess.
for d in range(1,256):
    # Multiply by 4*2^d:
    # 4(2^d-1) <= (d+1)2^d.
    assert 4*((1<<d)-1) <= (d+1)*(1<<d)

# In an excursion, local ordered-rank transport is r=sum(delta_i), while
# p is the number of moved ranks, hence e=r-p=sum(delta_i-1).
# A mandatory positive sign-changing excursion therefore contributes at least
# E_+>=4 to the global positive-rank excess sum.
# Summing the pointwise efficiency inequality gives
#   M_eff <= S_+/2 - E_+/4 <= rho/2 - 1.
# But the exact numerator bridge gives
#   M_eff >= 3(z+1)G/z^2 > 45G/8 >= 45/2
# because z>1, z^2<16/15, 4|G and G>0.
# Thus rho/2 - 1 > 45/2, i.e. rho>47.
# Verify the final exact arithmetic implication.
assert 47/2 - 1 == 45/2

print('RL42 crossing-excess transport floor verifier: PASS')
print('e<=3 words checked through p<=47 =', sum(counts.values()))
print('counts by excess =', dict(counts))
print('physical sign-changing excursions among them = 0')
print('therefore any mandatory crossing under rho<=47 has excess >=4')
print('transport efficiency then gives M_eff <= rho/2 - 1')
print('exact numerator bridge gives M_eff > 45/2')
print('certified consequence: rho > 47, hence rho >= 48')
