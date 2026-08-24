#!/usr/bin/env python3
from itertools import product


def v2(n: int) -> int:
    assert n != 0
    n = abs(n)
    return (n & -n).bit_length() - 1


def K_of(d,H):
    return H + d*(d+1)//2 - 1


def rl45_step(d,H,J,edge):
    if edge == '00':
        assert J & 1
        J2 = (J + 3**d - 2**d)//2
        return d, H+d-1, J2
    if edge == '11':
        assert J & 1
        J2 = (3*J + 2**d - 1)//2
        return d, H+d-1, J2
    if edge == '01':
        assert not (J & 1)
        J2 = (3*J + 3**(d+1) - 2**d - 1)//2
        return d+1, H+d-1, J2
    if edge == '10':
        assert not (J & 1) and d > 1
        return d-1, H+d-1, J//2
    raise ValueError(edge)


def T_of(d,J):
    return J - 3**d + 2**d


def t_formula(T,d,edge):
    if edge == '00': return T//2
    if edge == '11': return (3*T + 3**d - 1)//2
    if edge == '01': return (3*T - 1)//2
    if edge == '10': return (T + 3**(d-1))//2
    raise ValueError(edge)


def macro_C(word):
    # 0 = 00, 1 = 11.  C satisfies 2^n J_n = 3^s J_0 + C.
    n = len(word)
    C = 0
    for r,x in enumerate(word):
        later = sum(word[r+1:])
        C += (2**r) * (3**later)
    return C


def macro_direct(J0,word):
    J=J0
    vals=[J]
    for x in word:
        assert J & 1
        J = (J+1)//2 if x==0 else (3*J+1)//2
        vals.append(J)
    return vals

# 1. Check K increments and T transition formulas over a broad exact sample.
for d in range(1,9):
    for H in range(0,9):
        for J in range(-101,102):
            if J & 1:
                for e in ('00','11'):
                    d2,H2,J2=rl45_step(d,H,J,e)
                    assert K_of(d2,H2)-K_of(d,H) == d-1
                    assert T_of(d2,J2) == t_formula(T_of(d,J),d,e)
            else:
                d2,H2,J2=rl45_step(d,H,J,'01')
                assert K_of(d2,H2)-K_of(d,H) == 2*d
                assert T_of(d2,J2) == t_formula(T_of(d,J),d,'01')
                if d>1:
                    d2,H2,J2=rl45_step(d,H,J,'10')
                    assert K_of(d2,H2)-K_of(d,H) == -1
                    assert T_of(d2,J2) == t_formula(T_of(d,J),d,'10')
                    if J != 0:
                        assert v2(J2)-K_of(d2,H2) == v2(J)-K_of(d,H)

# 2. Check synchronized affine composition for all legal words <=7 and many odd entries.
checked_macros=0
for n in range(1,8):
    for word in product((0,1), repeat=n):
        s=sum(word); C=macro_C(word)
        for J0 in range(1,400,2):
            try:
                vals=macro_direct(J0,word)
            except AssertionError:
                continue
            Jn=vals[-1]
            assert (2**n)*Jn == (3**s)*J0 + C
            # prefix odd selector for every pre-exit state
            for r,Jr in enumerate(vals[:-1]):
                assert Jr & 1
            checked_macros += 1

# 3. Unrestricted all-11 obstruction family.
# For every tested H,n choose odd q = (3^n)^(-1) mod 2^(H+1).
# J0=2^n q-1 stays odd for n 11-steps and exits with Jn=3^n q-1 divisible by 2^(H+1).
family_cases=0
min_excess=10**9
for H in range(0,17):
    for n in range(1,9):
        M=2**(H+1)
        q=pow(3**n,-1,M)
        assert q & 1
        J0=2**n*q-1
        vals=macro_direct(J0,(1,)*n)
        for r in range(n):
            assert vals[r] == 2**(n-r)*3**r*q - 1
            assert vals[r] & 1
        Jn=vals[-1]
        assert Jn == 3**n*q-1 and Jn>0
        assert Jn % M == 0
        exc=v2(Jn)-H
        assert exc>=1
        min_excess=min(min_excess,exc)
        family_cases += 1

# 4. Exact sharp equality witness in the reachable quotient.
path='00 01 10 00 00 01 11 10 11 11'.split()
d,H,J=1,0,-13
for e in path:
    d,H,J=rl45_step(d,H,J,e)
assert (d,H,J)==(1,3,8)
assert K_of(d,H)==3 and v2(J)==3

print('PASS RL63 even-exit selector checks')
print('T_transition_and_K_delta_sample PASS')
print('synchronized_affine_macros_checked',checked_macros)
print('unrestricted_all11_family_cases',family_cases,'min_v2_minus_H',min_excess)
print('reachable_sharp_equality_state',d,H,J,'K',K_of(d,H),'v2',v2(J))
print('10_margin_invariance PASS')
