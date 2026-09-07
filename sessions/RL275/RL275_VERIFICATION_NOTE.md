# RL275 verification note

Date: 2026-09-07

Portable verifier:

`verification/verify_rl275_owned_determinant_telescope.py`

The verifier uses exact integer arithmetic only.

It checks:

1. the determinant-2 arithmetic family `a=16n+4`, `ell=10n+3`, `q=8n-2`, `r=5n-1` for `5<=n<=300`, including the exact clustered-word common-mode counterflow formula;
2. a fixed full-word-shape finite stress family with `u=110x100`, `v=111x000`, `x=y`, `H_can=0` at the rank/word level, for `5<=n<=300`;
3. the exact inherited derivative `Q-P=h-h_shift`;
4. the RL274 `(c,d)=(7,19)` determinant/window identity on both halfwords for `5<=n<=40`;
5. the new paired determinant telescope and its equality with the direct height endpoint telescope.

Independent exact replay during the RL275 session produced:

- clustered formula checks: 296;
- fixed-form stress checks: 296;
- derivative checks: 13,104;
- determinant identity checks: 26,208;
- paired telescope checks: 13,104;
- status: PASS.

Scope: these checks audit the algebra and finite stress families. They do not prove Gate A. The stress families are not asserted to satisfy the absolute canonical `J` recurrence, full-phase quotient, or full-`D` ownership.
