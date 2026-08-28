# RL138 — terminal local-defect barrier

RL138 tests whether the RL136 terminal nonnegative strip plus the terminal
defect recurrence can force a negative excursion, many zero-level contacts,
or a global dispersion input. It cannot.

For every `g>=1`, let `N=gL`, let
`c_j=floor(A(j+1)/L)-floor(Aj/L)`, and define

`h_0=h_1=h_N=0`, and `h_j=1` for `2<=j<N`.

Set `a_j=c_j+h_j-h_(j+1)`. Since `L<A<2L`, every `c_j` is 1 or 2. Moreover
`c_0=1`, `c_1=2`, and `c_(N-1)=2`; hence

`a_0=a_1=1`, `a_(N-1)=3`, and every other `a_j` is 1 or 2.

Thus this exact full-count exponent/defect model has `sum a_j=gA`, no
negative phase, only the forced initial contact and the final return, and the
same terminal identity `a_(N-1)=h_(N-1)+2`. It satisfies the local inputs
without yielding the requested occurrence or dispersion conclusion.

This is a **method barrier**, not an ordinary-cycle counterexample: no affine
cycle closure or full `D|Q` ownership is asserted. It therefore preserves
RL20/RL79/RL81 and says precisely that an RL139 theorem must use a genuinely
global ordinary-owned input beyond the local defect recurrence.

No multiplicity/frontier is excluded. Gate A/B, global cycle exclusion, and
Collatz remain open.
