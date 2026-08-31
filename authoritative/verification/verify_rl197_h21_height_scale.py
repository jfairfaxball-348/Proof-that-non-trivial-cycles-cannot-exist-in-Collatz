#!/usr/bin/env python3
A=217_976_794_617
L=137_528_045_312
B=A-L
R=L-B
p=65_470_613_321
u0=103_768_467_013
assert A*p-u0*L==1
DLO=23_369_453_298
DHI=41_775_866_136
DELETIONS={
23_369_453_298,23_783_761_791,26_058_127_773,26_058_127_774,
28_746_802_249,28_746_802_250,31_435_476_726,34_124_151_202,
36_398_517_184,36_398_517_185,36_812_825_678,39_087_191_660,
39_087_191_661,41_775_866_136}
assert len(DELETIONS)==14 and DHI in DELETIONS

def off_rank(r,k): return (r-k*B)%L
def bit(r): return 1 if r<R else 2

expected={
36:(15_303_429_870,33_709_842_708,1),
35:(95_752_179_175,114_158_592_013,2),
34:(38_672_883_168,57_079_296_006,1),
33:(119_121_632_473,137_528_045_311,2)}
for k,(lo,hi,c) in expected.items():
    assert off_rank(DLO,k)==lo and off_rank(DHI,k)==hi
    assert hi-lo==DHI-DLO
    assert bit(lo)==c and bit(hi)==c
assert off_rank(DHI,34)==R-1
assert off_rank(DHI,33)==L-1

triples=[]
zero=[]
for e35 in (0,1):
  for e34 in (0,1):
    for e33 in (0,1):
      if 2+e35-e34>=1 and 1+e34-e33>=1:
        triples.append((e35,e34,e33))
        if e34==0 and e33==0: zero.append((e35,e34,e33))
assert triples==[(0,0,0),(0,1,0),(0,1,1),(1,0,0),(1,1,0),(1,1,1)]
assert zero==[(0,0,0),(1,0,0)]

D35=7*(2**35)
D34=3*D35//4
D33=3*D34//2
assert D35==240_518_168_576
assert D34==21*(2**33)==180_388_626_432
assert D33==63*(2**32)==270_582_939_648
for D in (D35,D34,D33):
  for e in (0,1):
    C=(2**e)*D
    assert C//(2**e)==D
    assert (C%3==0)==(D%3==0)
assert D35%3!=0 and D34%3==0 and D33%3==0

print("PASS RL197 exact H21 height-scale selector certificate")
print("H21_local_mechanics=1|212")
print("admissible_height_triples=000,010,011,100,110,111")
print("owned_zero_edge_triples=000,100")
print("selector=tau34_common_height_zero")
print("normalized_gaps",D35,D34,D33)
print("scale_blind_normalization_and_mod3=yes")
