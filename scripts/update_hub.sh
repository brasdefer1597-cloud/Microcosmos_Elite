#!/bin/bash
# 1. Variables de entorno
SOURCE_JSON="/home/chalamandramagistral/Microcosmos_Elite/hub/cloud_snapshot.json"
TARGET_DIR="/home/chalamandramagistral/Microcosmos_Elite/deploy"
LOG_FILE="/home/chalamandramagistral/Microcosmos_Elite/data/telemetry.jsonl"

# 2. Generar JSON con Entropía
ENTROPIA=$(wc -l < "$LOG_FILE")
jq --arg e "$ENTROPIA" '. + {masa_critica: $e}' "$SOURCE_JSON" > "$TARGET_DIR/public/data.json"

# 3. Empujar a la Nube (Solo si hay un repo configurado)
cd "$TARGET_DIR"
if [ -d ".git" ]; then
    git add public/data.json
    git commit -m "🦎 Quantum Heartbeat: Entropy $ENTROPIA - $(date +'%H:%M:%S')"
    git push origin main
    echo "🚀 Datos emitidos al Horizonte de Sucesos (GitHub/Vercel)"
else
    echo "⚠️  Aviso: Carpeta deploy lista, pero no vinculada a GitHub aún."
fi
