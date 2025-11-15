# Teacher Guide — Week 4 (Tier-1) Mini-project: Teleportation

**Goal:** Students can assemble the classic teleportation recipe with Composer, use the two-bit rule to choose the correction, and verify success with a simple bar chart.

## Flow (≈40–45 min)
1) **Hook (2):** “Can we move a coin’s *setting* without moving the coin?”
2) **Plan (3):** Secret coin → Bell team → Link & peek → Two clues → Fixes → Check.
3) **Build (10):** Teams set up three qubits; confirm Bell team (middle+last) by showing 00/11 after H+CNOT.
4) **Teleport (15):** Do the full recipe. If conditional gates feel advanced, run the **four cases** as separate circuits and apply the matching fix.
5) **Verify (5):** Read the last qubit the same way as the secret (Z for 0/1, or add H before measure for “mix”) and compare bars.
6) **Share (5):** 1 screenshot + 3 sentences (“what we set,” “what clues we got,” “what fix we used”).

**Composer tips**
- 3 qubits: q0 = secret, q1 = middle, q2 = last. Measure q0 & q1 to get the two clue bits.
- **Case mapping:** `00: I`, `01: X`, `10: Z`, `11: X then Z` (X before Z is fine here).
- Keep language: **match/opposite**, **flip/twist**, **clues/fixes**. No symbols/matrices.
