#!/bin/bash
ROOT="/home/chalamandramagistral/microcosmos_elite"
DATA_FILE="$ROOT/data/cloud_snapshot.json"

# Solo actualización local de variables
MASA_DEVORADA=$(awk -F',' '{sum+=$1} END {print sum}' "$ROOT/data/money.log" 2>/dev/null || echo 0)
ENTROPIA_S=$(wc -l < "$ROOT/data/telemetry.jsonl" 2>/dev/null || echo 0)
REDSHIFT_Z=$(tail -n 1 "$ROOT/data/telemetry.jsonl" | cut -d':' -f3 || echo 0.00)

jq -n --arg s "$ENTROPIA_S" --arg z "$REDSHIFT_Z" --arg m "$MASA_DEVORADA" \
--arg owner "brasdefer1597-cloud" \
'{entropia: ($s | tonumber), redshift: ($z | tonumber), masa_devorada: ($m | tonumber), status: "LOCAL_ISOLATION", owner: $owner}' > "$DATA_FILE"

echo "🔒 Snapshot actualizado localmente. Sin radiación externa."
