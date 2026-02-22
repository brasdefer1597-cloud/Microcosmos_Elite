#!/bin/bash
# Uso: ./registrar_venta.sh 97 "Nombre Cliente"
MONTO=$1
CLIENTE=$2
FECHA=$(date '+%Y-%m-%d %H:%M')

# Registrar en el log de dinero
echo "$MONTO,{\"from_name\":\"$CLIENTE\",\"type\":\"VENTA_DIRECTA\"}" >> ~/Microcosmos_Elite/data/money.log

# Actualizar el Muro de Honor
python3 -c "import json, os; h = json.load(open('/home/chalamandramagistral/Chalamandra-HUB/honors.json')); h.insert(0, {'name': '$CLIENTE', 'amount': $MONTO, 'date': '$FECHA'}); json.dump(h[:5], open('/home/chalamandramagistral/Chalamandra-HUB/honors.json', 'w'))"

echo "✅ VENTA REGISTRADA: $MONTO USD de $CLIENTE"
