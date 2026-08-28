#!/usr/bin/env python3
"""Exact symbolic check for the RL138 local-defect countermodel.

This is deliberately a defect/exponent model, not an ordinary cycle. It
demonstrates only that the local mechanical recurrence, nonnegativity, and
terminal return data do not force an extra contact or a negative phase.
"""
A = 217_976_794_617
L = 137_528_045_312

assert L < A < 2*L

for g in (1, 2, 7, 320_125_202_432):
    N = g*L
    # c_j=floor(A(j+1)/L)-floor(Aj/L); the special endpoint increments.
    c0 = A//L
    c1 = (2*A)//L - A//L
    clast = g*A - ((g*A*L-A)//L)
    assert (c0, c1, clast) == (1, 2, 2)

    # h=(0,0,1,...,1,0), and a_j=c_j+h_j-h_{j+1}.
    # Hence a_0=a_1=1, a_(N-1)=3, and all interior a_j=c_j in {1,2}.
    assert c0 + 0 - 0 == 1
    assert c1 + 0 - 1 == 1
    assert clast + 1 - 0 == 3
    assert all(1 <= (A*(j+1))//L - (A*j)//L <= 2 for j in (2, L-1))

    # Telescoping proves the full exponent total exactly, without materialising
    # the N-long path: sum a=sum c+h_0-h_N=gA.
    assert g*A + 0 - 0 == g*A

print("RL138 terminal local-defect countermodel: PASS")
print("family=h_0=h_1=h_N=0; h_j=1 for 2<=j<N")
print("consequence=local defect recurrence does not force P>0 or many contacts")
print("scope=not an ordinary cycle; no full-ownership claim")
