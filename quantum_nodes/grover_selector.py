import numpy as np
import json, os
from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit_aer.primitives import Sampler

# Ruta interna del contenedor
root_internal = "/src"
sesgo_path = "/src/sesgo_copy.json" # Lo pasaremos por volumen

centro = 3.14
if os.path.exists(sesgo_path):
    with open(sesgo_path, "r") as f:
        sesgo = json.load(f)
        centro = sesgo.get("vqe_angulo", 3.14)

candidatos = np.linspace(centro - 0.2, centro + 0.2, 4)

qc = QuantumCircuit(2)
qc.h([0,1])
qc.cz(0,1)
qc.h([0,1])
qc.z([0,1])
qc.cz(0,1)
qc.h([0,1])
qc.measure_all()

sampler = Sampler()
result = sampler.run(qc).result()
quasi_probs = result.quasi_dists[0]
idx = max(quasi_probs, key=quasi_probs.get)

elegido = round(candidatos[idx % len(candidatos)], 4)
print(f"Grover ejecutado. Ángulo óptimo seleccionado: {elegido} rad")

# Guardar en la carpeta montada /src que mapea a quantum_nodes
with open("/src/tmp_grover.txt", "w") as f:
    f.write(str(elegido))
