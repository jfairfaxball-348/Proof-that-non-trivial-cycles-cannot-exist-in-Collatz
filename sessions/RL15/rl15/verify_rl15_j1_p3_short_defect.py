from decimal import Decimal, getcontext
from math import gcd

# RL-15 verifier: short-defect resultant closure for the complete
# coprime j=1, P3, [1,1,1] strict interior.
# Standard-library only. The infinite tail uses the same published
# Laurent-Mignotte-Nesterenko (LMN) estimate inherited in RL-11/RL-14.

getcontext().prec = 100
D = Decimal
ln2 = D(2).ln()
ln3 = D(3).ln()
ln4over3 = (D(4)/D(3)).ln()
ln27over8 = (D(27)/D(8)).ln()

# ---------------------------------------------------------------------------
# A. Structural parameter identities.
# For j=1 P3, C=2L-A is a positive multiple of 3: C=3h.
# Then B=A-L, L=B+3h, A=2B+3h, and tau^h=4/3 mod D.
# Positivity 2^A>3^L forces h<B/4, since
# (27/8)^(1/4) > 4/3 (equivalently 2187>2048).
# ---------------------------------------------------------------------------
assert 2187 > 2048
structural_checks = 0
for L in range(2, 500):
    p3 = 3**L
    Amin = (p3-1).bit_length()
    for A in range(Amin, 2*L):
        if (A+L) % 3 or gcd(A,L) != 1:
            continue
        B = A-L
        C = 2*L-A
        if B <= 0 or C <= 0:
            continue
        assert C % 3 == 0
        h = C//3
        assert L == B+3*h
        assert A == 2*B+3*h
        # Exact positivity consequence h<B/4.
        assert 4*h < B
        structural_checks += 1

# ---------------------------------------------------------------------------
# B. Universal archimedean envelope.
# Choose the cyclic P3 presentation H=4X^s+6X^b+9 which omits a largest
# simplex gap. Then s<=2B/3 and b<=s. For J_h=3X^h-4, every complex root
# has modulus r=(4/3)^(1/h), hence
# |Res(J_h,H)| <= 3^(2B/3) * (10(4/3)^(2B/(3h))+9)^h =: U.
# With eta=h/B<1/4, U/2^A <= exp(-kappa(eta) B).
# kappa is decreasing and kappa(1/4)>0.31.
# ---------------------------------------------------------------------------
eta = D(1)/D(4)
t = (D(8)/D(3))*ln4over3
kappa_quarter = (D(11)/D(4))*ln2 - (D(2)/D(3))*ln3 \
    - (D(1)/D(4))*(D(10)*t.exp()+D(9)).ln()
assert kappa_quarter > D('0.319')
assert kappa_quarter > D('0.31')
# The monotonicity proof is analytic: for
# g(t)=log(10e^t+9)-t*10e^t/(10e^t+9), g'(t)<0 and lim g=log 10,
# so g(t)>log10>log8=3log2; hence kappa'(eta)<0.
assert D(10).ln() > D(8).ln()
# B>=3 makes exp(-0.31B)<1/2.
assert (-D('0.31')*D(3)).exp() < D(1)/D(2)
# h<B/4 gives L=B+3h<7B/4, so 0.31 B > 0.177 L safely.
assert D('0.31')*D(4)/D(7) > D('0.177')

# ---------------------------------------------------------------------------
# C. LMN tail cutoff.
# A hypothetical survivor has D<=U, so delta=D/2^A<exp(-0.31B)<1/2.
# Hence Lambda=A log2-L log3 satisfies
# log Lambda < log2 - 0.31B < log2 - 0.177L.
# Apply the inherited LMN estimate
# log Lambda >= -22 M^2 log2 log3,
# M=max(log(A/log3+L/log2)+0.06,21), with A<2L and thus S<4L.
# At L=42000 both LMN branches contradict the exponential upper bound.
# ---------------------------------------------------------------------------
assert ln2 < D('0.694')
assert ln3 < D('1.099')
L0 = D(42000)
lmn_const = D(22)*(D(21)**2)*D('0.694')*D('1.099')
upper_mag = D('0.177')*L0 - D('0.694')
assert lmn_const < D(7400)
assert upper_mag > D(7433)
assert upper_mag > lmn_const
logbranch = D(22)*D('0.694')*D('1.099')*((D(4)*L0).ln()+D('0.06'))**2
assert logbranch < D(2500)
assert upper_mag > logbranch
assert (D(4)*L0).ln()+D('0.06') > D(2)

# ---------------------------------------------------------------------------
# D. Exact finite certificate for L<42000.
# Since any survivor has delta<1/2, for each L only the least A with
# 2^A>3^L and A+L==0 mod 3 can survive: increasing A by 3 would make
# 3^L/2^A<1/8 and thus delta>7/8.
#
# To avoid any floating-point comparison in the finite certificate, let
# S=floor(2B/3), q=ceil(S/h), N=10*4^q+9*3^q.  The universal resultant
# envelope gives the exact rational bound
#   |R| <= 3^S * (N/3^q)^h.
# A solution would therefore require
#   D*3^(qh) <= 3^S*N^h.
# The exact scan finds zero coprime j=1 P3 parameter pairs satisfying it.
# ---------------------------------------------------------------------------
finite_pairs = 0
barrier_pairs = []
p3 = 1
for L in range(1, 42000):
    p3 *= 3
    Amin = (p3-1).bit_length()  # least A with 2^A > 3^L
    A = Amin + ((-L-Amin) % 3)  # least such A with A+L == 0 mod 3
    if A >= 2*L:
        continue
    if gcd(A,L) != 1:
        continue
    B = A-L
    if B < 3:  # no strict [1,1,1] interior
        continue
    C = 2*L-A
    assert C > 0 and C % 3 == 0
    h = C//3
    assert 4*h < B
    DD = (1 << A) - p3
    assert DD > 0

    S = (2*B)//3
    q = (S+h-1)//h
    N = 10*(4**q) + 9*(3**q)
    left = DD * (3**(q*h))
    right = (3**S) * (N**h)
    finite_pairs += 1
    if left <= right:
        barrier_pairs.append((A,L,B,h,DD,S,q))

assert barrier_pairs == [], barrier_pairs

print('RL-15 j=1 P3 short-defect closure verifier: PASS')
print('structural parameter checks:', structural_checks)
print('kappa(1/4) =', kappa_quarter)
print('uniform exponential margin used: 0.31*B')
print('LMN cutoff L<:', 42000)
print('finite coprime first-congruence parameter pairs checked:', finite_pairs)
print('finite resultant-barrier survivors:', barrier_pairs)
