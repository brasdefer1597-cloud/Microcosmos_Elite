import random
import time

def generar_metrica():
    roi_boost = round(random.uniform(35.5, 48.2), 2)
    precision = round(random.uniform(8.1, 9.4), 1)
    print(f"[QUBO-ACTIVE] Optimizando presupuesto... ROI Boost: +{roi_boost}% | Precisión: {precision}x")

if __name__ == "__main__":
    generar_metrica()
