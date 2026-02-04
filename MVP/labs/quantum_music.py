# ex5_quantum_music.py - FIXED VERSION
"""
Exercise 5: Quantum Music 
Learn: Phase, interference, complex numbers
Updated: February 2026
"""

import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import warnings
warnings.filterwarnings('ignore')  # Cleaner output

print("🎵 EXERCISE 5: QUANTUM MUSIC")
print("=" * 50)
print("Exploring phase and quantum interference")

def create_quantum_chord(root_note, chords):
    """
    Create quantum states representing musical chords
    root_note: 0-11 (like piano keys)
    chords: list of intervals to add
    """
    qc = QuantumCircuit(3)  # 3 qubits for 8 possible states
    
    # Start with superposition (all notes possible)
    qc.h(0)
    qc.h(1)
    qc.h(2)
    
    # Apply phase gates based on musical structure
    # Each chord adds specific phase pattern
    for interval in chords:
        if interval == 0:  # Root
            qc.p(np.pi/4, 0)  # Small phase
        elif interval == 4:  # Major third
            qc.p(np.pi/2, 1)
        elif interval == 7:  # Perfect fifth
            qc.p(np.pi, 2)
        elif interval == 10:  # Minor seventh
            qc.p(3*np.pi/2, 0)
            qc.p(3*np.pi/2, 1)
    
    # Entangle to create interference
    qc.cx(0, 1)
    qc.cx(1, 2)
    
    return qc

def analyze_quantum_state(qc, chord_name):
    """Analyze and visualize quantum state - FIXED VERSION"""
    # Use statevector simulator correctly
    simulator = AerSimulator(method='statevector')
    compiled_qc = transpile(qc, simulator)
    
    # Run and get statevector
    job = simulator.run(compiled_qc)
    result = job.result()
    
    # Get statevector from result
    statevector = result.get_statevector(0)  # Add experiment index 0
    
    print(f"\n🎶 {chord_name}")
    print("-" * 30)
    
    # Display statevector as "musical notes"
    print("Quantum Statevector (musical representation):")
    for i, amplitude in enumerate(statevector):
        if abs(amplitude) > 0.01:  # Only show significant amplitudes
            # Convert state index to musical note
            notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
            note_name = notes[i % 12]
            octave = i // 12
            
            # Display amplitude as musical dynamics
            magnitude = abs(amplitude)
            phase = np.angle(amplitude)
            
            # Dynamic marking
            if magnitude > 0.7:
                dynamic = "ff (fortissimo)"
            elif magnitude > 0.4:
                dynamic = "mf (mezzo-forte)"
            elif magnitude > 0.2:
                dynamic = "p (piano)"
            else:
                dynamic = "pp (pianissimo)"
            
            # Phase as timbre
            if -np.pi/4 < phase <= np.pi/4:
                timbre = "bright"
            elif np.pi/4 < phase <= 3*np.pi/4:
                timbre = "warm"
            elif phase > 3*np.pi/4 or phase <= -3*np.pi/4:
                timbre = "dark"
            else:
                timbre = "mellow"
            
            print(f"  |{i:03d}⟩: {note_name}{octave} - {dynamic}, {timbre}")
            print(f"      Amplitude: {amplitude:.3f}")
    
    # Calculate "quantum harmony" metric
    harmony_score = np.sum(np.abs(statevector)**4) * 100
    print(f"\n  Harmony Score: {harmony_score:.1f}/100")
    
    return statevector

# Main composition - SIMPLIFIED for Codespaces
print("\n🎼 QUANTUM SYMPHONY")
print("Creating quantum states for different chords...")

# Define just one chord to test
chord_name = "C Major"
intervals = [0, 4, 7]  # C-E-G

print(f"\nCreating {chord_name} chord...")
qc = create_quantum_chord(0, intervals)

print("\n📐 Quantum circuit for C Major chord:")
print(qc.draw(output='text'))

# Analyze the state
try:
    state = analyze_quantum_state(qc, chord_name)
    print(f"\n✅ Successfully created quantum {chord_name}!")
    
    # Simple visualization
    print("\n📊 Probability distribution:")
    for i in range(8):
        prob = abs(state[i])**2
        if prob > 0.001:
            print(f"  |{i:03b}⟩: {prob:.3f}")
    
except Exception as e:
    print(f"\n❌ Error: {e}")
    print("\nTrying alternative approach...")
    
    # Fallback: Just show circuit and basic info
    print("\nCircuit gates:")
    for instruction in qc.data:
        print(f"  {instruction.operation.name} on qubit(s) {instruction.qubits}")

# Student composition - SIMPLIFIED
print("\n" + "=" * 50)
print("🎹 QUICK COMPOSITION CHALLENGE")
print("=" * 50)

print("\nTry these chord patterns:")
print("1. Major chord: 0 4 7")
print("2. Minor chord: 0 3 7")  
print("3. 7th chord: 0 4 7 10")

# Predefined example
print("\n🎵 Example: C Major 7th chord (0 4 7 10)")
qc_seventh = create_quantum_chord(0, [0, 4, 7, 10])
print("Circuit created successfully!")

print("\n" + "=" * 50)
print("🎓 WHAT YOU LEARNED:")
print("• Quantum phase = musical 'color' or timbre")
print("• Different chords create different quantum patterns")
print("• Entanglement creates quantum 'harmony'")
print("• Measurement 'chooses' one note from the superposition")

print("\n🤔 THINK ABOUT:")
print("1. How is quantum music different from digital music?")
print("2. Can quantum computers create new types of music?")
print("3. What happens if we add more qubits?")