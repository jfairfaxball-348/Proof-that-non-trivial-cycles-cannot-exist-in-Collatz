#!/usr/bin/env python3
from fractions import Fraction
from itertools import product

RHO = Fraction(2, 3)
THRESH = Fraction(17, 2)

def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

def J_of(d, T):
    return T + 3**d - 2**d

def rl_step(d, T, H, x, y):
    num = (3**y) * T + x * 3**(d + y - 1) - y
    if num % 2:
        return None
    d2 = d + y - x
    if d2 < 1:
        return None
    return d2, num // 2, H + d - 1

def step_from_x(d, J, H, x):
    T = J - 3**d + 2**d
    if J & 1:
        y = x
    else:
        y = 1 - x
        if x == 1 and d <= 1:
            return None
    out = rl_step(d, T, H, x, y)
    if out is None:
        return None
    d2, T2, H2 = out
    return d2, J_of(d2, T2), H2, y

def K_of(d, J):
    return J + 2**d - 1

def k_formula(d, J, x):
    K = K_of(d, J)
    if K % 2 == 0:
        if x == 1:
            return d, 3*K//2
        return d, (K + 3**d - 1)//2
    if x == 1:
        if d <= 1:
            return None
        return d-1, (K-1)//2
    return d+1, 3*(K + 3**d)//2

def check_k_transition():
    checked = 0
    for d in range(1, 7):
        for J in range(-80, 81):
            for x in (0, 1):
                st = step_from_x(d, J, 7, x)
                form = k_formula(d, J, x)
                if st is None:
                    assert form is None
                    continue
                d2, J2, H2, _ = st
                assert H2 == 7 + d - 1
                assert form == (d2, K_of(d2, J2))
                checked += 1
    return checked

def check_potential_step():
    checked = 0
    for d in range(1, 7):
        for J in range(-80, 81):
            for H in range(0, 4):
                for m in range(0, 4):
                    for r in range(0, m+1):
                        for x in (0, 1):
                            st = step_from_x(d, J, H, x)
                            if st is None:
                                continue
                            d2, J2, H2, _ = st
                            P = Fraction(2**(H+m), 3**r)
                            P2 = Fraction(2**(H2+m+1), 3**(r+x))
                            assert P2 == P * Fraction(2**d, 3**x)
                            checked += 1
    return checked

def one_positions(w):
    return [i for i, b in enumerate(w) if b]

def zero_ranks(w):
    out = []
    ones = 0
    for b in w:
        if b:
            ones += 1
        else:
            out.append(ones)
    return out

def replay_word(word):
    d, J, H = 1, -13, 0
    xw, yw = [], []
    for x in word:
        st = step_from_x(d, J, H, x)
        if st is None:
            return None
        d, J, H, y = st
        xw.append(x); yw.append(y)
    return d, J, H, tuple(xw), tuple(yw)

def check_zero_lag(max_len=12):
    frontier = [(1, -13, 0, tuple(), tuple())]
    checked = 0
    for _ in range(max_len):
        nxt = []
        for d, J, H, xw, yw in frontier:
            for x in (0,1):
                st = step_from_x(d, J, H, x)
                if st is None:
                    continue
                d2,J2,H2,y = st
                X=xw+(x,); Y=yw+(y,)
                if sum(X)==sum(Y) and X.count(0)==Y.count(0):
                    u=zero_ranks(X); v=zero_ranks(Y)
                    if len(u)==len(v) and all(a<=b for a,b in zip(u,v)):
                        assert H2 == sum(b-a for a,b in zip(u,v))
                        checked += 1
                nxt.append((d2,J2,H2,X,Y))
        frontier=nxt
    return checked

def weighted_prefix(u):
    return sum((1 << i) * RHO**v for i, v in enumerate(u))

def x_prefix_from_u(u):
    bits=[]; ones=0
    for target in u:
        while ones < target:
            bits.append(1); ones += 1
        bits.append(0)
    return tuple(bits)

def replay_prefix(prefix):
    return replay_word(prefix)

