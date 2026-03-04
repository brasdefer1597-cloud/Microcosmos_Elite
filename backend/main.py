from flask import Flask, request, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

# Base de datos volátil para el Dashboard
current_data = {
    "counts": {"0000": 0, "0100": 0, "1000": 0, "1100": 0},
    "business": {
        "poas": 0,
        "is_profitable": False,
        "ltv_cac_ratio": 0,
        "grover_boost": "0%"
    },
    "metrics": {"ram_mb": 0, "cpu_percent": 0}
}

def calcular_poas(ingresos, ad_spend, cogs, envio, comisiones):
    # Lógica central: ROAS es vanidad, POAS es realidad
    beneficio_bruto = ingresos - (cogs + envio + comisiones)
    if ad_spend <= 0: return 0
    return round(beneficio_bruto / ad_spend, 2)

@app.route('/api/shor', methods=['GET'])
def get_shor():
    return jsonify(current_data)

@app.route('/api/update', methods=['POST'])
def update_shor():
    global current_data
    # Recibimos los datos crudos del Celeron
    data = request.json
    
    # Procesamos la lógica de POAS en el Backend antes de guardar
    # (Simulamos entrada de ingresos/gastos basada en la telemetría)
    poas_calculado = calcular_poas(5000, 1200, 2000, 300, 100)
    
    data['business']['poas'] = poas_calculado
    data['business']['is_profitable'] = poas_calculado > 1.0
    
    current_data = data
    return jsonify({"status": "synchronized", "poas": poas_calculado})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
