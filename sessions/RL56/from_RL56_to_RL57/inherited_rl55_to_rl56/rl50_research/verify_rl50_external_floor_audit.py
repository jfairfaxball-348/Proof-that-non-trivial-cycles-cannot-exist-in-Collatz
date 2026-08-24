#!/usr/bin/env python3
"""Exact audit of the Ansari 2025 sieve identity used by RL49.

This verifies only elementary residue consequences of the printed definitions.
It does not purport to audit every theorem in the paper.
"""
from itertools import product
from math import gcd

MOD=36

def residues_F(n):
    """Residues mod 36 of the printed F_n definition."""
    step=4*(3**n)
    period=MOD//gcd(step,MOD)
    out=set()
    for k in range(period):
        for bits in product((0,1), repeat=n):
            val=step*k + 4*sum(bits[i]*(3**i) for i in range(n)) + 3
            out.add(val%MOD)
    return out

F1=residues_F(1)
F2=residues_F(2)
assert F1 == {3,7,15,19,27,31}, F1
assert F2 == {3,7,15,19}, F2
assert F1-F2 == {27,31}

# Printed auxiliary F'_n at n=1: a_0,a_1 range independently over {0,1,2}.
Fp1={ (4*(3*a1)+4*a0+3)%36 for a0 in range(3) for a1 in range(3) }
Ap1={ (4*(3*2)+4*2+3)%36 }
assert Fp1 == {3,7,11,15,19,23,27,31,35}, Fp1
assert Ap1 == {35}
assert Fp1-Ap1 == {3,7,11,15,19,23,27,31}
assert Fp1-Ap1 != F2

# The 31 mod 36 layer is nevertheless individually recursive by an explicit
# shortcut-Collatz merge chain.  Check the symbolic formulas on samples.
def T(n):
    return (3*n+1)//2 if n&1 else n//2
for k in range(1000):
    x=36*k+31
    y=(4*x-1)//3
    z=(8*x-5)//9
    assert (4*x-1)%3==0 and (8*x-5)%9==0
    assert y==48*k+41 and z==32*k+27 and z<x
    assert T(2*x)==x
    assert T(y)==2*x
    assert T(z)==y

# Numerical relation quoted in Ansari's Remark 3.1.  The arithmetic is true;
# the sieve induction needed to promote it to a verified-prefix extension is
# exactly what the residue check above does not validate.
lo=2*(3**44)+1
barina=2**71
hi=4*(3**44)+2
assert lo < barina < hi

print('RL50 Ansari external-floor audit: PASS')
print('F1 mod 36 =', sorted(F1))
print('F2 mod 36 =', sorted(F2))
print('F1\\F2 mod 36 =', sorted(F1-F2))
print("F'_1 mod 36 =", sorted(Fp1))
print("A'_1 mod 36 =", sorted(Ap1))
print("F'_1\\A'_1 mod 36 =", sorted(Fp1-Ap1))
print("printed identity F2 = F'_1\\A'_1: FAILS exactly")
print('31 mod 36 layer explicit merge chain: PASS on 1000 symbolic instances')
print('2*3^44+1 < 2^71 < 4*3^44+2: arithmetic PASS')
print('Conclusion: 4*3^44+2 is not admissible here as an audited external floor.')
