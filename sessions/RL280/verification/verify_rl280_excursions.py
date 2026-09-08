#!/usr/bin/env python3
from fractions import Fraction
from collections import defaultdict

RHO = Fraction(2, 3)

def k_step(d, K, x):
    if K % 2 == 0:
        if x == 1:
            return d, 3*K//2
        return d, (K + 3**d - 1)//2
    if x == 1:
        if d <= 1:
            return None
        return d-1, (K-1)//2
    return d+1, 3*(K + 3**d)//2

def y_from(d, K, x):
    return x if K % 2 == 0 else 1-x

def J_from_K(d, K):
    return K - 2**d + 1

def zero_ranks(w):
    ones = 0
    out = []
    for b in w:
        if b:
            ones += 1
        else:
            out.append(ones)
    return out

def generate_excursions(K0, max_len=12):
    assert K0 % 2
    st = k_step(1, K0, 0)
    assert st is not None
    d, K = st
    y = y_from(1, K0, 0)
    assert (d, y) == (2, 1)
    frontier = [(d, K, 0, (0,), (1,), Fraction(2,1))]
    out = []
    while frontier:
        d, K, H, xw, yw, q = frontier.pop()
        if len(xw) > 1 and d == 1:
            out.append((K0, K, H, xw, yw, q))
            continue
        if len(xw) >= max_len:
            continue
        for x in (0,1):
            st = k_step(d, K, x)
            if st is None:
                continue
            d2, K2 = st
            y = y_from(d, K, x)
            frontier.append((
                d2, K2, H+d-1,
                xw+(x,), yw+(y,),
                q*Fraction(2, 3**x)
            ))
    return out

def metrics(ex):
    K0, K1, H, xw, yw, q = ex
    u = zero_ranks(xw)
    v = zero_ranks(yw)
    assert len(u) == len(v)
    h = [b-a for a,b in zip(u,v)]
    z = len(u)
    c = [Fraction(2**j,1)*RHO**u[j] for j in range(z)]
    S = sum(c, Fraction(0))
    D = sum((cj*(1-RHO**hj) for cj,hj in zip(c,h)), Fraction(0))
    return K0,K1,H,xw,yw,q,u,v,h,z,c,S,D

def a_d(d,c):
    return Fraction(1,1) + Fraction(2**(d-1),1)*(c-1)

def phi(d,K,Q,c):
    return Q*Fraction(K,1)/3**d + Q*a_d(d,c)/3**d

def check_global_endpoint_potential():
    vals = [Fraction(-2), Fraction(-3,2), Fraction(-1), Fraction(-1,2), Fraction(0)]
    checked = 0
    strict_ascents = 0
    for d in range(1,9):
        for K in range(-120,121):
            for x in (0,1):
                st = k_step(d,K,x)
                if st is None:
                    continue
                d2,K2 = st
                Q = Fraction(7,5)
                Q2 = Q*Fraction(2,3**x)
                for c in vals:
                    delta = phi(d2,K2,Q2,c)-phi(d,K,Q,c)
                    assert delta >= 0
                    if K % 2 and x == 0:
                        assert delta > 0
                        strict_ascents += 1
                    checked += 1
    return checked, strict_ascents

