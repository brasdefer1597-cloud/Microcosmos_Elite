#!/bin/bash
cd /home/chalamandramagistral/Microcosmos_Elite

# 1. Actualizar el Snapshot de la Masa Crítica
# Sumamos el total del money.log (esto es un ejemplo simple)
TOTAL=$(awk -F',' '{sum+=$1} END {print sum}' data/money.log)
echo "{\"masa_critica\": \"$TOTAL\", \"status\": \"Quantum Active\", \"last_update\": \"$(date)\"}" > data/cloud_snapshot.json

# 2. Empujar al Hub (GitHub)
git add data/cloud_snapshot.json data/money.log
git commit -m "🚀 Quantum Sync: Masa Crítica $TOTAL"
git push origin main
