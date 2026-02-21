import json
import os
import re
import subprocess

root = "/home/chalamandramagistral/Microcosmos_Elite"
data_path = f"{root}/data/telemetry.jsonl"
sesgo_path = f"{root}/sesgo.json"
leads_path = f"{root}/data/leads.txt"  # Archivo con el número de nuevos leads (puede venir de tu CRM)

clics = 0
masa = 0
angulo = 3.2
max_entropy = 1.5

# Leer telemetría
if os.path.exists(data_path):
    with open(data_path, "r") as f:
        for line in f:
            try:
                d = json.loads(line)
                masa += 1
                if d.get("event") == "clic_refineria":
                    clics += 1
                if d.get("node") == "vqe_hydrogen" and d.get("success"):
                    match = re.search(r"procesador: ([\d\.]+)", d.get("output", ""))
                    if match:
                        angulo = float(match.group(1))
                if d.get("entropy"):
                    max_entropy = max(max_entropy, d["entropy"])
            except:
                continue

# Leer leads desde archivo (si existe)
leads_nuevos = 0
if os.path.exists(leads_path):
    with open(leads_path, "r") as f:
        try:
            leads_nuevos = int(f.read().strip())
        except:
            leads_nuevos = 0

# CONEXIÓN A KO-FI REAL (ingresos)
try:
    ingresos_reales = float(subprocess.check_output(["python3", f"{root}/scripts/kofi_bridge.py"]).decode().strip())
except:
    ingresos_reales = 0.0

# Parámetros fijos (ajústalos según tu negocio)
gasto_ads = 500
valor_por_lead = 10  # Estimación de cuánto vale un lead en tu embudo

# Cálculo de métricas
ingresos_potenciales = leads_nuevos * valor_por_lead
brillo_social = round(ingresos_potenciales / (masa + 1), 2) if masa > 0 else 0
poas_real = round((ingresos_reales - 100) / gasto_ads, 2) if gasto_ads > 0 else 0
cac_real = round(gasto_ads / (clics + 1), 2)
brillo_cuantico = round(ingresos_reales / (masa + 1), 3)

# Construir sesgo
sesgo = {
    "vqe_angulo": round(angulo, 2),
    "masa_critica": masa,
    "brillo_cuantico": brillo_cuantico,
    "brillo_social": brillo_social,
    "poas_real": poas_real,
    "cac_real": cac_real,
    "ingresos_totales": ingresos_reales,
    "leads_nuevos": leads_nuevos,
    "valor_por_lead": valor_por_lead
}

# Guardar
with open(sesgo_path, "w") as f:
    json.dump(sesgo, f, indent=2)

print(f"✅ Heurística: Leads {leads_nuevos} | Brillo Social {brillo_social} | POAS {poas_real}")
