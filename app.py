from flask import Flask, request, jsonify
import json
import os
import datetime
import subprocess

app = Flask(__name__)

# Rutas de la Bóveda
MONEY_LOG = "/home/chalamandramagistral/Microcosmos_Elite/data/money.log"
CLOUD_JSON = "/home/chalamandramagistral/Chalamandra-HUB/cloud_snapshot.json"
DEPLOY_SCRIPT = "/home/chalamandramagistral/Microcosmos_Elite/scripts/deploy_quantum.sh"

def calcular_masa_critica():
    total = 0.0
    if os.path.exists(MONEY_LOG):
        with open(MONEY_LOG, 'r') as f:
            for line in f:
                if line.strip():
                    try:
                        valor = float(line.split(',')[0])
                        total += valor
                    except:
                        pass
    return total

@app.route('/webhook-money', methods=['POST'])
def webhook_money():
    # Log para ver qué llega exactamente
    print(f"📡 Señal recibida: {request.data}")
    
    try:
        data = request.get_json(force=True) # Forzamos la lectura de JSON
    except Exception as e:
        print(f"❌ Error decodificando JSON: {e}")
        return jsonify({"error": "JSON inválido"}), 400

    print(f"✅ Inyección aceptada: {data}")
    
    # 1. Guardar en la bóveda
    amount = data.get('amount', 0)
    with open(MONEY_LOG, 'a') as f:
        f.write(f"{amount},{json.dumps(data)}\n")
    
    # 2. Recalcular y Actualizar
    nueva_masa = calcular_masa_critica()
    snapshot = {
        "masa_critica": nueva_masa,
        "last_update": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    with open(CLOUD_JSON, 'w') as f:
        json.dump(snapshot, f)
        
    # 3. Disparo de despliegue
    try:
        subprocess.Popen(["bash", DEPLOY_SCRIPT])
    except:
        pass

    return jsonify({"status": "OK", "total": nueva_masa}), 200

if __name__ == '__main__':
    # Escuchamos en todas las interfaces para evitar bloqueos
    app.run(host='0.0.0.0', port=5000, debug=True)
