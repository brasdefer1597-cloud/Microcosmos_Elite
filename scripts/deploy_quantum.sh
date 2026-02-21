#!/bin/bash
# 1. Calcular Masa Crítica
LOG_FILE="/home/chalamandramagistral/Microcosmos_Elite/data/money.log"
TOTAL=$(tr ',' '\n' < "$LOG_FILE" | awk -F',' '{for(i=1;i<=NF;i++) if($i ~ /^[0-9.]+$/) s+=$i} END {print s}')

# 2. Actualizar HUB
HUB_DIR="/home/chalamandramagistral/Chalamandra-HUB"
echo "{\"masa_critica\": \"$TOTAL\", \"last_update\": \"$(date)\"}" > "$HUB_DIR/cloud_snapshot.json"
cd "$HUB_DIR"
git add .
git commit -m "🚀 Sync Masa Crítica: $TOTAL"
git push origin main --force

# 3. Respaldar Búnker
cd /home/chalamandramagistral/Microcosmos_Elite
git add .
git commit -m "📦 Backup: $TOTAL"
git push origin main
