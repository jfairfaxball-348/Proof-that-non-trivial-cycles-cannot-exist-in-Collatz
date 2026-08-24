from fractions import Fraction
from math import isqrt

# RL31 exact balanced-prefix envelope / CF bootstrap verifier.
# Branch hypotheses used analytically in the companion note:
#   exact exceptional three-way-balanced branch,
#   z=2^b/3^e in (1,46/45), R>=2^71,
#   inherited RL24 q=L/gcd(A,L) floor.

N = 300
R0 = 1 << 71
Q0 = Fraction(46,45) * Fraction(R0 + 12, R0)
OLD_Q_FLOOR = 57397300723
C0 = Fraction(457841,1843200)

# ------------------------------------------------------------------
# 1. Exact N-step greedy envelope.
# Normalize x=q/Q with 0<x<=1.  Under the cap x<=1, the pointwise
# maximal admissible continuation is
#   x -> 2x       if x<=1/2,
#   x -> 2x/3     if x>1/2.
# For each initial interval x0 in (0,1], x_j=c_j*x0 and the N-step
# sum is linear. Split exactly at all threshold preimages.
# ------------------------------------------------------------------
states = [(Fraction(0), Fraction(1), Fraction(1), Fraction(0))]
for _ in range(N):
    new = []
    for lo, hi, c, S in states:
        S2 = S + c
        threshold = Fraction(1,2) / c
        # Greedy even branch, x_j<=1/2.
        ehi = min(hi, threshold)
        if ehi > lo:
            new.append((lo, ehi, 2*c, S2))
        # Greedy odd branch, x_j>1/2.
        olo = max(lo, threshold)
        if hi > olo:
            new.append((olo, hi, Fraction(2,3)*c, S2))
    states = new

best_sum = Fraction(0)
for lo, hi, c, S in states:
    # On each interval the sum S*x0 increases with x0.
    v = S * hi
    if v > best_sum:
        best_sum = v
M = best_sum / N

EXPECTED_M = Fraction(
    289661025475730124348366187773731846212314723592236134059063480299134845890983137619226395753,
    473884046723725653464253538204405286537042604564020039780668940186229359983539922912333900800,
)
assert M == EXPECTED_M
assert len(states) == 28637

# ------------------------------------------------------------------
# 2. The coarse rational b/e ceiling 317/200 is valid here.
# If b/e >=317/200, then z^200 >= (2^317/3^200)^e.
# The RHS already exceeds (46/45)^200 at e=846 and increases in e.
# ------------------------------------------------------------------
assert 2**317 > 3**200
assert (2**317)**846 * 45**200 > (3**200)**846 * 46**200

# Inherited q floor implies e >= ceil(q/3) because L=3e and L>=q.
def ceil_div(a,b): return (a+b-1)//b
E0 = ceil_div(OLD_Q_FLOOR, 3)
assert E0 == 19132433575
assert E0 >= 846

# Finite product coefficient from N-step blocks plus <N remainder.
def coeff(e_floor):
    return Fraction(317,200) * Q0 * M / 4 + Fraction(N) * Q0 / (4*e_floor)

c_first = coeff(E0)
assert c_first < C0

# ------------------------------------------------------------------
# 3. Rigorous logs / CF machinery copied in discipline from RL24H.
# If log(lambda)/L <= c/R and R>=R0, then
# 0 < p/q-beta <= (c/R0)/log2.
# ------------------------------------------------------------------
def ln_interval(x:Fraction, terms=280):
    x2=x*x; term=x; acc=Fraction(0)
    for j in range(terms):
        acc += term/(2*j+1)
        term *= x2
    lo=2*acc
    tail=2*term/(2*terms+1)/(1-x2)
    return lo,lo+tail

ln2_lo,ln2_hi=ln_interval(Fraction(1,3))
ln3_lo,ln3_hi=ln_interval(Fraction(1,2))
beta_lo=ln3_lo/ln2_hi
beta_hi=ln3_hi/ln2_lo

def cf_interval(lo,hi,terms=50):
    out=[]
    for _ in range(terms):
        a0=lo.numerator//lo.denominator
        a1=hi.numerator//hi.denominator
        assert a0==a1
        out.append(a0)
        lo-=a0; hi-=a0
        if lo<=0: break
        lo,hi=1/hi,1/lo
    return out

cf=cf_interval(beta_lo,beta_hi)
EXPECTED_ABOVE=[
    (2,1),(8,5),(65,41),(485,306),(24727,15601),
    (125743,79335),(301994,190537),(17087915,10781274),
    (272500658,171928773),(630138897,397573379),
    (10439860591,6586818670),
]

def cf_floor_from_coeff(c):
    cval = c / R0
    Tleg=ln2_lo/(2*cval)
    qmax=isqrt(Tleg.numerator//Tleg.denominator)
    while 2*qmax*qmax*cval >= ln2_lo: qmax-=1
    while 2*(qmax+1)*(qmax+1)*cval < ln2_lo: qmax+=1
    assert 2*qmax*qmax*cval < ln2_lo
    assert not (2*(qmax+1)*(qmax+1)*cval < ln2_lo)

    pm2,pm1=0,1; qm2,qm1=1,0
    above=[]; first_beyond=None
    for aa in cf:
        p=aa*pm1+pm2; q=aa*qm1+qm2
        pm2,pm1=pm1,p; qm2,qm1=qm1,q
        dlo=p*ln2_lo-q*ln3_hi
        dhi=p*ln2_hi-q*ln3_lo
        assert dhi<0 or dlo>0
        if q<=qmax and dlo>0:
            # Such an above-beta convergent is incompatible with the new bound.
            assert dlo > q*cval
            above.append((p,q))
        if q>qmax:
            first_beyond=(p,q,dlo>0)
            break
    assert above==EXPECTED_ABOVE
    assert first_beyond==(103768467013,65470613321,False)
    return qmax+1

# First bootstrap from inherited floor.
q1 = cf_floor_from_coeff(c_first)
assert q1 == 57490527166

# Reinsert the improved q floor into the finite remainder term.
E1 = ceil_div(q1,3)
c_final = coeff(E1)
q2 = cf_floor_from_coeff(c_final)
assert E1 == 19163509056
assert q2 == 57490527167
# Fixed: ceil(q2/3)=E1, so another iteration changes nothing.
assert ceil_div(q2,3) == E1
assert cf_floor_from_coeff(coeff(ceil_div(q2,3))) == q2

print('RL31 balanced-prefix envelope / CF bootstrap verifier: PASS')
print('N =',N,'terminal envelope intervals =',len(states))
print('M_N =',M)
print('M_N ~= %.15f' % float(M))
print('Q0 ~= %.15f' % float(Q0))
print('inherited e floor =',E0)
print('first coefficient ~= %.15f' % float(c_first))
print('first bootstrapped q floor =',q1)
print('fixed-point e floor =',E1)
print('final coefficient ~= %.15f' % float(c_final))
print('final q=L/gcd(A,L) floor =',q2)
print('old RL24H asymptotic coefficient ~= %.15f' % float(C0))
print('coefficient improvement ~= %.15f' % float(C0-c_final))
