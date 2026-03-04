#!/bin/bash
ROOT="/home/chalamandramagistral/microcosmos_elite"
DATA_FILE="$ROOT/data/cloud_snapshot.json"

# Asegurar que los archivos existen
touch "$ROOT/data/telemetry.jsonl"
touch "$ROOT/data/resultados_shor.log"

# Capturar métricas
ENTROPIA=$(wc -l < "$ROOT/data/telemetry.jsonl")
FIDELIDAD=$(grep -oP 'fidelidad:\s*\K[0-9.]+' "$ROOT/data/resultados_shor.log" | tail -1)
: ${FIDELIDAD:=0} # Si está vacío, poner 0

# Actualizar JSON
jq -n --arg ent "$ENTROPIA" --arg fid "$FIDELIDAD" \
'.masa_critica = ($ent | tonumber) | .ultima_fidelidad = ($fid | tonumber)' > "$DATA_FILE"

# Notificar al Nodo Xalapa
$ROOT/scripts/notificar.sh "✨ NODO #10: Masa Crítica $ENTROPIA | Fidelidad $FIDELIDAD%"

# Despliegue (solo si existe la carpeta)
if [ -d "$ROOT/frontend" ]; then
  cd "$ROOT/frontend" && vercel --prod --yes
else
  echo "Error: Carpeta frontend no encontrada."
fi
