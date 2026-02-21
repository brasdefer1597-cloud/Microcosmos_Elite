#!/bin/bash
# Matar procesos previos para evitar colisiones
pkill cloudflared
# Lanzar el túnel y guardar la URL en un log para Jules
/usr/local/bin/cloudflared tunnel --url http://localhost:8080 > ~/Microcosmos_Elite/deploy/tunel.log 2>&1 &
