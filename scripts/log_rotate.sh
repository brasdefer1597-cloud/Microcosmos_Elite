#!/bin/bash
LOG="/home/chalamandramagistral/Microcosmos_Elite/data/telemetry.jsonl"
DATE=$(date +"%Y-%m-%d")

if [ -f "$LOG" ]; then
    mv "$LOG" "/home/chalamandramagistral/Microcosmos_Elite/data/telemetry-$DATE.jsonl"
    gzip "/home/chalamandramagistral/Microcosmos_Elite/data/telemetry-$DATE.jsonl"
    echo "✅ Rotación completada: telemetry-$DATE.jsonl.gz"
fi
