import numpy as np
from qiskit import QuantumCircuit, Aer, execute
import json
import sys

# Cargar datos de campañas simuladas (podrían venir de un CSV)
# Por ahora, datos dummy
X = np.array([[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]])  # features
y = np.array([0, 1, 0])  # etiquetas (conversión o no)

# Circuito variacional simple
def circuito(theta, x):
    qc = QuantumCircuit(2)
    qc.ry(x[0], 0)
    qc.ry(x[1], 1)
    qc.cx(0, 1)
    qc.ry(theta[0], 0)
    qc.ry(theta[1], 1)
    qc.measure_all()
    return qc

# Optimización (simulada)
theta_opt = [0.5, 0.5]  # aquí usarías COBYLA como en VQE
predicciones = []
for xi in X:
    qc = circuito(theta_opt, xi)
    counts = execute(qc, Aer.get_backend('qasm_simulator'), shots=1024).result().get_counts()
    # Interpretar la medición como probabilidad de conversión
    prob_conv = counts.get('11', 0) / 1024
    predicciones.append(prob_conv)

# Calcular pérdida (binary cross-entropy simulada)
loss = -np.mean(y * np.log(predicciones + 1e-10) + (1-y) * np.log(1 - predicciones + 1e-10))
print(f"Pérdida de clasificación: {loss:.4f}")
# Guardar resultado para telemetría
resultado = {"loss": loss, "theta": theta_opt}
print(json.dumps(resultado))
