import json
import os

SESGO_PATH = "/home/chalamandramagistral/Microcosmos_Elite/sesgo.json"

def decidir_siguiente_paso():
    try:
        with open(SESGO_PATH, "r") as f:
            sesgo = json.load(f)
        
        poas = sesgo.get("poas_real", -1.0)
        brillo = sesgo.get("brillo_cuantico", 0)

        # LÓGICA DE SUPERVIVENCIA
        if poas < 0:
            # Si perdemos dinero, prioridad absoluta a Grover (Búsqueda de Mercado)
            return "grover_selector"
        elif brillo < 0.1:
            # Si el valor es bajo, optimizar con VQE
            return "vqe_hydrogen"
        else:
            # Solo si hay rentabilidad, ejecutamos el costoso Shor
            return "shor_15"
            
    except:
        return "vqe_hydrogen"

if __name__ == "__main__":
    print(decidir_siguiente_paso())
