
# Guía para el Docente — Semana 4 (Nivel 1) Mini-proyecto: Teleportación

**Objetivo:** Que los estudiantes puedan armar la receta clásica de teleportación con el Compositor, usar la regla de dos bits para elegir la corrección y verificar el éxito con un gráfico de barras sencillo.

## Flujo (≈40–45 min)
1) **Pregunta Clave (2):** “¿Podemos mover la *configuración* de una moneda sin mover la moneda?”
2) **Plan (3):** Moneda secreta → Equipo Bell → Conectar y mirar → Dos pistas → Ajustes → Verificación.
3) **Construir (10):** Equipos configuran tres qubits; confirman el equipo Bell (medio + último) mostrando 00/11 después de H+CNOT.
4) **Teleportar (15):** Haz la receta completa. Si las puertas condicionales parecen avanzadas, ejecuta los **cuatro casos** como circuitos separados y aplica el ajuste correspondiente.
5) **Verificar (5):** Lee el último qubit igual que el secreto (Z para 0/1, o agrega H antes de medir para “mezcla”) y compara las barras.
6) **Compartir (5):** 1 captura de pantalla + 3 oraciones (“qué configuramos”, “qué pistas obtuvimos”, “qué ajuste usamos”).

**Consejos para el Compositor**
- 3 qubits: q0 = secreto, q1 = medio, q2 = último. Mide q0 y q1 para obtener los dos bits de pista.
- **Mapa de casos:** `00: I`, `01: X`, `10: Z`, `11: X luego Z` (X antes que Z está bien aquí).
- Mantén el lenguaje: **coincidir/opuesto**, **voltear/girar**, **pistas/ajustes**. Sin símbolos ni matrices.
``
