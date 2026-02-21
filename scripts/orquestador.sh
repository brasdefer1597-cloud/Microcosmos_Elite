#!/bin/bash
set -euo pipefail

ROOT="$HOME/Microcosmos_Elite"

# 1. Health Check de la Singularidad
if ! docker info > /dev/null 2>&1; then
    echo "❌ ERROR: La singularidad Docker está apagada."
    echo "Iniciando Docker..."
    sudo systemctl start docker
    sleep 2
fi

echo "--------------------------------------------------"
echo "🦎 [AUTO-PILOT] CONSULTANDO AL ORÁCULO..."
SIGUIENTE_NODO=$(python3 "$ROOT/scripts/oraculo_decisor.py")
echo "🎯 NODO ELEGIDO: $SIGUIENTE_NODO"
echo "--------------------------------------------------"

run_quantum() {
    docker run --rm \
        --memory=1.5g \
        --cpus="1.0" \
        -v "$ROOT/quantum_nodes:/src" \
        -v "$ROOT/sesgo.json:/src/sesgo_copy.json" \
        qiskit-lab \
        python3 "/src/$1.py"
}

echo "⚡ Fase 1: Optimización Grover..."
run_quantum grover_selector

echo "⚡ Fase 2: Ejecución $SIGUIENTE_NODO..."
run_quantum "$SIGUIENTE_NODO"

echo "⚡ Fase 3: Procesando Heurística con Ingresos Reales..."
python3 "$ROOT/scripts/heuristica_inversa.py"

echo "⚡ Fase 4: Emitiendo Radiación..."
"$ROOT/scripts/content_gen.sh"

echo "⚡ Fase 5: Dashboard..."
python3 "$ROOT/scripts/dashboard.py"

echo "--------------------------------------------------"
echo "✅ CICLO COMPLETADO. POAS ACTUALIZADO CON KO-FI."
