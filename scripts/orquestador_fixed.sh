#!/bin/bash
echo "🦎 INICIANDO CICLO AUTÓNOMO CHALAMANDRA (VERSIÓN CORREGIDA)..."
# 1. Pensar (Grover elige el camino)
python3 ~/Microcosmos_Elite/quantum_nodes/grover_selector.py
# 2. Actuar (VQE ejecuta con inteligencia inyectada)
python3 ~/Microcosmos_Elite/quantum_nodes/vqe_hydrogen.py
# 3. Analizar (Heurística actualiza el sesgo)
python3 ~/Microcosmos_Elite/scripts/heuristica_inversa.py
# 4. Hablar (Generar el post para el mundo)
~/Microcosmos_Elite/scripts/content_gen.sh
# 5. Visualizar (Actualizar el dashboard)
python3 ~/Microcosmos_Elite/scripts/dashboard.py
echo "✅ CICLO COMPLETADO. SISTEMA EVOLUCIONADO."
