# RL266 mandatory red team

Result: **PASS**

The closeout red team checks the promoted `[3,2]`, `|kappa|=1` leaf from independent directions.

## Structural coverage

- A `[3,2]`, `kappa=+1` flow is cyclically normalized to `+++ 0^r -- 0^s`, `r,s>=1`.
- `qA-mL=1` forces `gcd(m,A)=1`, so the reconstruction equation traverses one complete `m`-cycle.
- The finite certificate enumerates every such `A,m,r,s` for `A<=56`; no word-pattern heuristic is used.

## Numerator indexing / cyclic wrap

For every finite candidate, the verifier independently computes:
1. direct `Q(tau^m x)-Q(x)` using the inherited rank convention;
2. the exact five-edge transport formula.

They agree identically.

## Full D versus proper factors

The finite certificate tests divisibility by the complete integer `D=2^A-3^L`. It records 434 proper-factor-only candidates but counts zero as full-D hits.

## Primitive / nonprimitive

Primitivity is not used to discard candidates. The finite certificate is therefore a strict superset of the written primitive theorem scope. All 7,040 finite candidates happen to be primitive.

## Negative D

The known `A=11,L=7,D=-139` regression is retained as a scope sentinel. The theorem and all infinite inequalities are explicitly positive-domain (`D>1`) statements.

## LMN dependency and denominator correction

The Laurent-Mignotte-Nesterenko specialization is reused only in the exact `Lambda=A log2-L log3>0` setting audited by RL238. No new external transcendence theorem is introduced.

RL238/RL239 repaired the possibility that a reduced continued-fraction denominator may lift to a multiple in unreduced variables. In RL266 determinant one gives `gcd(A,L)=1` and `gcd(m,q)=1`, so the variables used here are already reduced and the permitted multiplier is exactly one.

## Independent implementation

`verification/redteam_rl266_kappa1_32.py` brute-forces all positive-domain binary words through `A<=18` from the earth-mover definition rather than the canonical `[3,2]` parametrization.

It obtains:
- raw `[3,2]` distance-5 instances: 10,382;
- `|kappa|=1`: 4,774;
- `kappa=+1`: 2,387;
- `kappa=-1`: 2,387;
- full-D hits: 0.

This overlaps the canonical certificate and independently validates topology, determinant sign, cyclic orientation and full-D handling.

## Scope conclusion

PASS for the promoted local leaf only. The red team does not certify the other four determinant-one topologies or any `|kappa|=3,5` sector.
