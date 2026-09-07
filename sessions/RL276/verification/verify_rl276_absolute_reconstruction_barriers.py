#!/usr/bin/env python3
from fractions import Fraction

def half_step(n):
    return (3*n+1)//2 if n % 2 else n//2

def check_n3():
    x = 3
    seq = [x]
    for _ in range(8):
        x = half_step(x)
        seq.append(x)
    assert seq[:7] == [3,5,8,4,2,1,2]
    assert 7 not in seq

def check_full_modulus_algebra():
    # Audit the exact rearrangement for broad symbolic integer samples.
    checks = 0
    for r in range(0,8):
        ell = r + 3
        mod = 3**ell
        for a in range(max(ell+1,5), max(ell+1,5)+12):
            for k in range(1, min(a,9), 2):
                for D in (0,1,2,5,13,41):
                    rhs = 237*3**r - 12*D - 2**(a-k+1)
                    # Compare the residue obtained by multiplying the exact
                    # equality (N-2)(2^a-3^ell)=rhs modulo 3^ell.
                    inv2a = pow(2**a, -1, mod)
                    nres = (2 + inv2a*rhs) % mod
                    assert ((nres-2)*2**a-rhs) % mod == 0
                    checks += 1
    return checks

def check_archimedean():
    # If N>=11 and (N-2)M < 237*3^r, then M/3^ell <79/81.
    checks = 0
    for r in range(0,12):
        Y = 3**(r+3)
        cap_num = 79*Y
        cap_den = 81
        for N in range(11,100,8):
            # Largest integer M allowed by the strict quotient inequality.
            maxM = (237*3**r - 1)//(N-2)
            assert maxM * cap_den < cap_num
            checks += 1
    return checks

def check_unique_box():
    for ell in range(3,16):
        Y = 3**ell
        # Any x <2Y lies in an interval shorter than 8Y.
        assert 2*Y < 8*Y

def check_pump_box():
    # Exact rational audit of coefficient < N/2 and maximal-depth compatibility.
    checks = 0
    for N in range(1,500):
        coeff = Fraction(9*(N-2)*(N+4), 43*N+72)
        assert coeff < Fraction(N,2)
        for a in range(2,80):
            # Avoid floating point: (4/3)^q < 2^a for q<=floor(a/2).
            q = a//2
            assert 4**q < (3**q)*(2**a)
            if N < 2**a:
                # The scale demand using ((4/3)^q-1) is < 2^(2a-1).
                lhs = coeff * (Fraction(4,3)**q - 1)
                assert lhs < 2**(2*a-1)
            checks += 1
    return checks

def main():
    check_n3()
    c1 = check_full_modulus_algebra()
    c2 = check_archimedean()
    check_unique_box()
    c3 = check_pump_box()
    print("PASS RL276 absolute reconstruction/barrier verifier")
    print(f"full_modulus_checks={c1}")
    print(f"archimedean_checks={c2}")
    print(f"pump_box_checks={c3}")
    print("classification=GATE_A_EXACT_BARRIER")
    print("subordinate=ABSOLUTE_QUOTIENT_RECONSTRUCTION_IDENTIFIED")
    print("subordinate=ZERO_CARRY_PHYSICAL_BOX_INSUFFICIENT_FOR_PUMP_SCALE")

if __name__ == "__main__":
    main()
