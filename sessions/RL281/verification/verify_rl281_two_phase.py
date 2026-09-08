#!/usr/bin/env python3
from fractions import Fraction
from collections import deque, defaultdict

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

def J_from_K(d, K):
    return K - 2**d + 1

def y_from(d, K, x):
    return x if K % 2 == 0 else 1-x

def step_JQH(d, J, Q, H, x):
    K = J + 2**d - 1
    st = k_step(d, K, x)
    if st is None:
        return None
    d2, K2 = st
    return d2, J_from_K(d2, K2), Q*Fraction(2, 3**x), H+d-1

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
    hs = [b-a for a,b in zip(u,v)]
    z = len(u)
    c = [Fraction(2**j,1)*RHO**u[j] for j in range(z)]
    S = sum(c, Fraction(0))
    D = sum((cj*(1-RHO**hj) for cj,hj in zip(c,hs)), Fraction(0))
    return K0,K1,H,xw,yw,q,u,v,hs,z,c,S,D

def nu2(n):
    n = abs(n)
    assert n > 0
    s = 0
    while n % 2 == 0:
        s += 1
        n //= 2
    return s

def check_mod3_invariant():
    checked = 0
    for d in range(1,10):
        eps = pow(2,d,3)
        for J in range(-300,301):
            if J % 3 not in (0,eps):
                continue
            K = J + 2**d - 1
            for x in (0,1):
                st = k_step(d,K,x)
                if st is None:
                    continue
                d2,K2 = st
                J2 = J_from_K(d2,K2)
                assert J2 % 3 in (0,pow(2,d2,3))
                checked += 1
    for k in range(3,80):
        if k % 2 == 0:
            assert pow(2,k,3) != 2
        else:
            assert pow(2,k,3) == 2
    return checked

def check_low_height_closure():
    start = (1,-13,0)
    seen = {start}
    q = deque([start])
    edges = 0
    while q:
        d,J,H = q.popleft()
        for x in (0,1):
            st = step_JQH(d,J,Fraction(1),H,x)
            if st is None:
                continue
            d2,J2,Q2,H2 = st
            if H2 > 2:
                continue
            edges += 1
            assert not (d2 == 1 and J2 > 0)
            nxt = (d2,J2,H2)
            if nxt not in seen:
                seen.add(nxt)
                q.append(nxt)
    assert len(seen) == 28
    return len(seen), edges

def boundary_stay_exit(J,Q):
    assert J > 0 and J % 2
    n = (J-1)//2
    stay_x = 0 if n % 2 == 0 else 1
    exit_x = 1-stay_x
    def do(x):
        st = step_JQH(1,J,Q,0,x)
        assert st is not None
        d2,J2,Q2,H2 = st
        assert d2 == 1 and H2 == 0
        return J2,Q2,x
    stay = do(stay_x)
    exitst = do(exit_x)
    assert stay[0] > 0 and stay[0] % 2
    assert exitst[0] > 0 and exitst[0] % 2 == 0
    return stay, exitst

