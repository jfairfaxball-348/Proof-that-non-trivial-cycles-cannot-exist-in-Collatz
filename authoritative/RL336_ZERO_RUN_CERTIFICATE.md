# RL336 exact zero-run certificate provenance

Scope: ordered genuine `g=2`, `Z0>0`, `K<0` parent with inherited conditional floor `m>=2^71` and high-carry owned-state threshold `M=22689747442693040208618`. Physical starts satisfy `M<=P<U=2^76+2^36` and are odd.

For a zero run of length `z`, the verifier enumerates all `z` distinct mechanical factor words of length `L=z-1` by partitioning phase `0<=r<ell` at `(- (a-ell)j) mod ell` for `0<=j<=L`, sampling each cutpoint and its successor. With gaps `g_1,...,g_L`, set `G_j=sum_{i<=j}g_i`, `C_0=0`, `C_j=2^{g_j}C_{j-1}+3^{j-1}`. Every physical start has the unique residue

`P ≡ C_L*(2^{G_L})^{-1} (mod 3^L)`.

Every reconstructed odd state satisfies `P_j=(2^{G_j}P-C_j)/3^j`. Therefore every state in the owned run is at least M exactly when

`P >= max_{0<=j<=L} ceil((M*3^j+C_j)/2^{G_j})`.

The portable verifier computes this exact threshold for each factor, aligns it to the unique residue and odd parity, and enumerates every start below U in steps of `2*3^L`. No interval, factor, parity class, or endpoint is omitted. It applies deterministic odd Collatz continuation until the source falls below `2^71`, with a fail-closed 1,000-step limit.

Results:

| Zero-run length | Factors | Owned candidates | Maximum escape (odd steps) | Consequence |
|---:|---:|---:|---:|---|
| 37 | 37 | 5,343,788 | 229 | `z<=36` |
| 36 | 36 | 15,512,438 | 234 | `z<=35` |

The zero-run-37 Python verifier covers disjoint factor ranges `[0,12)`, `[12,24)`, `[24,37)`. The zero-run-36 Python verifier covers `[0,12)`, `[12,18)`, `[18,24)`, `[24,30)`, `[30,36)`. Each part asserts its exact per-factor count and maximum. The expected arrays assert the full aggregate; a separate C++ implementation, frozen in `sessions/RL336/scratch/`, agrees factor by factor. The red team independently checks maximum-escape witnesses `63442609230978977492819` and `69267243002915637332507`.

Classification: exact gap-free finite certificates, conditional on the inherited branch, ownership threshold, state band, and external least-state floor. They do not prove an unconditional global cycle bound.
