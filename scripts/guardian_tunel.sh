#!/bin/bash
# --- EL OJO DE CHALAMANDRA: WATCHDOG DE CONECTIVIDAD ---

# 1. Obtener la URL actual de ngrok
URL_ACTUAL=$(curl -s http://localhost:4040/api/tunnels | jq -r '.tunnels[0].public_url')
ULTIMA_URL_CONOCIDA=$(cat ~/Microcosmos_Elite/data/ultima_url.txt 2>/dev/null)

# 2. Verificar si ngrok está caído
if [ -z "$URL_ACTUAL" ] || [ "$URL_ACTUAL" == "null" ]; then
    echo "$(date): 🚨 ALERTA: ngrok está offline. Intentando reiniciar..." >> ~/Microcosmos_Elite/logs/guardian.log
    bash ~/Microcosmos_Elite/scripts/reset_microcosmos.sh
    exit 1
fi

# 3. Si la URL cambió, notificar a la Jefa
if [ "$URL_ACTUAL" != "$ULTIMA_URL_CONOCIDA" ]; then
    echo "$URL_ACTUAL" > ~/Microcosmos_Elite/data/ultima_url.txt
    
    # Notificar a Telegram
    TOKEN="TU_TOKEN_BOT"
    CHAT_ID="TU_CHAT_ID"
    MENSAJE="⚠️ <b>ALERTA DE MOVIMIENTO:</b>%0AEl túnel ha rotado.%0A%0A🌐 <b>Nueva URL:</b>%0A<code>$URL_ACTUAL</code>%0A%0A✍️ Actualiza Ko-fi de inmediato."
    
    curl -s -X POST "https://api.telegram.org/bot$TOKEN/sendMessage" \
         -d "chat_id=$CHAT_ID" \
         -d "text=$MENSAJE" \
         -d "parse_mode=HTML"
    
    echo "$(date): URL actualizada y notificada: $URL_ACTUAL" >> ~/Microcosmos_Elite/logs/guardian.log
fi
