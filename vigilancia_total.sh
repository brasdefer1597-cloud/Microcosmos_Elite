#!/bin/bash
while true; do
  clear
  echo "=== MONITOR DE ECOSISTEMA SOBERANO - $(date) ==="
  echo "[1] NODO XALAPA: $(docker ps --format '{{.Status}}' --filter name=microcosmos_core)"
  echo "[2] TELEMETRÍA: $(curl -s -I https://microcosmos-elite-h6bk.vercel.app/api/telemetry | grep "HTTP/2 200")"
  echo "[3] CTR ACTUAL: $(curl -s https://microcosmos-elite-h6bk.vercel.app/api/telemetry | jq -r '.ctr // "N/A"')"
  echo "[4] MEMORIA zRAM: $(free -h | grep "Swap" | awk '{print $3 " / " $2}')"
  echo "------------------------------------------------"
  echo "Últimos Logs de Shor:"
  docker logs microcosmos_core --tail 3
  sleep 30
done
