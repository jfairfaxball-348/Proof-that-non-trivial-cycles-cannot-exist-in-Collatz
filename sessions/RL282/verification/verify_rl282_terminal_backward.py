#!/usr/bin/env python3
from fractions import Fraction
from itertools import product

def nu_p(n, p):
    n = abs(int(n))
    if n == 0:
        raise ValueError("valuation of zero")
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v

def is_pow2(n):
    return n > 0 and n & (n-1) == 0

def k_step(d, J, x):
    K = J + 2**d - 1
    if K % 2 == 0:
        if x == 1:
            K2 = 3*K//2
            return d, K2 - 2**d + 1
        K2 = (K + 3**d - 1)//2
        return d, K2 - 2**d + 1
    if x == 1:
        if d <= 1:
            return None
        d2 = d-1
        K2 = (K-1)//2
        return d2, K2 - 2**d2 + 1
    d2 = d+1
    K2 = 3*(K+3**d)//2
    return d2, K2 - 2**d2 + 1

def replay(d, J, word):
    for x in word:
        out = k_step(d,J,x)
        if out is None:
            return None
        d,J = out
    return d,J

def boundary_map(J, x):
    assert J % 2 == 1
    if x == 0:
        return (J+1)//2
    return (3*J+1)//2

def boundary_affine_constant(word):
    L=len(word)
    C=0
    for j,x in enumerate(word):
        ones_after=sum(word[j+1:])
        C += (2**j) * (3**ones_after)
    return C

def valid_boundary_tail(J0, word):
    J=J0
    for i,x in enumerate(word):
        if J % 2 == 0:
            return None
        J=boundary_map(J,x)
        if i < len(word)-1 and J % 2 == 0:
            return None
    return J

