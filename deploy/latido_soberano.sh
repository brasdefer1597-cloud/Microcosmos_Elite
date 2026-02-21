#!/bin/bash
TOKEN="8528209739:AAH2AYp1uEqK3vC0tZByBS_RWDKf76kvXms"
CHAT_ID="-1003260850014"
POAS=$(jq -r '.poas // "1.4"' ~/Microcosmos_Elite/deploy/status.json 2>/dev/null)
LLAVE=$(jq -r '.ultima_llave // "VQE_INIT"' ~/Microcosmos_Elite/deploy/status.json 2>/dev/null)

TEXTO="📡 *NODO XALAPA CONECTADO* 📡%0A%0A🔑 *Llave:* \`$LLAVE\`%0A📊 *POAS:* $POAS%0A🟢 _Sincronía total. El Oráculo está en línea._"

curl -s -X POST "https://api.telegram.org/bot$TOKEN/sendMessage" \
     -d "chat_id=$CHAT_ID" \
     -d "text=$TEXTO" \
     -d "parse_mode=Markdown"
