import os, json, time, psutil, subprocess, sys, math, re

class ChalamandraEngine:
    def __init__(self):
        self.root = "/home/chalamandramagistral/Microcosmos_Elite"
        self.data_stream = f"{self.root}/data/telemetry.jsonl"
        self.sesgo_path = f"{self.root}/sesgo.json"

    def calcular_entropia(self, output):
        match = re.search(r"\{[^}]+\}", output)
        if match:
            try:
                freqs = eval(match.group())
                total = sum(freqs.values())
                probs = [f/total for f in freqs.values()]
                return round(-sum(p * math.log2(p) for p in probs if p > 0), 3)
            except: return None
        return None

    def run(self, node):
        start = time.time()
        
        # LÓGICA DE INYECCIÓN: Leer ángulo del sesgo si vamos a correr VQE
        extra_args = []
        if os.path.exists(self.sesgo_path):
            with open(self.sesgo_path, "r") as f:
                sesgo = json.load(f)
                if node == "vqe_hydrogen" and "vqe_angulo" in sesgo:
                    extra_args = [str(sesgo["vqe_angulo"])]

        cmd = ["docker", "run", "--rm", "-v", f"{self.root}/quantum_nodes:/src", "qiskit-lab", "python3", f"/src/{node}.py"] + extra_args
        
        proc = subprocess.run(cmd, capture_output=True, text=True)
        output_str = proc.stdout.strip()
        
        # Si ejecutamos el selector de Grover, el motor actualiza el sesgo automáticamente
        if node == "grover_selector" and "Selección óptima de parámetro:" in output_str:
            nuevo_angulo = output_str.split("parámetro: ")[1].split(" ")[0]
            with open(self.sesgo_path, "r+") as f:
                data = json.load(f)
                data["vqe_angulo"] = float(nuevo_angulo)
                f.seek(0); json.dump(data, f, indent=4); f.truncate()

        log = {
            "ts": time.time(), "node": node, "success": proc.returncode == 0,
            "duration": round(time.time() - start, 2),
            "entropy": self.calcular_entropia(output_str),
            "output": output_str
        }
        
        with open(self.data_stream, "a") as f:
            f.write(json.dumps(log) + "\n")
        
        print(f"🚀 [V6-ADAPTIVE] {node} ejecutado. Status: OK")
