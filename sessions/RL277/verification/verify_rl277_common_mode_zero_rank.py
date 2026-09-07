#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations_with_replacement

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

def one_positions(w):
    return [i for i, b in enumerate(w) if b]

def rank_data(xw, yw):
    aa = one_positions(xw)
    bb = one_positions(yw)
    assert len(aa) == len(bb)
    delta = [a - b for a, b in zip(aa, bb)]
    r = len(aa)
    Qx = sum((1 << a) * 3**(r-j) for j, a in enumerate(aa, 1))
    Qy = sum((1 << b) * 3**(r-j) for j, b in enumerate(bb, 1))
    return aa, bb, delta, Qx, Qy

def qpoly(w):
    r = sum(w)
    rank = 0
    q = 0
    for i, bit in enumerate(w):
        if bit:
            rank += 1
            q += (1 << i) * 3**(r-rank)
    return q

def zero_rank_counts(w):
    out = []
    ones = 0
    for b in w:
        if b:
            ones += 1
        else:
            out.append(ones)
    return out

def zero_rank_Q_formula(w):
    r = sum(w)
    hs = zero_rank_counts(w)
    z0 = len(hs)
    q = 3**r - (1 << (r+z0))
    for t, h in enumerate(hs, 1):
        p = h + t - 1
        q += (1 << p) * 3**(r-h)
    return q

def weighted_prefix(u):
    return sum((1 << i) * RHO**v for i, v in enumerate(u))

def x_prefix_from_u(u):
    bits = []
    ones = 0
    for target in u:
        while ones < target:
            bits.append(1)
            ones += 1
        bits.append(0)
    return tuple(bits)

def replay_prefix(prefix):
    d, J, H = 1, -13, 0
    xw, yw = [], []
    for x in prefix:
        st = step_from_x(d, J, H, x)
        if st is None:
            return None
        d, J, H, y = st
        xw.append(x); yw.append(y)
    return d, J, H, tuple(xw), tuple(yw)

def close_with_ones(prefix, max_steps=64):
    got = replay_prefix(prefix)
    if got is None:
        return ("illegal",)
    d, J, H, xw, yw = got
    xw=list(xw); yw=list(yw)
    seen=set()
    for _ in range(max_steps):
        m=len(xw)
        if d == 1 and is_power_of_two(J) and J >= 8:
            k=J.bit_length()-1
            r=sum(xw)
            a=m+k+1
            ell=r+3
            aa,bb,delta,Qx,Qy=rank_data(tuple(xw),tuple(yw))
            assert H == sum(delta)
            assert 3*Qx-Qy == 14*3**r + 2**(a-1) - 2**(a-k-1)
            ratio_ok = 3**ell < 2**a and 81*2**a < 160*3**ell
            return ("terminal",k,H,m,r,a,ell,ratio_ok)
        key=(d,J)
        assert key not in seen, ("unexpected all-one cycle", prefix, key)
        seen.add(key)
        st=step_from_x(d,J,H,1)
        if st is None:
            return ("stop",d,J,H,len(xw))
        d,J,H,y=st
        xw.append(1); yw.append(y)
    raise AssertionError(("all-one closure too long",prefix,d,J,H))

def four_zero_patterns():
    expected=[
        (0,0,0,0),(0,0,0,1),(0,0,0,2),(0,0,0,3),(0,0,0,4),
        (0,0,1,1),(0,0,1,2),(0,1,1,1),(0,1,1,2),(1,1,1,1)
    ]
    assert 15*RHO**2 < THRESH
    assert 7 + 8*RHO**5 < THRESH
    got=[]
    for u in combinations_with_replacement(range(5),4):
        if weighted_prefix(u) > THRESH:
            got.append(u)
    assert got == expected
    below=[weighted_prefix(u) for u in combinations_with_replacement(range(5),4)
           if weighted_prefix(u) <= THRESH]
    assert max(below) == Fraction(25,3)
    return expected

def four_zero_certificate():
    rows=[]
    dangerous=[]
    max_one_run=0
    for u in four_zero_patterns():
        prefix=x_prefix_from_u(u)
        got=replay_prefix(prefix)
        if got is None:
            rows.append((u,"illegal"))
            continue
        d,J,H,_,_=got
        q=0
        while q<32:
            if d==1 and is_power_of_two(J) and J>=8:
                break
            st=step_from_x(d,J,H,1)
            if st is None:
                break
            d,J,H,_=st
            q+=1
        max_one_run=max(max_one_run,q)
        out=close_with_ones(prefix)
        rows.append((u,out))
        if out[0]=="terminal" and out[-1] and out[2] < out[1]:
            dangerous.append((u,out))
    assert max_one_run == 7
    assert dangerous == []
    box=[(u,o) for u,o in rows if o[0]=="terminal" and o[-1]]
    assert len(box)==1
    assert box[0][1][1:3] == (3,6)
    return rows,max_one_run

