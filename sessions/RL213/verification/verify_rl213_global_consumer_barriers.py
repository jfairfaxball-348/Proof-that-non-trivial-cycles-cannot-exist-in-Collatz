#!/usr/bin/env python3
import hashlib
import json
from collections import defaultdict
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
A = 217_976_794_617
L = 137_528_045_312
p = 65_470_613_321
u = 103_768_467_013
K0 = 1 << 37

def b(i):
    return A * i // L

# Exact e=16 mechanical data used by the analytic collapse theorem.
assert A * p == u * L + 1
assert b(p) == u
assert b(16) == 25
assert b(p + 16) == u + 25
assert p + 16 < L - p  # the inherited no-carry p-shift regime

# Regression of the endpoint-moment cancellation on exact rational fixtures.
# The theorem itself is analytic; this verifies that after the substitutions
# P_a=P_p+P_e/alpha, rho_a=rho_e/alpha, local p-gap, and both z telescopes,
# its residual is exactly the root 0->p telescope residual.
from fractions import Fraction
for alpha in (Fraction(5, 4), Fraction(7, 5), Fraction(11, 8)):
    for rho in (Fraction(3, 5), Fraction(7, 9)):
        for y0 in (2, 5, 17):
            yp = Fraction(y0) + K0
            Pp = 3 * (yp / alpha - y0)
            for xe in (Fraction(9, 2), Fraction(17, 3)):
                Pe = 3 * (rho * xe - y0)
                xa = xe + Fraction(K0, 1) / rho
                Pa = Pp + Pe / alpha
                rhoa = rho / alpha
                lhs = 3 * (alpha - 1) * rhoa * xa
                rhs = 3 * K0 - alpha * Pp + (alpha - 1) * Pa
                assert lhs == rhs
                root_residual = alpha * Pp - 3 * (K0 - (alpha - 1) * y0)
                assert root_residual == 0

# RL210 G56 first-divergence continuation.
# Factor the congruence by 2^37. Modulus becomes 2^19 and target -3.
MOD = 1 << 19
FULL_MOD = 1 << 56
TARGET = (-3) % MOD
COEFF = [pow(pow(3, t, MOD), -1, MOD) for t in range(56)]
FULL_COEFF = [pow(pow(3, t, FULL_MOD), -1, FULL_MOD) for t in range(56)]

def term(s, t):
    if s >= 56:
        return 0
    return ((1 << (s - 37)) * COEFF[t]) % MOD

def next_candidates(s, t):
    bt = b(t)
    lo = s + 1
    if lo > bt:
        return ()
    if lo >= 56:
        # All later G56 terms vanish. The least legal exponent dominates all
        # larger choices because it leaves at least as much room for continuation.
        return (lo,)
    hi = min(bt, 55)
    vals = list(range(lo, hi + 1))
    if bt >= 56:
        # Every exponent >=56 contributes zero; 56 dominates larger choices.
        vals.append(56)
    return tuple(vals)

def find_witness(m, root_start, p_start):
    r0 = (term(p_start, m) - term(root_start, m)) % MOD

    @lru_cache(None)
    def dfs(t, sr, sp, residue):
        if t == 55:
            return () if residue == TARGET else None

        # Future root and p-shift exponents are at least sr+1 and sp+1.
        # Hence every future contribution is divisible by 2^k. If the already
        # frozen low k bits disagree with the target, no continuation exists.
        k = min(19, min(sr, sp) + 1 - 37)
        if k > 0 and (residue - TARGET) % (1 << k):
            return None

        nt = t + 1
        for nr in next_candidates(sr, nt):
            rt = term(nr, nt)
            for np in next_candidates(sp, nt):
                nrz = (residue + term(np, nt) - rt) % MOD
                tail = dfs(nt, nr, np, nrz)
                if tail is not None:
                    return ((nr, np),) + tail
        return None

    tail = dfs(m, root_start, p_start, r0)
    if tail is None:
        return None
    return ((root_start, p_start),) + tail

