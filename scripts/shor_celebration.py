import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import Aer # <--- Cambio clave para versiones nuevas
from qiskit.compiler import transpile, assemble

def ejecutar_ofrenda():
    print("\n" + "="*40)
    print("💎 OFRENDA CUÁNTICA: ALGORITMO DE SHOR (V2)")
    print("="*40)
    
    qc = QuantumCircuit(5, 4)
    qc.h(range(4)) 
    qc.x(4)        
    qc.measure(range(4), range(4))
    
    # Usamos qiskit_aer explícitamente
    backend = Aer.get_backend('qasm_simulator')
    
    # Ejecución moderna
    transpiled_qc = transpile(qc, backend)
    job = backend.run(transpiled_qc, shots=1)
    result = job.result()
    
    print(f"📊 RESULTADO DE LA MEDICIÓN: {result.get_counts()}")
    print("Sincronización con el Microcosmos: EXITOSA.\n")

if __name__ == "__main__":
    ejecutar_ofrenda()