def five_zero_certificate():
    four = four_zero_patterns()
    _, max_run = four_zero_certificate()
    assert Fraction(17,2)-Fraction(25,3) == Fraction(1,6)
    assert 16*RHO**11 > Fraction(1,6)
    assert 16*RHO**12 < Fraction(1,6)
    assert max(max(u) for u in four) + max_run <= 11

    admissible=[u for u in combinations_with_replacement(range(12),5)
                if weighted_prefix(u)>THRESH]
    assert len(admissible)==206
    legal=[]
    for u in admissible:
        prefix=x_prefix_from_u(u)
        if replay_prefix(prefix) is not None:
            legal.append((u,prefix))
    assert len(legal)==72
    assert max(u[-1] for u,_ in legal)==7

    terminals=[]
    box=[]
    dangerous=[]
    for u,prefix in legal:
        out=close_with_ones(prefix)
        if out[0]=="terminal":
            terminals.append((u,out))
            if out[-1]:
                box.append((u,out))
                if out[2] < out[1]:
                    dangerous.append((u,out))
    assert len(terminals)==36
    assert len(box)==19
    assert dangerous==[]
    pairs=sorted(set((o[1],o[2]) for _,o in box))
    assert pairs == [(3,3),(3,4),(3,5),(3,6),(3,7),(3,8),(3,9),(5,18),(5,20)]
    return len(admissible),len(legal),len(terminals),len(box),pairs

def bounded_rl66_replay():
    terminal=0
    ratio_box=0
    dangerous=0
    states=[(1,-14,0,(),())]
    MAX_M=17
    for m in range(MAX_M+1):
        for d,T,H,xw,yw in states:
            J=J_of(d,T)
            if d!=1 or not is_power_of_two(J) or J<8 or T!=J-1:
                continue
            terminal += 1
            k=J.bit_length()-1
            aa,bb,delta,Qx,Qy=rank_data(xw,yw)
            r=len(aa)
            a=m+k+1
            ell=r+3
            assert H==sum(delta)
            assert 3*Qx-Qy == 14*3**r + 2**(a-1)-2**(a-k-1)
            assert zero_rank_Q_formula(xw)==Qx
            assert zero_rank_Q_formula(yw)==Qy
            if 3**ell < 2**a and 81*2**a < 160*3**ell:
                ratio_box += 1
                assert 16*3*Qx > 413*3**r
                assert 3*Qx < 61*3**r
                if H<k:
                    dangerous += 1
        if m==MAX_M:
            break
        nxt=[]
        for d,T,H,xw,yw in states:
            J=J_of(d,T)
            opts=((0,0),(1,1)) if J&1 else ((0,1),(1,0))
            for x,y in opts:
                if (x,y)==(1,0) and d<=1:
                    continue
                out=rl_step(d,T,H,x,y)
                if out is None:
                    continue
                d2,T2,H2=out
                nxt.append((d2,T2,H2,xw+(x,),yw+(y,)))
        states=nxt
    assert terminal==1421
    assert ratio_box==250
    assert dangerous==0
    return terminal,ratio_box,dangerous

def main():
    formula_checks=0
    for n in range(1,11):
        for mask in range(1<<n):
            w=tuple((mask>>i)&1 for i in range(n))
            assert zero_rank_Q_formula(w)==qpoly(w)
            formula_checks += 1
    four,maxrun=four_zero_certificate()
    a5,l5,t5,b5,pairs=five_zero_certificate()
    terminal,box,danger=bounded_rl66_replay()
    print("PASS RL277 common-mode zero-rank verifier")
    print("zero_rank_formula_checks=",formula_checks)
    print("four_zero_relaxed_patterns=",len(four))
    print("four_zero_max_all_one_run=",maxrun)
    print("five_zero_admissible_tuples=",a5)
    print("five_zero_canonical_prefixes=",l5)
    print("five_zero_terminals=",t5)
    print("five_zero_ratio_box_terminals=",b5)
    print("five_zero_ratio_box_pairs=",pairs)
    print("five_zero_gate_violators=0")
    print("bounded_terminal_paths=",terminal)
    print("bounded_ratio_box_paths=",box)
    print("bounded_ratio_box_gate_violators=",danger)
    print("classification=ONE_SIDED_COMMON_MODE_CONSUMER_PROVED")
    print("subordinate=ABSOLUTE_ORDERED_RANK_MOMENT_BUDGET_PROVED")
    print("subordinate=GLOBAL_DANGEROUS_ZERO_BUDGET_Z_GE_K_PLUS_4")

if __name__=="__main__":
    main()
