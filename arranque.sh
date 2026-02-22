#!/bin/bash
# ============================================
# 🚀 Microcosmos Elite - GUNICORN VENV EDITION
# ============================================

echo "[INFO] Liquidando procesos antiguos..."
pkill -f python3
pkill -f gunicorn

cd ~/Microcosmos_Elite || exit 1

echo "[INFO] Iniciando Gunicorn desde el entorno virtual..."
# Usamos la ruta exacta al binario del entorno virtual
./venv/bin/gunicorn --bind 0.0.0.0:5000 app:app --daemon --workers 2

sleep 3

echo "[INFO] Lanzando prueba de inyección de materia..."
curl -s -X POST http://127.0.0.1:5000/webhook/payment \
     -d 'data={"from_name": "Inversor_Elite", "amount": "100.00", "currency": "USD"}'

echo -e "\n[INFO] Estado de la Masa Crítica:"
curl -s http://127.0.0.1:5000/api/status | grep -o '"masa_critica":[0-9.]*'

echo -e "\n[INFO] 🔥 SISTEMA OPERATIVO Y BLINDADO."
