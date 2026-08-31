#!/usr/bin/env python3
"""RL194 exact chronological speed-envelope necessary-state certificate."""
from fractions import Fraction
A = 217_976_794_617
L = 137_528_045_312
B = A-L
P = 65_470_613_321
Z = L-P
Q = 88_514_772_733
K0 = 2**37
KLO = 128_081_997_553
ELO, EHI = 72_797_034_370, 103_818_202_602
NEWLO, NEWHI = 75_446_746_413, 102_504_571_503
old_deletions = {
    r for r in ({(L-1+d*B) % L for d in range(1, 38)}
                | {(t*B) % L for t in range(25, 67)}
                | {(t*B) % L for t in range(24)})
    if ELO <= r <= EHI
}
assert len(old_deletions) == 24
assert Q in old_deletions
LIMIT = 1_826_035

def ln_bounds(value, terms=80):
    z = Fraction(value-1, value+1)
    z2 = z*z
    power = z
    total = Fraction(0)
    for k in range(terms):
        total += power/(2*k+1)
        power *= z2
    low = 2*total
    return low, low + 2*power/Fraction(2*terms+1)/(1-z2)

LN2LO, LN2HI = ln_bounds(2)
LN3LO, LN3HI = ln_bounds(3)
DLO = A*LN2LO-L*LN3HI
DHI = A*LN2HI-L*LN3LO
assert Fraction(2, 3) < LN2LO and 0 < DLO < DHI < Fraction(1, 2**40)
assert (L-1)*DHI < LN2LO

def exp_bounds(x, terms=8):
    assert 0 < x < 1
    term = total = Fraction(1)
    for k in range(1, terms+1):
        term *= x/k
        total += term
    first_omitted = term*x/(terms+1)
    tail = first_omitted/(1-x/(terms+2))
    return total, total+tail

def exact_flow_bounds(a, atom, r):
    if atom == 38:
        distance = Q-r
        lo = (distance*LN2LO+a*DLO)/L
        hi = (distance*LN2HI+a*DHI)/L
        low_exp, _ = exp_bounds(lo)
        _, high_exp = exp_bounds(hi)
        return 3*K0*(low_exp-1), 3*K0*(high_exp-1)
    distance = r-Q
    lo = (distance*LN2LO-a*DHI)/L
    hi = (distance*LN2HI-a*DLO)/L
    low_exp, _ = exp_bounds(lo)
    _, high_exp = exp_bounds(hi)
    return 3*K0*(1-1/low_exp), 3*K0*(1-1/high_exp)

def coarse_speed_allowed(a):
    """Necessary before-carry test from |sum f|<a and exact log bounds."""
    assert 0 < a < Z
    start_rank = (a*B) % L
    terminal_rank = (start_rank+Q) % L
    if not ELO <= terminal_rank <= EHI:
        return None
    if terminal_rank < Q:
        distance = Q-terminal_rank
        # 3(K_a-K0) > 2*K0*distance/L, while the prefix flow is <a.
        allowed = 2*K0*distance < a*L
        atom = 38
    else:
        distance = terminal_rank-Q
        # 3(K0-K_a) > (2*KLO*distance - 3*KLO*a/2^40)/L.
        allowed = 2*KLO*distance*2**40 < a*(L*2**40 + 3*KLO)
        atom = 37
    return atom, allowed, terminal_rank, start_rank

