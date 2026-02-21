#!/bin/bash
cd ~/Microcosmos_Elite/deploy

# Generar datos del Ciclo
LLAVE=$(openssl rand -hex 4 | tr '[:lower:]' '[:upper:]')
TIMESTAMP=$(date +%H:%M:%S)

# Simular lectura de Rango (Esto se conectará con tu LocalStorage después)
RANGO="SOBERANO_EN_ENTRENAMIENTO" 

# DISPARAR AL BÚNKER (Discord)
curl -H "Content-Type: application/json" -X POST -d "{
  \"username\": \"Chalamandra Operaciones\",
  \"embeds\": [{
    \"title\": \"🐍 REPORTE DE ESTADO: $TIMESTAMP\",
    \"color\": 15158332,
    \"fields\": [
      {\"name\": \"🔑 LLAVE ACTUAL\", \"value\": \"\`$LLAVE\`\", \"inline\": true},
      {\"name\": \"🏆 RANGO\", \"value\": \"$RANGO\", \"inline\": true},
      {\"name\": \"⚠️ ESTADO ORÁCULO\", \"value\": \"ACTIVO (Sin Fianzas)\", \"inline\": false}
    ],
    \"footer\": {\"text\": \"Enviado desde el Celeron N4020 - Xalapa Node\"}
  }]
}" $DISCORD_WEBHOOK

echo "✅ Dossier enviado al Búnker."
