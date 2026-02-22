#!/bin/bash
while true; do
    if ! pgrep -f "python3 /home/chalamandramagistral/Microcosmos_Elite/app.py" > /dev/null; then
        echo "[$(date)] Reiniciando Cerebro..." >> ~/Chalamandra-HUB/activity.log
        python3 /home/chalamandramagistral/Microcosmos_Elite/app.py &
    fi
    sleep 60
done
