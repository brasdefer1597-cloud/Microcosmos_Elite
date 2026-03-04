import requests
import json

def test_harvest():
    url = "http://localhost:5000/webhook-money"
    payload = {"amount": "1597", "currency": "USD", "from_name": "Inversor de Élite"}
    
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("💎 VICTORIA_CUANTICA_LOGRADA: Túnel de materia abierto.")
        else:
            print(f"⚠️ Error en radar: {response.status_code}")
    except Exception as e:
        print(f"❌ Fallo crítico de conexión: {e}")

if __name__ == "__main__":
    test_harvest()
