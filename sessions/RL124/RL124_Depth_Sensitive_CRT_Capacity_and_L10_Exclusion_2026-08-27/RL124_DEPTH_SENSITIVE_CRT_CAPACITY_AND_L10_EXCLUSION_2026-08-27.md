# RL124 — depth-sensitive CRT capacity and complete `L=10` exclusion

Date: 2026-08-27

## Outcome and classification

RL124 completes the target inherited from RL123.  It proves the following limited frontier advance:

> Every hypothetical primitive nontrivial positive ordinary shortcut cycle has `L >= 11`.

This is a **mixed result**: the capacity part is an analytic necessary-condition argument using the inherited physical CRT-fibre theorem, followed by an **exact finite certificate** for the explicitly bounded `L=10`, `6 <= Z <= 24` strip.  It is not a Gate A or Gate B closure, a global nontrivial-cycle exclusion, or a proof of Collatz.

No inherited claim was repaired or demoted.

## Incoming authority and notation

RL123 supplies, for a primitive ordinary-owned parity word with `L` ones, `Z` zeroes, `A=L+Z`,

`D=2^A-3^L`, `B=(2^Z-1)(3^L-2^L)`, and `D W <= B`.

For a transition-rooted alternating run profile

`1^(o_1)0^(z_1) ... 1^(o_t)0^(z_t)`,

RL123 additionally supplies the physical lower bounds

`W >= (O_j-1)3^j`, `W >= (Z_k-1)2^k+1`,

and

`W >= (C_(j,k)-1) 3^j2^k`,

where `O_j=sum_i(o_i-j+1)_+`, `Z_k=sum_i(z_i-k+1)_+`, and
`C_(j,k)=#{i:o_i>=j, z_i>=k}`.  The coarse `j=k=1` instance is
`W >= 6(t-1)`.

Thus, with

`P(profile)=max(6(t-1), max_j (O_j-1)3^j, max_k ((Z_k-1)2^k+1), max_(j,k)(C_(j,k)-1)3^j2^k)`,

every primitive ordinary-owned word with that profile must satisfy

`P(profile) <= floor(B/D)`.  This is the analytic capacity discriminator used below.

## RL124.1 — exhaustive depth-sensitive profile capacity

For `L=10` and every `Z=6,...,24`, the verifier enumerates **all ordered positive compositions** of 10 and `Z` into the same run count `t=1,...,min(10,Z)`.  It separately recognizes periodic bit words and applies the physical capacity condition only to primitive profiles, as required by the distinct-state use of the CRT theorem.

The enumerated profile total is `92,560,039`; of these, `4,369` are periodic and `92,555,670` are primitive.  The exact profile table is frozen in `audit/RL124_L10_PROFILE_OWNERSHIP_CERTIFICATE.txt`.

The capacity inequality alone excludes `91,625,515` primitive profiles.  In particular it excludes **all** primitive profiles for `Z=23` and `Z=24`; this is an analytic conclusion conditional only on the inherited ordinary physical-ownership hypotheses, not a raw-word scan.

Classification: **analytic necessary-condition sieve**, exhaustively instantiated over the finite `L=10` strip.

## RL124.2 — compressed exact ownership certificate

The capacity sieve leaves exactly `930,155` primitive ordered transition-rooted profiles.  For each such profile the verifier constructs its binary word and checks all `A=L+Z` cyclic roots using the exact numerator

`Q(w)=sum_{w_p=1}2^p3^(L-1-#{q<p:w_q=1})`.

It makes `24,826,595` exact checks of the necessary ordinary-ownership divisibility condition `D | Q(w)`.  There are zero hits.

Coverage is gap-free: a primitive binary word has at least one `0→1` transition; beginning there produces one of the enumerated ordered positive run profiles.  If its profile violates capacity it is analytically impossible for an ordinary physical cycle.  Otherwise its constructed word is scanned at every cyclic root, including the original word.  Therefore every primitive ordinary candidate in the RL123 residual strip is covered.  Periodic profiles are recorded but are outside the primitive target, exactly as in RL123.

Classification: **exact finite certificate**, restricted to `L=10`, `6 <= Z <= 24`, primitive positive binary words under the inherited ordinary ownership framework.

## Corollary RL124.3

RL123 had already analytically reduced any `L=10` primitive ordinary candidate to `6 <= Z <= 24`.  RL124.1--RL124.2 exclude that whole residual strip.  Hence every hypothetical primitive nontrivial positive ordinary shortcut cycle has `L >= 11`.

This corollary has no broader scope than its inherited framework.  It does not promote a branch-local fact to a Gate closure.

## Red-team and verification status

- RL20 ownership discriminator: the finite test is only the necessary full-`D` divisibility condition; no quotient representative is promoted to a physical state.
- RL79 generalized-increment scaling: untouched; the capacity theorem used is exactly RL123's product-modulus physical statement.
- RL81 physical ownership: `W` bounds are used only conditionally for ordinary-owned physical cycle states.
- Primitivity: periodic profiles are counted separately and never used as primitive exclusions.
- Raw/Farey: no restriction or closure claim.
- Exact finite scope: the certificate is only `L=10`, `6<=Z<=24`; its corollary relies on RL123's separately promoted strip reduction.

`verification/run_fast_rl124_verifiers.sh` compiles the frozen exact verifier, reruns the entire certificate, and requires byte-for-byte reproduction of the frozen audit output.  It passed before packaging and is required to pass from a fresh unpack.

## Open obligations and RL125 kickoff

Gate A and Gate B remain open; global nontrivial-cycle exclusion and Collatz remain unproved.

For `L=11`, positivity begins at `Z=7`.  The inherited zero-fibre bound gives `W>=2Z-1`, and direct exact arithmetic gives

`(2Z-1)(2^(11+Z)-3^11) > (2^Z-1)(3^11-2^11)`

first at `Z=44` (the difference is `54,131,156,443,431,342`); it remains increasing thereafter.  Thus the first RL125 strip is `L=11`, `7 <= Z <= 43`.  Start again with a depth-sensitive capacity sieve; do not raw-scan its word set before profile compression.
