# RL104 — prime-prefix content barrier

RL104 tested the direct prime-local continuation requested after RL103.  It
does not prove a multiplicity bridge, any Gate closure, nontrivial-cycle
exclusion, or Collatz.

## Exact barriers

Let `D=2^A-3^L` and let an inverse prefix have `o` odd steps.  Since `D` is
odd and `D==2^A (mod 3)`,

`gcd(D,2*3^o)=1`.

Thus the maximum-cylinder residue modulo `2*3^o` and any residue modulo `D`
are independently realizable by CRT.  No direct compatibility obstruction
exists without another inequality, ordering, or sparse-prefix input.

For a forward prefix `a` of length `m` and weight `p`, rotation transport is

`2^m Q(rot_m W)-3^pQ(W)=D Q(a)`.

Under ordinary ownership, write `Q(W)=DM` and
`Q(rot_mW)=DX`.  Exact division by `D` gives

`2^mX-3^pM=Q(a)`,

which is only the physical affine prefix equation.  Therefore every proposed
prime-local consequence obtained solely from this sparse-prefix transport
loses the full denominator before any prime factor can constrain it.

RL79 already proves that full return monodromy is the identity modulo every
divisor of `D`.  Together, these facts freeze the direct prime/order,
cylinder-residue, and transport-derived sparse-prefix variants.

Classification: **analytic route barrier**.

## Red team

- The result retains actual owned integer states while dividing exactly; no
  normalized state is used as a physical bound.
- It does not claim that no future non-modular sparse-prefix theorem exists;
  it freezes only the listed direct architectures.
- It uses no external minimum floor and makes no reduced-slope/raw-pair
  identification.
- Generalized-cycle scaling remains a negative control: the surviving
  physical prefix equation is not an `s=1`-specific prime consumer.

## Verification

- `verify_denominator_cylinder_crt.py`: 890,997 exact CRT residue-pair checks.
- `verify_owned_transport_division.py`: 72 exact small owned word/split
  checks.

## Stopping decision

The current first-Farey ownership path has exhausted the direct numerator,
inverse-cylinder, geometry-only, and prime-prefix consumers named in RL102--
RL104.  The remaining required step is a genuinely new non-homogeneous
ordinary-Collatz theorem (for example an actual basin-membership bridge), not
another rearrangement of present identities.  Bulk scans remain deferred.
