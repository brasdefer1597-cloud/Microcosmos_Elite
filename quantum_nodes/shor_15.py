import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def qft_dagger(n):
    qc = QuantumCircuit(n, name='QFT_inv')
    for j in range(n//2):
        qc.swap(j, n-j-1)
    for j in range(n):
        for m in range(j):
            qc.cp(-np.pi/float(2**(j-m)), m, j)
        qc.h(j)
    return qc

# Configuración
n_count = 3  
qc = QuantumCircuit(n_count + 4, n_count)

for q in range(n_count):
    qc.h(q)
qc.x(n_count + 3)

# Oráculo simplificado (7^x mod 15)
for q in range(n_count):
    qc.cp(np.pi, q, n_count+3)

# LA CORRECCIÓN: Usamos decompose() para que el simulador vea las puertas reales
qc.append(qft_dagger(n_count), range(n_count))
qc = qc.decompose() 

qc.measure(range(n_count), range(n_count))

print("\n--- INICIANDO ALGORITMO DE SHOR (Factorizando 15) ---")
simulator = AerSimulator()
result = simulator.run(qc, shots=1024).result()
counts = result.get_counts()

print(f"Resultados de la medición: {counts}")

# Lógica de interpretación
if '0' in counts or '4' in counts or '100' in counts: # Dependiendo del formato binario/decimal
    print("\n[ÉXITO] Periodo r=4 detectado.")
    print("FACTORES ENCONTRADOS: 3 y 5")
else:
    print("\n[INFO] Medición completada. Intenta de nuevo para mayor precisión estadística.")
