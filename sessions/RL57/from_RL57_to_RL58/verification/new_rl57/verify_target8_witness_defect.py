from fractions import Fraction

PATH = '11011101011101111001001101101101101101101101101001101011110101010110110'

def step(d, J, x):
    odd = J & 1
    if x == 0:
        y = 0 if odd else 1
    else:
        if odd:
            y = 1
        elif d > 1:
            y = 0
        else:
            raise AssertionError('illegal x=1 step at d=1, even J')
    if x == 0 and y == 0:
        return d, (J + 3**d - 2**d)//2, y
    if x == 1 and y == 1:
        return d, (3*J + 2**d - 1)//2, y
    if x == 0 and y == 1:
        return d+1, (3*J + 3**(d+1) - 2**d - 1)//2, y
    return d-1, J//2, y

d, J = 1, -13
i = px = py = 0
xw, yw = [], []
for c in PATH:
    x = int(c)
    if x == 0:
        xw.append(Fraction(2**i, 3**px))
    else:
        px += 1
    d, J, y = step(d, J, x)
    if y == 0:
        yw.append(Fraction(2**i, 3**py))
    else:
        py += 1
    i += 1

assert (i, px, len(xw), len(yw), d, J) == (71, 45, 26, 25, 2, 21)
matched_defect = sum(xw[:25], Fraction()) - sum(yw, Fraction())
pending_weight = xw[25]
min_final_defect = matched_defect + pending_weight/3
assert min_final_defect > Fraction(5,3)

print('matched_defect =', matched_defect, '=', float(matched_defect))
print('pending_weight =', pending_weight, '=', float(pending_weight))
print('minimum_final_defect =', min_final_defect, '=', float(min_final_defect))
print('5/3 =', float(Fraction(5,3)))
print('PASS: target-8 witness is incompatible with E < 5/3')
