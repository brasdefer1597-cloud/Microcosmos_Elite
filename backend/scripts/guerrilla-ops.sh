#!/bin/bash
# Actualización, Sincronía y Despliegue en Cascada
./sync_mass.sh
cd ~/microcosmos_elite/frontend && vercel --prod --yes
./notificar.sh "🚀 DESPLIEGUE MULTI-REPO COMPLETADO: Nodo Xalapa en Radiación Global."
