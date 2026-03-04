import numpy as np
import json

def ejecutar_grover_poas():
    # 8 estrategias de marketing (3 qubits)
    estrategias = [
        [1000, 200, 400, 100],   # 0
        [1200, 300, 500, 150],   # 1
        [1500, 400, 600, 150],   # 2
        [2000, 800, 900, 200],   # 3
        [900, 100, 200, 50],     # 4
        [1100, 250, 450, 100],   # 5
        [1800, 500, 400, 200],   # 6
        [1300, 400, 700, 100]    # 7
    ]

    def calcular_poas(e):
        beneficio_neto = e[0] - (e[2] + e[3])
        return beneficio_neto / e[1] if e[1] > 0 else 0.0

    poas_values = [calcular_poas(e) for e in estrategias]
    ganador_idx = np.argmax(poas_values)
    poas_max = poas_values[ganador_idx]

    # Fidelidad simulada (cuántica vibe)
    fidelidad = round(0.85 + (poas_max / 10.0) * 0.1, 2)  # entre 0.85 y ~0.95

    return {
        "poas_max": poas_max,
        "fidelidad": fidelidad,
        "ganador_idx": ganador_idx,
        "poas_values": poas_values
    }

if __name__ == "__main__":
    print(json.dumps(ejecutar_grover_poas()))
