# RL165 — shallow phase-pair non-forcing barrier

Date: 2026-08-28

## Outcome and classification

RL165 proves a precise local-grammar barrier for the proposed nonlocal shallow-arc route. The inherited shallow-population bound and the local `g=1` defect/exponent grammar do not force even one pair of shallow phases separated by the inverse phase step.

**RL165.1 — shallow phase-pair non-forcing theorem** is a finite exact local-grammar certificate. It is not a physical Collatz-cycle construction and does not exclude any cycle.

No frontier changes. The conditional external-floor provenance of the shallow-population number is retained. `g>1`, Gate A, Gate B, nontrivial-cycle exclusion, and Collatz remain open.

## 1. Scope

Use the first coprime survivor

`A=217,976,794,617`, `L=137,528,045,312`,

and its inverse phase step

`p=A^(-1) mod L=65,470,613,321`, `L-p=72,057,431,991`.

Let `c_j=floor(A(j+1)/L)-floor(Aj/L)`. The local grammar inherited from RL133 is `h_0=h_L=0`, `h_j>=0`, and `a_j=c_j+h_j-h_(j+1)>=1`. Let

`N4=3,399,794,205`,

the RL134 lower bound for `#{j:h_j<=4}`, conditional on the inherited external least-state floor.

## 2. RL165.1 — explicit countergrammar

Since `A/L>3/2`, every consecutive pair of mechanical increments contains a `2`: `c_j+c_(j+1)>=floor(2A/L)=3`. Starting at `N4`, take the first five positions `r_1<...<r_5` having `c_(r_i)=2`. Exact arithmetic gives

`(r_1,...,r_5)=(3,399,794,206, 3,399,794,208, 3,399,794,209, 3,399,794,211, 3,399,794,213)`.

For `0<=j<L`, set

`h_j=#{i:r_i<j}`, and set `h_L=0`.

The path rises only five times, each across a `c=2` edge, and then makes one terminal drop from height five to zero. Thus its exponents are positive: `a=1` on a rise, `a=c` away from height changes, and `a=c+5` on the terminal drop. Telescoping gives `sum a_j=A`.

The shallow set is exactly

`S={0,...,r_5}`, with `|S|=3,399,794,214>=N4`.

But `|S|<min(p,L-p)`. Hence `S` and `S+p mod L` are disjoint: the translated interval begins at `p` and neither circular gap can reach back to `S`. No two shallow phases are inverse-phase neighbours.

## 3. Consequence and red teams

This proves that the population statement `#{h<=4}>=N4`, even combined with all local nonnegative-defect and exponent-positivity rules, cannot force the premise required by a two-shallow-inverse-arc argument. Any successful use of two shallow arcs must add a genuinely physical ownership or state-separation theorem.

- **Physical-state red team:** PASS. The certificate is explicitly a local grammar only; it is not called an ordinary cycle.
- **Phase-order red team:** PASS. Disjointness is checked in the actual inverse-phase shift `p`, not chronological adjacency.
- **External-floor scope:** PASS. `N4` is used only as a numerical benchmark and retains its conditional label.
- **Multiplicity:** PASS. The barrier concerns the RL133 `g=1` grammar only.
- **No local-to-global promotion:** PASS. No cycle, frontier, or global theorem is inferred.

`RL165_CERTIFICATES/verify_shallow_phase_nonforcing.py` checks every exact constant, the five permitted rises, exponent positivity at every exceptional edge, and the two phase-gap inequalities without an impractical period scan.

## 4. Next target

Seek an ownership theorem that constrains the phase distribution of shallow states beyond their count and local chronological grammar, or record why such a theorem cannot be obtained from existing physical inputs. Do not retry bare inverse-cylinder, prefix/suffix, or shallow-pair counting arguments.
