#!/usr/bin/env python3
from fractions import Fraction
from pathlib import Path
import sys

DELTA0 = 13_201_833_154_443_526_323
C = 42_150_931_628
LOGM_UP = Fraction(42_150_931_628_751_333, 1_000_000)
K0 = 2_921_384_821
LAST = 2_921_406_839
NEXT = LAST + 2
SSTAR_EXPECTED = 26_594_276_905
DTH = 500_036
RTH = 550_000
SHORT = 500_053
MOD_BITS = SHORT + 3
EXPECTED_LAST_MARGIN = 197_551
EXPECTED_NEXT_MARGIN = -67_747
EXPECTED_ODD_COUNT = 11_010


def ceil_frac(x: Fraction) -> int:
    return -(-x.numerator // x.denominator)


def log_interval_int(x: int, terms: int = 260):
    y = Fraction(x - 1, x + 1)
    y2 = y * y
    s = Fraction(0)
    yp = y
    for n in range(terms):
        s += yp / (2*n + 1)
        yp *= y2
    lo = 2*s
    tail = 2*yp / ((2*terms + 1)*(1-y2))
    return lo, lo + tail

l2,u2 = log_interval_int(2)
l3,u3 = log_interval_int(3)
beta_lo = l3/u2
beta_hi = u3/l2
gamma = 2*beta_hi - 3
assert gamma > 0

# Exact safe synchronized-11 cap: 3^s < M and log2(M)<LOGM_UP.
SSTAR = (LOGM_UP.numerator * beta_lo.denominator) // (LOGM_UP.denominator * beta_lo.numerator)
assert SSTAR == SSTAR_EXPECTED


def q_lower(k: int) -> int:
    num = beta_hi*(DELTA0 - 2*k + 4) - 3*LOGM_UP - (4*beta_hi + 3)*(k-1)
    return ceil_frac(num/gamma)


def rsum_upper(k: int, b: int, q: int) -> int:
    # RL88: Q - beta*sum(s_i) < logM + beta*R_exc + b,
    # with R_exc <= H <= k-1.  Put s_i=SSTAR-r_i and Q>=q.
    U = Fraction(k-1, 1) + b*SSTAR + (LOGM_UP + b - q)/beta_hi
    return ceil_frac(U) - 1  # largest integer strictly below U


def top_margin(k: int):
    b = k-1
    q = q_lower(k)
    D = C*b - q
    Ru = rsum_upper(k,b,q)
    bad_d = D // (DTH+1)
    bad_r = Ru // (RTH+1)
    rectangle = b - bad_d - bad_r
    exceptions = 0
    short_cap = D // (C-SHORT)
    margin = rectangle - exceptions - short_cap
    return q,D,Ru,bad_d,bad_r,rectangle,short_cap,margin

# The b-monotonicity needed to reduce every k to its top stratum.
# D(b+1)=D(b)+C. Hence floor(D/(DTH+1)) rises by at least floor(C/(DTH+1)).
# The r-deficiency and short-successor penalty terms are nondecreasing in b,
# while b-(k-1-b) contributes only +2. Therefore the margin falls strictly.
assert C // (DTH+1) == 84_295
assert 2 - (C // (DTH+1)) < 0

# Parse the independently generated GMP certificate.
scan_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name('RL90_DLOG_BAND550K_SCAN.txt')
text = scan_path.read_text()
required = [
    'modulus_bits=500056',
    'r_range=0..550000',
    'global_min_balanced_bitlen=500038 at_r=298303',
    'tail_min_balanced_bitlen=500041 at_r=519699 tail_start=500001',
    'certificate: every balanced inverse residue has |mu_r| >= 2^500037',
    'RL90 band550k 2-adic scan: PASS',
]
for line in required:
    assert line in text, line

# Rectangle implication. If d<=500036 then |m|<2^(d+1)<=2^500037.
# If r<=550000 and n_next>=500054, the minimal recurrence forces
# m == 3^{-(s+1)} mod 2^500056, contradicting the balanced-residue certificate.
assert MOD_BITS == 500_056
assert SHORT == 500_053

worst_margin = None
worst_k = None
count = 0
for k in range(K0, LAST+1, 2):
    stats = top_margin(k)
    margin = stats[-1]
    assert margin > 0, (k, stats)
    count += 1
    if worst_margin is None or margin < worst_margin:
        worst_margin, worst_k = margin, k

assert count == EXPECTED_ODD_COUNT
assert worst_k == LAST
assert worst_margin == EXPECTED_LAST_MARGIN
next_stats = top_margin(NEXT)
assert next_stats[-1] == EXPECTED_NEXT_MARGIN
assert next_stats[-1] <= 0

# Freeze detailed endpoint arithmetic.
last = top_margin(LAST)
assert last == (
    123_139_091_657_886_183_891,
    928_228_223_488_373,
    585_678_568_122_399,
    1_856_319_079,
    1_064_868_187,
    219_572,
    22_021,
    197_551,
)
nxt = top_margin(NEXT)
assert nxt == (
    123_139_091_657_886_183_744,
    928_312_525_351_776,
    585_731_756_676_305,
    1_856_487_670,
    1_064_964_894,
    -45_724,
    22_023,
    -67_747,
)

print('RL90 interval verifier: PASS')
print('SSTAR =', SSTAR)
print('rectangle: d<=500036 and r<=550000 => next block length <=500053')
print('b-monotonic decrement floor from ordinary deficit =', C//(DTH+1))
print('odd values eliminated =', count)
print('eliminated odd interval =', K0, 'through', LAST)
print('last margin =', worst_margin)
print('next odd =', NEXT, 'fixed-certificate margin =', next_stats[-1])
print('new surviving odd lower endpoint >=', NEXT)
