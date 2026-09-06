#!/usr/bin/env python3
"""RL268 analytic / finite-cover verifier for determinant-one [2,1,1,1].

Uses only integer arithmetic for determinant-pair and Stern-Brocot decisions.
The only transcendental input is the already-audited RL238 LMN theorem; the
cutoff arithmetic below uses rational enclosures recorded in the closure note.
"""
from fractions import Fraction
from math import gcd, comb
from pathlib import Path
import csv

C = 5 * 3**7
PAIR_CUTOFF = 429
LMN_CUTOFF = 195421


def U4(A):
    return (3*A + 1)//4


def rshort(A,L,m,q):
    return q if m <= A-m else L-q


def B(A,L,m,q):
    r = rshort(A,L,m,q)
    return C * (2**(U4(A)-r)) * (3**r)


def Bcoarse(A):
    r = A//3
    return C * (2**(U4(A)-r)) * (3**r)


def determinant_pairs_to_A(N):
    out=[]
    for A in range(2,N+1):
        twoA=1<<A
        p3=3
        for L in range(1,A):
            if p3>=twoA:
                break
            if gcd(A,L)==1:
                m=(-pow(L,-1,A))%A
                if m:
                    q=(m*L+1)//A
                    if 0<q<L:
                        assert q*A-m*L==1
                        r=rshort(A,L,m,q)
                        assert 0<=r<=A//3
                        out.append((A,L,m,q))
            p3*=3
    return out


def sb_upper_rows(maxA):
    lo=(1,1)
    hi=(2,1)
    rows=[]
    while hi[0] <= maxA:
        n=lo[0]+hi[0]
        d=lo[1]+hi[1]
        if (1<<n) > 3**d:
            hi=(n,d)
            A,L=hi; m,q=lo
            if 0<m<A and 0<q<L:
                assert q*A-m*L==1
                if A <= maxA:
                    rows.append((A,L,m,q))
        else:
            lo=(n,d)
    return rows


def exact_nonbracket_tail_check():
    bad=[A for A in range(9,430) if (1<<A) <= 3*A*Bcoarse(A)]
    assert max(bad)==429
    assert all((1<<A) > 3*A*Bcoarse(A) for A in range(430,442))
    for A in range(21,100):
        assert U4(A+12)==U4(A)+9
        assert (A+12)//3==A//3+4
        assert 128*A > 81*(A+12)
    return max(bad)


def lmn_rational_tail_check():
    def Eup(A):
        U=U4(A); r=A//3
        return (Fraction(10,1)
                + (U-A)*Fraction(693,1000)
                + r*Fraction(406,1000)
                + 22*441*Fraction(694,1000)*Fraction(1099,1000))
    assert Eup(195421) >= 0
    assert all(Eup(A)<0 for A in range(195422,195434))
    for A in range(100,200):
        assert Eup(A+12)-Eup(A)==Fraction(-455,1000)
    return LMN_CUTOFF


def main():
    last_nb=exact_nonbracket_tail_check()
    last_lmn=lmn_rational_tail_check()
    pairs=determinant_pairs_to_A(PAIR_CUTOFF)
    survivors=[p for p in pairs if ((1<<p[0])-3**p[1]) <= B(*p)]
    rows=sb_upper_rows(last_lmn)
    br_survivors=[p for p in rows if ((1<<p[0])-3**p[1]) <= B(*p)]
    expected_br=[(5,3,3,2),(8,5,3,2),(27,17,19,12),(46,29,19,12),(65,41,19,12),(149,94,84,53)]
    assert br_survivors==expected_br
    assert len(pairs)==34931
    assert len(survivors)==967
    assert max(p[0] for p in survivors)==174
    assert len(rows)==35
    assert set(br_survivors) <= set(survivors)
    out=Path(__file__).with_name('rl268_2111_pairs.csv')
    with out.open('w',newline='') as f:
        w=csv.writer(f); w.writerow(['A','L','m','q']); w.writerows(survivors)
    gap_total=sum(4*comb(A-6,3) for A,L,m,q in survivors if A>=9)
    assert gap_total==179403060
    print(f'nonbracketing_last_possible_A={last_nb}')
    print(f'bracketing_LMN_cutoff_A={last_lmn}')
    print(f'determinant_pairs_A_le_429={len(pairs)}')
    print(f'stern_brocot_upper_rows={len(rows)}')
    print(f'bracketing_size_survivors={len(br_survivors)}')
    print(f'finite_size_survivors={len(survivors)}')
    print(f'max_size_survivor_A={max(p[0] for p in survivors)}')
    print(f'gap_configurations={gap_total}')
    print('PASS')

if __name__=='__main__':
    main()
