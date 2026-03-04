#!/bin/bash
echo "🌀 Sincronizando Microcosmos con la Nube..."
cd ~/microcosmos_elite
git pull origin main
cd frontend && npm install && npm run build
echo "🚀 Despliegue completado. Sistema en línea."
