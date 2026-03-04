#!/bin/bash
# Leer la última fidelidad registrada
ULTIMA_FID=$(tail -n 1 ~/microcosmos_elite/data/informe_cuantico.csv | cut -d',' -f3)

if (( $(echo "$ULTIMA_FID == 100.00" | bc -l) )); then
    echo "🌌 [ESTADO: NIRVANA] Fidelidad absoluta alcanzada."
    echo "🎯 Acción: Grover ha filtrado la campaña óptima con interferencia perfecta."
    # Aquí puedes añadir el comando para enviar un mensaje o activar un LED
else
    echo "📡 [ESTADO: ESCALANDO] Fidelidad actual: $ULTIMA_FID%. Optimizando iteraciones..."
fi
