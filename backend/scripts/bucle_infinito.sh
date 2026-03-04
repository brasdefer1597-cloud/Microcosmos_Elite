#!/bin/bash
ROOT="/home/chalamandramagistral/microcosmos_elite"

echo "🌌 Iniciando Simulación de Evolución Cósmica..."
while true; do
  # Monitoreo de RAM (Límite de Bekenstein)
  FREE_RAM=$(free -m | awk '/Mem:/ { print $4 }')
  
  if [ "$FREE_RAM" -lt 250 ]; then
    echo "⚠️ Saturación de Información detectada ($FREE_RAM MB). Ejecutando Purga Adiabática..."
    sudo sync; echo 3 | sudo tee /proc/sys/vm/drop_caches > /dev/null
  fi

  # Generar Masa Devorada (Ejecutar Shor)
  docker exec microcosmos_core python3 /app/scripts/shor_15.py
  
  # Sincronizar con el Horizonte (Vercel)
  $ROOT/scripts/sync_mass.sh
  
  echo "🟢 Estado del Cosmos: ESTABLE | RAM: ${FREE_RAM}MB"
  sleep 60
done
