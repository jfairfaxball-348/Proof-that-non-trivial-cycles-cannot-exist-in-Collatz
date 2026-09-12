from itertools import product

def step(d,K,x):
    if K % 2 == 0:
        return (d,3*K//2,d-1) if x else (d,(K+3**d-1)//2,d-1)
    if x:
        return None if d <= 1 else (d-1,(K-1)//2,d-1)
    return (d+1,3*(K+3**d)//2,d-1)

def run(s,w):
    d,K=s
    c=0
    for ch in w:
        z=step(d,K,int(ch))
        if z is None:
            return None
        d,K,dc=z
        c += dc
    return (d,K),c

def comp(A,B):
    a,ka=A
    b,kb=B
    return (a+b,3**b*ka+kb)

P=(2,6)
Q=(2,18)
C8=(1,9)
R3=(2,27)

def qpow(n):
    x=(0,0)
    for _ in range(n):
        x=comp(x,Q)
    return x

def C(n):
    return comp(comp(qpow(n-1),P),Q)

def T(n):
    return comp(qpow(n),P)

def F(m):
    return (1,3*(3**m+1)//2)

def G(m):
    return (1,3*(1-3**m)//2)

formula_checks=0
for n in range(1,101):
    assert qpow(n)==(2*n,9*(9**n-1)//4)
    assert C(n)==(2*n+2,(3**(2*n+4)-441)//4)
    assert T(n)==(2*n+2,(3**(2*n+4)-57)//4)
    assert T(n)[1]-C(n)[1]==96
    assert comp(C(n),(0,96))==T(n)
    formula_checks += 1

grammar_checks=0
cost_checks=0
for n in range(1,101):
    for bits in product('01', repeat=6):
        w=''.join(bits)
        ds,ks=C(n)
        do,ko=T(n)
        cs=co=0
        ys=[]
        legal=True
        for i,ch in enumerate(w):
            x=int(ch)
            zs=step(ds,ks,x)
            zo=step(do,ko,x)
            if zs is None or zo is None:
                legal=False
                break
            ds2,ks2,dcs=zs
            do2,ko2,dco=zo
            y=ds2-ds+x
            ys.append(y)
            if i < 5:
                assert ds2==do2
                assert (ko2-ks2)==96*3**sum(ys)//2**(i+1)
            cs += dcs
            co += dco
            ds,ks=ds2,ks2
            do,ko=do2,ko2
        if not legal:
            continue
        assert cs==co
        m=1+sum(ys[:5])
        assert 1<=m<=6
        assert 96*3**sum(ys[:5])//32==3**m
        y6=ys[5]
        if y6==0:
            assert (do,ko)==comp((ds,ks),F(m))
        else:
            assert (ds,ks)==comp((do,ko),G(m))
        grammar_checks += 1
        cost_checks += 1

whole = {
1:('01110',14),
2:('00101110001',53),
3:('010011111001001001',127),
4:('100011101110111000001',187),
5:('100001110101010000001110',260),
6:('0110100000111110110010001',339),
7:('1001111100110001100001010110',413),
}
whole_checks=0
for n,(w,c) in whole.items():
    assert run(C(n),w)==(T(n),c)
    whole_checks += 1

compositional = {
1:('01110',14),
2:('00101110001',53),
3:('001011000111101010001',143),
4:('000011010100100011111100100',249),
5:('011010001000110110000111110001001',373),
6:('101110000011001110010101101100100101011100',582),
}
compositional_checks=0
for n,(w,c) in compositional.items():
    assert run(C(n),w)==(T(n),c)
    compositional_checks += 1

assert run(F(1),'1')==(C8,0)
assert run(F(2),'0')==(R3,0)

assert len(compositional[6][0])==42
assert compositional[6][1]==582
assert 6*6+3==39
assert 9*6*6+43*6-67==515

print('RL304_FIXED96_CLOSEOUT_GREEN')
print('formula_checks',formula_checks)
print('six_column_grammar_checks',grammar_checks)
print('zero_relative_cost_checks',cost_checks)
print('whole_stack_witness_checks',whole_checks)
print('compositional_witness_checks',compositional_checks)
print('O1','OPEN')
print('Gate_A','OPEN')
