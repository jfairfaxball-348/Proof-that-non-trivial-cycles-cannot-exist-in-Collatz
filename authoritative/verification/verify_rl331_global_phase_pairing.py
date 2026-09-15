#!/usr/bin/env python3
"""RL331 scratch verifier: uniform phase gain from recurrent zero-slack blocks."""
import contextlib
import io
import runpy
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    base = runpy.run_path(str(Path(__file__).with_name("verify_rl331_self_consistent_ownership.py")))

A = base["A"]
ELL = base["ELL"]
T = base["T"]
K0 = base["K"]
LAM = base["LAM"]
ideal = base["ideal"]
W0 = base["weighted"]
states = base["states"]
edges = base["edges"]
pot = base["pot"]
b2 = base["b2"]


def log_interval_atanh(x, terms=280):
    x2 = x * x
    term = x
    total = Fraction()
    for j in range(terms):
        total += term / (2 * j + 1)
        term *= x2
    lower = 2 * total
    upper = lower + 2 * term / (2 * terms + 1) / (1 - x2)
    return lower, upper


_, LN2_UPPER = log_interval_atanh(Fraction(1, 3))
GAMMA = 1 / LN2_UPPER - 1  # certified lower bound for integral(2^x)-1

# Continued fraction of the step-45 rational rotation.
step = (45 * A) % ELL
x, y = step, ELL
cf = []
while x:
    q, y, x = y // x, x, y % x
    cf.append(q)
assert cf == [3, 10, 1, 3, 13, 107, 4, 1, 4, 3, 1, 3, 3, 2, 2, 5, 2, 1, 1, 3]
assert sum(cf) == 172
# Denjoy--Koksma plus Ostrowski decomposition therefore gives, uniformly in
# starting phase and 0<=m<ELL,
#   sum_{j<m} 2^{{x+j step/ELL}} >= m/ln(2) - 2*172.
DK_ERROR = 2 * sum(cf)

# Build the zero-slack graph and its SCC condensation.
zero_edges = []
adj = defaultdict(list)
for s, t, z, k in edges:
    slack = pot[t] - pot[s] - (2 * z - 43 * k)
    assert slack >= 0
    if slack == 0:
        zero_edges.append((s, t, z, k))
        adj[s].append(t)

index = 0
stack = []
on_stack = set()
indices = {}
lowlink = {}
components = []


def visit(v):
    global index
    indices[v] = lowlink[v] = index
    index += 1
    stack.append(v)
    on_stack.add(v)
    for w in adj[v]:
        if w not in indices:
            visit(w)
            lowlink[v] = min(lowlink[v], lowlink[w])
        elif w in on_stack:
            lowlink[v] = min(lowlink[v], indices[w])
    if lowlink[v] == indices[v]:
        component = []
        while True:
            w = stack.pop()
            on_stack.remove(w)
            component.append(w)
            if w == v:
                break
        components.append(component)


for vertex in range(len(states)):
    if vertex not in indices:
        visit(vertex)

component_of = {v: c for c, members in enumerate(components) for v in members}
cyclic = set()
for c, members in enumerate(components):
    if len(members) > 1 or any(s == t and component_of[s] == c for s, t, _, _ in zero_edges):
        cyclic.add(c)
assert len(cyclic) == 16

# Every internal recurrent edge represents exactly one positive rank.  In each
# cyclic SCC choose N(z), z<=21 as the low class.  Edges alternate classes, and
# successive entries to the low class are exactly 45 ranks apart.
low_class = {v for v, state in enumerate(states) if state[0] == "N" and state[1] <= 21}
internal = defaultdict(list)
for s, t, z, k in zero_edges:
    if component_of[s] == component_of[t] and component_of[s] in cyclic:
        assert k == 1
        assert (s in low_class) != (t in low_class)
        internal[s].append((t, z + k))
for s, outs in internal.items():
    for mid, advance1 in outs:
        for target, advance2 in internal[mid]:
            assert target in low_class if s in low_class else target not in low_class
            if s in low_class:
                assert advance1 + advance2 == 45

# Condensation is a DAG.  Audit the maximum positive multiplicity on external
# zero-slack edges and maximum number of cyclic SCCs met by one zero-slack path.
dag = defaultdict(list)
indegree = [0] * len(components)
seen_arcs = set()
for s, t, _, k in zero_edges:
    c, d = component_of[s], component_of[t]
    if c != d:
        dag[c].append((d, k))
        if (c, d) not in seen_arcs:
            seen_arcs.add((c, d))
            indegree[d] += 1
queue = [c for c, degree in enumerate(indegree) if degree == 0]
topological = []
while queue:
    c = queue.pop()
    topological.append(c)
    for d in {target for target, _ in dag[c]}:
        indegree[d] -= 1
        if indegree[d] == 0:
            queue.append(d)
assert len(topological) == len(components)
external_positive = [0] * len(components)
recurrent_segments = [int(c in cyclic) for c in range(len(components))]
for c in topological:
    for d, k in dag[c]:
        external_positive[d] = max(external_positive[d], external_positive[c] + k)
        recurrent_segments[d] = max(recurrent_segments[d], recurrent_segments[c] + int(d in cyclic))
assert max(external_positive) == 16
assert max(recurrent_segments) == 16

