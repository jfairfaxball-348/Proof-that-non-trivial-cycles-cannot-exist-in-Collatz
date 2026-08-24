from itertools import product


def vp(x,p):
    assert x
    c=0
    while x%p==0:
        x//=p;c+=1
    return c

def v2(x): return vp(x,2)
def v3(x): return vp(x,3)

def coeff(n,t,mup):
    ell=(1<<mup)*3**n
    c=(1<<(n+mup))*((1<<t)-1)
    d=(1<<(n+t))*3**mup
    return ell,c,d

def compose(word,start=0):
    Lin,C,Den=1,0,1; P=len(word)
    for k in range(P):
        ell,c,d=coeff(*word[(start+k)%P])
        C=ell*C+c*Den
        Lin*=ell; Den*=d
    return Lin,C,Den

def rotate(word,r): return word[r:]+word[:r]

def cyclic_mus(word):
    return [word[(j-1)%len(word)][2] for j in range(len(word))]

def valid_cyclic(word):
    mus=cyclic_mus(word)
    return all(word[j][0]>mus[j] for j in range(len(word)))

def invariants(word):
    mus=cyclic_mus(word)
    M=sum(mus)
    L=sum(word[j][0]-mus[j] for j in range(len(word)))
    A=L+sum(t for n,t,m in word)
    D=(1<<A)-3**L
    return mus,M,L,A,D

def hs(word):
    return [n-mup for n,t,mup in word]

def good_rotations(word):
    # Every nonempty suffix sum of the rotated h-word is >0.
    out=[];P=len(word)
    for r in range(P):
        wr=rotate(word,r); h=hs(wr)
        if all(sum(h[i:])>0 for i in range(P)):
            out.append(r)
    return out

def term_vals3(word):
    mus,M,L,A,D=invariants(word)
    vals=[]
    P=len(word)
    for i,(n,t,mup) in enumerate(word):
        r=v3((1<<t)-1)
        a=r-mup
        suf=sum(word[k][0]-word[k][2] for k in range(i+1,P))
        vals.append(a+suf)
    return vals

def boundary_gate_scan(word,start):
    # Start must have v3(C)=M. Scan forward. At generic edges, signature
    # must propagate. At boundary r=n, exact declared c=mup-n is equivalent
    # to kappa=c, where kappa is the normalized RHS cancellation depth.
    _,M,L,A,D=invariants(word)
    K=(6**M)*D
    Cs=[compose(word,r)[1] for r in range(len(word))]
    assert v3(Cs[start])==M
    current=start
    gates=[]
    for _ in range(len(word)):
        j=current
        n,t,mup=word[j]
        r=v3((1<<t)-1)
        nxt=(j+1)%len(word)
        ell,caff,d=coeff(n,t,mup)
        assert d*Cs[nxt]==ell*Cs[j]+caff*K
        if r!=n:
            # if the current numerator is an M-unit, a unique lower term
            # forces the next one to be an M-unit.
            assert v3(Cs[j])==M
            assert v3(Cs[nxt])==M
        else:
            assert v3(Cs[j])==M
            cdecl=mup-n
            H=((1<<t)-1)//(3**n)
            Chat=Cs[j]//(3**M)
            kappa=v3(Chat + (1<<(M+n))*D*H)
            # equivalent form from transport numerator
            U=(ell*Cs[j]+caff*K)//(3**(M+n))
            assert v3(U)==kappa
            assert v3(Cs[nxt])-M==kappa-cdecl
            gates.append((j,cdecl,kappa))
            if kappa!=cdecl:
                return False,gates,Cs
        current=nxt
    return True,gates,Cs

# Pseudorandom symbolic audit, deliberately includes boundaries and c>0.
good_rotation_checks=0
unique_min_checks=0
gate_equivalence_checks=0
for P in (2,3,4,5,6):
    for seed in range(1,1800):
        word=[]
        for j in range(P):
            n=1+((13*seed+5*j)%9)
            t=1+((17*seed+11*j)%20)
            r=v3((1<<t)-1)
            if r<n: mup=r
            elif r>n: mup=n
            else: mup=n+((seed+3*j)%4)
            word.append((n,t,mup))
        if not valid_cyclic(word): continue
        mus,M,L,A,D=invariants(word)
        assert L>0
        gs=good_rotations(word)
        assert gs, (word,hs(word))
        for gr in gs:
            wr=rotate(word,gr)
            _,Mr,_,_,_=invariants(wr)
            C=compose(wr,0)[1]
            vals=term_vals3(wr)
            assert vals[-1]==0
            assert all(x>0 for x in vals[:-1]), (wr,hs(wr),vals)
            assert v3(C)==Mr
            good_rotation_checks+=1
            unique_min_checks+=1
            # Compare boundary scan with direct all-rotation signature.
            ok,gates,Cs=boundary_gate_scan(word,gr)
            direct=all(v3(c)==M for c in Cs)
            assert ok==direct, (word,gr,gates,[v3(c)-M for c in Cs])
            gate_equivalence_checks+=1
            break

# Exhaustive small criterion audit, matching RL-5's declared P<=3,n,t<=6,c<=2 domain.
def local_opts(n,t):
    r=v3((1<<t)-1)
    if r<n:return [r]
    if r>n:return [n]
    return [n,n+1,n+2]
