#!/usr/bin/env python3
"""Fast algebra/sanity verifier for RL146.

This script does not replace the analytic proof.  It checks the constant arithmetic,
the normalized local recurrence, and exhaustive small binary instances of the
one-step order lemma.
"""
A = 217_976_794_617
L = 137_528_045_312
assert 1 < A/L < 2
assert (A*0)//L == 0
assert (A*L)//L == A

# Mechanical increments sampled at the first/last and many deterministic residues.
for r in [0,1,2,3,10,22,23,10**3,10**6,L//3,L//2,L-2,L-1]:
    if 0 <= r < L:
        a = (A*(r+1))//L - (A*r)//L
        assert a in (1,2)

# Exhaustively verify the local strict-order implication for all binary height digits,
# a in {1,2}, and a generous small integer state window whenever the recurrence is integral.
checked = 0
for a in (1,2):
    M = 2**a
    for yt in range(-20,21):
        for ys in range(-20,21):
            if yt <= ys:
                continue
            for ht in (0,1):
                for htn in (0,1):
                    numt = 3*yt + htn - ht
                    if numt % M:
                        continue
                    ytn = numt//M
                    for hs in (0,1):
                        for hsn in (0,1):
                            nums = 3*ys + hsn - hs
                            if nums % M:
                                continue
                            ysn = nums//M
                            assert ytn > ysn
                            checked += 1
assert checked > 1000

# Toy carry-ladder round trips: build epsilon from binary blocks and check unrolling.
def ladder(d, eps, b):
    z=d
    for r,e in enumerate(eps):
        z=3*z-e*(2**b[r])
    return z

# Direct symbolic identity on toy lengths: z_L = 3^L d - weighted epsilon sum.
for Lt in range(1,8):
    At=Lt+max(1,Lt//2)
    if At >= 2*Lt:
        At=2*Lt-1
    b=[(At*r)//Lt for r in range(Lt+1)]
    for d in range(-3,4):
        for mask1 in range(1<<Lt):
            h1=[(mask1>>r)&1 for r in range(Lt)]
            mask2=(mask1*5+3)%(1<<Lt)
            h2=[(mask2>>r)&1 for r in range(Lt)]
            eps=[h1[r]-h2[r] for r in range(Lt)]
            z=ladder(d,eps,b)
            direct=(3**Lt)*d-sum(eps[r]*(2**b[r])*(3**(Lt-1-r)) for r in range(Lt))
            assert z==direct

print("RL146 fast verifier: PASS")
print("checked local order instances =", checked)
print("scope = analytic proof is in report; verifier is algebra/sanity only")
