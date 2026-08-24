from fractions import Fraction
import sympy as sp

# ------------------------------------------------------------
# 1. Full three-pair cubic spread repair
# ------------------------------------------------------------
# After factoring the common 2^r prefix, the two RL22 coordinates are
#   a = Y*K + B*N = (U-W)/2^r
#   c = (B+Y)*K - Y*N = (V-W)/2^r
# and the omitted third pair is
#   a-c = B*(N-K) + Y*N = (U-V)/2^r.
# In the G>H sector N>K, nonzero-mod-3 ownership excludes (N,K)=(2,1).
# The true max over all three pairwise differences is therefore >=2B+3Y.

for b,e in [(65,41),(149,94),(214,135),(233,147)]:
    B=1<<b; Y=3**e
    assert Y < B < 2*Y
    for N in range(1,80):
        for K in range(1,N):
            if not (N%3==0 or K%3==0 or (N-K)%3==0):
                continue
            a=Y*K+B*N
            c=(B+Y)*K-Y*N
            d=a-c
            Delta=max(abs(a),abs(c),abs(d))
            assert Delta >= 2*B+3*Y
    # Equality is attained by the old coordinate extremizer (3,1),
    # but through the omitted U-V pair, not U-W.
    N,K=3,1
    a=Y*K+B*N
    c=(B+Y)*K-Y*N
    d=a-c
    assert a==3*B+Y
    assert c==B-2*Y
    assert d==2*B+3*Y
    assert max(abs(a),abs(c),abs(d))==2*B+3*Y
    assert 2*B+3*Y > 3*B+Y  # because B<2Y

# H>G was already correctly controlled by the two W-referenced coordinates.
for b,e in [(65,41),(149,94)]:
    B=1<<b; Y=3**e
    for K in range(2,60):
        for N in range(1,K):
            if not (N%3==0 or K%3==0 or (N-K)%3==0):
                continue
            a=Y*K+B*N
            c=(B+Y)*K-Y*N
            d=a-c
            assert max(abs(a),abs(c),abs(d)) >= 2*B+3*Y

# Old weak root residue 27 mod32 remains the weakest residue after the repair,
# but its full-spread minimum is now 2B+3Y rather than 3B+Y.
A32={7,15,27,31}
allowed_N={}
for rr in sorted(A32):
    allowed_N[rr]=tuple(n for n in range(8) if (rr+4*n)%32 in A32)
assert allowed_N=={
    7:(0,2,5,6),
    15:(0,3,4,6),
    27:(0,1,3,5),
    31:(0,2,4,7),
}
for b,e in [(65,41),(149,94)]:
    B=1<<b; Y=3**e
    mins={}
    pairs={}
    for rr in sorted(A32):
        vals=[]
        for N in range(1,100):
            if N%8 not in allowed_N[rr] or N%3==2: continue
            for K in range(1,N):
                if K%8 not in allowed_N[rr] or K%3==2: continue
                a=Y*K+B*N
                c=(B+Y)*K-Y*N
                d=a-c
                vals.append((max(abs(a),abs(c),abs(d)),N,K))
        vals.sort()
        mins[rr]=vals[0][0]
        pairs[rr]=vals[0][1:]
    assert pairs=={7:(10,6),15:(4,3),27:(3,1),31:(7,4)}
    assert mins[7]==10*B+6*Y
    assert mins[15]==4*B+3*Y
    assert mins[27]==2*B+3*Y
    assert mins[31]==7*B+4*Y
    assert mins[27] < mins[15] < mins[31] < mins[7]

# Global RL25 range + repaired full-spread floor gives e>=29.
def glob_rhs(e):
    return Fraction(4*e,5)-3+3*Fraction(2,3)**e
assert all(glob_rhs(e) <= 20 for e in range(1,29))
assert glob_rhs(29) > 20

