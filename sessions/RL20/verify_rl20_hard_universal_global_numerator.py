from fractions import Fraction
from itertools import product


def Qword(w):
    pos = [i+1 for i,b in enumerate(w) if b]
    L = len(pos)
    return sum((1 << (p-1)) * 3**(L-k-1) for k,p in enumerate(pos))

assert Qword([1,1,0]) == 5
assert Qword([1,0]) == 1

# Exact concatenation identity and the fixed endpoint formula are checked on
# every middle word through length 8.
checks = 0
for M in range(0,9):
    for e in product([0,1], repeat=M):
        e = list(e)
        N = sum(e)
        d = [1,1,0] + e + [1,0]
        A = M + 5
        L = N + 3
        qd = Qword(d)
        rhs = 5*3**(L-2) + 24*Qword(e) + 2**(A-2)
        assert qd == rhs

        # For fixed length/weight, all ones first minimize Q(e).
        emin = [1]*N + [0]*(M-N)
        assert Qword(e) >= Qword(emin)
        assert Qword(emin) == 3**N - 2**N

        # R20N.4 follows exactly.
        lower = Fraction(13,9)*3**L + 2**(A-2) - 3*2**L
        assert Fraction(qd,1) >= lower
        checks += 1

# Clean constant threshold: already L>=12 makes R20N.6 exceed 5/3.
for L in range(12,100):
    rhs = Fraction(61,36) - 3*Fraction(2,3)**L
    assert rhs > Fraction(5,3)

# Near resonance lambda<16/15 converts the lambda-1 bound into the stated
# D/2^A constant: (15/16)*(5/3)=25/16.
assert Fraction(15,16)*Fraction(5,3) == Fraction(25,16)

print('RL20 hard-universal global-numerator verifier: PASS')
print('exhaustive fixed-endpoint word checks =', checks)
print('61/36 - 3(2/3)^L > 5/3 for all tested L>=12')
print('near-resonant defect coefficient = 25/16')