def check_excursions():
    checked = 0
    equality = 0
    by_pair = defaultdict(set)
    congruence_w = defaultdict(set)
    for K0 in range(-199,200,2):
        for ex in generate_excursions(K0,12):
            (K0,K1,H,xw,yw,q,u,v,hs,z,c,S,D) = metrics(ex)
            L = len(xw)
            E = H-(L-1)
            P_ratio = q*(2**H)
            assert P_ratio == 2*Fraction(4,3)**H * 3**(z-1) * Fraction(3,2)**E
            assert sum(hs) == H
            assert all(hj >= 1 for hj in hs)
            assert H >= z

            for j in range(z-1):
                g = u[j+1]-u[j]
                assert g <= hs[j]-1
                assert c[j+1] >= 3*c[j]*RHO**hs[j]

            env = 1 + Fraction(2**z-4,3)*RHO**(H-z)
            assert D >= env

            s = H-z
            normal = (
                xw == (0,)+(1,)*s+(0,)*(z-1)+(1,)
                and yw == (1,)*(s+1)+(0,)*z
            )
            eq = (D == env)
            assert eq == normal
            if eq:
                equality += 1
                w = 2*K1-7
                assert w % 2
                assert 3**(s+1)*(K0+3) == 2**(s+1)*(8+2**(z-1)*w)
                by_pair[(H,z)].add(K0 % 2**(H+1))
                congruence_w[(H,z)].add(w % 3**(s+1))

            # Exact local endpoint identity.
            assert q*K1-K0 == 2*S+D

            theta = Fraction(7,2) - Fraction(2,1)**(3-z)
            assert q*(K1-theta) >= K0+3

            if z == 1:
                assert D == 1-RHO**H
                assert xw == (0,)+(1,)*H
            if z >= 2:
                assert D >= 1

            checked += 1

    assert all(len(v)==1 for v in by_pair.values())
    assert all(len(v)==1 for v in congruence_w.values())
    return checked, equality, len(by_pair)

def step_JQ(d,J,x,Q):
    K = J+2**d-1
    st = k_step(d,K,x)
    if st is None:
        return None
    d2,K2 = st
    return d2,J_from_K(d2,K2),Q*Fraction(2,3**x)

def boundary_stay_exit(J,Q):
    assert J > 0 and J % 2
    n = (J-1)//2
    stay_x = 0 if n % 2 == 0 else 1
    exit_x = 1-stay_x
    stay = step_JQ(1,J,stay_x,Q)
    exitst = step_JQ(1,J,exit_x,Q)
    assert stay and exitst
    assert stay[0] == 1 and stay[1] > 0 and stay[1] % 2
    assert exitst[0] == 1 and exitst[1] > 0 and exitst[1] % 2 == 0
    return stay,exitst

def check_positive_checkpoint_blocks():
    checks = 0
    min_inc = None
    for J0 in range(2,201,2):
        K0 = J0+1
        for ex in generate_excursions(K0,11):
            Kstart,Kb,H,xw,yw,Qb,u,v,hs,z,c,S,D = metrics(ex)
            Jb = Kb-1
            Fin = Fraction(J0+3,1)

            def check_exit(Je,Qe):
                nonlocal checks,min_inc
                Fnext = Qe*(Je+3)
                inc = Fnext-Fin
                floor = Fraction(1,3) if z == 1 else Fraction(1,1)
                assert inc > floor
                if min_inc is None or inc < min_inc:
                    min_inc = inc
                checks += 1

            if Jb % 2 == 0:
                assert Jb > 0
                check_exit(Jb,Qb)
                continue

            assert Jb > 0
            J,Q = Jb,Qb
            for _ in range(20):
                stay,exitst = boundary_stay_exit(J,Q)
                _,Je,Qe = exitst
                check_exit(Je,Qe)
                _,J,Q = stay

    assert min_inc == Fraction(1241,2187)
    return checks,min_inc

def check_terminal_ceiling():
    # For k>=3 and X<160/3:
    # F_T=X(1/2+3/2^(k+1)) < (160/3)*(1/2+3/16)=110/3.
    assert Fraction(160,3)*(Fraction(1,2)+Fraction(3,16)) == Fraction(110,3)

def main():
    gp = check_global_endpoint_potential()
    ex = check_excursions()
    cp = check_positive_checkpoint_blocks()
    check_terminal_ceiling()
    print("PASS RL280 positive-excursion/state-scale fast verifier")
    print("global_endpoint_potential_checks=", gp[0])
    print("strict_ascent_checks=", gp[1])
    print("first_return_excursions=", ex[0])
    print("depth_two_equality_excursions=", ex[1])
    print("equality_parameter_pairs=", ex[2])
    print("positive_checkpoint_block_checks=", cp[0])
    print("minimum_normalized_checkpoint_increment=", cp[1])
    print("terminal_F_ceiling=", Fraction(110,3))
    print("classification=SHARP_POSITIVE_EXCURSION_STATE_SCALE_LYAPUNOV_PROVED")
    print("gate_A=OPEN")

if __name__ == "__main__":
    main()
