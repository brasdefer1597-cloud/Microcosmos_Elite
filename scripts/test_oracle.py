import os
import json
import requests
import time

def consultar_oraculo():
    api_key = os.getenv('AI_GATEWAY_API_KEY')
    if not api_key:
        print("❌ Error: AI_GATEWAY_API_KEY no está definida en el entorno.")
        return

    # Cargamos el último resultado del motor cuántico
    ruta_data = '/home/chalamandramagistral/microcosmos_elite/data/ultimo_resultado.json'
    try:
        with open(ruta_data, 'r') as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ Error al leer {ruta_data}: {e}")
        return

    # Payload para OpenAI (ChatCompletion)
    payload = {
        "model": "gpt-4o-mini",  # o gpt-4o, gpt-3.5-turbo, según tu plan
        "messages": [
            {"role": "system", "content": "Eres el Oráculo Cuántico del Nodo Xalapa. Analiza datos de simulación cuántica y da consejos soberanos."},
            {"role": "user", "content": f"""
Datos del motor Grover (6 qubits):
- Timestamp: {data['timestamp']}
- Fidelidad: {data['fidelidad']}%
- POAS: {data['poas']}x
- Mejor campaña: #{data['mejor_campana']}
- Estados: {data['estados']}

¿Es momento de escalar? ¿Qué acción recomiendas ahora mismo para maximizar soberanía?
Responde corto, directo y en tono guerrero.
"""}
        ],
        "temperature": 0.7,
        "max_tokens": 150
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    try:
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload, timeout=15)
        response.raise_for_status()
        result = response.json()
        mensaje = result['choices'][0]['message']['content'].strip()
        print("🌌 Respuesta del Oráculo:")
        print(mensaje)
    except requests.exceptions.RequestException as e:
        print(f"❌ Error de conexión al Oráculo: {e}")
        if hasattr(e.response, 'status_code'):
            print(f"Status: {e.response.status_code}")
            print(e.response.text)

if __name__ == "__main__":
    consultar_oraculo()
