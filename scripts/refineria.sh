#!/bin/bash
# Simulación de recepción de tráfico desde el Amplificador
SOURCE=$1
CAMPAIGN=$2

if [ -z "$SOURCE" ]; then SOURCE="directo"; fi

LOG_ENTRY="{\"ts\": $(date +%s), \"event\": \"clic_refineria\", \"source\": \"$SOURCE\", \"campaign\": \"$CAMPAIGN\"}"

echo $LOG_ENTRY >> ~/Microcosmos_Elite/data/telemetry.jsonl
echo "✅ Tráfico inyectado desde $SOURCE. Refinería procesando..."
