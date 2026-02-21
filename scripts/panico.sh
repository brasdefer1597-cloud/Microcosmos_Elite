#!/bin/bash
echo "🛡️ ACTIVANDO MODO PÁNICO..."
# Matar ngrok y gunicorn
pkill ngrok
pkill gunicorn
pkill -f money_trigger
# Cerrar puertos en el firewall
sudo ufw deny 5000/tcp
echo "🔒 Búnker sellado. Conexiones externas cortadas."