trip=[]
for n in range(1,7):
    for t in range(1,7):
        for mup in local_opts(n,t): trip.append((n,t,mup))

criterion_words=0
boundary_words=0
boundary_gate_pass_words=0
Ddiv_words=0
criterion_survivors=0
nontrivial_survivors=0
for P in (1,2,3):
    for wordt in product(trip,repeat=P):
        word=list(wordt)
        if not valid_cyclic(word): continue
        mus,M,L,A,D=invariants(word)
        if D<=0: continue
        criterion_words+=1
        has_boundary=any(v3((1<<t)-1)==n for n,t,mup in word)
        if has_boundary: boundary_words+=1
        gs=good_rotations(word); assert gs
        gr=gs[0]
        Cg=compose(word,gr)[1]
        assert v2(Cg)==M+word[gr][0]
        assert v3(Cg)==M
        gates_ok,gates,Cs=boundary_gate_scan(word,gr)
        direct_sig=all(v3(c)==M for c in Cs)
        assert gates_ok==direct_sig
        if gates_ok and has_boundary: boundary_gate_pass_words+=1
        # Generalized realization criterion: D|C at the good rotation and
        # all boundary gates pass. Compare with direct full realization.
        predicted=(Cg%D==0 and gates_ok)
        if Cg%D==0: Ddiv_words+=1
        actual=True; Ws=[]
        K=(6**M)*D
        for r0 in range(P):
            Cr=Cs[r0]
            if Cr%K:
                actual=False;break
            W=Cr//K
            n,t,mup=word[r0]
            if W<=0 or v2(W)!=n or W%3==0:
                actual=False;break
            q=W>>n
            if q%2==0 or q%3==0:
                actual=False;break
            X=3**n*q-1
            if v2(X)!=t:
                actual=False;break
            z=X>>t
            if v3(z+1)!=mup:
                actual=False;break
            Ws.append(W)
        if actual:
            for j,W in enumerate(Ws):
                n,t,mup=word[j]; q=W>>n
                z=(3**n*q-1)>>t
                Wn=Ws[(j+1)%P]
                # xi(z)=(2/3)^mu (z+1) in +1 coordinates.
                if (1<<mup)*(z+1) != 3**mup*Wn:
                    actual=False;break
        assert predicted==actual, (word,gr,gates,Cg%D,[v3(c)-M for c in Cs],Ws)
        if predicted:
            criterion_survivors+=1
            if not all(W==2 for W in Ws): nontrivial_survivors+=1

assert nontrivial_survivors==0
print('RL-6 good-rotation / boundary-gate verifier: PASS')
print('symbolic good-rotation checks:',good_rotation_checks)
print('symbolic unique-3adic-minimum checks:',unique_min_checks)
print('symbolic boundary-gate equivalence checks:',gate_equivalence_checks)
print('exhaustive admissible D>0 words:',criterion_words)
print('exhaustive words containing exact boundaries:',boundary_words)
print('boundary words passing all 3-adic gates:',boundary_gate_pass_words)
print('words with D dividing good-rotation numerator:',Ddiv_words)
print('generalized criterion survivors:',criterion_survivors)
print('generalized nontrivial survivors:',nontrivial_survivors)

# RL-6 minimum-anchor denominator defect budget.
from fractions import Fraction

def ae(n,t,mup):
    h=n-mup
    a=(Fraction(3,2)**h)*Fraction(1,1<<t)
    e=(Fraction(2,3)**mup)*(1-Fraction(1,1<<t))
    return a,e

def rational_Ws(word):
    mus,M,L,A,D=invariants(word)
    K=(6**M)*D
    return [Fraction(compose(word,r)[1],K) for r in range(len(word))]

defect_checks=0
for P in (2,3,4,5,6):
    for seed in range(1,1300):
        word=[]
        for j in range(P):
            n=1+((19*seed+7*j)%10)
            t=1+((23*seed+5*j)%16)
            r=v3((1<<t)-1)
            if r<n:mup=r
            elif r>n:mup=n
            else:mup=n+((seed+j)%3)
            word.append((n,t,mup))
        if not valid_cyclic(word):continue
        mus,M,L,A,D=invariants(word)
        if D<=0:continue
        Ws=rational_Ws(word)
        rmin=min(range(P), key=lambda r: Ws[r])
        wr=rotate(word,rmin)
        Wsr=rational_Ws(wr)
        assert Wsr[0]==min(Wsr)
        rho=Fraction(3**L,1<<A)
        # Direct composition error sum with suffix coefficient products.
        E=Fraction(0,1)
        es=[]
        for i,tr in enumerate(wr):
            a_i,e_i=ae(*tr); es.append(e_i)
            B=Fraction(1,1)
            for k in range(i+1,P): B*=ae(*wr[k])[0]
            E += e_i*B
            if i<P-1:
                assert B*Wsr[i+1] < Wsr[0]
            else:
                assert B==1 and Wsr[i+1-P]==Wsr[0]
        assert Wsr[0]*(1-rho)==E
        defect=Fraction(D,1<<A)
        assert defect==E/Wsr[0]
        assert es[-1]/Wsr[0] < defect
        assert defect < sum(es,Fraction(0,1))/Wsr[0]
        assert defect < Fraction(P,1)/Wsr[0]
        defect_checks+=1
print('minimum-anchor denominator-defect checks:',defect_checks)
