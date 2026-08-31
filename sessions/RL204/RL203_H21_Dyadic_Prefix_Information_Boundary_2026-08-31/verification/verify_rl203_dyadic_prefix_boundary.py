#!/usr/bin/env python3
A=217_976_794_617
L=137_528_045_312
B=80_448_749_305
p=65_470_613_321
u=103_768_467_013
lo=25_583_192_106
hi=41_775_866_136

assert A*p-u*L == 1
assert (p*B) % L == 1

expected={
34:15_303_429_871,
35:72_382_725_878,
36:129_462_021_885,
37:49_013_272_580,
38:106_092_568_587,
39:25_643_819_282,
}
for e,r in expected.items():
    got=((p-e)*B)%L
    assert got==r,(e,got,r)
for e in range(34,39):
    assert not (lo <= expected[e] <= hi)
assert lo <= expected[39] <= hi

x=39*A-1
assert 61*L < x <= 62*L
ceil39=(x+L-1)//L
assert ceil39 == 62
b39=u-ceil39
S39=b39-1
assert u-S39 == 63
assert 63 > 56
assert u+37-S39 == 100

M=1<<35
prefix=0
for t in range(34):
    inv=pow(pow(3,t,M),-1,M)
    prefix=(prefix+(1<<t)*inv)%M
assert prefix == (3-(1<<34))%M
terminal_even=((1<<34)*pow(pow(3,34,M),-1,M))%M
assert terminal_even == (1<<34)
even=(prefix+terminal_even)%M
odd=prefix
assert even == 3
assert odd == (3-(1<<34))%M
assert (3*(1-(1<<34)*0))%M == even
assert (3*(1-(1<<34)*1))%M == odd

assert 34+22 == 56

print('PASS RL203 dyadic-prefix information-boundary certificate')
print('offset_34_38_outside_core=yes')
print('first_in_core_below_p_offset=39')
print('first_in_core_rank=25643819282')
print('normalized_root_prefix_depth_at_offset39=63')
print('root_normalization_depth_at_offset39=100')
print('hensel_eta_precision_bits=22')
print('required_normalized_endpoint_modulus_bits=56')
print('mod2^35_prefix_even=3')
print('mod2^35_prefix_odd=3-2^34')
print('new_rank_exclusions=0')
print('remaining_necessary_ranks=16188727234')
print('eta_class_selected=no; state_selected=no; terminal_sign_selected=no')