# ------------------------------------------------------------
# 2. Prefix-aware Q floor in exact G=12,H=4 geometry
# ------------------------------------------------------------
def Qword(bits):
    e=sum(bits); p=0; q=0
    for i,bit in enumerate(bits):
        if bit:
            q += (1<<i)*3**(e-1-p)
            p += 1
    return q

def qmin_prefix_11101(e):
    # Forced one positions 0,1,2,4; remaining ones as early as possible
    # at 5,6,...,e. Valid because b>e in the near-resonant block.
    pos=[0,1,2,4]+list(range(5,e+1))
    bits=[0]*(e+1)
    for i in pos: bits[i]=1
    return Qword(bits)

for e in range(4,13):
    q=qmin_prefix_11101(e)
    assert q*27 == 35*3**e - 54*2**e

# Thus V >= (35/27)Y - 2^(e+1).
# With V=(B-Y)R+4B-12Y, z=B/Y<46/45 and RL25
# R(z-1)<23e/90, a necessary condition is
#   1243/135 - 2(2/3)^e < 23e/90.
def prefix_gate_lhs(e):
    return Fraction(1243,135)-2*Fraction(2,3)**e
def prefix_gate_rhs(e):
    return Fraction(23*e,90)
assert all(prefix_gate_lhs(e) >= prefix_gate_rhs(e) for e in range(4,37))
assert prefix_gate_lhs(37) < prefix_gate_rhs(37)

# ------------------------------------------------------------
# 3. Incoming odd-map valuation congruences at the three balanced cuts
# ------------------------------------------------------------
# If an odd predecessor q maps to odd endpoint s with odd-map valuation nu,
# 3q+1=2^nu s. Integrality requires 2^nu s=1 mod3; q nonzero mod3
# further excludes 2^nu s=1 mod9.
def allowed_nu_classes(smod9):
    out=[]
    for nu in range(1,7):
        v=(pow(2,nu,9)*smod9)%9
        if v%3==1 and v!=1:
            out.append(nu%6)
    return sorted(set(out))

# R==91 mod288 gives R mod9=1, x=R+12 mod9=4, y=R+4 mod9=5.
assert allowed_nu_classes(4)==[0,2]   # incoming to x
assert allowed_nu_classes(5)==[3,5]   # incoming to y
assert allowed_nu_classes(1)==[2,4]   # general incoming to an R==1 mod9 endpoint
# Exceptional weak close fixes nu_R=2 exactly: 3z+1=4R.

# ------------------------------------------------------------
# 4. Exact early three-trajectory braid
# ------------------------------------------------------------
R=sp.symbols('R', integer=True, positive=True)
u=R
v=R+12
w=R+4

def T_aff(x,bit):
    return sp.expand((3*x+1)/2 if bit else x/2)

pu=[1,1,0,1,1]
pv=[1,1,1,0,1]
pw=[1,1,1,1,1]
vals={'u':[u], 'v':[v], 'w':[w]}
for name,pref in [('u',pu),('v',pv),('w',pw)]:
    x=vals[name][0]
    for bit in pref:
        x=T_aff(x,bit)
        vals[name].append(sp.factor(x))

assert sp.simplify((vals['v'][3]-vals['w'][3])-27)==0
assert sp.simplify((vals['w'][4]-vals['v'][4])-(27*R+23)/8)==0
assert sp.simplify((vals['v'][4]-vals['u'][4])-20)==0
assert sp.simplify((vals['v'][5]-vals['u'][5])-30)==0

print('RL27 full-spread / adjacent-ownership verifier: PASS')
print('corrected universal full spread at r=2: Delta >= 4(2B+3Y)')
print('root 27 mod32 full-spread minimum: 4(2B+3Y), attained at (N,K)=(3,1)')
print('global-range consequence: e >= 29')
print('exact-geometry prefix-aware V floor consequence: e >= 37')
print('incoming valuation classes: nu_x mod6 in {0,2}, nu_y mod6 in {3,5}, weak-close nu_R=2')
print('forced v/w first reversal separation after four steps: (27R+23)/8')
