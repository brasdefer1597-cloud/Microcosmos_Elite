#!/bin/bash
ROOT="$HOME/microcosmos_elite"
while true; do
    echo "💓 Latido: $(date)"
    python3 "$ROOT/scripts/shor_15.py"
    bash "$ROOT/scripts/sync_metrics.sh"
    sleep 10
done