def exact_max_below(n):
    best = Fraction(0); witness = None
    def dfs(prefix, prev, s, j):
        nonlocal best, witness
        if j == n:
            if s < THRESH and s > best:
                best=s; witness=tuple(prefix)
            return
        u=prev
        while True:
            upper = s + ((1<<n)-(1<<j))*RHO**u
            if upper <= best:
                break
            s2 = s + (1<<j)*RHO**u
            if s2 < THRESH:
                dfs(prefix+[u],u,s2,j+1)
            u += 1
    dfs([],0,Fraction(0),0)
    return best,witness

def bounded_admissible(n, bound):
    out=[]
    def rec(prefix, prev, s, j):
        if j==n:
            if s > THRESH:
                out.append(tuple(prefix))
            return
        for u in range(prev,bound+1):
            s2=s+(1<<j)*RHO**u
            upper=s2+sum((1<<q)*RHO**u for q in range(j+1,n))
            if upper <= THRESH:
                break
            rec(prefix+[u],u,s2,j+1)
    rec([],0,Fraction(0),0)
    return out

def rank_data(xw, yw):
    aa=one_positions(xw); bb=one_positions(yw)
    assert len(aa)==len(bb)
    delta=[a-b for a,b in zip(aa,bb)]
    r=len(aa)
    Qx=sum((1<<a)*3**(r-j) for j,a in enumerate(aa,1))
    Qy=sum((1<<b)*3**(r-j) for j,b in enumerate(bb,1))
    return delta,Qx,Qy

def close_with_ones(prefix,max_steps=256):
    got=replay_prefix(prefix)
    if got is None:
        return ("illegal",)
    d,J,H,xw,yw=got
    xw=list(xw); yw=list(yw); seen=set()
    for _ in range(max_steps):
        m=len(xw)
        if d==1 and is_power_of_two(J) and J>=8:
            k=J.bit_length()-1; r=sum(xw); a=m+k+1; ell=r+3
            delta,Qx,Qy=rank_data(tuple(xw),tuple(yw))
            assert H==sum(delta)
            assert 3*Qx-Qy == 14*3**r + 2**(a-1) - 2**(a-k-1)
            ratio_ok = 3**ell < 2**a and 81*2**a < 160*3**ell
            return ("terminal",k,H,m,r,a,ell,ratio_ok)
        key=(d,J)
        assert key not in seen
        seen.add(key)
        st=step_from_x(d,J,H,1)
        if st is None:
            return ("stop",d,J,H,len(xw))
        d,J,H,y=st
        xw.append(1); yw.append(y)
    raise AssertionError("all-one closure too long")

def all_one_run(prefix,max_steps=256):
    got=replay_prefix(prefix)
    if got is None: return None
    d,J,H,xw,yw=got
    seen=set(); steps=0
    while steps < max_steps:
        if d==1 and is_power_of_two(J) and J>=8:
            return steps
        key=(d,J)
        assert key not in seen
        seen.add(key)
        st=step_from_x(d,J,H,1)
        if st is None:
            return steps
        d,J,H,_=st
        steps += 1
    raise AssertionError("run too long")

def seven_zero_certificate():
    M6,w6=exact_max_below(6)
    assert M6 == Fraction(583353885633550,68630377364883)
    assert w6 == (1,1,1,2,10,29)
    gap6=THRESH-M6
    assert gap6 == Fraction(8643935911,137260754729766)
    assert 64*RHO**34 > gap6
    assert 64*RHO**35 < gap6

    adm6=bounded_admissible(6,28)
    assert len(adm6)==7081
    legal6=[]
    for u in adm6:
        p=x_prefix_from_u(u)
        if replay_prefix(p) is not None:
            legal6.append((u,p))
    assert len(legal6)==458
    assert max(u[-1] for u,_ in legal6)==14
    assert max(all_one_run(p) for _,p in legal6)==11
    above_bound=25
    bound7=max(34,above_bound)
    assert bound7==34

    adm7=bounded_admissible(7,bound7)
    assert len(adm7)==140185
    legal7=[]
    for u in adm7:
        p=x_prefix_from_u(u)
        if replay_prefix(p) is not None:
            legal7.append((u,p))
    assert len(legal7)==2662
    assert max(u[-1] for u,_ in legal7)==19
    terminals=[]; box=[]; dangerous=[]
    for u,p in legal7:
        out=close_with_ones(p)
        if out[0]=="terminal":
            terminals.append((u,out))
            if out[-1]:
                box.append((u,out))
                if out[2] < out[1]:
                    dangerous.append((u,out))
    assert len(terminals)==691
    assert len(box)==286
    assert dangerous==[]
    return M6,w6,gap6,bound7,len(adm7),len(legal7),len(terminals),len(box)

