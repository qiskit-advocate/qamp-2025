
# Mini-proyecto de Teleportación — Tarjeta del Equipo

**Roles:** Alice (lado secreto) • Bob (receptor)

**Receta (rápida):**
1) Alice configura la moneda secreta en q0.  
2) Forma el equipo Bell en q1–q2 (H en q1; CNOT q1→q2).  
3) Conectar y mirar (CNOT q0→q1; H en q0; mide q0 y q1).  
4) Usa las dos pistas para elegir el ajuste en q2:  
   00→ninguno, 01→voltear (X), 10→girar (Z), 11→voltear+girar (X luego Z).  
5) Verifica que q2 coincida con q0 cuando lo leas de la misma manera.

