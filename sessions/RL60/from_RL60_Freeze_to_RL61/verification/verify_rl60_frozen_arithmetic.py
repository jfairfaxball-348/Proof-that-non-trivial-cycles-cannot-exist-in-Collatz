#!/usr/bin/env python3
q = 45_446_975_257_190_057_863
assert q + 3 == 45_446_975_257_190_057_866
rows = {
    25: (11_184_810, 9_457_747),
    27: (13_256_071, 11_209_181),
    29: (125_687_199, 106_279_619),
    31: (715_827_882, 605_295_637),
    33: (1_908_874_353, 1_614_121_697),
    35: (10_180_663_219, 8_608_649_047),
    37: (45_812_984_490, 38_738_920_711),
    39: (122_167_958_641, 103_303_788_559),
}
def next_odd(n): return n if n & 1 else n + 1
for K, (N, z_expected) in rows.items():
    J = 2*N + 1
    amin = (115*J)//272 + 1
    z = next_odd(amin + 1)
    assert z == z_expected, (K,N,J,amin,z,z_expected)
Ks = list(range(25,130,2))
assert len(Ks)==53 and Ks[0]==25 and Ks[-1]==129
ts=[K-3 for K in Ks]
assert ts[0]==22 and ts[-1]==126 and all(t%2==0 for t in ts)
z_min=q+3-129; z_max=q+3-25
assert z_min==45_446_975_257_190_057_737
assert z_max==45_446_975_257_190_057_841
print('RL60 frozen arithmetic: PASS')
print('q+3 =', q+3)
print('K39-derived internal z floor =', rows[39][1])
print('audit-pending external K interval: 25..129 odd (53 exponents)')
print('corresponding z interval:', z_min, '..', z_max)
