# Week 4 — Mini-project: Teleportation (Tier-1, Grades 6–8)

**Big idea:** We can send the “setting of a coin” from one place to another using a **Bell team** and **two clue bits**.

## What you’ll build
1) **Secret coin:** set the first qubit (choose: always 0, always 1, or “mix” with H).
2) **Bell team:** link the other two qubits with **H on the middle** → **CNOT to the last**.
3) **Link & peek:** **CNOT from secret → middle**, then **H on secret** and read the first two.
4) **Two clues → fixes:** use the two results to choose the right fix on the last qubit:  
   - **00 → do nothing**  
   - **01 → flip** (X)  
   - **10 → twist** (Z)  
   - **11 → flip then twist** (X then Z)
5) **Check:** the last qubit should now match the original “secret coin” when you read it the same way.

**We use everyday words (mix, flip, twist) and simple chances—no heavy math.**
