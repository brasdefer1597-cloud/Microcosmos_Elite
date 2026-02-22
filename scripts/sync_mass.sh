#!/bin/bash
# NODO #10: Gamificación y Ascensión
RESULTS_FILE="/home/chalamandramagistral/Microcosmos_Elite/data/resultados_shor.csv"
STATUS_FILE="/home/chalamandramagistral/Chalamandra-HUB/status.json"

# Extraer última fidelidad del simulador
ULTIMA_FIDELIDAD=$(tail -n 1 $RESULTS_FILE | cut -d',' -f2)

# Calcular nueva Masa Crítica (Base 1.0 + (Fidelidad / 10))
# Si la fidelidad es 95%, MC sube +9.5
NUEVA_MC=$(echo "scale=2; 1.0 + ($ULTIMA_FIDELIDAD / 10)" | bc)

# Actualizar el Corazón del HUB
jq ".masa_critica = $NUEVA_MC | .ultima_fidelidad = $ULTIMA_FIDELIDAD" $STATUS_FILE > tmp.json && mv tmp.json $STATUS_FILE

echo "✨ NODO #10: Masa Crítica elevada a $NUEVA_MC basada en Fidelidad $ULTIMA_FIDELIDAD%"
