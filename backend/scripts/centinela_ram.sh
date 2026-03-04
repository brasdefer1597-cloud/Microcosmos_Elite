#!/bin/bash
echo "🛡️ Centinela de RAM Activado [Umbral: 200MB]"
while true; do
  FREE_RAM=$(free -m | awk '/Mem:/ { print $4 }')
  if [ "$FREE_RAM" -lt 200 ]; then
    echo "⚠️ RAM Crítica ($FREE_RAM MB). Ejecutando Purga de Guerrilla..."
    sudo sync; echo 3 | sudo tee /proc/sys/vm/drop_caches > /dev/null
    ~/microcosmos_elite/scripts/notificar.sh "♻️ Purga de RAM completada en Nodo Xalapa."
  fi
  sleep 5
done
