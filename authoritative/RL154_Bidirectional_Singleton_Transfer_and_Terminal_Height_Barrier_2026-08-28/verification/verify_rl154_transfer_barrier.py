#!/usr/bin/env python3
"""Exact count of the unpruned 75-step RL154 defect-prefix relaxation."""

A = 217_976_794_617
L = 137_528_045_312
N = 75

b = [(A*j)//L for j in range(N + 1)]
for j in range(1, N + 1):
    # RL133's floor lock gives b_j=floor(j log_2(3)); the strict inequality
    # is checked here directly.  Thus h_j>=0 implies 2^S_j<3^j.
    assert 2**b[j] < 3**j
dp = {0: 1}
for j in range(N):
    c = b[j + 1] - b[j]
    cap = b[j + 1] - (j + 1)  # S_(j+1)>=j+1 because every a_i>=1.
    nxt = {}
    for h, count in dp.items():
        # a_j=c+h-h_next>=1, h_next>=0, and S_(j+1)>=j+1.
        for h_next in range(min(cap, h + c - 1) + 1):
            nxt[h_next] = nxt.get(h_next, 0) + count
    dp = nxt

total = sum(dp.values())
assert b[-1] == 118
assert min(b[-1] - h for h in dp) >= N
assert total == 15_537_359_898_820_273_235_593_329_305_889

print("RL154 75-step defect-prefix relaxation: PASS")
print(f"S75_min={min(b[-1] - h for h in dp)}")
print(f"reachable_terminal_heights={len(dp)}")
print(f"legal_height_paths={total}")
print("all_nonnegative_prefixes_have_2^S_less_than_3^j=PASS")
assert 3**N > 2**75
print("suffix_75_modulus_3^75_exceeds_m_window=PASS")

# At the terminal cut j=L-N, positivity gives S_j>=j and therefore
# h_j<=b_j-j.  This upper bound is attained locally: use a_i=1 up to the
# cut (so h_i=b_i-i), take one large downward step, then use h=0.
jcut = L - N
bcut = (A*jcut)//L
hmax = bcut - jcut
assert hmax == 80_448_749_261
c_cut = (A*(jcut + 1))//L - bcut
assert c_cut in (1, 2)
# The constructed total exponent is exact without materializing L entries.
# First jcut exponents are 1; at the cut it is c_cut+hmax; the remaining
# mechanical increments sum to A-b_(jcut+1).
assert jcut + (c_cut + hmax) + (A - ((A*(jcut + 1))//L) ) == A
print(f"terminal_cut_height_max_under_local_grammar={hmax}")
print("scope=exact count of a necessary-prefix relaxation; no cycle exclusion")
