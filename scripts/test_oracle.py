import os
import json
import requests

def test_ai_connection():
    # Tu llave vck_... funciona en el Gateway
    api_key = os.getenv("AI_GATEWAY_API_KEY")
    url = "https://gateway.ai/v1/chat/completions" # URL ajustada al Gateway
    
    try:
        with open('/home/chalamandramagistral/microcosmos_elite/data/ultimo_resultado.json', 'r') as f:
            datos = json.load(f)
        
        prompt = f"Analiza estos datos del Microcosmos: POAS {datos['poas']}x, Fidelidad {datos['fidelidad']}%. Dame una recomendación de inversión estratégica breve."
        
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "gpt-4-turbo", # O el modelo que tengas asignado en tu Gateway
            "messages": [{"role": "user", "content": prompt}]
        }
        
        response = requests.post(url, headers=headers, json=payload)
        
        if response.status_code == 200:
            print("\n🔮 CONSEJO DEL ORÁCULO:")
            print(response.json()['choices'][0]['message']['content'])
        else:
            print(f"\n❌ Error de Conexión: {response.status_code}")
            print(response.text)
            
    except Exception as e:
        print(f"⚠️ Error en el sistema: {e}")

if __name__ == "__main__":
    test_ai_connection()
