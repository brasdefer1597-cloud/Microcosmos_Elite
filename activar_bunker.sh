#!/bin/bash
echo "Iniciando Receptor de Materia..."
python3 money_trigger.py & 
sleep 2
echo "Abriendo Túnel SSH (Serveo)..."
ssh -R 80:localhost:5002 serveo.net
