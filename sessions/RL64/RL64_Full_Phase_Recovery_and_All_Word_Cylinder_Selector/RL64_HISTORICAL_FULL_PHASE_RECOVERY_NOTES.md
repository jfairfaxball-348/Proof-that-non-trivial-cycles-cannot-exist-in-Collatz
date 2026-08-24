# RL64 — historical full-phase recovery notes

Date: 2026-08-24

## Purpose

RL63 explicitly required recovery of the exact historical full-phase/macro-entry provenance before any ownership-sensitive theorem was promoted. This session used the connected GitHub archive as supporting provenance and recovered exact source bytes from the archived RL47->RL48 and RL48->RL49 bundles.

The current RL63 handover remained the authoritative incoming mathematical state throughout.

---

## 1. GitHub archive provenance

Repository:

`jfairfaxball-348/Proof-that-non-trivial-cycles-cannot-exist-in-Collatz`

Historical bundles used:

- `Archive/Collatz_Rsharp_RL47_to_RL48_Handover_2026-08-22.zip`
  - Git blob SHA observed through the connector: `59c068dcf6c21c36315113d2cc0764bbb295ef0e`
  - archived sidecar SHA-256: `fa164c65c0910fc25ee5724328b2ea15914204049f15e0a00b2781a8ffc979e9`
- `Archive/Collatz_Rsharp_RL48_to_RL49_Handover_2026-08-22.zip`
  - Git blob SHA observed through the connector: `158f3ac051c0bfe964929d7d9051ec63d46b066a`
  - archived sidecar SHA-256: `053548eb5f09566d7772389322e3b59a66531ea3a5c5b98aad3ed51d5baa2572`

Exact sidecar texts are included under `historical/`.

The connector exposes binary repository files as encoded content rather than a directly mounted raw ZIP. The two exact internal source files used in RL64 were decoded from those archived ZIP representations and independently checked against their ZIP local-entry metadata/CRC during recovery. RL64 does **not** claim that the historical outer ZIP hashes were recomputed from a fresh local raw download in this session. That limitation is provenance bookkeeping only; it does not affect the checksum-clean authoritative incoming RL63 bundle, and the exact source files used here are frozen in RL64 for future audit.

---

## 2. Exact recovered RL47 phase source

Frozen file:

`historical/RL47_verify_rl47_phase_coordinate.py`

Historical internal path:

`Collatz_Rsharp_RL47_to_RL48_Handover_2026-08-22/rl47_additions/verify_rl47_phase_coordinate.py`

The script defines exactly

`Phi(d,T,n,pa) = 2^n (T+3^d-1)/3^(pa+d)`.

For an edge `(x,y)`, it verifies the exact telescope

`Phi' - Phi = (2^n/3^pa) * ((1-x) - (1-y)/3^d)`.

It also verifies on the inherited exact `(a,ell,t)=(65,41,2)` witness that every `11` edge has `Delta Phi=0` and that the terminal value is

`9*zeta*(1+2^-(t+3))`.

This source is the exact historical basis for RL64's phase-coordinate translation. RL64 uses `(i,p)` rather than the script's `(n,pa)` when a local synchronized-block length is also denoted by `n`.

At `d=1`, frozen RL45 gives `J=T+1`, hence

`Phi = 2^i(J+1)/3^(p+1)`.

No guessed phase definition is used.

---

## 3. Exact recovered RL48 full-phase source

Frozen file:

`historical/RL48_FULL_PHASE_FOUR_SWAP_BRIDGE.md`

Historical internal path:

`RL48_continued/RL48_FULL_PHASE_FOUR_SWAP_BRIDGE.md`

Key exact statements recovered from this source are:

- full half-words are
  - `u=110 x 1 0^t`,
  - `v=111 y 0^(t+1)`;
- the RL47 internal pair word starts after the mandatory local `(0,1)` column and omits the terminal `(1,0)` column;
- with `X=2^a`, `Y=3^ell`, `M=X-Y`, and the standard binary-word `Q`, the full phase condition is `M | V+4Y`;
- when that condition holds, `N=(V+4Y)/M>0` and
  - `F_u(N)=N+4`,
  - `F_v(N+4)=N`;
- the binary-word congruence selects actual integer Collatz parity trajectories, not merely rational affine maps;
- along the internal pair columns,
  - `T_i=3^(d_i)A_i-B_i`,
  - start `T_0=-14`,
  - terminal `T=2^(t+3)-1` before the omitted terminal `(1,0)`;
- therefore at terminal `d=1`, the frozen RL45 `J=T+1` gives exactly `J_terminal=2^(t+3)`.

These statements are used in RL64's terminal-ownership collapse.

---

## 4. What “ownership” means in RL64

The exact recovered RL47 phase verifier and RL48 full-phase bridge do **not** present a separately named historical Boolean function called an “ownership predicate”. RL63 used “ownership” as shorthand for the restriction that a local quotient state/prefix must come from, and be completable inside, the genuine full-phase word geometry rather than from the unrestricted local Markov quotient.

To avoid inventing a historical definition, RL64 does **not** promote a new inherited predicate under that name. Instead it uses two exact recovered constraints:

1. **historical phase ownership data:** the exact `Phi` coordinate/telescope at the macro entry;
2. **terminal/full-word extendability data:** the exact RL48 full-word conventions and canonical terminal value `J=2^(t+3)`.

For future work, if a compact predicate is convenient it should be introduced explicitly as a **new definition**, e.g. “full-phase extendable prefix”, with its existential word-completion hypotheses written out. It must not be cited as though RL47/RL48 had already named or proved an independent ownership theorem.

---

## 5. Exact full-phase extendability data available for a new definition

A future formal definition can be based on the recovered RL48 source. The ambient one-excursion data include integers `(a,ell,t)`, `k=t+3`, internal pair words `(x,y)`, and full words

`u=110 x 1 0^t`, `v=111 y 0^(t+1)`.

The internal RL path begins after the mandatory `(0,1)` and ends before the omitted `(1,0)`, with the exact RL recurrence, legal positive height, start `T=-14`, and terminal `T=2^k-1`. The full phase condition is the exact divisibility `M | V+4Y` in the notation of the recovered source. Any prefix-level “ownership” theorem must be proved from these exact existential completion requirements (plus whatever inherited phase/rank/zero-position hypotheses are explicitly needed), not from local `(d,H,J)` reachability alone.

---

## 6. Provenance conclusion

RL63's historical-source obligation is repaired far enough to establish the exact phase coordinate and exact full-word/terminal conventions needed for a rigorous next attack. What is **not** yet recovered into a single formal object is a historical named macro-entry ownership predicate, because the exact sources inspected do not define one under that name.

This is not a foundational failure and does not invalidate RL63. It is a terminology/provenance clarification: the next proof should speak in terms of exact full-phase extendability conditions unless and until an older source containing a separately named predicate is located.
