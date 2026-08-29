# RL171 — residue-rank coordinate barrier

Date: 2026-08-29

## Outcome and classification

RL171 tests whether the inverse-phase arithmetic supplies a rank-position
constraint stronger than the universal rank budget. It proves that, after the
natural residue reparameterization, the apparent relation is exactly a
coordinate formula for the transported height profile. No independent
arithmetic rank constraint results.

New results:

1. **RL171.1 — residue-coordinate rank decomposition** (analytic, coprime
   `g=1` first-survivor defect scope).
2. **RL171.2 — inverse-phase rank-coordinate barrier** (analytic): the
   `p=A^(-1) mod L` phase step is only residue succession plus height lift.

No cycle is constructed or excluded.

## 1. Residue coordinate and exact rank

For a residue `r mod L`, put `j(r)=pr mod L` and transport the height by
`H(r)=h_(j(r))`. Since `Aj(r)=r mod L`, the lifted defect is

`E_(j(r))=r+LH(r)`.                                        (1.1)

The state order of RL168 is the order of these `E` values. Therefore its
rank is exactly

`rank(r)=sum_(t<H(r)) #{s:H(s)=t}`
`        + #{0<=s<r:H(s)=H(r)}`.                            (1.2)

This is simply lexicographic order by height first and residue second.

## 2. The inverse-phase step

The phase map `sigma(j)=j+p mod L` sends `r` to `r+1 mod L`. Subtracting
(1.1) at successive residues gives

`E_sigma-E_j=1-L*1_(r=L-1)+L(H(r+1)-H(r))`.                (2.1)

In chronological notation this is

`E_sigma-E_j=1-L*1_(j=L-p)-Lh_j+Lh_sigma`,

the lifted form already underlying RL163's physical arc theorem. Thus the
new rank expression does not create a recurrence beyond the freely varying
transported height profile `H`.

### Theorem RL171.2

Any proposed rank-versus-inverse-phase arithmetic relation that uses only
`p`, residue succession, and the lifted defect is a restatement of (1.2) and
(2.1). It cannot add a rank-position restriction without a genuinely new
theorem constraining `H` itself.

This is a coordinate barrier, not a claim that every height profile is a
physical cycle or that all future rank-position arguments are impossible.

## 3. Exact audit and red teams

`RL171_CERTIFICATES/verify_residue_rank_decomposition.py` checks the direct
defect lift, exact rank formula, and wrapped inverse-phase difference on 311
bounded coprime positive-defect paths.

- **Phase order:** PASS. `p` is used only as the inverse-phase map, not as a
  chronological neighbor.
- **Physical/quotient:** PASS. This is a defect-coordinate identity; no
  residue class is promoted to a physical state.
- **Scope:** PASS. It remains in the inherited coprime `g=1` branch.
- **No false closure:** PASS. No dense closure congruence or cycle exclusion
  is claimed.

## 4. Next target

Seek a new physical theorem constraining the transported residue-height
profile `H`, rather than another reparameterization of it. Preserve all
ordinary-`+1`, physical-state, external-floor, phase-order, and prior barrier
qualifications.
