#!/bin/bash
LOG_FILE="$HOME/microcosmos_elite/data/money_server.log"
touch "$LOG_FILE"  # Asegura que existe
tail -Fn0 "$LOG_FILE" | while read LINE; do
  if echo "$LINE" | grep -qiE "error|fail|critical"; then
    ~/microcosmos_elite/scripts/notificar.sh "⚠️ ALERTA CRÍTICA EN BÚNKER: $LINE"
  fi
done
