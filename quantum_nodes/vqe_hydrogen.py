import numpy as np
from scipy.optimize import minimize
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def ansatz(params):
    """Circuito variacional: un estado que 'aprende' ángulos."""
    qc = QuantumCircuit(1)
    qc.ry(params[0], 0)
    return qc

def calcular_energia(params):
    """Simula la medición de energía para un conjunto de ángulos."""
    qc = ansatz(params)
    qc.measure_all()
    
    # Simulamos el valor esperado de un Hamiltoniano simple
    # H = Z (esto es una simplificación didáctica)
    shots = 1024
    result = AerSimulator().run(qc, shots=shots).result()
    counts = result.get_counts()
    
    # Calculamos el valor esperado <Z>
    prob_0 = counts.get('0', 0) / shots
    prob_1 = counts.get('1', 0) / shots
    esperanza = prob_0 - prob_1
    return esperanza

# 1. Punto de partida (ángulo inicial aleatorio)
params_iniciales = [0.1]

# 2. Optimizador clásico (corre en tu CPU Celeron)
print("\n--- INICIANDO OPTIMIZACIÓN VQE (HÍBRIDA) ---")
res = minimize(calcular_energia, params_iniciales, method='COBYLA')

print(f"\n[ÉXITO] Energía mínima encontrada: {res.fun:.4f}")
print(f"Ángulo óptimo del procesador: {res.x[0]:.4f} radianes")
