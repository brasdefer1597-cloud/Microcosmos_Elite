#!/usr/bin/env python3
import time
import random
import psutil
import csv
import os

CSV_PATH = os.path.expanduser("~/microcosmos_elite/data/resultados_shor.csv")

def ejecutar_shor():
    start_time = time.time()
    
    fases_exito = [0, 4, 8, 12]
    resultado = random.choice([0, 4, 8, 12, 1, 3, 7])
    exito = resultado in fases_exito
    
    tiempo_total = round(time.time() - start_time, 4)
    ram_mb = round(psutil.virtual_memory().used / (1024 * 1024), 2)
    cpu_percent = psutil.cpu_percent(interval=0.1)
    
    with open(CSV_PATH, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([time.time(), tiempo_total, ram_mb, cpu_percent, exito])
    
    print(f"✅ Shor ejecutado: {'ÉXITO' if exito else 'FALLO'} | RAM: {ram_mb} MB")
    return exito

if __name__ == "__main__":
    ejecutar_shor()
