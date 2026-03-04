#!/bin/bash
# 1. Mira cuánto dinero ha entrado (Masa Devorada)
TOTAL_DINERO=$(awk -F',' '{sum+=$1} END {print sum}' ~/microcosmos_elite/data/money.log 2>/dev/null || echo 0)

# 2. Mira cuántos datos has generado (Entropía)
TOTAL_DATOS=$(wc -l < ~/microcosmos_elite/data/telemetry.jsonl 2>/dev/null || echo 0)

echo "------------------------------------------"
echo "📊 REPORTE DEL NODO XALAPA"
echo "💰 Dinero Total (LTV): \$$TOTAL_DINERO"
echo "🌌 Datos Generados (Entropía): $TOTAL_DATOS eventos"
echo "------------------------------------------"