first = {}
first_exact = {}
first_weighted = {}
coarse_hits = []
eligible_counts = {37: 0, 38: 0}
rejected_counts = {37: 0, 38: 0}
weighted_survivors = []
tested = 0
SCALE = 2**96
rho_lo = rho_hi = SCALE
positive_sum_lo = positive_sum_hi = 0
negative_sum_lo = negative_sum_hi = 0
rank_i = 0
for phase in range(1, LIMIT+1):
    source = phase-1
    # The first24 physical flows vanish; sources24..28 are negative.
    # These are upper bounds for the positive and negative prefix magnitudes.
    if source >= 24:
        negative_sum_lo += rho_lo
        negative_sum_hi += rho_hi
    if source >= 29:
        positive_sum_lo += rho_lo
        positive_sum_hi += rho_hi
    digit = 1 if rank_i < 2*L-A else 2
    rho_lo = (rho_lo << digit)//3
    rho_hi = ((rho_hi << digit)+2)//3
    rank_i = (rank_i+B) % L
    assert rho_lo <= rho_hi
    result = coarse_speed_allowed(phase)
    tested = phase
    if result is not None:
        atom, allowed, rank, start_rank = result
        eligible = NEWLO <= rank <= NEWHI and rank not in old_deletions
        weighted_allowed = False
        if eligible:
            eligible_counts[atom] += 1
        if allowed and atom not in first:
            first[atom] = (phase, rank, start_rank)
            print(f"first_coarse_atom_{atom}={first[atom]}")
        if allowed:
            flow_lo, flow_hi = exact_flow_bounds(phase, atom, rank)
            assert flow_lo >= phase or flow_hi < phase, "unresolved exact envelope comparison"
            exact_allowed = flow_hi < phase
            coarse_hits.append((phase, atom, rank, exact_allowed))
            if exact_allowed and atom not in first_exact:
                first_exact[atom] = (phase, rank, start_rank)
                print(f"first_exact_speed_atom_{atom}={first_exact[atom]}")
                print(f"first_exact_flow_interval_atom_{atom}=({float(flow_lo)},{float(flow_hi)}) [decimal display only]")
            sum_lo, sum_hi = ((positive_sum_lo, positive_sum_hi) if atom == 38
                              else (negative_sum_lo, negative_sum_hi))
            envelope_lo = Fraction(sum_lo, SCALE)
            envelope_hi = Fraction(sum_hi, SCALE)
            assert flow_lo >= envelope_hi or flow_hi < envelope_lo, "unresolved weighted comparison"
            weighted_allowed = flow_hi < envelope_lo
            if weighted_allowed and eligible:
                weighted_survivors.append((phase, atom, rank))
            if weighted_allowed and atom not in first_weighted:
                first_weighted[atom] = (phase, rank, start_rank)
                print(f"first_weighted_speed_atom_{atom}={first_weighted[atom]}")
                print(f"weighted_envelope_interval_atom_{atom}=({float(envelope_lo)},{float(envelope_hi)}) [decimal display only]")
        if eligible and not weighted_allowed:
            rejected_counts[atom] += 1
    if len(first_weighted) == 2:
        break
assert len(first_weighted) == 2, "finite certificate did not reach both claimed boundaries"
assert first_weighted == {
    38: (190_537, 88_514_759_934, 137_528_032_513),
    37: (1_826_035, 88_515_371_864, 599_131),
}
assert all(NEWLO <= r <= NEWHI and r not in old_deletions
           for _, r, _ in first_weighted.values())
assert sum(eligible_counts.values()) == sum(rejected_counts.values())+len(weighted_survivors)
assert tested == 1_826_035
assert eligible_counts == {37: 185_747, 38: 173_508}
assert rejected_counts == {37: 185_746, 38: 173_499}
assert weighted_survivors == [
    (190_537, 38, 88_514_759_934),
    (381_074, 38, 88_514_747_135),
    (571_611, 38, 88_514_734_336),
    (762_148, 38, 88_514_721_537),
    (952_685, 38, 88_514_708_738),
    (1_143_222, 38, 88_514_695_939),
    (1_333_759, 38, 88_514_683_140),
    (1_524_296, 38, 88_514_670_341),
    (1_714_833, 38, 88_514_657_542),
    (1_826_035, 37, 88_515_371_864),
]
assert Fraction(negative_sum_hi-negative_sum_lo, SCALE) < Fraction(1, 2**40)
assert Fraction(positive_sum_hi-positive_sum_lo, SCALE) < Fraction(1, 2**40)
print(f"coarse_hits={coarse_hits}")
print(f"eligible_rank_counts={eligible_counts}")
print(f"additional_rejected_rank_counts={rejected_counts}")
print(f"weighted_survivors={weighted_survivors}")
print(f"remaining_necessary_rank_cardinality={27_057_825_069-sum(rejected_counts.values())}")
print("canonical_lower_terminal_floor=190574")
print("canonical_upper_terminal_floor=1826072")
print(f"gap_free_checked_start_phases=1..{tested}")
print(f"outside_claimed_scan_after={tested}")
print("scope=necessary_speed_envelope_not_physical_realization")
