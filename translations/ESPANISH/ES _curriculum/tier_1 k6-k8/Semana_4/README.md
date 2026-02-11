
# Semana 4 — Mini-proyecto: Teleportación (Nivel 1, Grados 6–8)

**Idea principal:** Podemos enviar la “configuración de una moneda” de un lugar a otro usando un **equipo Bell** y **dos bits de pista**.

## Lo que construirás
1) **Moneda secreta:** configura el primer qubit (elige: siempre 0, siempre 1, o “mezcla” con H).
2) **Equipo Bell:** conecta los otros dos qubits con **H en el del medio** → **CNOT al último**.
3) **Conectar y mirar:** **CNOT del secreto → medio**, luego **H en el secreto** y lee los dos primeros.
4) **Dos pistas → ajustes:** usa los dos resultados para elegir el ajuste correcto en el último qubit:  
   - **00 → no hagas nada**  
   - **01 → voltear** (X)  
   - **10 → girar** (Z)  
   - **11 → voltear y luego girar** (X luego Z)
5) **Verificación:** el último qubit ahora debe coincidir con la “moneda secreta” original cuando lo leas de la misma manera.

**Usamos palabras cotidianas (mezcla, voltear, girar) y probabilidades simples—sin matemáticas complicadas.**
