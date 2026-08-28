# RL158 session state / RL159 kickoff

RL158 proves an exact method barrier for the RL157 dense resultant. With `(A,L)=(13,8)` and valid excursion `h=(0,0,1,1,0,0,0,0,0)`, one has `D=1631=7*233`, `Res(2T^8-1,P_h)=1631`, but `P_h(rho)=17 mod 1631`. Modulo `7` and `233`, different nontrivial eighth-root twists supply the common roots. Therefore bare resultant divisibility forgets the distinguished physical character.

The surviving exact resource is the joint physical-root system

`2T^L-1 = 0`,
`3T^(A-L)-2 = 0     (mod D)`,

whose binomial resultant has absolute value `D=|2^A-3^L|` and whose simultaneous root is unique modulo each prime divisor of `D` up to the physical root.

## RL159 primary target

Attack the joint distinguished-root ideal rather than the one-binomial resultant.

1. Compute an exact Bezout/Sylvester/Smith-normal-form description of `(2T^L-1, 3T^(A-L)-2)` over `Z`.
2. Determine whether adding the dense primitive `P_h` produces a scalar divisibility/minor condition that is strictly stronger than `D | Res(2T^L-1,P_h)` and still visibly remembers the distinguished root.
3. Red-team any candidate against the RL158 `(13,8)` counterexample and against generic root-of-unity twisting.
4. If the joint invariant reduces algebraically to the original condition `P_h(rho)=0 mod D` with no new size/factor/positivity leverage, freeze that equivalence as a method barrier and pivot to an explicitly different branch resource.
5. Do not revive the demoted `3T^L-2` normalization, sparse phase, `F_1`, individual-level ownership, a small-prime sieve, or the legacy `g=2` one-excursion resultant route.

Verification economy and sustained attack remain in force. No global gate is closed.
