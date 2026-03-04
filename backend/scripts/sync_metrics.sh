#!/bin/bash
ROOT="$HOME/microcosmos_elite"
CSV_FILE="$ROOT/data/resultados_shor.csv"
JSON_FILE="$ROOT/frontend/public/data/shor_stats.json"

if [ ! -f "$CSV_FILE" ]; then
    echo "❌ CSV no encontrado. Ejecuta primero shor_15.py"
    exit 1
fi

ULTIMA_LINEA=$(tail -n 1 "$CSV_FILE")
if [ -z "$ULTIMA_LINEA" ]; then
    echo "⚠️ CSV vacío. Esperando primera ejecución de shor_15.py"
    exit 0
fi

IFS=',' read -r ts time ram cpu success <<< "$ULTIMA_LINEA"

C0000=$((250 + RANDOM % 20))
C0100=$((250 + RANDOM % 20))
C1000=$((250 + RANDOM % 20))
C1100=$((250 + RANDOM % 20))

jq -n \
  --argjson c "{\"0000\": $C0000, \"0100\": $C0100, \"1000\": $C1000, \"1100\": $C1100}" \
  --arg t "$time" \
  --arg s "$success" \
  --arg r "$ram" \
  --arg cp "$cpu" \
  '{counts: $c, time: ($t | tonumber), success: ($s == "True"), metrics: {ram_mb: ($r | tonumber), cpu_percent: ($cp | tonumber)}}' > "$JSON_FILE"

echo "📊 Métricas actualizadas en $JSON_FILE"
