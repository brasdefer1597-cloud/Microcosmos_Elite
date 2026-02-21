#!/bin/bash
cd /home/chalamandramagistral/Microcosmos_Elite

# Actualizar el snapshot con el nuevo balance
# (Esto asume que guardamos montos separados por comas en money.log)
TOTAL=$(tr ',' '\n' < data/money.log | awk '{s+=$1} END {print s}')

echo "{\"masa_critica\": \"$TOTAL\", \"last_update\": \"$(date)\"}" > data/cloud_snapshot.json

# Empujar cambios al Hub
git add data/cloud_snapshot.json data/money.log
git commit -m "🚀 Actualización Automática: Masa Crítica $TOTAL"
git push origin main
