#!/bin/bash
TOKEN="TU_TOKEN_AQUI"
CHAT_ID="-1003260850014"
REPORTE=$(~/Microcosmos_Elite/scripts/radiacion_global.sh | tail -n 15)

curl -s -X POST https://api.telegram.org/bot$TOKEN/sendMessage \
     -d chat_id=$CHAT_ID \
     -d text="🚀 REPORTANDO DESDE EL NODO XALAPA:
     
$REPORTE" > /dev/null

echo "✉️ Reporte enviado al Gran Oráculo (Telegram)."
