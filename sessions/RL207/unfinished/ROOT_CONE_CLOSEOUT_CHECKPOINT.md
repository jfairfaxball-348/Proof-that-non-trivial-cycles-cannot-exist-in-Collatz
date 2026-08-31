# RL207 root-cone subtask — closeout checkpoint

Status: **UNFINISHED — NOT PROMOTED**.
Recorded only for CLOSEOUT_LOCK after the user requested RL207 be the last session.
This checkpoint records work already present before interruption; it adds no new
derivation, verification, rank deletion, or proposed theorem promotion.

## Artifact and verification state at interruption

- No `ROOT_CONE_EXTENSION_PROOF.md` had been written.
- No RL207 verifier, endpoint arithmetic output, rank-boundary search, or rank count
  had been produced by this subtask.
- The incoming corrected H21 interface, target, RL202 root-anchor source, and
  RL206-C2 source/terminal repair had been read.
- Elementary endpoint/path arguments had been completed in working reasoning and
  communicated to the root. They had not been frozen as a complete proof artifact
  or independently reviewed. The broader requested interval/layer consumption
  proof remained unwritten and unfinished.

## Pre-interruption endpoint observations already sent to root

Using only the inherited noncarry speed bound, the unique carry source
`z=L-p=72057431991`, and the lifted endpoint gap
`epsilon=K_L-K_0 in (0,1)`, the recorded observations were:

1. The carry edge is `z -> z+1`. The forward path from phase 0 is carry-free exactly
   through canonical phase `z`. For `1<=i<=z`, the working bound was
   `|K_i-K_0|<i/3`; phase `i=0` has equality `K_i=K_0` and must be treated separately.
2. The backward path from lifted phase `L` is carry-free down through phase `z+1`.
   For `z+1<=i<L`, the working interval was
   `K_i in K_0+(epsilon-(L-i)/3, epsilon+(L-i)/3)`, hence the common enclosure
   `K_i in K_0+(-(L-i)/3, 1+(L-i)/3)`.
3. For half-open windows `[0,N)` and `[L-N,L)`, equivalently inclusive integer
   windows `[0,N-1]` and `[L-N,L-1]`, the assigned paths remain carry-free when
   `1<=N<=min(z+1,L-z-1)=65470613320`. These were path-range observations, not a
   claim that no different argument could bound any larger window.
4. A separate working note distinguished a maximal forward path domain from the
   validity domain of its weaker numerical inequality: the actual constants place
   `z` beyond `L/2`, so a backward estimate may also imply a weaker bound expressed
   with `i/3` after the carry. This note was not made into a selected theorem or
   independently verified certificate.

The elementary path argument was locally complete, but **no complete, reviewed
extension theorem or finite certificate existed**. These notes remain unpromoted.

## Unfinished interval/layer work

The intended consumption had to use terminal phase `i=I(r)=pr mod L` and the
inherited strictly decreasing terminal law `K_H21(r)`, never the tau34 source rank.
The source would instead be `i-34 mod L`.

Before interruption, the working plan noted that larger common radii produce
weaker rank bands. Existing smaller-window exclusions therefore cannot simply be
replaced by a larger-window cut. New cuts would need disjoint layer accounting or
explicit subtraction from the already surviving predicate. This accounting was
not completed, and no layer partition, sign-certified rank band, exact count,
independent review, or resulting rank deletion was delivered by this subtask.

The uncompleted coverage is the requested complete interval/layer rank-band
consumption theorem and its verification. Nothing here changes necessary ranks,
eta classes, physical H21 occurrence/charge, either Gate, or global cycle exclusion.
