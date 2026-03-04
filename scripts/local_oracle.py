import json
import os
import subprocess

def analista_local():
    ruta = '/home/chalamandramagistral/microcosmos_elite/data/ultimo_resultado.json'
    # Código ANSI para Rosa/Magenta vibrante
    ROSA = '\033[1;95m'
    RESET = '\033[0m'
    
    try:
        with open(ruta, 'r') as f:
            d = json.load(f)
        
        # Limpiamos pantalla para el gran debut
        os.system('clear')
        
        print(f"{ROSA}")
        # Usamos figlet para el título en grande
        subprocess.run(['figlet', 'MICROCOSMOS'])
        print(f"--------------------------------------------------")
        
        if d['poas'] >= 3.5:
            subprocess.run(['figlet', '-f', 'small', 'ESCALAR!'])
            print(f"ESTADO: POAS DE {d['poas']} ES OPTIMO.")
        else:
            subprocess.run(['figlet', '-f', 'small', 'ESPERAR...'])
            print(f"ESTADO: POAS DE {d['poas']} BAJO VIGILANCIA.")
            
        print(f"\nFIDELIDAD: {d['fidelidad']}% | QUBITS: {d['qubits']}")
        print(f"--------------------------------------------------{RESET}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    analista_local()
