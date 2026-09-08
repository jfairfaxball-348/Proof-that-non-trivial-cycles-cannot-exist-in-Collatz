# RL282 closeout

Date: 2026-09-08

## Authority snapshot

- `BASE_HEAD`: `2ef3fd6b3dcc06756f40497c3951da2fded23cdd`
- incoming authority `START_HERE.md` blob: `639d8a40189a95d96dfca3333bb94fdedb0892b4`
- incoming target blob: `a78482b3ac673f7f6f8944f3239425fc4881e097`
- incoming RL: `RL282`
- successor RL: `RL283`

## Frozen classification

Primary:

`TERMINAL_BACKWARD_HEIGHT_DIGIT_PRICING_AND_LOCAL_TAIL_BARRIER_PROVED`

Subordinate:

- `ONE_ZERO_MOD3_OUTPUT_SHELL_PROVED`
- `ARBITRARY_POSITIVE_BOUNDARY_SUFFIX_AFFINE_COMPRESSION_PROVED`
- `TERMINAL_ONE_ZERO_HEIGHT_DIGIT_PRICING_PROVED`
- `BOUNDARY_INVERSE_RUN_RECURRENCE_PROVED`
- `PURE_ZERO_FINAL_TAIL_LOCAL_REALIZABILITY_FAMILY_PROVED`
- `POSITIVE_TAIL_MASS_AND_F_BARRIER_PROVED`
- `UPSTREAM_CHECKPOINT_REACHABILITY_IDENTIFIED_AS_GATE_A_OBSTRUCTION`

All promoted mathematical items are analytic. Finite verifier runs are regression support only.

No correction or demotion of inherited authoritative mathematics was required.

The large RL282 `H<=26` scratch computation is preserved as **unpromoted evidence** rather than promoted as an exact certificate, because the closeout fast suite does not reproduce that multi-million-state search. This is a proof-state classification boundary, not a retraction of inherited authority.

## Scope

Gate A remains open with exact target

`H_can>=k`

at terminal `d=1,J=2^k`.

The authoritative residual remains

`k>=5`, `k` odd, `H_can<k`.

RL282 does not narrow that residual using its unpromoted height-capped exploration.

The inherited necessary condition

`m0>=8`, equivalently `z>=k+6`

remains valid for any hypothetical Gate-A violator.

Gate B is unchanged/open/frozen. The fifth selector was not scanned. Radius 6+ remains frozen. No global non-trivial-cycle exclusion is claimed.

## Main promoted advances

RL282 establishes:

1. every reachable positive one-zero output lies on the exact shell `nu_3(J)=1`;
2. every legal final positive boundary suffix is compressed exactly to `(L,r,C_w)` by
   `2^(k+L)=3^r J_0+C_w`;
3. for a one-zero shell state,
   `nu_3(2^(k+L)-C_w)=r+1`;
4. the terminal-only height quantity
   `N_w(k)=2^(k+L+1)-2C_w+3^(r+1)`
   satisfies exactly
   `N_w(k)=3^r(2J_0+3)`;
5. therefore a preceding one-zero excursion of height `h` obeys
   `h<=nu_3(N_w(k))-r`, so each additional cheap height unit for a fixed suffix selects one ternary lift of the terminal exponent class;
6. the exact positive-boundary inverse block
   `R_t(A)=2(2^t A/3^t-1)` and its deep/near/full valuation trichotomy;
7. a positive neutral-loop mass barrier showing boundary-zero count cannot be turned directly into height using `S_positive`;
8. an exact infinite local family: for every odd `k>=3` and every `h>=2`, infinitely many locally legal positive blocks
   `J_in --0 1^h--> J_0 --0^q--> 2^k`
   exist with total height `h`;
9. exact local-family scale formulas
   `S_block -> Q_T`
   and
   `F_T-F_in -> 4Q_T`
   as the boundary tail length grows;
10. consequently, final-tail 3-adic thinning plus the inherited positive zero-mass/terminal-scale/`F` ceilings cannot by themselves close Gate A;
11. a local counterexample to blockwise 2-adic monotonicity (`30 -> 24` at height one), isolating upstream global checkpoint reachability as the remaining obstruction.

## Verification

Portable verifier:

`verification/verify_rl282_terminal_backward.py`

Clean execution passes with:

- positive one-zero shell checks: `1666`;
- height-one shell checks: `834`;
- valid boundary affine-tail checks: `7500`;
- terminal shell-tail checks: `29`;
- inverse-block checks: `7494`;
- deep-undershoot checks: `829`;
- near-full checks: `1666`;
- full-consumption checks: `4999`;
- exact pure-zero family `(k,h)` pairs: `114`;
- complete pure-zero terminal-block replays: `114`;
- primitive-root/order regressions through modulus `3^7`;
- positive neutral-loop mass checks: `39`.

The recorded deterministic stdout is frozen in

`verification/RL282_FAST_VERIFIER_OUTPUT.txt`.

Closeout scope/proof-state red team:

`verification/RL282_RED_TEAM.md`

passes with no correction or demotion.

## Transport

Connector-worker closeout uses direct Git-object transport. The committed `sessions/RL282/` tree is the complete lossless handover. `SHA256SUMS.txt` covers every frozen payload except itself. No ZIP or outer `.zip.sha256` sidecar applies.

Candidate reconstruction is performed in clean local temporary storage, the manifest is checked there, and the portable verifier is rerun from that reconstruction before promotion.

## Successor

Prepared successor:

`RL283_UPSTREAM_2ADIC_CHECKPOINT_REACHABILITY_GATE_A_TARGET.md`

RL283 must attack the upstream global positive-checkpoint reachability/state-height obstruction.

The preferred sufficient target is

`nu_2(J)<=H`

for globally reachable positive even `d=1` checkpoints. This is **not** an RL282 theorem.

The stronger observed candidate `J<=2^H` is also unproved.

RL283 should not restart final-tail 3-adic classification, positive zero-count/mass-only arguments, or raw height-cap enumeration as the principal route.

## Catalogue

Generated knowledge catalogues are unchanged and are `stale/deferred` under the connector-worker closeout policy.
