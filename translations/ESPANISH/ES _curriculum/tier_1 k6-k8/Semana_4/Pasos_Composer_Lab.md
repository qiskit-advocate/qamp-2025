
# Laboratorio — Teleportación con Compositor (Nivel 1)

## Configuración
- q0 = secreto, q1 = medio, q2 = último.
- **Equipo Bell en q1–q2:** H en q1 → CNOT q1→q2.

## A) Moneda secreta (elige una)
- 0: deja q0 sin cambios      • 1: X en q0      • “Mezcla”: H en q0

## B) Conectar y mirar
- CNOT q0→q1, luego H en q0
- Mide q0 y q1 (estos dos bits son tus **pistas**)

## C) Ajustes para el último qubit (regla de dos bits)
- Si **00** → no hagas nada
- Si **01** → **X** en q2 (voltear)
- Si **10** → **Z** en q2 (girar)
- Si **11** → **X luego Z** en q2

> **Modo fácil:** En lugar de puertas condicionales, ejecuta **cuatro circuitos pequeños**, uno por caso, aplicando el ajuste correspondiente cada vez.

## D) Verificación
- Lee q2 de la misma forma en que configuraste q0:
  - Para 0/1: mide Z directamente.
  - Para “mezcla”: agrega **H** en q2 antes de medir.
- Las barras para q2 deben coincidir con la elección original en q0.
