# Lab — Teleportation with Composer (Tier-1)

## Setup
- q0 = secret, q1 = middle, q2 = last.
- **Bell team on q1–q2:** H on q1 → CNOT q1→q2.

## A) Secret coin (pick one)
- 0: leave q0 alone      • 1: X on q0      • “Mix”: H on q0

## B) Link & peek
- CNOT q0→q1, then H on q0
- Measure q0 and q1 (these two bits are your **clues**)

## C) Fixes for the last qubit (two-bit rule)
- If **00** → do nothing
- If **01** → **X** on q2 (flip)
- If **10** → **Z** on q2 (twist)
- If **11** → **X then Z** on q2

> **Easy mode:** Instead of conditional gates, run **four tiny circuits**, one per case, applying the matching fix each time.

## D) Check
- Read q2 the same way you set q0:
  - For 0/1: measure Z directly.
  - For “mix”: add **H** on q2 before measure.
- Bars for q2 should match the original choice on q0.
