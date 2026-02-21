from flask import Flask, request, jsonify
import json, os, datetime, subprocess, requests

app = Flask(__name__)

# Configuración del Búnker
MONEY_LOG = "/home/chalamandramagistral/Microcosmos_Elite/data/money.log"
CLOUD_JSON = "/home/chalamandramagistral/Chalamandra-HUB/cloud_snapshot.json"
DEPLOY_SCRIPT = "/home/chalamandramagistral/Microcosmos_Elite/scripts/deploy_quantum.sh"
TELEGRAM_TOKEN = "TU_TOKEN_AQUÍ"
TELEGRAM_CHAT_ID = "TU_ID_AQUÍ"

def notificar_telegram(monto):
    texto = f"💰 *MATERIA CAPTURADA* 💰\n\n💵 *Monto:* ${monto}\n📡 *Origen:* Ko-fi/Stripe\n🟢 _La Singularidad se expande._"
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    try:
        requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "text": texto, "parse_mode": "Markdown"})
    except Exception as e:
        print(f"❌ Error Telegram: {e}")

def calcular_masa_critica():
    total = 0.0
    if os.path.exists(MONEY_LOG):
        with open(MONEY_LOG, 'r') as f:
            for line in f:
                if line.strip():
                    try:
                        total += float(line.split(',')[0])
                    except: pass
    return total

@app.route('/webhook-money', methods=['POST'])
def webhook_money():
    data = request.get_json(force=True)
    amount = data.get('amount', 0)
    
    # 1. Registro y Telegram
    with open(MONEY_LOG, 'a') as f:
        f.write(f"{amount},{json.dumps(data)}\n")
    notificar_telegram(amount)
    
    # 2. Actualización de Masa Crítica
    nueva_masa = calcular_masa_critica()
    with open(CLOUD_JSON, 'w') as f:
        json.dump({"masa_critica": nueva_masa, "last_update": str(datetime.datetime.now())}, f)
        
    # 3. Despliegue y Beep (Celebración Algorítmica)
    subprocess.Popen(["bash", DEPLOY_SCRIPT])
    os.system('speaker-test -t sine -f 1000 -l 1 & sleep 0.5 && killall speaker-test') # Beep físico
    
    return jsonify({"status": "Masa Asimilada", "total": nueva_masa}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
