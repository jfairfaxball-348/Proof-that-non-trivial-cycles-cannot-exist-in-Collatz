#!/usr/bin/env python3
from math import ceil

A = 1100
Q = 317

def step_x(d, J, x):
    """Exact RL45/RL64 u-driven internal transition. Return (d',J',y) or None."""
    if J & 1:  # same-bit edge
        y = x
        if x == 0:  # 00
            return d, (J + 3**d - 2**d)//2, y
        else:       # 11
            return d, (3*J + 2**d - 1)//2, y
    else:      # skew edge
        y = 1 - x
        if x == 0:  # 01
            return d+1, (3*J + 3**(d+1) - 2**d - 1)//2, y
        else:       # 10
            if d <= 1:
                return None
            return d-1, J//2, y

# Exact historical internal start after the mandatory local (0,1) column.
d, J = 1, -13
for x in (1, 1):
    out = step_x(d, J, x)
    assert out is not None
    d, J, _ = out
assert (d, J) == (1, -28)
assert step_x(d, J, 1) is None  # third leading internal one is impossible.

# RL256 proves k=33 => u_3...u_6 = 1111. Since u=110 x 1 0^(k-3),
# positions 3... are the internal x-word, so k=33 is impossible.
K33_ELIMINATED = True

# k=31 right flank: u_3...u_11 are the first 9 internal x-bits.
right_weights = list(range(9, 0, -1))
states = [(1, -13, "", 0)]
for w in right_weights:
    nxt = []
    for d, J, bits, cost in states:
        for x in (0, 1):
            out = step_x(d, J, x)
            if out is None:
                continue
            d2, J2, _ = out
            nxt.append((d2, J2, bits + str(x), cost + (0 if x else w)))
    states = nxt

assert len(states) == 199
min_right = min(s[3] for s in states)
minimizers = sorted(s[2] for s in states if s[3] == min_right)
assert min_right == 11
assert minimizers == ["110110111", "110111010"]

# RL256 gives E_31 <= 27, so the left ten internal flank sites
# (-39,...,-30) of weights 1,...,10 have budget at most 16.
left_weights = list(range(1, 11))
left_budget = 27 - min_right
assert left_budget == 16
assert sum(left_weights[:5]) == 15
assert sum(left_weights[:6]) == 21 > left_budget

# Exact number of left 10-bit x-patterns inside the universal weight budget.
left_patterns = []
for mask in range(1 << 10):
    bits = "".join("1" if ((mask >> (9-i)) & 1) else "0" for i in range(10))
    cost = sum(w for i, w in enumerate(left_weights) if bits[i] == "0")
    if cost <= left_budget:
        left_patterns.append((bits, cost))
assert len(left_patterns) == 141

# Exact RL256 seven-layer complement.
blocks = [(129,161),(278,310),(446,478),(595,627),
          (763,795),(912,944),(1061,1093)]
U = set()
for lo, hi in blocks:
    U.update(range(lo, hi+1))
comp = set(range(A)) - U

gaps = []
for idx, (lo, hi) in enumerate(blocks):
    next_lo = blocks[(idx+1) % len(blocks)][0]
    start = (hi + 1) % A
    end = (next_lo - 1) % A
    if idx < len(blocks)-1:
        pts = list(range(start, end+1))
    else:
        pts = list(range(start, A)) + list(range(0, end+1))
    gaps.append(pts)
assert [len(g) for g in gaps] == [116,135,116,135,116,116,135]

def excluded_roots(zero_positions):
    # From P_(i+1)-P_i=u_i-u_(i+q), a zero u_p excludes a negative
    # root at p and at p-q+1, because Branch-C negative roots are isolated -1s.
    ex = set()
    for p in zero_positions:
        p %= A
        ex.add(p)
        ex.add((p - Q + 1) % A)
    return ex

def capacity(excluded):
    # Exact maximum number of roots in each complement gap with spacing >=3.
    # Greedy earliest-choice is optimal on a line for equal-weight points.
    total = 0
    for pts in gaps:
        if pts[0] > pts[-1]:  # unwrap the cyclic gap across 0
            coords = [p if p >= pts[0] else p + A for p in pts]
        else:
            coords = pts
        last = -10**18
        for c, p in zip(coords, pts):
            if p in excluded:
                continue
            if c - last >= 3:
                total += 1
                last = c
    return total

tail31 = [p % A for p in range(-28, 0)]
tail_ex = excluded_roots(tail31)
assert capacity(tail_ex) == 287

# Enumerate exact finite flank x-word supersets:
# right prefix must be canonically legal; left suffix is any x-pattern.
# First filter E<=27, then apply exact complement capacity after all known zeros.
suffixes = []
for mask in range(1 << 10):
    bits = "".join("1" if ((mask >> (9-i)) & 1) else "0" for i in range(10))
    cost = sum(w for i, w in enumerate(left_weights) if bits[i] == "0")
    suffixes.append((bits, cost))

budget_pairs = 0
capacity_pairs = 0
for d, J, rbits, rcost in states:
    rzeros = [3+i for i, ch in enumerate(rbits) if ch == "0"]
    rex = excluded_roots(rzeros)
    for lbits, lcost in suffixes:
        E = rcost + lcost
        if E > 27:
            continue
        budget_pairs += 1
        lzeros = [(-39+i) % A for i, ch in enumerate(lbits) if ch == "0"]
        ex = tail_ex | rex | excluded_roots(lzeros)
        cap = capacity(ex)
        # Complement must support at least 260+E isolated negative roots.
        if 260 + E <= cap:
            capacity_pairs += 1

assert budget_pairs == 3064
assert capacity_pairs == 2719

print("RL257 terminal/prefix verifier: PASS")
print("k33_eliminated=", K33_ELIMINATED)
print("k31_legal_right_prefixes=", len(states))
print("k31_min_right_zero_cost=", min_right)
print("k31_minimizers=", minimizers)
print("k31_left_budget_max=", left_budget)
print("k31_left_patterns_universal=", len(left_patterns))
print("k31_flank_pairs_E_budget=", budget_pairs)
print("k31_flank_pairs_after_exact_capacity=", capacity_pairs)
print("classification=R4_BRIDGE_REDUCED")
