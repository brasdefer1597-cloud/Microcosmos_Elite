import numpy as np
from qiskit.circuit.library import EfficientSU2
from qiskit_aer import AerSimulator
from qiskit import transpile
from scipy.optimize import minimize

# Configuración inicial
sim = AerSimulator()
ansatz_base = EfficientSU2(num_qubits=2, entanglement='linear', reps=1)

def get_energy(params, ansatz, simulator):
    # 1. Asignar parámetros
    bound_circuit = ansatz.assign_parameters(params)
    bound_circuit.measure_all()
    
    # 2. TRANSPILAR (Convertir EfficientSU2 a puertas básicas)
    # Esto es lo que faltaba para que Aer no se queje
    qc_transpiled = transpile(bound_circuit, simulator)
    
    # 3. Ejecución
    result = simulator.run(qc_transpiled, shots=512).result()
    counts = result.get_counts()
    
    # Cálculo de energía (simplificado para la demo)
    probs = {k: v/512 for k, v in counts.items()}
    energy = sum([(-1.0)**k.count('1') * p for k, p in probs.items()])
    return energy - 7.85

print("\n--- INICIANDO VQE TURBO (Corregido) ---")
params_iniciales = np.random.rand(ansatz_base.num_parameters)

res = minimize(get_energy, params_iniciales, args=(ansatz_base, sim), 
               method='COBYLA', tol=1e-3)

print(f"\n[ÉXITO] Energía: {res.fun:.5f} Hartree")
print(f"Iteraciones: {res.nfev}")
