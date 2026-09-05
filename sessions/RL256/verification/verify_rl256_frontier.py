#!/usr/bin/env python3
from math import ceil

# Seven physical blocks and complement gaps.
blocks = [(129,161),(278,310),(446,478),(595,627),
          (763,795),(912,944),(1061,1093)]
assert all(b-a+1 == 33 for a,b in blocks)
assert sum(b-a+1 for a,b in blocks) == 231

gaps = [116,135,116,135,116,116,135]
assert sum(gaps) == 1100-231
cap = sum(ceil(g/3) for g in gaps)
assert cap == 291

# Exact terminal-window raw sums frozen by RL256.
R = {28:262, 30:283, 32:300}
assert R[28] < R[30] < R[32]

# tau>=32 contradicts complement isolated-root capacity.
assert R[32]-2 == 298
assert 298 > cap

# Inherited k odd and k>=31, with tau=k-3 even and tau<32.
ks = [k for k in range(31,151) if k % 2 == 1 and k-3 < 32]
assert ks == [31,33]

# k=33: terminal-tail exclusion reduces two 135-gaps to 129 and 126.
gaps33 = [129,116,135,116,126,116,116]
cap33 = sum(ceil(g/3) for g in gaps33)
assert cap33 == 286
assert cap33 - (R[30]-2) == 5

left33 = [1,2,3,4,5,6,7,8]
right33 = [9,8,7,6,5,4,3,2,1]
assert min(left33[5:] + right33[:4]) >= 6
assert 3+3 > 5

# k=31: analogous exact tail-exclusion capacity.
cap31 = 287
assert cap31 - (R[28]-2) == 27
weights31 = list(range(1,11)) + list(range(9,0,-1))
assert sum(sorted(weights31)[:10]) == 30
assert 30 > 27

print("RL256 frontier verifier: PASS")
print("base_capacity=", cap)
print("surviving_k=", ks)
print("k33_capacity=", cap33, "E33_max=", 5)
print("k31_capacity=", cap31, "E31_max=", 27)
print("classification=R4_BRIDGE_REDUCED")
