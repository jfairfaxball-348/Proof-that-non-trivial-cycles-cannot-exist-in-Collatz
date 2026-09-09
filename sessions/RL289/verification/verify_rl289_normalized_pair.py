#!/usr/bin/env python3
"""Portable RL289 fast verifier.

This is a regression verifier for the frozen RL289 structural identities and
barriers. Analytic proofs are in the session report. It intentionally does not
claim Gate A or duplicate the inherited exhaustive H<=22 certificate.
"""

from itertools import product

MAX_DEPTH = 16

def v2(n):
    assert n != 0
    n = abs(n)
    return (n & -n).bit_length() - 1

def step(d, J, H, x):
    K = J + 2**d - 1
    if K % 2 == 0:
        y = x
        if x == 1:
            d2, K2 = d, 3*K//2
        else:
            d2, K2 = d, (K + 3**d - 1)//2
    else:
        y = 1-x
        if x == 1:
            if d <= 1:
                return None
            d2, K2 = d-1, (K-1)//2
        else:
            d2, K2 = d+1, 3*(K+3**d)//2
    J2 = K2 - 2**d2 + 1
    return d2, J2, H + d - 1, y

def append_U(U, n, bit):
    return U if bit == 0 else 3*U + 2**n

def append_Q(Q, n, bit):
    return Q if bit == 0 else 3*Q + 2**n

def zeta_from_Q(Q, r, n):
    if n == 0:
        return 0
    mod = 2**n
    return (-Q * pow(3, -r, mod)) % mod

def parity_bits(z, n):
    out = []
    for _ in range(n):
        b = z & 1
        out.append(b)
        z = z//2 if b == 0 else (3*z+1)//2
    return tuple(out)

def prefix_dominant(x, y):
    sx = sy = 0
    for a,b in zip(x,y):
        sx += a; sy += b
        if sy < sx:
            return False
    return True

# records: (d,J,H,xword,yword,Ux,Uy,Qx,Qy,rx,ry)
levels = [[(1,-13,0,(),(),-7,-7,0,0,0,0)]]
edge_checks = 0
shadow_checks = 0
cylinder_checks = 0
mixed_checks = 0
positive_carry3 = 0
terminals = []

for n in range(MAX_DEPTH):
    nxt = []
    for rec in levels[-1]:
        d,J,H,xw,yw,Ux,Uy,Qx,Qy,rx,ry = rec
        for x in (0,1):
            st = step(d,J,H,x)
            if st is None:
                continue
            d2,J2,H2,y = st
            Ux2 = append_U(Ux,n,x)
            Uy2 = append_U(Uy,n,y)
            Qx2 = append_Q(Qx,n,x)
            Qy2 = append_Q(Qy,n,y)
            rx2, ry2 = rx+x, ry+y
            x2, y2 = xw+(x,), yw+(y,)
            nn = n+1

            T2 = J2 - 3**d2 + 2**d2
            assert 2**nn * T2 == 3**d2 * Ux2 - Uy2
            shadow_checks += 1

            zx = zeta_from_Q(Qx2, rx2, nn)
            zy = zeta_from_Q(Qy2, ry2, nn)
            assert (zy - (3*zx+14)) % (2**nn) == 0
            cylinder_checks += 1

            ax = (3**rx2 * zx + Qx2)//(2**nn)
            by = (3**ry2 * zy + Qy2)//(2**nn)
            assert 0 <= ax < 3**rx2
            assert 0 <= by < 3**ry2
            alpha = 3**rx2 - ax
            beta  = 3**ry2 - by
            cnum = 3*zx + 14 - zy
            assert cnum % (2**nn) == 0
            c = cnum // (2**nn)
            if nn >= 4:
                assert c in (0,1,2,3)
            Jmix = (2-c)*3**ry2 + beta - 3**d2*alpha + 3**d2 - 2**d2
            assert Jmix == J2
            assert (2**nn * alpha + Ux2) % (3**rx2) == 0
            assert (2**nn * beta + Uy2) % (3**ry2) == 0
            if J2 > 0 and c == 3:
                positive_carry3 += 1
            mixed_checks += 1

            if d2 == 1 and J2 > 0 and (J2 & (J2-1)) == 0 and J2 > 1:
                terminals.append((nn,J2,H2,Qx2,Qy2,rx2))

            nxt.append((d2,J2,H2,x2,y2,Ux2,Uy2,Qx2,Qy2,rx2,ry2))
            edge_checks += 1
    levels.append(nxt)

assert positive_carry3 == 0

expected = [2,3,5,9,16,30,56,105,199,379,721,1377]
ballot_counts = []
for n in range(1,13):
    cnt = 0
    for z in range(2**n):
        x = parity_bits(z,n)
        y = parity_bits(3*z+14,n)
        if prefix_dominant(x,y):
            cnt += 1
    ballot_counts.append(cnt)
assert ballot_counts == expected, ballot_counts

tube_checks = 0
for level in levels[1:]:
    for d,J,H,*_ in level:
        if d != 1 or J <= 0 or J % 2:
            continue
        k = v2(J)
        q = J >> k
        words = product((0,1), repeat=k-1) if k <= 8 else [
            (0,)*(k-1), (1,)*(k-1),
            tuple(i&1 for i in range(k-1)),
            tuple((i+1)&1 for i in range(k-1))
        ]
        for w in words:
            jj = J//2
            rr = 0
            for b in w:
                if b:
                    jj = 3*jj//2
                    rr += 1
                else:
                    jj //= 2
            assert jj == 3**rr * q
            assert jj % 2 == 1
            ret = (3*jj+1)//2
            assert ret == (3**(rr+1)*q+1)//2
            tube_checks += 1

seam_checks = 0
for n,J,H,Qx,Qy,r in terminals:
    k = v2(J)
    assert 3*Qx - Qy == 14*3**r + 2**n*(2**k-1)
    B = 18*Qx + 6*2**n - 3**r - 2*Qy
    assert B % 2 == 1
    for e in range(k):
        D = (2**e)*B - 14*3**(r+1)
        vv = v2(D)
        expected_v = 0 if e == 0 else (2 if e == 1 else 1)
        assert vv == expected_v, (n,J,H,k,e,vv,expected_v)
        seam_checks += 1

print("RL289 normalized-pair verifier: PASS")
print(f"max_depth={MAX_DEPTH}")
print(f"canonical_edges_checked={edge_checks}")
print(f"two_shadow_identity_checks={shadow_checks}")
print(f"fixed_seed_cylinder_checks={cylinder_checks}")
print(f"mixed_signed_defect_checks={mixed_checks}")
print("positive_states_with_carry3=0")
print("ballot_bijection_counts_depth1_12=" + ",".join(map(str, ballot_counts)))
print(f"rejected_tube_branch_checks={tube_checks}")
print(f"terminal_occurrences_checked={len(terminals)}")
print(f"cycle_lemma_seam_checks={seam_checks}")
print("signed_defect_absolute_rank_leverage=DEMOTED_GAUGE_ARTIFACT")
print("inherited_H22_certificate=NOT_DUPLICATED")
print("gate_A=NOT_CLAIMED")
