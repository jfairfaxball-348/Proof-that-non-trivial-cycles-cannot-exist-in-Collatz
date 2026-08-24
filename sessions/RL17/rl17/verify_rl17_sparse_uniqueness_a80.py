from math import gcd

# Exact finite arithmetic experiment for the normalized cubic sparse equation.
# This is COMPUTATIONAL EVIDENCE ONLY, not an infinite theorem.
# Domain: a<=80, 1<=ell<a, gcd(a,ell)=1, 2^a>3^ell,
# 1<=m<3a, gcd(3a,m)=1, and ap-m*ell=1 with integer p.
# The usual prefix feasibility inequalities are automatic on this domain but
# are asserted explicitly below.

LIMIT = 80
parameter_count = 0
gap_triple_count = 0
cofactor_zero_count = 0
fullD_zero_count = 0
cofactor_skew = []
fullD_skew = []
fullD_zeros = []

for a in range(1, LIMIT + 1):
    X = 1 << a
    for ell in range(1, a):
        if gcd(a, ell) != 1:
            continue
        Y = 3 ** ell
        if X <= Y:
            continue
        C = X * X + X * Y + Y * Y
        D = X ** 3 - Y ** 3

        for m in range(1, 3 * a):
            if gcd(3 * a, m) != 1:
                continue
            num = 1 + m * ell
            if num % a:
                continue
            p = num // a
            assert a * p - m * ell == 1
            assert 0 <= p <= m
            assert 0 <= 3 * ell - p <= 3 * a - m
            parameter_count += 1

            thetaC = pow(pow(2, m, C), -1, C) * pow(3, p, C) % C
            rhoC = pow(thetaC, -1, C)
            thetaD = pow(pow(2, m, D), -1, D) * pow(3, p, D) % D
            rhoD = pow(thetaD, -1, D)

            pC = [1] * (3 * a + 1)
            pD = [1] * (3 * a + 1)
            for r in range(1, 3 * a + 1):
                pC[r] = pC[r - 1] * rhoC % C
                pD[r] = pD[r - 1] * rhoD % D

            zeros_here_C = 0
            for u in range(1, 3 * a - 1):
                baseC = 1 + 3 * pC[u]
                baseD = 1 + 3 * pD[u]
                for v in range(1, 3 * a - u):
                    w = 3 * a - u - v
                    gap_triple_count += 1
                    zC = (baseC + 9 * pC[u + v]) % C == 0
                    zD = (baseD + 9 * pD[u + v]) % D == 0
                    if zC:
                        cofactor_zero_count += 1
                        zeros_here_C += 1
                        if (u, v, w) != (a, a, a):
                            cofactor_skew.append((a, ell, m, p, u, v, w))
                    if zD:
                        fullD_zero_count += 1
                        fullD_zeros.append((a, ell, m, p, u, v, w))
                        if (u, v, w) != (a, a, a):
                            fullD_skew.append((a, ell, m, p, u, v, w))

            # The observed cofactor uniqueness claim is checked per parameter.
            assert zeros_here_C == 1

assert parameter_count == 2785
assert gap_triple_count == 39719443
assert cofactor_zero_count == 2785
assert cofactor_skew == []
assert fullD_zero_count == 2
assert fullD_skew == []
assert {(z[0], z[1], z[4], z[5], z[6]) for z in fullD_zeros} == {(2, 1, 2, 2, 2)}
assert {z[2] for z in fullD_zeros} == {1, 5}

print('RL17 sparse uniqueness finite scan: PASS')
print('a limit:', LIMIT)
print('admissible (a,ell,m,p) parameter choices:', parameter_count)
print('ordered positive gap triples tested:', gap_triple_count)
print('cofactor sparse zeros:', cofactor_zero_count)
print('cofactor skew zeros:', len(cofactor_skew))
print('full-D sparse zeros:', fullD_zero_count)
print('full-D skew zeros:', len(fullD_skew))
print('full-D zeros:', fullD_zeros)
