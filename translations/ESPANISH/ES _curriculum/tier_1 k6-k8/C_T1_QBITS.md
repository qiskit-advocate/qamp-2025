
## **GUÍA MAESTRA DEL DOCENTE**
### **Título de la Unidad: Alfabetización Cuántica y Modelado Aplicado (Grados 6–8)**

Este currículo está diseñado para ser una introducción de 4 semanas, basada en proyectos, a los fundamentos cuánticos usando el **IBM Quantum Composer** (una herramienta visual sin código).

#### **1. Descripción General del Currículo:**
| **Campo**                | **Detalle**                                                                                   |
|--------------------------|----------------------------------------------------------------------------------------------|
| **Público Objetivo**     | **Tier 1: Grados 6–8 (Secundaria)**                                                          |
| **Principio de Diseño**  | **Alineación Transversal:** Conceptos alineados con estándares de Matemáticas (CCSS-M), Ciencia (NGSS) y Computación (CSTA). |
| **Progresión de Aprendizaje** | **Precarga Conceptual** (Narrativa) → **Modelado Aplicado** (IBM Composer) → **Lógica Computacional** (Multi-Qubit). |
| **Duración**             | **4 semanas (aprox. 4 sesiones de 45-60 minutos)**                                           |
| **Guía para el Docente** | **Semana 1** enfocada en Conceptos/Alfabetización. **El uso del Quantum Composer inicia en la Semana 2.** |

QMAP Edición #18: Quantum For All - Tier 1 (Semana 1) Página 1

---

### **1. Marco Pedagógico: La Bóveda Cuántica**

Esta unidad está diseñada para implementarse de manera modular en diferentes materias, asegurando alta accesibilidad y adopción.

| **Área de Enfoque**      | **Objetivo (El estudiante será capaz de...)**                                                | **Nivel de Bloom**         |
|--------------------------|----------------------------------------------------------------------------------------------|----------------------------|
| **Ciencia/Alfabetización** | Definir y **comparar** los modelos atómicos Clásico (Bohr) y Cuántico (Onda).               | Analizar, Comprender       |
| **Matemáticas**          | **Aplicar** la regla de probabilidad 100% (α% + β% = 100%) para resolver ecuaciones básicas. | Aplicar                    |
| **Computacional**        | **Secuenciar** comandos cuánticos conceptuales (Puerta Hadamard, Medición) y comprender **Entrelazamiento/Correlación** básica. | Crear                      |

QMAP Edición #18: Quantum For All - Tier 1 (Semana 1) Página 2

---

### **2. Secuencia Curricular Tier 1 (4 Semanas)**

El currículo incrementa la complejidad gradualmente, desde comprensión lectora hasta lógica multi-qubit.

| **Módulo**               | **Semanas** | **Actividad Principal**                                         | **Concepto Cuántico Clave**                                         |
|--------------------------|-------------|-----------------------------------------------------------------|---------------------------------------------------------------------|
| **1. Alfabetización Fundamental** | **Semana 1** | **Hojas de trabajo de comprensión** (El Candelabro / El Fantasma en la Máquina). | **Superposición, Cuantización, Medición/Colapso.**                  |
| **2. Laboratorio Aplicado 1**     | **Semana 2** | **La Brújula Cuántica** (Laboratorio Composer).                 | **Estados de Qubit**                                                |
| **3. Laboratorio Aplicado 2**     | **Semana 3** | **Girando la Flecha** (Laboratorio Composer, enfoque en geometría). | **Puertas Cuánticas como Rotaciones** (Visualización de cambio porcentual; **Círculo de Probabilidad 2D** solamente). |
| **4. Proyecto Final de Lógica**   | **Semana 4** | **El Cerrajero Cuántico** (Lógica Multi-Qubit).                 | **Entrelazamiento/Correlación** (usando la **"Conexión en Tándem"** puerta CNOT). |

QMAP Edición #18: Quantum For All - Tier 1 (Semana 1) Página 3

---

### **3. Unidades de Alfabetización Fundamental (Semana 1)**

Estos recursos proveen la precarga conceptual necesaria para los laboratorios con Composer.

#### **Unidad A: El Candelabro Encantado del Qubit (Enfoque Narrativo/ELA)**

| **Metáfora Central**     | **Concepto Cuántico**      | **Idea Principal para el Estudiante**                  |
|--------------------------|----------------------------|--------------------------------------------------------|
| **Hechizo de Mezclador Perfecto** | Superposición (puerta H)         | El Qubit puede estar en dos estados (0 y 1) al mismo tiempo. |
| **Ataque del Medidor Monstruo**   | Medición / Colapso               | La observación obliga a elegir solo una respuesta.     |
| **Regla del Todo**                 | Normalización (∑P=1)             | Todas las posibilidades deben sumar **una unidad** (100%). |

#### **Unidad B: El Fantasma en la Máquina (Enfoque Ciencia/Comprensión)**

| **Concepto Central**     | **Metáfora / Analogía**    | **Área Clave de Evaluación**                           |
|--------------------------|----------------------------|--------------------------------------------------------|
| **Dualidad Onda-Partícula** | El electrón es una **Onda de Energía Cuántica** (sonido/vibración). | Comparar los modelos de **Partícula** vs. **Onda**.    |
| **Spin y Superposición**     | La **Brújula Secreta** que gira (Superposición). | Aplicar el concepto para explicar por qué las computadoras cuánticas son más rápidas. |

