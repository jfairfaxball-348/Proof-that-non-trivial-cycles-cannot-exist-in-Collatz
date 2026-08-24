from fractions import Fraction

# Full-parity shortcut map and affine prefix formula.
def T(n):
    return (3*n+1)//2 if n&1 else n//2

def bits(n,m):
    out=[]
    for _ in range(m):
        out.append(n&1)
        n=T(n)
    return out

def affine(bs):
    # T^m(s)=(3^p s+Q)/2^m on the fixed parity branch bs.
    p=0; q=0
    for j,b in enumerate(bs):
        if b:
            q=3*q+(1<<j)
            p+=1
    return p,q

# Every near-minimum odd phase is already 3 mod 4.  At five bits,
# residues 3,11,19,23 mod32 are impossible: even the maximal s<16R/15
# is sent below R by step <=5 for R>=161.  The survivors are exactly
# {7,15,27,31} modulo 32.
R0=161
candidates=[3,7,11,15,19,23,27,31]
survivors=[]
witness={}
for r in candidates:
    bs=bits(r,5)
    bad=None
    for j in range(1,6):
        p,q=affine(bs[:j])
        # 3^p*(16/15)R + q < 2^j R, tested at R0;
        # the q/R term only decreases for larger R.
        if Fraction(3**p*16,15)+Fraction(q,R0) < 2**j:
            bad=(j,tuple(bs[:j]),p,q)
            break
    if bad is None:
        survivors.append(r)
    else:
        witness[r]=bad
assert survivors==[7,15,27,31]
assert set(witness)=={3,11,19,23}

# In particular a hard root beginning 1101 cannot have fifth bit 0:
# 11010 gives T^5(R)=(27R+23)/32<R for R>=5.
p,q=affine([1,1,0,1,0])
assert (p,q)==(3,23)
assert 27*5+23 < 32*5

# Hard cubic sector: R ==1 mod3, G>H, universal shared 11 so
# G=4N,H=4K.  Nonzero x,y mod3 force N,K !=2 mod3.
# The mod32 near-min set restricts N,K modulo 8 according to R mod32.
A32={7,15,27,31}
allowed_N={}
for r in sorted(A32):
    vals=[]
    for n in range(0,8):
        if (r+4*n)%32 in A32:
            vals.append(n)
    allowed_N[r]=tuple(vals)
assert allowed_N=={
    7:(0,2,5,6),
    15:(0,3,4,6),
    27:(0,1,3,5),
    31:(0,2,4,7),
}

# Smallest positive hard-sector pair N>K in each root residue.
expected_pair={7:(10,6),15:(4,3),27:(3,1),31:(7,4)}
for r,(Ne,Ke) in expected_pair.items():
    good=[]
    for N in range(1,80):
        if N%8 not in allowed_N[r] or N%3==2: continue
        for K in range(1,N):
            if K%8 not in allowed_N[r] or K%3==2: continue
            good.append((N,K))
    assert good
    # Lexicographic by N then K is enough after checking there is no
    # smaller N admissible; verify the exact expected coordinate-minimal pair.
    minN=min(N for N,K in good)
    sub=[(N,K) for N,K in good if N==minN]
    minK=min(K for N,K in sub)
    assert (minN,minK)==(Ne,Ke)

# Verify exact lattice minima in representative near-resonant B/Y pairs.
for b,e in [(65,41),(149,94)]:
    B=1<<b; Y=3**e
    assert Y < B < 2*Y
    expected_val={
        7:10*B+6*Y,
        15:4*B+3*Y,
        27:3*B+Y,
        31:7*B+4*Y,
    }
    for r in sorted(A32):
        vals=[]
        for N in range(1,80):
            if N%8 not in allowed_N[r] or N%3==2: continue
            for K in range(1,N):
                if K%8 not in allowed_N[r] or K%3==2: continue
                a=Y*K+B*N
                c=(B+Y)*K-Y*N
                vals.append((max(abs(a),abs(c)),N,K))
        vals.sort()
        assert vals[0][0]==expected_val[r]
        assert vals[0][1:]==expected_pair[r]

# H=4K and H<(23/90)e gives analytic e floors by root mod32.
# r=27 has K>=1 (weak); the other residues force much larger H.
for r,emin in [(15,47),(31,63),(7,94)]:
    K=expected_pair[r][1]
    threshold=Fraction(360*K,23)  # 4K < 23e/90 => e>360K/23
    assert emin-1 <= threshold < emin

# Exact terminal arithmetic: once e>=47 but e<94 there is no near-resonant
# integer pair.  Thus every hard-sector root residue except 27 mod32 has e>=94.
near=[]
for e in range(1,94):
    for b in range(1,2*e+3):
        B=1<<b; Y=3**e
        if B>Y and 15*B**3 < 16*Y**3:
            near.append((b,e))
assert near==[(65,41)]

# Exact weakest-vector residue: R==1 mod3 and R==27 mod32 gives R==91 mod96.
weak96=[r for r in range(96) if r%3==1 and r%32==27]
assert weak96==[91]

# Intersections with the inherited hard root classes 43/91 mod144 after the
# forced fifth bit are 187 and 91 mod288 respectively.
assert [r for r in range(288) if r%144==43 and r%32==27]==[187]
assert [r for r in range(288) if r%144==91 and r%32==27]==[91]

# RL23 saturation family refinement: among the old hard-compatible t classes,
# the forced fifth bit leaves t mod48 in {3,35}; infinitely many remain.
sol=[]
for tt in range(48):
    RR=361+486*tt
    if RR%144==91 and RR%32==27 and tt%3!=1:
        sol.append(tt)
assert sol==[3,35]

print('RL26 cubic mod-32 hard-sector verifier: PASS')
print('near-minimum residues mod32 =',survivors)
print('excluded residue witnesses =',witness)
print('hard-sector minimal (N,K) by R mod32 =',expected_pair)
print('unique weak root class: R == 91 mod96')
print('hard-root classes refine to 91 or 187 mod288')
print('RL23 local saturation hard-compatible t refines to t mod48 in {3,35}')
