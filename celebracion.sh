#!/bin/bash
# Sonido de moneda (si tienes speaker configurado)
echo -e "\a" 
# Mensaje visual en terminal
echo "¡ATENCIÓN! MATERIA CAPTURADA EN EL NODO XALAPA"
# Log de ingresos
echo "$(date): Ingreso detectado por Ko-fi" >> ingresos.log