def validate_witness(m, k, orientation, witness):
    root_start, p_start = ((37, k) if orientation == "root_smaller" else (k, 37))
    assert witness[0] == (root_start, p_start)
    assert len(witness) == 56 - m

    # A common pre-mismatch prefix S_t=S'_t=t is a legal abstract prefix.
    root = list(range(m)) + [x[0] for x in witness]
    prime = list(range(m)) + [x[1] for x in witness]
    assert len(root) == len(prime) == 56
    assert root[0] == prime[0] == 0
    assert root[1] == prime[1] == 1
    for t in range(56):
        assert root[t] <= b(t) and prime[t] <= b(t)
        if t:
            assert root[t] > root[t - 1]
            assert prime[t] > prime[t - 1]
    assert root[:m] == prime[:m]
    assert root[m] != prime[m]
    assert min(root[m], prime[m]) == 37

    total = 0
    for t in range(56):
        total = (total + ((1 << root[t]) * 0)) % FULL_MOD if False else total
        total = (total + ((pow(2, prime[t], FULL_MOD) - pow(2, root[t], FULL_MOD)) * FULL_COEFF[t])) % FULL_MOD
    assert total == (-3 * (1 << 37)) % FULL_MOD
    return root, prime

cases = []
witness_payload = []
by_m = defaultdict(lambda: {"feasible": 0, "total": 0})
for m in range(24, 38):
    for k in range(38, b(m) + 1):
        for orientation in ("root_smaller", "prime_smaller"):
            by_m[m]["total"] += 1
            rs, ps = ((37, k) if orientation == "root_smaller" else (k, 37))
            witness = find_witness(m, rs, ps)
            feasible = witness is not None
            if feasible:
                by_m[m]["feasible"] += 1
                root, prime = validate_witness(m, k, orientation, witness)
                witness_payload.append({
                    "m": m,
                    "k": k,
                    "orientation": orientation,
                    "root": root[m:],
                    "prime": prime[m:],
                })
            cases.append((m, k, orientation, feasible))

assert len(cases) == 304
infeasible = [(m, k, o) for m, k, o, ok in cases if not ok]
assert infeasible == [(24, 38, "root_smaller")]
assert sum(1 for *_, ok in cases if ok) == 303
expected_by_m = {
    24: (1, 2), 25: (4, 4), 26: (8, 8), 27: (10, 10),
    28: (14, 14), 29: (16, 16), 30: (20, 20), 31: (24, 24),
    32: (26, 26), 33: (30, 30), 34: (32, 32), 35: (36, 36),
    36: (40, 40), 37: (42, 42),
}
assert {m: (v["feasible"], v["total"]) for m, v in by_m.items()} == expected_by_m

witness_blob = json.dumps(witness_payload, sort_keys=True, separators=(",", ":")).encode()
witness_digest = hashlib.sha256(witness_blob).hexdigest()

out = {
    "status": "PASS",
    "endpoint_moment_e16_collapses_to_root_telescope": True,
    "g56_first_divergence_start_cases": 304,
    "g56_inherited_m24_excluded_cases": 1,
    "g56_feasible_start_cases": 303,
    "g56_only_infeasible_case": {
        "m": 24,
        "larger_exponent": 38,
        "orientation": "root_smaller",
    },
    "g56_feasible_by_m": {str(m): by_m[m]["feasible"] for m in range(24, 38)},
    "g56_total_by_m": {str(m): by_m[m]["total"] for m in range(24, 38)},
    "witness_digest_sha256": witness_digest,
    "new_rank_exclusions": 0,
    "frontier": 13_415_865_871,
}
(ROOT / "certificates/verify_rl213_global_consumer_barriers_output.json").write_text(
    json.dumps(out, indent=2, sort_keys=True) + "\n"
)
print("PASS RL213 endpoint-moment collapse regression and exact G56 saturation")
print("endpoint_moment=e16_collapses_to_root_telescope")
print("g56_start_cases=304 feasible=303 only_infeasible=m24_root_smaller")
print(f"witness_digest={witness_digest}")
print("rank_deletions=0 frontier=13415865871")
