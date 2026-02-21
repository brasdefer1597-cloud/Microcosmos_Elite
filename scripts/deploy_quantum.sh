#!/bin/bash
# 1. Calcular total real (Masa Crítica)
LOG_FILE="/home/chalamandramagistral/Microcosmos_Elite/data/money.log"
TOTAL=$(tr ',' '\n' < "$LOG_FILE" | awk -F',' '{for(i=1;i<=NF;i++) if($i ~ /^[0-9.]+$/) s+=$i} END {print s}')

# 2. Actualizar el HUB
HUB_DIR="/home/chalamandramagistral/Chalamandra-HUB"
if [ -d "$HUB_DIR" ]; then
    echo "{\"masa_critica\": \"$TOTAL\", \"last_update\": \"$(date)\"}" > "$HUB_DIR/cloud_snapshot.json"
    cd "$HUB_DIR"
    git add .
    git commit -m "🚀 Quantum Sync: $TOTAL"
    git push origin main
else
    echo "⚠️ Error: No se encuentra la carpeta HUB"
fi

# 3. Respaldar el Búnker
cd /home/chalamandramagistral/Microcosmos_Elite
git add .
git commit -m "📦 Búnker Sync: $TOTAL"
git push origin main
