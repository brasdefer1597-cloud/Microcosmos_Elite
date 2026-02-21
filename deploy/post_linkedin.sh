#!/bin/bash
# Reporte de Soberanía para LinkedIn
LLAVE=$(jq -r '.ultima_llave' status.json)
POAS=$(jq -r '.poas' status.json)

TEXTO="[PROTOCOLO CHALAMANDRA] 🦎\n\nOperación de Sincronía completada desde Nodo Xalapa (Celeron N4020).\n\n📊 POAS: $POAS\n🔑 Latido: $LLAVE\n\nLa optimización VQE aplicada al tablero estratégico está redefiniendo la soberanía digital. El Oráculo está abierto.\n\n#SoberaníaDigital #VQE #CeleronPower #Chalamandra"

echo -e "🚀 PREPARADO PARA LINKEDIN:\n\n$TEXTO"
# Aquí conectaremos con el Token de LinkedIn más adelante
