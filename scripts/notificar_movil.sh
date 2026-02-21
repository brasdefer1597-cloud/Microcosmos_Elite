#!/bin/bash
TOKEN="TU_TOKEN_AQUI"
CHAT_ID="TU_CHAT_ID_AQUI"
MONTO=$1
MSG="🦎 <b>INYECCIÓN DETECTADA</b>%0A💰 Monto: \$$MONTO%0A🔑 Llave: $(jq -r '.ultima_llave' ~/Microcosmos_Elite/hub/cloud_snapshot.json)"

curl -s -X POST "https://api.telegram.org/bot$TOKEN/sendMessage" \
     -d "chat_id=$CHAT_ID" \
     -d "text=$MSG" \
     -d "parse_mode=HTML"
