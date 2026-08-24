from fractions import Fraction

# First two near-resonant exponent pairs encountered by the RL41 search.
pairs = [(46,29),(65,41)]
for a,l in pairs:
    x=1<<a; y=3**l
    assert x > y, (a,l,'wrong side of 1')
    assert 15*x*x < 16*y*y, (a,l,'outside sqrt(16/15) window')

m1=(1<<46)-3**29
m2=(1<<65)-3**41
assert m1 == 39409*44110909
assert m2 == 19*29*17021*44835377399
assert 323399 == 19*17021
assert m2 % 323399 == 0

# Single-excursion obstruction through rho<=28.
# For a canonical area-rho excursion, h<=rho+1, hence for rho<=28 D<3^29.
# A one-excursion half-return at the first near resonance would require
# D >= 2^46+3^29, which is already > 3^29.
assert (1<<46)+3**29 > 3**29

# Frozen exact envelopes/counts from the retained area<=25 enumeration.
E = {
1:Fraction(1,4),2:Fraction(16,27),3:Fraction(13,16),4:Fraction(188,135),
5:Fraction(53,32),6:Fraction(560,243),7:Fraction(377,135),8:Fraction(401,128),
9:Fraction(5068,1215),10:Fraction(1321,270),11:Fraction(1369,256),12:Fraction(13552,2187),
13:Fraction(8713,1215),14:Fraction(8929,1080),15:Fraction(9121,1024),16:Fraction(22300,2187),
17:Fraction(28361,2430),18:Fraction(28793,2160),19:Fraction(466832,32805),20:Fraction(59083,4096),
21:Fraction(179297,10935),22:Fraction(181241,9720),23:Fraction(182969,8640),24:Fraction(147604,6561),
25:Fraction(185963,8192),
}
F=[Fraction(0)]*26
for n in range(1,26):
    F[n]=max(E[r]+F[n-r] for r in range(1,n+1))
assert F[25] == Fraction(596977,26244), F[25]
assert F[25] < Fraction(93,4)

# Session-computed area-26 exact envelope values.
# These are arithmetic consistency checks only; the massive enumeration itself
# must be reconstructed/rerun in RL42 for artifact-level certification.
E26=Fraction(112397,4374)
C26=Fraction(3631696,177147)
assert E26 > 0 and C26 > 0 and C26 <= E26

print('PASS RL41 arithmetic checkpoint')
print('near pairs:', pairs)
print('M46,29 =',m1,'=',39409,'*',44110909)
print('M65,41 =',m2,'=',19,'*',29,'*',17021,'*',44835377399)
print('small witness for (65,41):',323399)
print('F(25)=',F[25],float(F[25]),'< 93/4')
print('area26 E=',E26,'C=',C26)