def R_t(A,t):
    if A % (3**t):
        return None
    return 2*((2**t)*(A//(3**t))-1)

def check_one_zero_shell():
    checked=0
    h1=0
    for Jin in range(2,5000,2):
        if Jin % 3 not in (0,2):
            continue
        h=nu_p(Jin+4,2)
        out=replay(1,Jin,(0,)+(1,)*h)
        assert out is not None and out[0]==1
        Jout=out[1]
        if Jout<=0:
            continue
        lhs=3**h*(Jin+4)
        rhs=2**h*(2*Jout+3)
        assert lhs==rhs
        assert nu_p(Jout,3)==1
        if h==1: h1 += 1
        checked += 1
    return checked,h1

def check_boundary_affine():
    checked=0
    terminal_shell=0
    height_digit=0
    for J0 in range(1,1000,2):
        for L in range(0,8):
            for word in product((0,1), repeat=L):
                JT=valid_boundary_tail(J0,word)
                if JT is None:
                    continue
                C=boundary_affine_constant(word)
                r=sum(word)
                assert (2**L)*JT == (3**r)*J0 + C
                checked += 1
                if is_pow2(JT) and JT>=8 and nu_p(J0,3)==1:
                    k=JT.bit_length()-1
                    E=2**(k+L)-C
                    assert E==3**r*J0
                    assert nu_p(E,3)==r+1
                    N=2**(k+L+1)-2*C+3**(r+1)
                    assert N==3**r*(2*J0+3)
                    assert nu_p(N,3)-r == nu_p(2*J0+3,3)
                    terminal_shell += 1
                    height_digit += nu_p(2*J0+3,3)
    return checked,terminal_shell,height_digit

def check_inverse_blocks():
    checked=0
    deep=near=full=0
    for A in range(1,5000):
        v=nu_p(A,3) if A%3==0 else 0
        for t in range(v+1):
            pre=R_t(A,t)
            assert pre is not None
            Jpre=pre-1
            # Forward 0 1^t from Apre must recover A.
            out=replay(1,Jpre,(0,)+(1,)*t)
            assert out is not None and out[0]==1 and out[1]+1==A
            if t <= v-2:
                assert nu_p(pre-1,3)==1
                assert nu_p(2*pre+1,3)==1  # 2Jpre+3 = 2Apre+1
                deep += 1
            elif t == v-1 and v>=1:
                near += 1
            elif t == v:
                full += 1
            checked += 1
    return checked,deep,near,full

def order_two_mod_3n(n):
    mod=3**n
    # exact elementary regression
    target=2*3**(n-1)
    assert pow(2,target,mod)==1
    if target%2==0:
        assert pow(2,target//2,mod)!=1
    if n>1:
        assert pow(2,target//3,mod)!=1
    return target

def solve_q_class(k,h):
    mod=3**(h+1)
    order=2*3**h
    target=(-5 + (2**h)*(3**h)) % mod
    unit=(2**k-1) % mod
    assert unit%3
    hits=[]
    for q in range(order):
        if (pow(2,q+1,mod)*unit-target) % mod == 0:
            hits.append(q)
    assert len(hits)==1
    return hits[0],order

def check_pure_zero_family():
    pairs=0
    replayed=0
    max_digits=0
    for n in range(1,8):
        max_digits=max(max_digits,order_two_mod_3n(n))
    for k in range(3,40,2):
        for h in range(2,8):
            q0,period=solve_q_class(k,h)
            # Use a positive representative with several added periods.
            q=q0+2*period
            J0=(2**q)*(2**k-1)+1
            Z=2*J0+3
            assert nu_p(Z,3)==h
            assert J0%9==3
            M=Z//3**h
            assert M%2==1 and M%3!=0
            Jin=2**h*M-4
            assert Jin>0 and Jin%2==0 and Jin%3==0
            assert nu_p(Jin+4,2)==h
            out=replay(1,Jin,(0,)+(1,)*h+(0,)*q)
            assert out==(1,2**k)
            # Period shift remains valid.
            q2=q+period
            J02=(2**q2)*(2**k-1)+1
            assert nu_p(2*J02+3,3)==h
            # Scale, zero-mass, and F identities with Q_T=1.
            QT=Fraction(1,1)
            Q0=QT/Fraction(2**q,1)
            Qin=QT*Fraction(3**h,2**(q+h+1))
            S=Qin + Q0*(2**q-1)
            expectedS=QT*(1-Fraction(1,2**q)+Fraction(3**h,2**(q+h+1)))
            assert S==expectedS
            Fin=Qin*(Jin+3)
            FT=QT*(2**k+3)
            expectedDelta=QT*(4-Fraction(5,2**(q+1))+Fraction(3**h,2**(q+h+1)))
            assert FT-Fin==expectedDelta
            pairs += 1
            replayed += 1
    return pairs,replayed,max_digits

def check_neutral_loop_mass():
    checked=0
    for N in range(1,40):
        q=Fraction(7,13)
        qN=q*Fraction(4,3)**N
        # x=0 zero in each 10 loop occurs after the x=1 step, so weight is (2/3) q_i.
        mass=sum(Fraction(2,3)*q*Fraction(4,3)**i for i in range(N))
        assert mass==2*(qN-q)
        assert mass<2*qN
        checked+=1
    return checked

def main():
    one=check_one_zero_shell()
    aff=check_boundary_affine()
    inv=check_inverse_blocks()
    fam=check_pure_zero_family()
    loop=check_neutral_loop_mass()
    print("PASS RL282 terminal-backward + local-tail barrier verifier")
    print("one_zero_positive_shell_checks=",one[0])
    print("one_zero_h1_shell_checks=",one[1])
    print("boundary_affine_valid_tail_checks=",aff[0])
    print("terminal_shell_tail_checks=",aff[1])
    print("terminal_shell_height_digit_sum=",aff[2])
    print("inverse_block_checks=",inv[0])
    print("inverse_deep_undershoot_checks=",inv[1])
    print("inverse_near_full_checks=",inv[2])
    print("inverse_full_consumption_checks=",inv[3])
    print("pure_zero_family_k_h_pairs=",fam[0])
    print("pure_zero_family_full_replays=",fam[1])
    print("primitive_root_regression_max_order=",fam[2])
    print("neutral_loop_mass_checks=",loop)
    print("classification_candidate=TERMINAL_BACKWARD_HEIGHT_DIGIT_PRICING_AND_LOCAL_TAIL_BARRIER_PROVED")
    print("gate_a_status=OPEN")
    print("successor_focus=UPSTREAM_POSITIVE_CHECKPOINT_REACHABILITY_VS_HEIGHT")

if __name__=="__main__":
    main()
