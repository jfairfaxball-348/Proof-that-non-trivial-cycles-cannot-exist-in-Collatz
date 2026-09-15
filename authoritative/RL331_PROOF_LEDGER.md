# RL331 proof ledger — global phase pairing and support-uniform residue gain

Date: 2026-09-15
Status: FROZEN CANDIDATE FOR RL331 CLOSEOUT
Incoming authoritative HEAD: `5d704826f16916c97e1aa9185b486c4f8a5b8440`

## Scope retained

Work remains in the ordered genuine `g=2`, `Z0>0`, `K<0` late-row parent branch at `(a,ell)=(217976794617,137528045312)`, with `d=80448749305`, `lambda=2^a/3^ell<1+2^-40`, and incoming cap `1<=n<=32551214631`.

RL330's exact total-44 ownership, exact successor supports, 323-state conservative automaton, and potential `2Z<=43K+129` are retained. The external `2^71` least-state floor remains conditional. Gate A, Gate B, R1, and global positive non-trivial-cycle exclusion remain open.

## RL331.1 — exact critical-slack decomposition

For an abstract automaton edge `(s,t,z,k)`, define

`sigma = Phi(t)-Phi(s)-(2z-43k) >= 0`.

The zero-slack subgraph has 288 strongly connected components, exactly 16 cyclic. Every internal edge of a cyclic component represents one positive rank and alternates between a low class `N(z), z<=21`, and its complementary class. Consecutive entries to the low class are exactly 45 ranks apart.

The SCC condensation is acyclic. Along any zero-slack path it contains at most 16 positive ranks outside cyclic components and meets at most 16 cyclic components. These constants are checked over all 26,514 edges.

For a genuine path with `K=K_base+h`, exact slack telescoping gives `S<=45h+s0`, where the rounded endpoint slack satisfies `0<=s0<=44` (and `s0=3` at `rho=60`). There are at most `S` positive-slack edges. Even when the graph's `k=3` edge represents a longer run, every extra positive rank costs 43 further units of true slack, so all positives on defect edges total at most `3S`.

After deleting defect edges there are at most `S+1` zero-slack blocks. Pairing alternate recurrent positives therefore leaves at least

`H >= (K-35S-32)/2`

positive ranks in step-45 phase progressions, split among at most `16(S+1)` segments.

Classification: **proved finite-state global critical-slack decomposition and anchor-count theorem**.

## RL331.2 — uniform step-45 Beatty discrepancy

The residue step of every anchor progression is `45a mod ell = 44464540613`, coprime to `ell`. Its continued-fraction partial quotients are

`[3,10,1,3,13,107,4,1,4,3,1,3,3,2,2,5,2,1,1,3]`,

whose sum is 172.

Apply Denjoy--Koksma to the periodic bounded-variation function `f(x)=2^x`, whose circle variation is 2, then decompose an arbitrary block length by its Ostrowski expansion. Uniformly in starting phase and every block length below `ell`,

`sum f(x+j(45a/ell)) >= m/ln(2)-344`.

The verifier uses an exact rational upper enclosure for `ln(2)`, so the resulting lower bound is wholly rational.

Classification: **proved analytic support-phase theorem with exact continued-fraction certificate**.

## RL331.3 — support-uniform weighted gain

Combine the anchor theorem with unit weight for every other positive rank. Independently, retain RL327's distinct-residue quartic lower bound `W0(K_base)`; if `K=K_base+h`, it increases by at least `h`.

At `rho=60`, the maximum of these two lower envelopes has a global integer minimum at `h=5072`. Thus every admissible support loses at least `W0(K_base)+5072`, not merely `W0(K_base)`. For every rounded density floor occurring from `rho=61` through `rho=1845`, exhaustive exact evaluation of all 45 endpoint-slack classes gives the uniform gain `>=5071`.

This is not a fixed-critical-cycle or catalogue claim: defect edges, arbitrary phase resets, long `k>=3` runs, transient zero-slack paths, every actual `h>=0`, and every starting phase are included.

Classification: **proved support-uniform residue-weighted strengthening**.

## RL331.4 — self-consistent all-rho contraction

At `rho=60`, subtracting the certified gain gives `n < 32551214208.93585...`.

At `rho=61`, the uniform 5071 gain already gives `n<32551214208.70768...`; inherited monotonicity then covers through `rho=1845`. At `rho=1846`, the ordinary inherited residue bound is already `n<32551214208.73916...`, and its monotonicity covers every larger `rho`. The companion inequality covers `rho<=59`.

Rerunning the complete total-44, large-singleton, two-positive, exact-link, owned-successor, and graph reconstruction at the lower bootstrap `n>=32551214209` changes none of RL330's counts, supports, links, or potential constants. Hence the bootstrap is self-consistent and

`n<=32551214208`.

The authoritative carry cap improves by exactly 423.

Classification: **proved self-consistent all-rho carry contraction from a global phase/support theorem**.

## Verification and remaining obstruction

Portable verifier: `verification/verify_rl331_global_phase_pairing.py` (with separately runnable reconstruction dependency `verify_rl331_self_consistent_ownership.py`).

Independent reconstruction/red team: `verification/red_team_rl331_global_phase_pairing.py`.

The phase-reset obstruction is no longer absolute: a uniform positive gain survives every slack/phase pattern. Present constants are deliberately conservative, especially the charge of up to 16 Denjoy--Koksma segments per zero-slack block. The gain contracts but does not close the parent branch.

`PARENT_DIFFICULTY_DELTA = EASIER`.
