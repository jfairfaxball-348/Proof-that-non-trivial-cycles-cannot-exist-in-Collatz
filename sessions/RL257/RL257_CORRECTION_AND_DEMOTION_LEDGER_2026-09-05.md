# RL257 correction and demotion ledger

Date: 2026-09-05

## Binding correction 1 — terminal indexing

The RL257 incoming kickoff repeated an incorrect endpoint sentence from the
RL256 closeout.

Exact RL64 source-derived convention:

- the internal path ends at `d=1`, `T=2^k-1`, hence `J=2^k`;
- this is **before** the omitted terminal `(1,0)` column;
- the omitted `(1,0)` and the terminal synchronized zeros are appended in the
  full-word reconstruction outside the internal `x,y` path.

Future sessions must use this convention.

## Binding correction 2 — H notation

At the current arithmetic selector,

`H_sel=19z-7a=14`

is the RL254/RL255 half-window selector quantity.

It must not be silently identified with RL45/RL64 accumulated canonical area
`H_can`. No such equality is proved here.

## Retained RL256 results

Retain:

- `k in {31,33}`;
- `k=31 => E_31<=27`;
- `k=33 => beta(P)>=281`;
- `k=33 => E_33<=5`;
- the forced `k=33` right four-one block `u_3...u_6=1111`.

## New promoted correction/result

Using the exact canonical start `(d,J)=(1,-13)`, the first three internal
`x` bits cannot all be `1`. Hence the RL256 forced block
`u_3...u_6=1111` eliminates `k=33`.

The exact first halving frontier is therefore `k=31`.

## Still demoted / non-evidentiary

RL256's provisional four-state backward tree remains demoted. RL257 does not
need it and makes no claim about whether parts of it can be repaired.

The exploratory RL256 MILP infeasibility remains non-evidentiary because no
exact certificate was promoted.

All RL249/RL250 demotions remain binding. RL251's Gabriel-horn equivalence
remains frozen.