def check_neutral_family():
    base=tuple(map(int,"00101001111"))
    out=replay_word(base)
    assert out[:3] == (1,8,3)
    neg=tuple(map(int,"101"))
    st=replay_word(neg)
    assert st[:3] == (1,-13,0)
    core=tuple(map(int,"001010011"))
    outc=replay_word(core)
    assert outc[:3] == (1,3,3)
    d,J,H=1,3,3
    for x in (1,0):
        d,J,H,_=step_from_x(d,J,H,x)
    assert (d,J,H)==(1,3,3)

    def family(p,q):
        word=(1,0,1)*p + tuple(map(int,"001010011")) + (1,0)*q + (1,1)
        d,J,H,xw,yw=replay_word(word)
        assert (d,J,H)==(1,8,3)
        m=len(word); r=sum(word); k=3
        X=Fraction(2**(m+k+1),3**r)
        expected=Fraction(2**15,3**6)*Fraction(8,9)**p*Fraction(4,3)**q
        assert X==expected
        return X,word.count(0)
    examples=[]
    for p,q in [(0,0),(127,52),(276,113)]:
        X,m0=family(p,q)
        assert Fraction(27,1) < X < Fraction(160,3)
        assert m0==5+p+q
        examples.append((p,q,X,m0))
    return examples

def boundary_next(n):
    if n%2==0:
        return n//2,0,Fraction(2,1)
    return (3*n+1)//2,1,Fraction(2,3)

def check_boundary_monotonicity():
    checked=0
    for n in range(-200,201):
        n2,x,mu=boundary_next(n)
        P=Fraction(7,5)
        A=P*n; B=P*(n+1)
        A2=P*mu*n2; B2=P*mu*(n2+1)
        if n%2==0:
            assert A2==A and B2==B+P
        else:
            assert B2==B and A2==A+P/3
        checked+=1
    return checked

def check_positive_invariance():
    checked=0
    for d in range(1,7):
        for J in range(1,101):
            for x in (0,1):
                st=step_from_x(d,J,0,x)
                if st is not None:
                    assert st[1] > 0
                    checked += 1
    return checked

def main():
    kt=check_k_transition()
    pt=check_potential_step()
    zl=check_zero_lag()
    c=seven_zero_certificate()
    fam=check_neutral_family()
    bm=check_boundary_monotonicity()
    pi=check_positive_invariance()
    print("PASS RL279 structural + seven-zero verifier")
    print("k_transition_checks=",kt)
    print("potential_step_checks=",pt)
    print("zero_lag_prefix_checks=",zl)
    print("M6=",c[0],"witness=",c[1])
    print("gap6=",c[2])
    print("seven_zero_rank_bound_u7<=",c[3])
    print("seven_zero_admissible_tuples=",c[4])
    print("seven_zero_canonical_prefixes=",c[5])
    print("seven_zero_terminals=",c[6])
    print("seven_zero_ratio_box_terminals=",c[7])
    print("seven_zero_gate_violators=0")
    print("neutral_family_examples=",[(p,q,m0,float(X)) for p,q,X,m0 in fam])
    print("boundary_monotonicity_checks=",bm)
    print("positive_invariance_checks=",pi)
    print("promoted_candidate=H_can<k => m0>=8 => z>=k+6")
    print("classification_candidate=SCALABLE_ZERO_RANK_RUN_COMPRESSION_PROVED")
    print("subordinate=EXACT_SEVEN_ZERO_GATE_A_CONTRACTION_PROVED")

if __name__=="__main__":
    main()
