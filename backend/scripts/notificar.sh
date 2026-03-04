#!/bin/bash
BOT_TOKEN="8528209739:AAH2AYp1uEqK3vC0tZByBS_RWDKf76kvXms"
CHAT_ID="-1003260850014"
MESSAGE=$1
curl -s -X POST "https://api.telegram.org/bot$BOT_TOKEN/sendMessage" -d "chat_id=$CHAT_ID" -d "text=🛡️ *NODO XALAPA:* $MESSAGE" -d "parse_mode=Markdown"
