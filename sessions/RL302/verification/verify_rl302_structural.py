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
        if z is None: return None
        d,K,dc=z; c+=dc
    return (d,K),c


def comp(A,B):
    a,ka=A; b,kb=B
    return a+b,3**b*ka+kb

P=(2,6); C8=(1,9); U=(1,6); R2=(2,9); R3=(3,27); D0=(3,24)
Z=(1,0)
def Rt(d): return d,3**d
def S(d): return d-1,(3**d-1)//2
def L(D): return D,(5*3**D-3)//4
def R(D): return D,(9*3**D-3)//4
def V(d): return d,3**d-3
def W(d): return d,3**d-2
def F(d): return d-1,(3**d-3)//2
def A(d): return d,(3**(d+1)-9)//2

# Fixed source factorisations.
assert comp(P,C8)==R3
assert comp(P,U)==D0
assert run(U,'1')==(C8,0)

# Tower zipper and wall factorisation.
for d in range(3,60):
    assert run(Rt(d),'0')==(Rt(d+1),d-1)
    assert run(Rt(d),'1')==(S(d),d-1)
for D in range(3,60,2):
    assert comp(R2,R(D-2))==L(D)
    assert run(S(D),'0')[0]==L(D)
    assert run(S(D),'1')[0]==R(D-2)
    assert run(S(D+1),'0')[0]==L(D)
    assert run(S(D+1),'1')[0]==R(D)

# RL297 merger and wall run-length normal form.
for D in range(3,36,2):
    a=run(L(D),'101100'); b=run(R(D-2),'000001')
    assert a and b and a[0]==b[0] and b[1]-a[1]==-2
    for k in range(15):
        a=run(L(D),'0'+'1'*k+'01'); b=run(R(D),'1'*(k+1)+'00')
        if a and b:
            assert a[0]==b[0] and b[1]-a[1]==-(k+2)
        a=run(L(D),'0'+'1'*k+'00'); b=run(R(D),'1'*(k+1)+'01')
        if a and b:
            assert a[0]==comp(P,b[0]) and b[1]-a[1]==-(k+2)

# D0 zero spine, departures, and F/S credit.
for d in range(3,60):
    assert run(V(d),'0')==(W(d),d-1)
    assert run(W(d),'0')==(V(d+1),d-1)
    assert run(V(d),'1')[0]==A(d)
    assert run(W(d),'1')[0]==F(d)
    assert comp(F(d),Z)==A(d)
    src=run(D0,'0'*(2*(d-3)+1)+'1')
    own=run(R2,'0'*(d-2)+'1')
    assert src and own and src[0]==F(d) and own[0]==S(d)
    assert src[1]-own[1]==(d*d-d-4)//2

# Odd F/S normal forms.
for d in range(3,50,2):
    for j in range(15):
        a=run(F(d),'00'+'1'*j+'01'); b=run(S(d),'1'*(j+2)+'00')
        if a and b:
            assert a[0]==b[0] and b[1]-a[1]==-(j+3)
        a=run(F(d),'00'+'1'*j+'00'); b=run(S(d),'1'*(j+2)+'01')
        if a and b:
            assert a[0]==comp(P,b[0]) and b[1]-a[1]==-(j+3)

# Even F/S mod-4 normal forms.
for d in range(4,80,2):
    wm,wb=('010','011') if d%4==2 else ('011','010')
    a=run(F(d),wm); b=run(S(d),wm)
    assert a and b and a[0]==b[0] and b[1]-a[1]==-2
    a=run(F(d),wb); b=run(S(d),wb)
    assert a and b and a[0]==comp(b[0],P) and b[1]-a[1]==-2

# Exact counterexamples to generic P insertion monotonicity.
a=run((1,13),'01001'); b=run(comp(P,(1,13)),'11')
assert a and b and a[0]==b[0] and (a[1],b[1])==(4,3)
a=run((1,3),'01110110111011'); b=run(comp((1,3),P),'1110111110101')
assert a and b and a[0]==b[0] and (a[1],b[1])==(10,7)

# Index-shift bootstrap splice and quadratic margin.
samples=0
for D in range(3,42,2):
    d=D+2
    assert run(S(d),'1')==(R(D),D)
    BL=(D*D+D-6)//2
    CF=d*d-d-2
    assert run(R3,'0'*(D-3)+'10')==(L(D),BL)
    assert run(D0,'00'*(d-3)+'01')==(F(d),CF)
    for k in range(10):
        rw=run(L(D),'0'+'1'*k+'00')
        fw=run(F(d),'00'+'1'*k+'00')
        if rw and fw:
            assert rw[0]==fw[0]
            assert (CF+fw[1])-(BL+rw[1])==(D*D+7*D+8)//2
            samples+=1

assert run(D0,'01')==(F(3),4)
assert run(C8,'011000')==(F(3),4)

print('RL302_STRUCTURAL_CLOSEOUT_GREEN')
print('index_shift_samples',samples)
print('first_margin_D3',(3*3+7*3+8)//2)
print('last_margin_D41',(41*41+7*41+8)//2)
