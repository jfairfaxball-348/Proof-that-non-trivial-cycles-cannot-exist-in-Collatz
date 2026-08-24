# RL61 branch and dependency ledger

This ledger records the reconstructed logical tree as of the RL61 audit. “Closed” means closed **within the hypotheses of the bundled RL architecture**, not a claim that the Collatz conjecture has been solved.

## Status vocabulary

- **Analytic theorem:** symbolic proof in the project, possibly with named external theorems.
- **Exact finite certificate:** exhaustive bounded computation with exact integer arithmetic, replayed or inherited with verification.
- **External computational certificate:** exact consequence of an externally supplied verified dataset whose completeness is not reproved inside this bundle.
- **Open:** theorem target not established.
- **Dead route:** a particular proposed implication/method has been disproved or shown insufficient; the underlying target can remain open.
- **Stress regime:** a restricted subfamily used to test/attack a global theorem; not exhaustive.

## Top-level dependency graph

```text
Inherited RL reductions
       |
       +--> exact radius-3 local case tree ---------------------- CLOSED (RL19)
       |
       +--> retained one-excursion/full-phase RL regime
                 |
                 +--> Gate A: H >= t+3 uniformly --------------- OPEN
                 |       |
                 |       +--> q-specific finite work ----------- local certificates
                 |       +--> safe-CF regime ------------------- restricted subtree
                 |                 |
                 |                 +--> fixed convergent
                 |                       |
                 |                       +--> RL59/RL60 tail
                 |                       +--> K thresholds
                 |                       +--> external K<=129
                 |                       +--> survivor ---------- OPEN
                 |
                 +--> Gate B: global bridge / contradiction ---- OPEN
                         |
                         +--> local endpoint grammar ------------ DEAD route (RL20)
                         +--> RL48 half-period radius-3 match --- DEAD route (RL49)
                         +--> balanced-return weighted diff ----- OPEN route
                         +--> strict-excursion packing ---------- OPEN route
                         +--> new ownership/full-phase bridge --- OPEN target
```

A sufficiently strong universal full-phase impossibility theorem could collapse both open obligations at once; none is currently available.

## Detailed branch ledger

