#!/usr/bin/env python3
"""Independent RL195 adjacency constant audit; NOT PROMOTED.

Uses 128 positive logarithm terms and degree-12 exponential sums, distinct
from the proposed verifier's 96 terms and quadratic expm1 enclosures.
No actual phase enumeration and no new research-range extension.
"""

from fractions import Fraction as Q
from itertools import product


A, L = 217976794617, 137528045312
p, u0 = 65470613321, 103768467013
B, R, z = A - L, 2 * L - A, L - p
K = 1 << 37


def log_interval(n, terms=128):
    t = Q(n - 1, n + 1)
    lo = 2 * sum((t ** (2 * k + 1) / (2 * k + 1) for k in range(terms)), Q(0))
    tail = 2 * t ** (2 * terms + 1) / ((2 * terms + 1) * (1 - t * t))
    return lo, lo + tail


def expm1_interval(lo, hi, degree=12):
    assert 0 < lo <= hi < 1
    slo, shi = Q(0), Q(0)
    tlo, thi = Q(1), Q(1)
    for k in range(1, degree + 1):
        tlo, thi = tlo * lo / k, thi * hi / k
        slo, shi = slo + tlo, shi + thi
    first_omitted = thi * hi / (degree + 1)
    tail_upper = first_omitted / (1 - hi / (degree + 2))
    return slo, shi + tail_upper


def decimal_enclosure(lo, hi, places=12):
    scale = 10**places
    il = (lo.numerator * scale) // lo.denominator
    ih = -((-hi.numerator * scale) // hi.denominator)
    def show(n):
        return str(n // scale) + "." + str(n % scale).zfill(places)
    return show(il), show(ih)


assert A * p - u0 * L == 1
assert 0 < R < B < 2 * R < L
assert (p * B) % L == 1
assert ((p - 1) * B) % L == R + 1 < 2 * R
assert ((L - 1) * B) % L == R < 2 * R
assert ((R - 1) * p) % L == z - 1
assert ((2 * R - 1) * p) % L == z - 2
assert 0 < z - 2 < z - 1 < z < L
assert 2 * R - 1 >= R and 0 <= R - 1 < R

# All possible binary assignments in the doublet inequality after division
# by its positive first weight. This is exhaustive, not a sampled check.
for x, y in product((0, 1), repeat=2):
    assert x + Q(4, 3) * y <= Q(4, 3) + x * y

l2, h2 = log_interval(2)
l3, h3 = log_interval(3)
dlo, dhi = A * l2 - L * h3, A * h2 - L * l3
assert 0 < dlo < dhi < Q(1, 2**40)
elo, ehi = expm1_interval(dlo, dhi)
tlo, thi = expm1_interval((l2 + z * dlo) / L, (h2 + z * dhi) / L)
etalo, etahi = expm1_interval((l2 - p * dhi) / L, (h2 - p * dlo) / L)
assert 0 < etalo < etahi < tlo < thi
Flo, Fhi = 3 * K * elo, 3 * K * ehi
Mlo, Mhi = 2 * Flo - Q(1, 2) - Q(3, 2) * thi, 2 * Fhi - Q(1, 2) - Q(3, 2) * tlo
Clo, Chi = Q(3, 16) * (1 + tlo), Q(3, 16) * (1 + thi)
assert Mlo > Chi > 0
nlo, nhi = 2 * Flo - Q(11, 16), 2 * Fhi - Q(11, 16)
assert nlo > 0
qlo, qhi = nlo / thi - Q(27, 16), nhi / tlo - Q(27, 16)
assert Q(9719139551) < qlo < qhi < Q(9719139552)
assert qhi - qlo < Q(1, 10**40)
# For integer J-1 strictly above q, the first possible value is
# 9719139552, hence J >= 9719139553.
assert qlo > 9719139551 and qhi < 9719139552
print("PASS independent RL195 adjacency red-team constant certificate")
print("log_terms=128; expm1_degree=12; exact_Fraction_only")
print("M_decimal_enclosure=", decimal_enclosure(Mlo, Mhi))
print("C_decimal_enclosure=", decimal_enclosure(Clo, Chi))
print("threshold_decimal_enclosure=", decimal_enclosure(qlo, qhi))
print("rational_threshold_width<1e-40")
print("J>=9719139553; binary_assignment_coverage=4/4")
print("no_actual_phase_scan; conditional_chronological_adjacency_only")
