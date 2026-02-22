import subprocess
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/webhook/payment', methods=['POST'])
def payment_received():
    data = request.json
    print(f"💰 ¡PAGO DETECTADO! Cantidad: {data.get('amount')} {data.get('currency')}")
    
    # Ejecutar la celebración física en el búnker
    subprocess.Popen(["/bin/bash", "/home/chalamandramagistral/Microcosmos_Elite/celebracion.sh"])
    
    return jsonify({"status": "celebration_initiated", "message": "Materia capturada"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
