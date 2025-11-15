# Teleportation Mini-project — Team Card

**Roles:** Alice (secret side) • Bob (receiver)

**Recipe (quick):**
1) Alice sets the secret coin on q0.  
2) Make Bell team on q1–q2 (H on q1; CNOT q1→q2).  
3) Link & peek (CNOT q0→q1; H on q0; measure q0,q1).  
4) Use the two clues to choose the fix on q2:
   00→none, 01→flip (X), 10→twist (Z), 11→flip+twist (X then Z).  
5) Check q2 matches q0 when read the same way.
