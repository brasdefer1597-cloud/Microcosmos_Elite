#!/bin/bash
MONTO=$1
NOMBRE=$2

# 1. GENERAR LLAVE DE 8 DÍGITOS
LLAVE=$(cat /dev/urandom | tr -dc '0-9' | fold -w 8 | head -n 1)

# 2. AVISO SONORO Y VISUAL
echo -e "\a\a\a"
clear
echo -e "\033[1;35m"
echo "##################################################"
echo "         🦎 ACCESO AL ORÁCULO GENERADO          "
echo "##################################################"
echo -e "\033[1;32m"
echo "  INVERSOR: $NOMBRE"
echo "  MATERIA:  \$$MONTO"
echo "  TOKEN:    $LLAVE"
echo -e "\033[1;34m"
echo "  Sincronizando con el Clúster y Vercel..."
echo -e "\033[0m"

# 3. ACTUALIZAR SNAPSHOT CON TODA LA LÓGICA DE ESCALA
# Leemos cuántos workers hay en el archivo de registro
if [ -f "/home/chalamandramagistral/Microcosmos_Elite/data/workers_active.json" ]; then
    WORKER_COUNT=$(jq '. | length' /home/chalamandramagistral/Microcosmos_Elite/data/workers_active.json)
else
    WORKER_COUNT=1
fi

python3 -c "
import json
path='/home/chalamandramagistral/Microcosmos_Elite/hub/cloud_snapshot.json'
with open(path, 'r+') as f:
    d = json.load(f)
    d['masa_critica'] = round(float(d.get('masa_critica', 0)) + float('$MONTO'), 2)
    d['ultima_llave'] = '$LLAVE'
    d['nodos_activos'] = $WORKER_COUNT
    d['prediccion_trafico_24h'] = str(round(float(d['masa_critica']) * 12.5)) + ' req/s'
    d['status_red'] = 'EXPANDING' if $WORKER_COUNT > 1 else 'STABLE'
    f.seek(0)
    json.dump(d, f, indent=2)
    f.truncate()
"

# 4. PUSH AUTOMÁTICO A GITHUB/VERCEL
~/Microcosmos_Elite/scripts/update_hub.sh
