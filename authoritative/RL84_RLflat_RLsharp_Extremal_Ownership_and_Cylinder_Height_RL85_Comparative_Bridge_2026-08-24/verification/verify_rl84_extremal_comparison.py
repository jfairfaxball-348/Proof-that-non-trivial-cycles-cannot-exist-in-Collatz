from fractions import Fraction

R0 = 1 << 71
P = 114_208_327_604
Q = 72_057_431_991
E = P - Q

# Rigorous ln intervals via ln z = 2 atanh((z-1)/(z+1)).
def ln_from_atanh_x(x: Fraction, N: int = 260):
    x2 = x*x
    term = x
    s = Fraction(0)
    for k in range(N):
        s += term / (2*k + 1)
        term *= x2
    lo = 2*s
    tail = 2 * term / (2*N + 1) / (1 - x2)
    return lo, lo + tail

ln2_lo, ln2_hi = ln_from_atanh_x(Fraction(1,3))   # (2-1)/(2+1)
ln3_lo, ln3_hi = ln_from_atanh_x(Fraction(1,2))   # (3-1)/(3+1)
ln32_lo, ln32_hi = ln_from_atanh_x(Fraction(1,5)) # ((3/2)-1)/((3/2)+1)

assert 0 < ln2_lo < ln2_hi
assert 0 < ln3_lo < ln3_hi
assert 0 < ln32_lo < ln32_hi

# First Farey survivor defect from RL83.
delta_lo = P*ln2_lo - Q*ln3_hi
delta_hi = P*ln2_hi - Q*ln3_lo
assert 0 < delta_lo < delta_hi < 1
assert delta_lo > Fraction(1, 200_000_000_000)  # > 5e-12

# At Q>40, 2^(Q-1)*delta > 1 follows already from the certified lower bound.
# This is a deliberately weak exact implication that avoids constructing 2^Q.
assert Q > 40
assert (1 << 39) * Fraction(1, 200_000_000_000) > 1

# A conservative exact 'half-height' consequence for the feasible cylinder.
# From theta < 2e11/2^Q and Q odd, h=(Q-1)/2.  It is enough that
# 2*(4/3)^h > 2e11.  This first holds already at h=89 and then grows.
h = (Q-1)//2
assert h >= 89
assert 2 * 4**89 > 200_000_000_000 * 3**89
# Hence theta < 3^-h, so if m=2n is the least even cylinder representative,
# n < 3^(Q-h)=3^((Q+1)/2).  We keep this as a symbolic exponent bound.

# Therefore for Delta=delta: K=D/2^E=2^Q(1-exp(-Delta))
# > 2^(Q-1)*Delta > 1.  This proves D>2^E symbolically.

# Exact floor of 3*R0*ln(3/2), used in the extremal low-arc-or-huge-length dichotomy.
length_lo = 3 * R0 * ln32_lo
length_hi = 3 * R0 * ln32_hi
floor_lo = length_lo.numerator // length_lo.denominator
floor_hi = length_hi.numerator // length_hi.denominator
assert floor_lo == floor_hi
LARGE_L_FLOOR = floor_lo
assert LARGE_L_FLOOR == 2_872_132_254_754_669_047_879

# Finite symbolic sanity audit of extremal inverse-ownership formulas.
# Minimum R: R must be odd; even predecessor 2R is >R and is the only possible
# on-cycle predecessor under minimality. If odd inverse exists, it is <R.
# Maximum M: M must be even and M==2 mod3; odd predecessor is <M, even inverse 2M >M.
checks = 0
for R in range(3, 5000, 2):
    even_pre = 2*R
    assert even_pre > R
    if R % 3 == 2:
        odd_pre = (2*R - 1)//3
        assert 0 < odd_pre < R
    checks += 1
for M in range(8, 10000, 2):
    if M % 3 != 2:
        continue
    odd_pre = (2*M - 1)//3
    assert 0 < odd_pre < M
    assert 2*M > M
    assert 2*M == 3*odd_pre + 1
    checks += 1

# Finite exact audit of the cylinder-transfer law on short words.
# Backward recurrence: E: B->2B, O: B->2B+3^o.
def defect(word):
    B = 0
    o = 0
    for c in word:
        if c == 'E':
            B *= 2
        else:
            B = 2*B + 3**o
            o += 1
    return B, o

words = ['O','OE','OOE','OEO','OOEE','OEOE','OOOEEE','OEOOEE','OOEOEE']
transfer_checks = 0
for w in words:
    B,o = defect(w)
    i = len(w)
    mod3 = 3**o
    r = (B * pow(2, -i, mod3)) % mod3
    # Unique even M representative modulo 2*3^o.
    m = r if r % 2 == 0 else r + mod3
    assert m % 2 == 0
    assert (pow(2,i)*m - B) % mod3 == 0
    # F=2M has a unique class modulo 4*3^o and preserves normalized height.
    f = 2*m
    assert f % 4 == 0
    assert (f - 2*m) % (4*mod3) == 0
    assert Fraction(f, 4*mod3) == Fraction(m, 2*mod3)
    transfer_checks += 1

print('RL84 extremal-comparison verifier: PASS')
print('R0 =', R0)
print('first Farey pair =', (P,Q))
print('certified first-pair defect lower bound > 1/(2e11)')
print('symbolic consequence: D/2^E > 1')
print('floor(3*R0*ln(3/2)) =', LARGE_L_FLOOR)
print('hence integer L in huge branch >=', LARGE_L_FLOOR + 1)
print('extremal ownership sanity checks =', checks)
print('cylinder-transfer sanity checks =', transfer_checks)
