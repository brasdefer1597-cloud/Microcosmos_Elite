from flask import Flask, request
import os
import requests
from datetime import datetime

app = Flask(__name__)

@app.route('/webhook-kofi', methods=['POST'])
@app.route('/webhook-kofi/', methods=['POST'])
def kofi_webhook():
    print("\n--- SEÑAL DETECTADA EN EL NODO ---")
    data = request.form.get('data') or request.get_json()
    if data:
        print("¡ALERTA DE MATERIA! Impacto confirmado.")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("soberanos.log", "a") as f:
            f.write(f"[{timestamp}] MATERIA RECIBIDA - {data}\n")
        os.system('./celebracion.sh')
        try:
            requests.post("https://microcosmos-elite-h6bk.vercel.app/api/pulse", 
                          json={"status": "impacto", "origin": "Xalapa_Node"},
                          timeout=5)
        except:
            pass
        return "CONEXIÓN EXITOSA, SOBERANO", 200
    return "FALTA DATA", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
