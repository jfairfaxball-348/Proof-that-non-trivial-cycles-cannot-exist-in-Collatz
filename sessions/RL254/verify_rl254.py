#!/usr/bin/env python3
from decimal import Decimal, getcontext
from fractions import Fraction

getcontext().prec = 80
D = Decimal
ln2 = D(2).ln()
rho = D(3).ln() / ln2
cut = (D(16) / D(15)).ln() / (D(2) * ln2)

# General 65/41 sharpening at ell>=77.
assert D(65)/D(41) > rho
lb_65_41 = D(77) * (D(65)/D(41) - rho) + D(1)/D(41)
assert lb_65_41 > cut

# H bound from z/a <= 24/65.
assert 19 * Fraction(24,65) - 7 == Fraction(1,65)

# Known terminal/prefix pattern: tail 0^28 followed cyclically by prefix 110.
known_zeros = set(range(-28,0)) | {2}
def zeros(start, length):
    return sum(1 for x in range(start, start+length) if x in known_zeros)

z38_19 = [zeros(s,38) for s in range(-42,-23)]
assert z38_19 == [24,25,26,27,28,28,28,29,29,29,29,29,29,29,29,28,27,26,25]
assert sum(v-14 for v in z38_19) == 258
assert 258 - 2 == 256

# Bootstrap z and ell floors.
assert 256 + 31 - 4 == 283
assert Fraction(41*283,24) > 483

# Tighter 149/94 sharpening at ell>=484.
assert D(149)/D(94) > rho
lb_149_94 = D(484) * (D(149)/D(94) - rho) + D(1)/D(94)
assert lb_149_94 > cut
assert 19 * Fraction(55,149) - 7 == Fraction(2,149)

# Halving case: 19-window score.
z19 = [zeros(s,19) for s in range(-39,-6)]
assert len(z19) == 33
assert sum(v-7 for v in z19) == 262
assert 262 - 2 == 260

# Non-halving case: 37 useful 38-windows after dropping one endpoint.
z38_37 = [zeros(s,38) for s in range(-51,-14)]
assert len(z38_37) == 37
assert sum(v-14 for v in z38_37) == 357
assert 357 - 2 == 355

# Disjointness coefficient bounds used in the proof.
assert Fraction(56,65) < 1
assert Fraction(51,149) < 1
assert Fraction(148,149) < 1

# Immediate inherited consequences.
assert 260 + 31 - 4 == 287
assert 4*(260-2) == 1032


# Finite exact red-team of the parity/disjointness implementation.
# This is not the proof of the unbounded theorem; it is a regression check.
from math import gcd
checked = 0
for a in range(123, 3001):
    zmin = max(283, (7*a)//19 + 1)
    zmax = (55*a)//149
    for z in range(zmin, zmax+1):
        H = 19*z - 7*a
        if H <= 0:
            continue
        gg = gcd(a,z)
        if 2 % gg:
            continue
        aa, zz, rhs = a//gg, z//gg, 2//gg
        q0 = (rhs * pow(zz, -1, aa)) % aa
        for lift in range(gg):
            q = q0 + lift*aa
            if not (0 < q < a):
                continue
            B = (q*z-2)//a
            assert q*z-a*B == 2
            n = 19*B-7*q
            assert H*q-n*a == 38
            checked += 1
            if H % 2 == 0 and n % 2 == 0:
                K = H//2
                assert K*q-(n//2)*a == 19
                starts = range(-39,-6)
                sets = [{(s+j*q) % a for j in range(K)} for s in starts]
                assert all(len(S) == K for S in sets)
            else:
                starts = range(-51,-14)
                sets = [{(s+j*q) % a for j in range(H)} for s in starts]
                assert all(len(S) == H for S in sets)
            seen = set()
            for S in sets:
                assert not (seen & S)
                seen |= S
assert checked == 2715

print(f"RL254 verifier: PASS ({checked} red-team determinant tuples)")
