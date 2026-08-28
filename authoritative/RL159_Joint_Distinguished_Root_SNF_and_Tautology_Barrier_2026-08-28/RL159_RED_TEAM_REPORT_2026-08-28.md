# RL159 red-team report

- **Normalization:** only the corrected `B1=2T^L-1` and the correctly derived companion `B2=3T^(A-L)-2` are used. The demoted `3T^L-2` normalization is not revived.
- **Integral vs localized statement:** the main proof is integral. Localization at `6` is only an interpretation; the exact Sylvester lattice already gives `Z^A/row(S) ~= Z/dZ`.
- **Composite modulus:** the exact identity `T-rho_bar in (B1,B2)` forces the distinguished root modulo `d` and every divisor, so uniqueness is not being inferred only prime-by-prime.
- **RL158 counterexample:** `(13,8)`, `d=1631`, `P(rho)=17` gives augmented determinantal divisor `1`, so the earlier false positive is rejected.
- **Generic twist:** any root-of-unity twist preserving both exponents has order dividing `gcd(L,A-L)=1`; no character ambiguity remains.
- **No overclaim:** recovering the correct character is not a singleton exclusion. The augmented invariant is exactly equivalent to `P_h(rho)=0 mod d`.
- **Barrier discipline:** larger equivalent Sylvester/Macaulay/subresultant encodings are not promoted as new routes unless they introduce structure not reducible to the same evaluation quotient.
- **Historical audit:** RL160 may consult old sessions broadly, but verification economy remains in force; old expensive certificates are rerun only when a concrete synthesis depends on them or a contradiction/repair trigger appears.