# Let K=K0+h.  Exact telescoping of edge slack and the RL330 endpoint boundary
# gives total true slack S<=45h+3.  There are at most S positive-slack edges.
# Even when an abstract k=3 edge stands for a longer positive run, its extra
# ranks cost 43 slack each; hence all defect-edge positives total at most 3S.
# Removing defects leaves at most S+1 zero-slack blocks.  The audits above then
# give at most 16(S+1) external positive ranks and 16(S+1) recurrent segments.
# Pairing alternating recurrent ranks leaves at least
#   H >= (K - 3S - 16(S+1) - 16(S+1))/2
# step-45 anchors.  Each anchor segment receives the DK lower bound.
@lru_cache(None)
def weighted_residue_lower(K):
    s1 = K * (K + 1) // 2
    s2 = K * (K + 1) * (2 * K + 1) // 6
    s3 = s1 * s1
    s4 = K * (K + 1) * (2 * K + 1) * (3 * K * K + 3 * K - 1) // 30
    l2lo = base["l2lo"]
    return (Fraction(K) + l2lo * s1 / ELL + l2lo**2 * s2 / (2 * ELL**2)
            + l2lo**3 * s3 / (6 * ELL**3) + l2lo**4 * s4 / (24 * ELL**4))


def structural_lower(Kbase, h, base_slack):
    K = Kbase + h
    S = 45 * h + base_slack
    twice_H = K - 35 * S - 32
    return Fraction(K) + GAMMA * twice_H / 2 - DK_ERROR * 16 * (S + 1)


assert 2 * (T + 1) - 45 * K0 == 126
assert b2 == 129

# The inherited distinct-residue lower bound grows by at least one per extra
# positive rank.  Intersect it with the decreasing structural lower envelope.
def certified_gain(Kbase, h, base_slack):
    Wbase = weighted_residue_lower(Kbase)
    return max(Fraction(h), structural_lower(Kbase, h, base_slack) - Wbase)


cross = ((structural_lower(K0, 0, 3) - W0) /
         (1 - (structural_lower(K0, 1, 3) - structural_lower(K0, 0, 3))))
candidates = {0, cross.numerator // cross.denominator, cross.numerator // cross.denominator + 1}
best_h, gain = min(((h, certified_gain(K0, h, 3)) for h in candidates if h >= 0), key=lambda row: row[1])
assert gain > 5000
W_UNIFORM = W0 + gain
rhs = 1 + ideal - W_UNIFORM / (12 * LAM)
new_cap = rhs.numerator // rhs.denominator
assert new_cap < 32_551_214_631

# All-rho closure.  At rho=60 the unusually small endpoint slack gives gain
# 5072.  For rho=61..1845, exhaust the only 80 rounded density floors and all
# 45 possible endpoint slacks; the same argument always gives gain >=5071.
def minimum_gain(Kbase, base_slack):
    Wbase = weighted_residue_lower(Kbase)
    slope = structural_lower(Kbase, 1, base_slack) - structural_lower(Kbase, 0, base_slack)
    crossing = (structural_lower(Kbase, 0, base_slack) - Wbase) / (1 - slope)
    q = max(0, crossing.numerator // crossing.denominator)
    return min(certified_gain(Kbase, h, base_slack) for h in {q, q + 1})


for Kbase_test in range(K0 - 79, K0 + 1):
    for base_slack_test in range(45):
        assert minimum_gain(Kbase_test, base_slack_test) >= 5071

def omitted_lower(last_r):
    return sum((Fraction(1 << ((A * r) // ELL), 3**r) for r in range(1, last_r + 1)), Fraction()) / LAM

full = base["full"]
def baseline_rhs(rho):
    Kbase = (2 * (ELL - rho + 1) - b2 + 44) // 45
    return 1 + (full - omitted_lower(rho - 1)) / 3 - weighted_residue_lower(Kbase) / (12 * LAM)

BOOTSTRAP = 32_551_214_209
assert rhs < BOOTSTRAP  # rho=60, gain 5072
assert baseline_rhs(61) - Fraction(5071, 12) / LAM < BOOTSTRAP
assert baseline_rhs(1846) < BOOTSTRAP
assert base["rho59"] < BOOTSTRAP
# From rho=61 onward, the inherited monotonicity applies both with the fixed
# 5071 gain (through rho 1845) and without it (from rho 1846 onward).
max_weight = base["max_weight"]
assert max_weight / (12 * LAM) < Fraction(1, 6) / LAM

print("RL331_GLOBAL_PHASE_PAIRING_VERIFIER_GREEN")
print("step45", step, "cf_digit_sum", sum(cf), "dk_error", DK_ERROR)
print("zero_sccs", len(components), "cyclic_sccs", len(cyclic))
print("max_external_positive", max(external_positive), "max_recurrent_segments", max(recurrent_segments))
print("intersection_h", best_h)
print("uniform_weight_gain", float(gain))
print("carry_rhs", float(rhs), "candidate_cap", new_cap)
print("rho61_enhanced_rhs", float(baseline_rhs(61) - Fraction(5071, 12) / LAM))
print("rho1846_baseline_rhs", float(baseline_rhs(1846)))
print("self_consistent_bootstrap", BOOTSTRAP)