QMAP Edición #18: Quantum For All - Tier 1 (Semana 1) Página 4

---

### **4. Refinamientos de Lógica Computacional (Semanas 2-4)**

#### **A. Lógica y Geometría Tier 1 (Semanas 2-3)**

El enfoque en geometría se limita estrictamente a probabilidad 2D y movimiento visual para evitar conflictos de alineación.

| **Enfoque de Puerta**    | **Modelo Conceptual (Tier 1)** | **Concepto Evitado (Reservado para el siguiente Tier)** |
|--------------------------|-------------------------------|---------------------------------------------------------|
| **Puertas X/H**          | **La Brújula Cuántica**        | Notación Formal de Dirac                                |
| **Diales RX, RY**        | **La Puerta de Inclinación** (Cambiando el porcentaje de probabilidad). | **Geometría de la Esfera de Bloch** (coordenadas 3D formales, radianes/grados). |

#### **B. Introducción al Entrelazamiento (Semana 4: El Cerrajero Cuántico)**

El proyecto final introduce el poder de los sistemas multi-qubit sin matemáticas complejas.

| **Elemento**             | **Descripción**               | **Lógica Computacional**                                |
|--------------------------|-------------------------------|---------------------------------------------------------|
| **Puerta CNOT**          | Llamada **"Conexión en Tándem"** o **"Cable de Conexión"**. | Vincula los estados del Qubit 0 y Qubit 1.              |
| **Meta de la Actividad** | Probar la **Correlación**. Los estudiantes aplican H al Qubit 0 y enlazan el Qubit 1 con CNOT. | Si el Qubit 0 se mide como **Arriba (1)**, el Qubit 1 _también debe_ ser **Arriba (1)**. Este vínculo perfecto es el poder simple del **Entrelazamiento**. |

QMAP Edición #18: Quantum For All - Tier 1 (Semana 1) Página 5

---

### **5. Puente Conceptual de Tier 1 a Tier 2**

Esta sección define claramente el cambio de complejidad requerido para el siguiente nivel.

| **Concepto Tier 1 (Grados 6-8)** | **Explicación del Puente** | **Concepto Tier 2 (Grados 9-11)** |
|-----------------------------------|----------------------------|------------------------------------|
| **Brújula Cuántica** (Flecha 2D)  | La **Brújula** solo era el movimiento de la flecha en un mapa plano. El siguiente nivel explica el verdadero espacio 3D. | **Esfera de Bloch** (Modelo 3D Formal) |
| **Inclinación → Porcentaje**      | Usamos un dial para cambiar porcentajes. Ahora, usamos **ángulos y vectores** para describir la posición exacta en el espacio. | **Representación Vectorial** y Matrices de Rotación |
| **Eje Z Oculto** (Fase)           | Ignoramos intencionalmente el "giro" oculto de la flecha (giro atrás/adelante). Este giro oculto es la **Fase**. | **Fase** (La Metáfora del **Manecilla del Reloj Cuántico**) |

---

### **6. Recursos para la Implementación del Currículo**

Los siguientes recursos son esenciales para desplegar el currículo Tier 1.

| **Nombre del Recurso**   | **Tipo**                      | **Propósito en el Currículo**                           |
|--------------------------|-------------------------------|---------------------------------------------------------|
| **IBM Quantum Composer** | Herramienta Visual (Web)      | Plataforma central para todos los laboratorios (Módulos 2, 3, 4). Permite a los estudiantes construir y ejecutar circuitos visualmente sin código. |
| **Hojas de Trabajo Tier 1** | Documentación (PDF/MD)      | Tareas para estudiantes de **Alfabetización Fundamental** (Semana 1) y **Lógica Computacional** (Semanas 2-4). Incluye claves de respuestas. |
| **IBM Qiskit Classroom** | Portal Educativo              | Proporciona material complementario y documentación/tutoriales oficiales sobre puertas cuánticas básicas para el docente. |
| **Documentación Qiskit** | Referencia (Web)              | Usada por el docente para confirmar definiciones de puertas y resolver resultados esperados durante los laboratorios con Composer. |
| **Plan de Lección Ejemplar** | La Brújula Cuántica        | Este plan detallado y con bloques de tiempo muestra cómo ejecutar el **Módulo 2 (Laboratorio Aplicado 1)** usando el IBM Quantum Composer. Está diseñado para ser **abierto**, permitiendo a los docentes ajustar el tiempo y la actividad según el ritmo de su clase (Laboratorio de Ciencias, Clase de Matemáticas o Alfabetización Computacional). |

---

### **Conclusión y Siguientes Pasos**

Esta **Guía Maestra Tier 1** logra cerrar la brecha entre la ciencia cuántica y la educación secundaria. Usando un enfoque transversal y basado en metáforas, este recurso elimina requisitos previos, haciendo accesibles los conceptos de superposición, medición e incluso entrelazamiento para estudiantes de 6° a 8° grado.

La siguiente fase de desarrollo se enfocará en **Tier 2 (Grados 9–11)**, desarrollando el **Puente Conceptual** para introducir formalmente la Esfera de Bloch, la rotación vectorial y la definición matemática de Fase, continuando el progreso hacia el dominio computacional.

Se anticipa que este marco será un gran paso para expandir la comunidad de Qiskit y la cuántica a estudiantes más jóvenes a nivel global.

QMAP Edición #18: Quantum For All - Tier 1 (Semana 1) Página 8
``