def check_excursions():
    checked = 0
    equality = 0
    one_zero = 0
    negative_to_positive = 0
    negative_to_positive_one_zero = 0
    zero_gateway = []
    min_C_inc = None
    for K0 in range(-199,200,2):
        J0 = K0-1
        for ex in generate_excursions(K0,12):
            K0,K1,H,xw,yw,q,u,v,hs,z,c,S,D = metrics(ex)
            J1 = K1-1
            s = H-z
            assert all(h >= 1 for h in hs)
            assert H >= z
            # RL280 sharp envelopes, plus RL281 zero-mass envelope.
            d_env = 1 + Fraction(2**z-4,3)*RHO**s
            s_env = 1 + (2**z-2)*RHO**s
            assert D >= d_env
            assert S >= s_env
            normal = (
                xw == (0,)+(1,)*s+(0,)*(z-1)+(1,)
                and yw == (1,)*(s+1)+(0,)*z
            )
            assert (D == d_env) == normal
            assert (S == s_env) == normal
            if normal:
                equality += 1
                if J0 > 0 and z >= 5:
                    w = 2*K1-7
                    assert w >= 1 and w % 2
                    assert 3**(s+1)*(J0+4) == 2**(s+1)*(8+2**(z-1)*w)
                    assert nu2(J0+4) == s+4
                    assert J0+4 >= 2**(s+4)
                    assert Fraction(J0+4,1) >= RHO**(s+1)*(8+2**(z-1))

            # Exact endpoint/B identity and C-entry lower cost.
            assert q*K1-K0 == 2*S+D
            Binc = (q*K1-K0)/2
            assert Binc == S + D/2
            Cinc = q*(J1-1) - (J0-1)
            assert Cinc >= Fraction(5,3)
            if min_C_inc is None or Cinc < min_C_inc:
                min_C_inc = Cinc

            if z == 1:
                one_zero += 1
                assert xw == (0,)+(1,)*H
                assert q == 2*RHO**H
                assert 3**H*(J0+4) == 2**H*(2*J1+3)
                if J0 != -4:
                    assert H == nu2(J0+4)
                if J0 < 0 and J1 > 0:
                    negative_to_positive_one_zero += 1
                if J0 == 0 and J1 > 0:
                    zero_gateway.append((H,J1,xw,q))
            if J0 < 0 and J1 > 0:
                negative_to_positive += 1
                assert z >= 2
            checked += 1
    assert checked == 13909
    assert equality == 399
    assert negative_to_positive_one_zero == 0
    assert zero_gateway == [(2,3,(0,1,1),Fraction(8,9))]
    assert min_C_inc == Fraction(5,3)
    return checked,equality,one_zero,negative_to_positive,min_C_inc

def check_positive_checkpoint_blocks():
    checks = 0
    multi = 0
    for J0 in range(2,201,2):
        K0 = J0+1
        for ex in generate_excursions(K0,11):
            Kstart,Kb,H,xw,yw,Qb,u,v,hs,z,c,S,D = metrics(ex)
            Jb = Kb-1
            Fin = Fraction(J0+3,1)
            explicit = 1 + Fraction(7*2**z-16,3)*RHO**(H-z)

            def check_exit(Je,Qe):
                nonlocal checks,multi
                Fnext = Qe*(Je+3)
                inc = Fnext-Fin
                assert inc > 2*S + D - 2
                assert inc > explicit
                if z >= 2:
                    assert inc > S
                    multi += 1
                checks += 1

            if Jb % 2 == 0:
                assert Jb > 0
                check_exit(Jb,Qb)
                continue

            assert Jb > 0
            J,Q = Jb,Qb
            # Regression over 20 arbitrary positive retaining steps.
            for _ in range(20):
                stay,exitst = boundary_stay_exit(J,Q)
                Je,Qe,xe = exitst
                check_exit(Je,Qe)
                # Exact boundary B pricing: x=0 costs Q; x=1 costs zero.
                Js,Qs,xs = stay
                B0 = Q*(J+1)/2
                B1 = Qs*(Js+1)/2
                assert B1-B0 == (Q if xs == 0 else 0)
                J,Q = Js,Qs

    assert checks == 45170
    return checks,multi

def check_terminal_algebra():
    # RL280 terminal F ceiling.
    assert Fraction(160,3)*(Fraction(1,2)+Fraction(3,16)) == Fraction(110,3)
    # RL281 positive-phase B ceiling.
    assert Fraction(160,3)*(Fraction(1,4)+Fraction(1,32)) == 15

def main():
    mod3 = check_mod3_invariant()
    low = check_low_height_closure()
    ex = check_excursions()
    cp = check_positive_checkpoint_blocks()
    check_terminal_algebra()
    print("PASS RL281 two-phase Gate-A compression verifier")
    print("mod3_transition_checks=", mod3)
    print("height_le_2_reachable_states=", low[0])
    print("height_le_2_edges=", low[1])
    print("first_return_excursions=", ex[0])
    print("depth_two_equality_excursions=", ex[1])
    print("one_zero_excursions=", ex[2])
    print("negative_to_positive_excursions=", ex[3])
    print("minimum_normalized_C_excursion_increment=", ex[4])
    print("positive_checkpoint_block_checks=", cp[0])
    print("multi_zero_checkpoint_block_checks=", cp[1])
    print("terminal_F_ceiling=", Fraction(110,3))
    print("positive_phase_zero_mass_ceiling=", 15)
    print("classification=TWO_PHASE_GATE_A_COMPRESSION_PROVED")
    print("gate_A=OPEN_ODD_K_GE_5_ONLY")

if __name__ == "__main__":
    main()
