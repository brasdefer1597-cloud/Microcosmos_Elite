#!/bin/bash
# Guardar en el almacenamiento persistente para que sobreviva al cierre de RAM
PATH_CSV="/home/chalamandramagistral/microcosmos_elite/data/resultados_shor.csv"
FECHA=$(date +%s)
POAS=$1
LTV=$2
EXITO=$3

echo "$FECHA,$POAS,$LTV,$EXITO" >> $PATH_CSV
