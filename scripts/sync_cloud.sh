#!/bin/bash
# Ir a la carpeta vinculada a tu repo de GitHub
cd ~/Microcosmos_Elite/deploy
# Copiar el último snapshot generado por el orquestador
cp ~/Microcosmos_Elite/hub/cloud_snapshot.json .
# Subir a la nube
git add cloud_snapshot.json
git commit -m "🦎 Autonomous Update: POAS $(jq .poas cloud_snapshot.json)"
git push origin main
