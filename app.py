import json, os, subprocess
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"status": "Soberano", "nodo": "Xalapa", "sistema": "Microcosmos Elite"})

@app.route('/money-trigger', methods=['POST'])
def money_trigger():
    print("\n💰 [SISTEMA] ¡INYECCIÓN DE CAPITAL DETECTADA!")
    try:
        # Lanza la lluvia Matrix que creamos antes
        subprocess.Popen(["bash", "./scripts/celebracion.sh"])
        return jsonify({"status": "Singularidad Alcanzada", "mensaje": "Celebración iniciada"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
