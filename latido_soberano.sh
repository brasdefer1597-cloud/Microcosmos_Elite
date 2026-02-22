#!/bin/bash
while true
do
  # Extraer log real omitiendo basura
  STATUS=$(docker logs microcosmos_core 2>&1 | grep "FACTORIZACIÓN" | tail -n 1)
  if [ -z "$STATUS" ]; then STATUS="EJECUTANDO_SHOR_MODERN_V2"; fi

  # Enviar al Hub
  RESPONSE=$(curl -s -X POST -H "Content-Type: application/json" \
       -d "{\"status\": \"$STATUS\", \"node\": \"XALAPA_01\"}" \
       https://microcosmos-elite-h6bk.vercel.app/api/telemetry)
       
  if [[ $RESPONSE == *"SYNC_OK"* ]]; then
    echo -e "\e[32m[VICTORIA]\e[0m Sincronizado: $STATUS"
  else
    echo -e "\e[31m[ERROR]\e[0m Hub no responde."
  fi
  sleep 15
done
