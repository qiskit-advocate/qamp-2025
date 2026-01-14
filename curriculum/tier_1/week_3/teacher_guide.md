# Teacher Guide — Week 3 (Tier-1)

**Tone:** warm, encouraging, concrete. Use everyday comparisons (coins, magic dice).
**Goal:** students can build a Bell pair, flip the pattern with one gate, and explain their choices.

## Flow (≈35–40 min)
1) Hook (2): “Two coins that always match—trick or tech?”  
2) Demo (5): H(q0) → CNOT(q0→q1) → measure → show 00/11 bars.  
3) Explore (10): students replicate.  
4) Remix (8): add X on q1 → show 01/10; compare to “no CNOT”.  
5) Pixel “Postcards” (8): pairs use a 16-bit shared bitstring + a given cipher to reveal a 4×4 icon.  
6) Share (2): pairs explain “what I changed & why” (predict → test → explain → iterate).

**Settings**
- Bell histograms: Shots=1024, measure both qubits.
- For a 16-bit “key”: Shots=1, run 16 times; each partner keeps their bit.
- Language to use: “linked outcomes”, “matching/opposite”, “simple rule (same=0, different=1)”.
