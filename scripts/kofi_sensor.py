import requests
import json
import os

# CONFIGURACIÓN
KOFI_TOKEN = "TU_TOKEN_AQUÍ" # Consíguelo en Ko-fi -> Buttons & Widgets -> Webhooks
SESGO_PATH = "/home/chalamandramagistral/Microcosmos_Elite/sesgo.json"

def obtener_ingresos_reales():
    # Nota: Ko-fi suele usar Webhooks, pero para este búnker 
    # simularemos la captura de la última "Donación/Suscripción"
    # vía un archivo de log que tu servidor web reciba.
    ingresos_totales = 0
    try:
        # Aquí iría el fetch a la API o lectura de log de webhook
        # Por ahora, extraemos el 'pago_reciente' de un archivo temporal
        if os.path.exists("kofi_log.json"):
            with open("kofi_log.json", "r") as f:
                data = json.load(f)
                ingresos_totales = sum(item['amount'] for item in data)
    except:
        pass
    return ingresos_totales

if __name__ == "__main__":
    valor = obtener_ingresos_reales()
    print(valor)
