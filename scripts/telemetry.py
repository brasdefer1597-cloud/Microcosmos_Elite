import json
import time
from pathlib import Path

LOG_FILE = Path("/home/chalamandramagistral/Microcosmos_Elite/data/telemetry.jsonl")

def log_event(event_type: str, fidelity: float = 0.0, temperature: float = 0.0, zram: int = 0, node: str = "", success: bool = False, entropy: float = None):
    entry = {
        "timestamp": time.time(),
        "event": event_type,
        "node": node,
        "success": success,
        "fidelity": round(fidelity, 4),
        "temperature": round(temperature, 1),
        "zram_usage_mb": zram,
        "entropy": entropy
    }
    # Filtrar claves con None para no ensuciar el JSON
    entry = {k: v for k, v in entry.items() if v is not None}
    
    with LOG_FILE.open("a", buffering=1) as f:
        f.write(json.dumps(entry) + "\n")

if __name__ == "__main__":
    # Ejemplo de uso
    log_event("simulacion", fidelity=0.99, temperature=45.2, zram=128, node="grover", success=True)
