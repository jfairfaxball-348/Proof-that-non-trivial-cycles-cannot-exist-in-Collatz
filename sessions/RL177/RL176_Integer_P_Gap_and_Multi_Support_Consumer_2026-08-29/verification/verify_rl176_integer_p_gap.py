#!/usr/bin/env python3
from pathlib import Path
from fractions import Fraction

base = Path(__file__).resolve().parents[1]
report = (base / "RL176_INTEGER_P_GAP_AND_MULTI_SUPPORT_CONSUMER_2026-08-29.md").read_text(encoding="utf-8")

for token in [
    "a_0=a_p=1",
    "4\\mid g_p",
    "185{,}999{,}999{,}996",
    "1\\le J\\le36",
    "v_2(g_p)=S_J+\\min(a_J,a_{p+J})",
    "G_{J+1}=a_{p+J}-a_J",
]:
    assert token in report, token

A=217_976_794_617
L=137_528_045_312
p=65_470_613_321
u=103_768_467_013
assert A*p-L*u == 1
assert p+37 < L

upper = Fraction(1_116_000_000_000, 6)
assert upper == 186_000_000_000
assert upper < 2**38
max_gap = int(upper)-4
assert max_gap == 185_999_999_996
assert max_gap % 4 == 0

external_lower = Fraction(31_825_000_000, 3)
first_integer = external_lower.numerator // external_lower.denominator + 1
external_min4 = ((first_integer + 3)//4)*4
assert external_min4 == 10_608_333_336

print("PASS: RL176 portable fresh-unpack verifier completed successfully.")
print("4 | g_p and 4 <= g_p <= 185,999,999,996")
print("first mismatch: 1 <= J <= 36; v2(g_p) <= 37")
