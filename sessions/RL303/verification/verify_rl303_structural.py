from fractions import Fraction


def step(d,K,x):
    if K % 2 == 0:
        return (d,3*K//2,d-1) if x else (d,(K+3**d-1)//2,d-1)
    if x:
        return None if d <= 1 else (d-1,(K-1)//2,d-1)
    return (d+1,3*(K+3**d)//2,d-1)


def run(s,w):
    d,K=s; c=0
    for ch in w:
        z=step(d,K,int(ch))
        if z is None:
            return None
        d,K,dc=z
        c += dc
    return (d,K),c


def comp(A,B):
    a,ka=A; b,kb=B
    return (a+b,3**b*ka+kb)

P=(2,6)
C8=(1,9)
Q=(2,18)
U=(1,6)
R2=(2,9)


def Rt(d): return (d,3**d)
def L(D): return (D,(5*3**D-3)//4)
def RW(D): return (D,(9*3**D-3)//4)
def W(D,t): return (D,((4*t+5)*3**D-3)//4)
def Cdt(D,t): return (1,3*(4*t+1)*2**(D-2)+3)
def BL(D): return (D*D+D-6)//2
def BR(D): return (D*D+3*D-4)//2
def lift_cost(D): return (D*D-D-2)//2

# 1. Exact checkpoint-8 +3 entry to the two tight wall families.
entry_checks=0
for D in range(3,100,2):
    tower='001'+'0'*(D+1)
    r=run(C8,tower)
    assert r==(Rt(D),(D*D-3*D+6)//2)
    assert run(C8,tower+'10')==(L(D),BL(D)+3)
    assert run(C8,tower+'011')==(RW(D),BR(D)+3)
    entry_checks += 1

# 2. Generalized dyadic wall-lift lattice.
lift_checks=0
for D in range(3,100,2):
    for t in range(20):
        assert run(Cdt(D,t),'0'*D)==(W(D,t),lift_cost(D))
        lift_checks += 1

# 3. Fixed-cell factorisation of the R-wall family and the inherited L-wall factorisation.
factor_checks=0
for D in range(3,100,2):
    n=(D-1)//2
    x=U
    for _ in range(n):
        x=comp(Q,x)
    assert x==RW(D)
    assert comp(R2,RW(D-2))==L(D)
    factor_checks += 1

# 4. Translation-invariant adjacent-wall normal form across the full lattice.
merge_checks=sibling_checks=0
for D in range(3,80,2):
    for t in range(20):
        for k in range(20):
            a=run(W(D,t),'0'+'1'*k+'01')
            b=run(W(D,t+1),'1'*(k+1)+'00')
            if a and b:
                assert a[0]==b[0]
                assert a[1]-b[1]==k+2
                merge_checks += 1
            a=run(W(D,t),'0'+'1'*k+'00')
            b=run(W(D,t+1),'1'*(k+1)+'01')
            if a and b:
                assert a[0]==comp(P,b[0])
                assert a[1]-b[1]==k+2
                sibling_checks += 1

# 5. Four exact D -> D-2 merger families obtained through the universal quotient gateway.
peel_checks=0
for D in range(5,80,2):
    for k in range(2,20):
        a=run(L(D),'10'+'1'*k+'00')
        b=run(RW(D-2),'0000'+'1'*(k-2)+'01')
        if a and b:
            assert a[0]==b[0] and a[1]-b[1]==4-k
            peel_checks += 1
        a=run(L(D),'010'+'1'*k+'00')
        b=run(L(D-2),'00000'+'1'*(k-2)+'01')
        if a and b:
            assert a[0]==b[0] and a[1]-b[1]==6-k
            peel_checks += 1
        a=run(RW(D),'0100'+'1'*k+'00')
        b=run(RW(D-2),'000000'+'1'*(k-2)+'01')
        if a and b:
            assert a[0]==b[0] and a[1]-b[1]==7-k
            peel_checks += 1
    for k in range(1,20):
        a=run(RW(D),'1100'+'1'*k+'00')
        b=run(L(D-2),'00000'+'1'*(k-1)+'01')
        if a and b:
            assert a[0]==b[0] and a[1]-b[1]==2-k
            peel_checks += 1

# 6. Physical quadratic counterfamily to any generic linear-credit wall-debt transport lemma.
debt_checks=0
for n in range(1,101):
    D=6*n+3
    src=run(W(D,4),'1'*(3*n))
    own=run(W(D,0),'110'*n)
    assert src and own
    (ds,Ks),cs=src; (do,Ko),co=own
    assert do-ds==n
    assert Ks==Ko+4*3**do
    assert cs-co==-3*n*(n-1)//2
    debt_checks += 1

# 7. Exact physical P/Q commutation identity.
assert comp(P,Q)==(4,72)
assert comp(Q,P)==(4,168)
assert run(comp(P,Q),'01110')==(comp(Q,P),14)

# 8. Exact all-r Q return family and propagated output pattern.
def factor_outputs(s,w):
    d,K=s; outs=[]; c=0
    for ch in w:
        x=int(ch)
        z=step(d,K,x)
        assert z is not None
        d2,K2,dc=z
        y=d2-d+x
        outs.append(str(y))
        d,K=d2,K2
        c += dc
    return (d,K),''.join(outs),c

qreturn_checks=0
for r in range(101):
    w='0'+'10'*r+'110'
    endpoint,out,cost=factor_outputs(Q,w)
    assert endpoint==Q and cost==2
    assert out=='00'+'01'*r+'11'
    qreturn_checks += 1

# 9. Small direct O1 splice used as a correction to the root renewal detour.
assert run((3,27),'011')==(RW(3),7)
assert run(C8,'01001')==(RW(3),6)

print('RL303_STRUCTURAL_CLOSEOUT_GREEN')
print('entry_checks',entry_checks)
print('lift_checks',lift_checks)
print('factor_checks',factor_checks)
print('adjacent_merge_checks',merge_checks)
print('adjacent_sibling_checks',sibling_checks)
print('peel_checks',peel_checks)
print('debt_counterfamily_checks',debt_checks)
print('qreturn_checks',qreturn_checks)
print('O1', 'OPEN')
print('Gate_A', 'OPEN')
