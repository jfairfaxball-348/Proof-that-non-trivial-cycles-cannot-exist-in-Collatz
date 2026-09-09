#!/usr/bin/env python3
"""Portable regression verifier for frozen RL290 analytic identities and witnesses.

This is regression support only. The promoted RL290 statements are analytic.
It intentionally does not reproduce the multi-million-state RL282 H<=22 search.
"""

def v2(n):
    assert n != 0
    n = abs(n)
    return (n & -n).bit_length() - 1

def step(d, J, H, x):
    K = J + 2**d - 1
    if K % 2 == 0:
        if x == 1:
            d2, K2 = d, 3*K//2
        else:
            d2, K2 = d, (K + 3**d - 1)//2
    else:
        if x == 1:
            if d <= 1:
                return None
            d2, K2 = d-1, (K-1)//2
        else:
            d2, K2 = d+1, 3*(K+3**d)//2
    J2 = K2 - 2**d2 + 1
    return d2, J2, H + d - 1

def replay(J, word, d=1, H=0):
    out = [(d,J,H)]
    for ch in word:
        st = step(d,J,H,int(ch))
        assert st is not None
        d,J,H = st
        out.append(st)
    return out

def check_mergers():
    count = 0
    for d in range(2, 18, 2):
        K = (3**d - 1)//2
        J = K - 2**d + 1
        a = step(d,J,0,0)
        b = step(d,J,0,1)
        assert a == b
        count += 1

    assert replay(-13, "0001")[-1] == (2,1,3)
    assert replay(-13, "00010")[-1] == (2,3,4)
    assert replay(-13, "00011")[-1] == (2,3,4)

    A = replay(3, "01", d=2, H=1)[-1]
    B = replay(3, "110", d=2, H=1)[-1]
    assert A == B == (1,2,3)
    return count

def check_height_one_launchpads():
    checked = 0
    shell_survivors = 0
    for k in range(3, 100, 2):
        for q in range(1, 42, 2):
            Jin_num = 2**(q+2)*(2**k-1)-2
            assert Jin_num % 3 == 0
            Jin = Jin_num//3
            J0 = 1+2**q*(2**k-1)
            assert 3*(Jin+4) == 2*(2*J0+3)
            assert v2(Jin) == 1
            assert (4*Jin+2) == (2**(q+4)*(2**k-1)-2)//3

            tr = replay(Jin, "01" + "0"*q)
            assert tr[-1] == (1,2**k,1)

            shell = (J0 % 9) in (3,6)
            criterion = (q-k-2) % 6 != 0
            assert shell == criterion
            if shell:
                shell_survivors += 1
            checked += 1
    return checked, shell_survivors

def check_stripped_unit():
    checked = 0
    for J in range(2, 10000, 2):
        t = v2(3*J+2)
        if t < 3:
            continue
        u = (3*J+2)//(2**t)
        tr = replay(J, "01" + "0"*(t-2))
        assert tr[-1] == (1,u+1,1)
        checked += 1
    return checked

def check_exact_witnesses():
    assert replay(21842, "010")[-1] == (1,8192,1)
    assert replay(5378, "01101011110110111")[-1] == (1,21842,1)
    assert replay(2514, "0111110101")[-1] == (1,5378,1)
    assert replay(1074, "011101")[-1] == (1,1364,1)

    assert v2(3*1074+2) == 3
    assert v2((3*1074+2)//8 + 1) == 2
    t = v2(3*1364+2)
    assert t == 1
    assert v2((3*1364+2)//2 + 1) == 11

    assert v2(21842) == 1
    assert 3*21842+2 == 8*8191
    assert 8191+1 == 8192

def check_boundary_loop_formula():
    # Frozen globally reached J=3 seam state.
    B,C,P = 295,-89,128
    assert B-C == 3*P
    for N in range(81):
        # After N loop insertions, physical J remains 3.
        assert B-C == 3*P
        B,C,P = 3*B+3*P, 3*C, 4*P
    return 81

def main():
    mergers = check_mergers()
    launchpads, survivors = check_height_one_launchpads()
    stripped = check_stripped_unit()
    check_exact_witnesses()
    loops = check_boundary_loop_formula()

    print("RL290 fast verifier: PASS")
    print(f"analytic_merger_family_cases={mergers}")
    print(f"height_one_launchpad_cases={launchpads}")
    print(f"height_one_shell_survivors={survivors}")
    print(f"stripped_unit_suffix_cases={stripped}")
    print(f"boundary_loop_iterations={loops}")
    print("extremal_chain=2514->5378->21842->8192")
    print("nested_jump=1074:2->1364:11")
    print("scope=regression_support_only")

if __name__ == "__main__":
    main()
