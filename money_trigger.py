from flask import Flask, request
import requests
import os
from dotenv import load_dotenv

# Carga forzada
base_dir = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(base_dir, ".env"))

app = Flask(__name__)

TG_TOKEN = os.getenv("TG_TOKEN")
TG_CHAT_ID = os.getenv("TG_CHAT_ID")
KOFI_TOKEN = os.getenv("KOFI_TOKEN")

@app.route('/webhook-money', methods=['POST'])
def webhook():
    data = request.get_json(silent=True) or request.form.to_dict()
    if data.get('verification_token') != KOFI_TOKEN:
        return "Forbidden", 403

    monto = data.get('amount', '0.00')
    msg = f"💎 <b>INYECCIÓN: ${monto}</b>"
    
    # Intento de envío con reporte
    url = f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage"
    payload = {"chat_id": TG_CHAT_ID, "text": msg, "parse_mode": "HTML"}
    
    try:
        r = requests.post(url, json=payload, timeout=5)
        # Esto escribirá el resultado real en el log
        print(f"DEBUG TELEGRAM: {r.status_code} - {r.text}")
    except Exception as e:
        print(f"DEBUG ERROR: {e}")

    return "OK", 200

if __name__ == "__main__":
    app.run(port=5000)
