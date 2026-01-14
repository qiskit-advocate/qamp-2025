# Week 2 — Bloch Sphere & Single-Qubit Rotations (First Assessment)

**Builds on Week 1:** Move from the 2D “Quantum Compass” (|0⟩/|1⟩, superposition via H, Z-basis measurement) to the **3D Bloch Sphere**.
- **Tilt** the state with **RX(θ), RY(θ)** → changes Z-basis probabilities.
- **Twist** the state with **RZ(θ)/Phase** → changes relative phase (invisible in Z; visible in X via H).
- Canonical demo: **H → RZ(π) → H** maps |+⟩ → |−⟩ (Z 50/50 unchanged; X flips).

## Learning Goals
1. Explain the Bloch parameterization: \(|ψ⟩=\cos(θ/2)|0⟩+e^{iφ}\sin(θ/2)|1⟩\).
2. Distinguish rotations **RX/RY** (probabilities) vs **RZ/Phase** (phase).
3. Predict outcomes in Z vs X basis; make phase observable with **H** pre/post measurement.
4. Produce tiered deliverables (lab + assessment) that scale in tools and math.

> **Angles:** Use **radians** in code (pair any degrees: π/4 = 45°).  
> **Composer note:** RZ may appear as **P(λ)/Phase**; `p(λ)` and `rz(λ)` differ only by a **global phase** (measurement-invariant).

## Deliverables (Due EOW)
- **Tier-1 (G6–8):** Composer lab + 1-page worksheet.
- **Tier-2 (G9–11):** Qiskit notebook + short assessment (hit specified Bloch points).
- **Tier-3 (UG/Adv):** Qiskit notebook + phase derivation/assessment.

## Repo Locations
- Labs (code/screens): `labs/week_2/...`
- Assessments (worksheets/rubrics): `assessments/week_2/...`
- Teacher notes: `docs/week_2/teacher_guide.md`
