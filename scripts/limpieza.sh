#!/bin/bash
# Comprimir logs viejos y limpiar Docker
find ~/Microcosmos_Elite/data/*.jsonl -mtime +1 -exec gzip {} \;
docker container prune -f
