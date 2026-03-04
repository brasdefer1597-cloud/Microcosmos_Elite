#!/bin/bash
# Cálculo de Salud del Sistema (LTV vs CPA)
TOTAL_INGRESOS=$(awk -F',' '{sum+=$1} END {print sum}' ../data/money.log)
TOTAL_LEADS=$(wc -l < ../data/telemetry.jsonl)

# ROAS Simulado (Retorno de Inversión)
if [ $TOTAL_LEADS -gt 0 ]; then
    LTV=$(echo "scale=2; $TOTAL_INGRESOS / $TOTAL_LEADS" | bc)
    echo "📈 LTV por Lead: \$$LTV"
    echo "📊 ROAS Global: $(echo "scale=2; $TOTAL_INGRESOS / 1" | bc)x" # Asumiendo costo de infraestructura 0 (Guerrilla)
fi
