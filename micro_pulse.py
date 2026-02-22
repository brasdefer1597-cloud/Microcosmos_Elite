import requests
import json

data = {
    "node": "XALAPA-CENTRAL",
    "entropy": 27,
    "critical_mass": 1134,
    "quantum_fidelity": 0.9882,
    "disk_avail": "4.6G",
    "status": "Shor_Ready"
}

def sync_hub():
    # URL de tu HUB en Vercel
    url = "https://chalamandra-hub.vercel.app/api/telemetry"
    try:
        response = requests.post(url, json=data, timeout=10)
        print(f"📡 Sincronización exitosa: {response.status_code}")
    except Exception as e:
        print(f"⚠️ Error de entrelazamiento: {e}")

if __name__ == "__main__":
    sync_hub()
