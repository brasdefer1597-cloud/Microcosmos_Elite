#!/bin/bash
while true; do
  # Mira cuánta RAM queda libre
  RAM_LIBRE=$(free -m | awk '/Mem:/ { print $4 }')
  
  # Si queda menos de 300MB, limpia la basura
  if [ "$RAM_LIBRE" -lt 300 ]; then
    echo "⚠️ Memoria baja ($RAM_LIBRE MB). Limpiando sistema..."
    sudo sync; echo 3 | sudo tee /proc/sys/vm/drop_caches > /dev/null
  fi
  
  sleep 30 # Revisa cada 30 segundos
done
