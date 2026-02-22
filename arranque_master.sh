#!/bin/bash
# Limpiar procesos viejos
fuser -k 5000/tcp
pkill -9 gunicorn

# Entrar al entorno y lanzar en segundo plano
cd ~/Microcosmos_Elite
source venv/bin/activate

# Usamos Gunicorn para que sea robusto y profesional
nohup gunicorn --workers 3 --bind 0.0.0.0:5000 app:app > ~/Chalamandra-HUB/activity.log 2>&1 &

echo "[$(date)] Cerebro iniciado en segundo plano con Gunicorn." >> ~/Chalamandra-HUB/activity.log
