#!/bin/bash
ROOT="$HOME/microcosmos_elite"

# 1. Notificar al Oráculo
$ROOT/scripts/notificar.sh "💰 ¡Materia Capturada! El Celeron N4020 está procesando..."

# 2. Activar entorno virtual y ejecutar simulación cuántica
source $ROOT/quantum_env/bin/activate
python3 $ROOT/scripts/shor_15.py

# 3. Instalar cmatrix si no está y mostrar efecto Matrix
if ! command -v cmatrix &> /dev/null; then
    sudo apt update && sudo apt install -y cmatrix
fi
timeout 5s cmatrix -C green
