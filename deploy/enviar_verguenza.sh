#!/bin/bash
TOKEN="8528209739:AAH2AYp1uEqK3vC0tZByBS_RWDKf76kvXms"
CHAT_ID="-1003260850014"

USUARIO=${1:-"Invasor"}
MOVIMIENTOS=${2:-"?"}
# URL Sincronizada con el Hub de Vercel
URL_HUB="https://chalamandra-hub.vercel.app/partidas"

TEXTO="🔞 *DOSSIER DE VERGÜENZA* 🔞%0A%0A👤 *Sujeto:* $USUARIO%0A♟️ *Caída:* $MOVIMIENTOS movimientos%0A🌐 *Evidencia:* [Ver en Chalamandra HUB]($URL_HUB)%0A%0A🐍 _Sincronía Xalapa-Vercel establecida._"

curl -s -X POST "https://api.telegram.org/bot$TOKEN/sendMessage" \
     -d "chat_id=$CHAT_ID" \
     -d "text=$TEXTO" \
     -d "parse_mode=Markdown"
