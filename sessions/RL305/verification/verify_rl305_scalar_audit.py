#!/usr/bin/env python3
"""Portable arithmetic regression for RL305 exact scalar-audit formulas."""

def BL(D):
    return (D*D + D - 6)//2

def BR(D):
    return (D*D + 3*D - 4)//2

def CA(d):
    return d*d - 2*d - 1

def CF(d):
    return d*d - d - 2

# Min-plus elimination:
# m2=1+min(r,e8), mA=1+min(m2,d0), mP=1+min(mA,m2)
for r in range(0, 15):
    for e8 in range(0, 15):
        for d0 in range(0, 15):
            m2 = 1 + min(r, e8)
            mA = 1 + min(m2, d0)
            mP = 1 + min(mA, m2)
            assert mP == 2 + min(r, e8, d0)

# D0 exact first-departure source costs by summing the zero-spine edges.
for d in range(3, 101):
    to_Vd = sum(2*(j-1) for j in range(3, d))
    got_A = to_Vd + (d-1)
    got_F = to_Vd + 2*(d-1)
    assert got_A == CA(d)
    assert got_F == CF(d)

# RL302 wall credit differences.
for D in range(5, 201, 2):
    assert BL(D) - BR(D-2) == D
    assert BR(D) - BL(D) == D + 1
    assert BL(D) - BL(D-2) == 2*D - 1
    assert BR(D) - BR(D-2) == 2*D + 1
    assert BR(D) - BL(D-2) == 3*D

# RL303 normalized branch weights.
# weight = owner_credit - source_credit - (source_cost-owner_cost)
for D in range(5, 101, 2):
    for k in range(2, 40):
        w1 = BR(D-2) - BL(D) - (4-k)
        assert w1 == k-D-4
        w2 = BL(D-2) - BL(D) - (6-k)
        assert w2 == k-2*D-5
        w4 = BR(D-2) - BR(D) - (7-k)
        assert w4 == k-2*D-8
    for k in range(1, 40):
        w3 = BL(D-2) - BR(D) - (2-k)
        assert w3 == k-3*D-2

for D in range(3, 101, 2):
    for k in range(0, 40):
        wadj = BR(D) - BL(D) - (k+2)
        assert wadj == D-k-1

print("RL305_SCALAR_AUDIT_GREEN")
print("minplus_checks", 15**3)
print("d0_source_cost_checks", 98)
print("wall_credit_depths", len(range(5,201,2)))
print("normalized_weight_regressions", "PASS")
print("Gate_A", "OPEN")
print("Bcal_P", "OPEN")
print("O1", "OPEN")
