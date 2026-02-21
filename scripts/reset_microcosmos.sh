#!/bin/bash
echo "🦎 Reiniciando el Microcosmos Elite..."

# 1. Limpieza de procesos
pkill -9 gunicorn
pkill -9 ngrok
sudo fuser -k 5000/tcp 2>/dev/null

# 2. Iniciar Gunicorn (Motor)
cd ~/Microcosmos_Elite
source venv/bin/activate
nohup gunicorn --workers 1 --bind 0.0.0.0:5000 --preload money_trigger:app > ~/Microcosmos_Elite/logs/money_server.log 2>&1 &
echo "✅ Motor Gunicorn iniciado."

# 3. Iniciar Ngrok (Túnel)
screen -dmS ngrok_tunnel /usr/local/bin/ngrok http 5000
echo "⏳ Generando URL pública..."

for i in {1..15}; do
    URL=$(curl -s http://localhost:4040/api/tunnels | jq -r '.tunnels[0].public_url')
    if [ "$URL" != "null" ] && [ -n "$URL" ]; then
        break
    fi
    sleep 1
done

if [ -z "$URL" ] || [ "$URL" == "null" ]; then
    echo "❌ Error: ngrok no respondió. Revisa con 'screen -r ngrok_tunnel'"
else
    echo "🌐 URL PÚBLICA: $URL"
    echo "📱 Notificaciones configuradas para Chalamandra Magistral."
    echo "$URL" > ~/Microcosmos_Elite/data/ultima_url.txt
fi
echo "🦎 Sistema 100% Operativo."
