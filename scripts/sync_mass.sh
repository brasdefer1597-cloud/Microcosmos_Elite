#!/bin/bash
ROOT="/home/chalamandramagistral/Microcosmos_Elite"

# 1. Calcular entropía (número de líneas en telemetría)
ENTROPIA=$(wc -l < "$ROOT/data/telemetry.jsonl" 2>/dev/null || echo 0)

# 2. Actualizar cloud_snapshot.json con la masa crítica y timestamp
TMP_FILE=$(mktemp)
jq --arg e "$ENTROPIA" \
   --arg t "$(date -u +"%Y-%m-%dT%H:%M:%SZ")" \
   '. + {masa_critica: ($e | tonumber), ultimo_pulso: $t}' \
   "$ROOT/hub/cloud_snapshot.json" > "$TMP_FILE"
mv "$TMP_FILE" "$ROOT/hub/cloud_snapshot.json"

# 3. Copiar a la carpeta deploy y subir a GitHub
cp "$ROOT/hub/cloud_snapshot.json" "$ROOT/deploy/"
cd "$ROOT/deploy"
git add cloud_snapshot.json
git commit -m "🦊 Pulso cuántico: masa $ENTROPIA" || true
git push origin main

echo "⚡ MASA CRÍTICA ACTUALIZADA: $ENTROPIA"