| ID | Branch / object | Exact hypotheses or input | Exact target | Status | Dependencies | Exhaustive? | What closes if discharged? |
|---|---|---|---|---|---|---|---|
| R3.0 | Exact radius-3 theorem | Primitive `D`-divisible self-rotations in historical RL7–RL19 case tree, exact cyclic adjacent-transposition distance 3 | Exclude every admissible radius-3 configuration | **Closed local theorem** | RL7–RL19 reductions; some old leaves use LMN + finite checking | Exhaustive only for exact radius-3 hypotheses | Any global argument that produces such a pair gets an immediate contradiction |
| R3.1 | Final cubic skew leaf | `gcd(A,L)=3`, `gcd(A,m)=1`; `A=3a`, `L=3ell`, `ap-mell=1`; sparse full-`D` cubic zero | Exclude primitive skew/equal-gap possibilities | **Analytic theorem (RL19)** | Eisenstein norm/resultant/integer inequalities; no LMN for this leaf | Exhaustive for this last leaf | Completed the radius-3 local case tree |
| R3.old | Older radius-3 leaves | Mixed/coprime/gcd/boundary sectors in RL7–RL18 | Exclude each leaf | **Closed; analytic + exact finite** | Explicit Laurent–Mignotte–Nesterenko dependency in relevant branches | Exhaustive inside radius-3 tree | Already consumed by R3.0 |
| B.local | Local endpoint/final-return grammar bridge | Endpoint grammar without full genuine RL divisibility | Force some pair at radius <=3 | **Dead route (RL20)** | Exact radius-4-packed countermodel | No | Nothing global; tells us required bridge must use stronger hypotheses |
| B.half | RL48 four-swap/half-period bridge | Full-phase four-swap relation for `d=uv`, half rotation `vu` | Invoke exact radius 3 directly | **Dead route (RL49)** | Exact distance identity `2(a-t-3+H)` | No | Nothing; geometry is always even |
| B.wd | Balanced-return weighted-difference | Genuine RL global phase/ownership; a balanced return/cut | Derive contradiction from weighted difference / force closed local geometry | **Open research route** | RL19/RL20 global identities | No proof of exhaustiveness by itself | Potentially Gate B if made uniform |
| B.pack | Strict-excursion packing | Genuine RL strict excursion plus global ownership/divisibility | Derive global packing contradiction | **Open research route** | RL19/RL20 population/packing identities | No proof yet | Potentially Gate B if made uniform |
| B.new | Ownership/full-denominator radius-3 bridge | Genuine RL object including `D|Q` / full phase, primitive ownership, support/orientation/gcd control | Produce a pair satisfying *all* exact radius-3 hypotheses, or direct contradiction | **Open theorem target** | Radius-3 theorem + full-phase structure | Must become exhaustive to close Gate B | Gate B |
| A.0 | One-excursion terminal reduction | Retained full-phase one-excursion geometry | `q=z+t`, even `t>=2`, `H=e-z+1`; reduce target to `H>=t+3` | **Inherited analytic baseline** | Pre-RL46 reductions | Treated as exhaustive within retained architecture | Defines Gate A |
| A.1 | Uniform Gate A | Every retained A.0 geometry | Prove `H>=t+3` (equiv. terminal `e>=q+2`) | **Open** | Full phase/terminal invariants | Yes, if theorem proved under all retained hypotheses | Gate A globally |
| A.q | q-specific terminal exclusions | Fixed/small `q` instances of A.0 | Exclude strict Gate-A violation | **Exact finite certificates** | RL46/RL47 verifiers | No | Only certified q-slices |
| A.sep | Cap/room + total-displacement separable relaxation | RL47 near-resonance hypotheses; separable rank bounds | Exclude `H<t+3` | **Dead method for large z** | RL48 barrier theorem | No | Does not close target; forces new coupled information |
| A.h1 | Synchronized height-one subsystem | Exact height-one synchronized dynamics; `n=(J-1)/2` | Understand local pumping | **Exact conjugacy / warning** | RL50 | No | Shows unconstrained route can re-embed shortcut Collatz |
| A.safe | Safe-CF denominator regime | Phase squeeze + stable external `2^71` floor + `ell <= 92,524,042,457,747,860,050` | Classify convergents | **Restricted stress regime** | Legendre/continued fractions; stable external verification floor | No | Reduces this denominator slice to fixed survivor |
| A.safe.s | Sole safe-CF convergent | `a=123139092617126647266`, `ell=77692117359936589403`, fixed `q` | Eliminate retained full-phase object | **Open restricted branch** | A.safe + RL50–RL60 lemmas | No | Safe-CF subtree only |
| A.nonsafe | Non-safe / above Legendre gate | Retained Gate-A object outside A.safe | Establish uniform Gate A or alternative contradiction | **Open / underworked** | Must use more than safe-CF classification | Part of global A.1 | Necessary for Gate A globally unless bypassed |
| T.pot | Terminal potential/mass lemmas | A.safe.s plus RL59 terminal geometry | Positive terminal potential; `M_final>23/4`; synchronize final d=1 tail | **Analytic within fixed survivor** | RL59 verifiers | Local | Enables exact terminal-ancestor certificates |
| T.K25-29 | First terminal-ancestor thresholds | Fixed survivor + T.pot | exact minimal starts for K25/K27/K29 | **Exact finite certificates; replayed inherited suite** | RL59 exact search | Local | Internal z floors for fixed survivor |
| T.K31-39 | Extended terminal-ancestor thresholds | Same | exact `N(K)` through K39 | **Re-audited exact finite certificates** | RL60 source + RL61 second implementation | Local | Internal floor `z>=103303788559` at K39 |
| T.ext | Barina path-record envelope | Fixed survivor; stable published completeness below `2^71` | Contradict K>=131 | **Audited external computational certificate** | Barina path-record table and verified range | Local | Restricts fixed survivor to odd `25<=K<=129` |
| T.s | Frozen terminal-tail survivor | A.safe.s + all T.* restrictions | Eliminate all remaining exact cases | **Open** | Fixed `q`; odd K; phase/tail grammar | No | Safe-CF subtree, not Gate A globally |
| G.full | Universal full-phase impossibility | Every genuine retained RL full-phase object | Direct contradiction before separate A/B | **Open high-leverage alternative** | Coupled E, telescoping, terminal power, ownership/divisibility | Would need to be exhaustive | Could bypass Gate A and Gate B simultaneously |

## Dependency cautions

### External theorem dependency in radius 3

The historical radius-3 tree is not dependency-free. Relevant older branches invoke the rational specialization of the Laurent–Mignotte–Nesterenko two-logarithm theorem. The final RL19 cubic leaf does not. The recovered dependency audit found **no Jacobian conjecture dependency**.

### External computation in safe-CF

Two external inputs must be distinguished:

1. the stable peer-reviewed verification floor through `2^71`, used to make the continued-fraction gate safe;
2. the complete path-record table below `2^71`, used in RL61 to promote `K<=129` for the fixed survivor.

Neither should be described as an analytic theorem proved inside the project.

### Internal computation

The K-threshold certifier proves exact statements only on its submitted bounded intervals. The original RL60 program has a `j>=36` fallback that checks a single representative; this is safe for the supplied replay chunks because every chunk has width less than `2^36`. It is **not** a general proof for arbitrary wider intervals without additional iteration. RL61's second implementation repairs this generic limitation and cross-checks the deployed certificates.

## Closure accounting

### If T.s is eliminated

Closed:
- the sole fixed safe-CF convergent;
- the current RL50–RL60 terminal-tail subtree.

Still open:
- A.nonsafe / uniform A.1;
- Gate B (B.wd/B.pack/B.new or another valid global bridge);
- therefore full RL closure.

### If Gate A is proved uniformly but Gate B remains open

The one-excursion terminal-area obstruction is discharged, but the project still lacks the global bridge/closure step encoded by Gate B unless the Gate-A theorem itself is strengthened to a direct full-phase impossibility result.

### If Gate B is proved but Gate A remains open

The radius-3 theorem becomes globally useful wherever the bridge hypotheses are met, but retained one-excursion objects not forced through that bridge still require Gate A unless the bridge is truly exhaustive over the whole retained RL class.

### Minimum closure standard

No “RL solved” claim is warranted until every retained top-level class is covered by an exhaustive theorem with its dependencies stated and checked. A dead route may be removed; an open target may not.
