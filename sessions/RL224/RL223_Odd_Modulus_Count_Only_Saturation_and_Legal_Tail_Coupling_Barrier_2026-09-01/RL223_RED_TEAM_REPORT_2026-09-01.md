# RL223 red-team report

Date: 2026-09-01.

Verdict: **PASS with zero deletions**.

## Required checks

1. **Recurrence check.**  Both set recurrences were derived independently from
   the affine word formula and agree on exact small cases.
2. **Block indexing check.**  A `B0 -> B1` change moves only the last one of a
   block.  Its numerator increment includes exactly the ones in later blocks and
   the fixed filler.  Consecutive increments have ratio
   `2^(2H)3^(-H)=1 mod q`.
3. **Unit check.**  Every claimed modulus is coprime to 6, so Euler's theorem and
   all inverse/unit steps are legal.  Composite examples `25,35,49,55,65,77`
   were replayed explicitly.
4. **Capacity and endpoint check.**  The exact products at `q=283635` and
   `q=283636` were recomputed.  A totient sieve replayed every one of the 94,544
   admissible moduli in the uniform range.
5. **Finite certificate check.**  Independent forward DP covers the complete
   declared interval `5<=q<=1023` with no omitted eligible modulus: 340/340 are
   saturated and the certificate's witness maps replay exactly.
6. **Short falsifier check.**  `S_(2,1)(5)={1,2}` confirms that the proof has a
   real capacity hypothesis rather than an unconditional hidden assumption.
7. **Fixed-start type guard.**  Ordinary parity-cylinder legality varies the
   start with the word.  It was not substituted for continuation from a fixed
   exact `y16`.
8. **Phase-51-prefix type guard.**  The 52 inherited prefix bits were directly
   iterated from `y16` and reach the stated `y51`.  The following switchable
   blocks are explicitly formal; no actual continuation claim is made.
9. **Target check.**  The modulo-5 target equals the formal numerator for one
   block mask, falsifying any claimed empty intersection based only on the exact
   totals, that fixed prefix, and modulo 5.  It is not counted as a physical
   survivor.
10. **Endpoint and affine-lift checks.**  The equivalence
    `Qtail=T mod q <=> y_end=y0 mod q` and the slope
    `T(k+1)-T(k)=3*2^34*D` were replayed exactly modulo representative composite
    and prime moduli.
11. **Inherited-scope check.**  A raw-depth fact about one deterministic witness
    continuation is outside RL223's target and does not contradict the
    conditional physical H21 floor theorem.  It is not promoted.
12. **Global locks.**  Candidate/prefix/rank deletions remain `0/0/0`; physical
    H21 incidence/charge, Gate A, Gate B, branch contradiction, and global
    exclusion remain open.

No inherited mathematical correction/demotion is required.
