from itertools import combinations
from math import gcd

# Standard full-parity affine numerator.
def Qword(w):
    L=sum(w); p=0; q=0
    for i,b in enumerate(w):
        if b:
            q += (1<<i)*3**(L-1-p)
            p += 1
    return q

def v_p(n,p):
    n=abs(n); c=0
    while n and n%p==0:
        c+=1; n//=p
    return c

def excursions(u,v):
    d=0; out=[]; s=None; sign=None
    cu=cv=0
    for j,(a,b) in enumerate(zip(u,v)):
        if d==0 and a!=b:
            s=j; sign=1 if b>a else -1; cu=cv=0
        if s is not None:
            cu += a; cv += b
        d += b-a
        if s is not None and d==0:
            assert cu==cv
            out.append((s,j+1,j+1-s,cu,sign))
            s=None
    assert d==0 and s is None
    return out

def localQ(w): return Qword(w)

def transport_area(u,v):
    du=dv=0; rho=0
    for a,b in zip(u,v):
        rho += abs(dv-du)
        du += a; dv += b
    return rho

def ordered_position_distance(u,v):
    pu=[i for i,b in enumerate(u) if b]
    pv=[i for i,b in enumerate(v) if b]
    return sum(abs(i-j) for i,j in zip(pu,pv))

def sparse_min_swap_path(u,v):
    # Greedily choose an adjacent transposition that reduces earth-mover area by 1.
    w=u[:]; terms=[]; steps=0
    while w!=v:
        prefw=prefv=0; chosen=None
        for i in range(len(w)-1):
            prefw += w[i]; prefv += v[i]
            d=prefv-prefw
            if d<0 and w[i]==1 and w[i+1]==0:
                chosen=(i,1)   # 10 -> 01, Q increment positive
                break
            if d>0 and w[i]==0 and w[i+1]==1:
                chosen=(i,-1)  # 01 -> 10, Q increment negative
                break
        assert chosen is not None
        i,sgn=chosen
        q0=Qword(w)
        k=sum(w[i+2:])
        w[i],w[i+1]=w[i+1],w[i]
        q1=Qword(w)
        assert q1-q0==sgn*(1<<i)*3**k
        terms.append((sgn,i,k))
        steps+=1
    return terms

# Exhaustive combinatorial checks through length 9.
checked=0
for a in range(2,10):
    for ell in range(1,a):
        words=[]
        for pos in combinations(range(a),ell):
            w=[0]*a
            for i in pos:w[i]=1
            words.append(w)
        for u in words:
            U=Qword(u)
            for v in words:
                if u==v: continue
                V=Qword(v); diff=U-V
                rho=transport_area(u,v)
                assert rho==ordered_position_distance(u,v)
                terms=sparse_min_swap_path(u,v)
                assert len(terms)==rho
                # Path telescopes U -> V, hence U-V is the negative path sum.
                pathsum=sum(sgn*(1<<i)*3**k for sgn,i,k in terms)
                assert V-U==pathsum
                # fixed-weight first-disagreement / v2 lemma
                first=next(i for i,(x,y) in enumerate(zip(u,v)) if x!=y)
                assert v_p(diff,2)==first
                ex=excursions(u,v)
                # exact excursion decomposition
                recon=0
                pu=0
                ex_by_start={e[0]:e for e in ex}
                for s,t,h,p,sgn in ex:
                    c=sum(u[:s])
                    alpha=u[s:t]; beta=v[s:t]
                    assert sum(alpha)==sum(beta)==p
                    # one-sided excursion and leading bit
                    d=0
                    vals=[]
                    for aa,bb in zip(alpha,beta):
                        d += bb-aa
                        vals.append(d)
                    assert vals[-1]==0
                    assert all((x>0 if sgn>0 else x<0) for x in vals[:-1])
                    lead=beta if sgn>0 else alpha
                    assert lead[0]==1
                    # leading segment p odd states cover at least h valuation positions combinatorially
                    ones=[i for i,b in enumerate(lead) if b]
                    assert len(ones)==p and ones[0]==0
                    cover=sum(ones[i+1]-ones[i] for i in range(len(ones)-1)) + (h-ones[-1])
                    assert cover==h
                    recon += (1<<s) * 3**(ell-c-p) * (Qword(alpha)-Qword(beta))
                assert recon==diff
                # terminal common suffix weight divides the 3-adic valuation of the difference
                k=0
                while k<a and u[a-1-k]==v[a-1-k]: k+=1
                q=sum(u[a-k:]) if k else 0
                assert v_p(diff,3)>=q
                checked += 1

# RL21 exact gap-factor countermodel: the new one-excursion bound is sharp.
UWORD='11011011010110110110101101110011011100110110110101110101011011100'
VWORD='11111111110111000111110011011011110101010111110011101000011100000'
u=[int(c) for c in UWORD]; v=[int(c) for c in VWORD]
a=65; ell=41; X=1<<a; Y=3**ell
U=Qword(u); V=Qword(v)
assert U-V==4*(X+Y)
G=4
ex=excursions(u,v)
assert ex==[(2,63,61,39,1)]
r=v_p(G,2); s3=v_p(G,3)
assert ex[0][3]==ell-r-s3==39

# Synchronized-rotation identities on the gap-factor countermodel.
def rot_num_pair(u,v,s):
    ur=u[s:]+v[:s]
    vr=v[s:]+u[:s]
    assert len(ur)==len(vr)==len(u)
    assert sum(ur)==sum(vr)==sum(u)
    return Qword(ur),Qword(vr)

# First common odd step recovers X-Y combinatorially.
U0,V0=rot_num_pair(u,v,0)
U1,V1=rot_num_pair(u,v,1)
assert 2*(U1+V1)-3*(U0+V0)==2*(X-Y)

# First divergence r=v2(G) recovers X+Y times oddpart(G).
# Common prefix has p odd bits; formal gap evolves by 3^p/2^r.
p=sum(u[:r]); assert u[:r]==v[:r]
Ur,Vr=rot_num_pair(u,v,r)
B0=U0-V0; Br=Ur-Vr
Godd=G//(1<<r)
assert gcd(abs(B0),abs(Br))==(X+Y)*Godd
assert Br==(X+Y)*(3**p*G//(1<<r))

rho_counter=transport_area(u,v)
assert rho_counter==ordered_position_distance(u,v)==170
terms_counter=sparse_min_swap_path(u,v)
assert len(terms_counter)==170
assert V-U==sum(sgn*(1<<i)*3**k for sgn,i,k in terms_counter)

print('RL36 g=2 excursion charging / factor-recovery verifier: PASS')
print('exhaustive equal-weight word-pair checks =',checked)
print('RL21 countermodel excursions =',ex)
print('one-excursion charged weight =',ex[0][3])
print('ell-v2(G)-v3(G) =',ell-r-s3)
print('relative two-rotation gcd cofactor G_odd =',Godd)
print('RL21 countermodel transport area rho =',rho_counter)
