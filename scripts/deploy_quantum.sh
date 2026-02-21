#!/bin/bash
# 1. Calcular total real
TOTAL=$(tr ',' '\n' < /home/chalamandramagistral/Microcosmos_Elite/data/money.log | awk -F',' '{for(i=1;i<=NF;i++) if($i ~ /^[0-9.]+$/) s+=$i} END {print s}')

# 2. Inyectar dato en la raíz del HUB (donde está tu app.py)
echo "{\"masa_critica\": \"$TOTAL\", \"last_update\": \"$(date)\"}" > /home/chalamandramagistral/Chalamandra-HUB/cloud_snapshot.json

# 3. Empujar al GitHub del HUB (brasdefer1597-cloud/Chalamandra-HUB)
cd /home/chalamandramagistral/Chalamandra-HUB
git add .
git commit -m "🚀 Quantum Sync: $TOTAL"
git push origin main

# 4. Respaldar el Búnker
cd /home/chalamandramagistral/Microcosmos_Elite
git add .
git commit -m "📦 Búnker Sync: $TOTAL"
git push origin main
