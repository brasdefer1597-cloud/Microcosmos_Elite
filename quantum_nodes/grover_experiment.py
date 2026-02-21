import csv
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def ejecutar_experimento(n_qubits, iteraciones):
    circuit = QuantumCircuit(n_qubits)
    circuit.h(range(n_qubits))
    for _ in range(iteraciones):
        circuit.h(n_qubits-1)
        circuit.mcx(list(range(n_qubits-1)), n_qubits-1)
        circuit.h(n_qubits-1)
        circuit.h(range(n_qubits))
        circuit.x(range(n_qubits))
        circuit.h(n_qubits-1)
        circuit.mcx(list(range(n_qubits-1)), n_qubits-1)
        circuit.h(n_qubits-1)
        circuit.x(range(n_qubits))
        circuit.h(range(n_qubits))
    circuit.measure_all()
    simulator = AerSimulator()
    return simulator.run(circuit, shots=1024).result().get_counts()

# Configuración del Informe Final
pruebas = [(3, 2), (4, 3), (5, 4)]
resultados_informe = []

print("\n--- GENERANDO INFORME DE VICTORIA ---")
for n, it in pruebas:
    res = ejecutar_experimento(n, it)
    ganador = max(res, key=res.get)
    porcentaje = (res[ganador] / 1024) * 100
    resultados_informe.append([n, it, ganador, res[ganador], f"{porcentaje:.2f}%"])
    print(f"Completado: {n} Qubits -> Fidelidad: {porcentaje:.2f}%")

# Guardar en CSV (Persistencia en Debian)
ruta_csv = "/src/informe_cuantico.csv"
with open(ruta_csv, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Qubits", "Iteraciones", "Estado_Ganador", "Disparos", "Fidelidad"])
    writer.writerows(resultados_informe)

print(f"\n[ÉXITO] Informe guardado en: {ruta_csv}")
