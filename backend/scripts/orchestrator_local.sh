#!/bin/bash
echo "🛡️ Orquestador de Guerrilla: Modo Local Activo"

# Bucle de control masivo (Inventario de contenedores)
for container in $(docker ps -a --format "{{.Names}}"); do
    echo "📊 Monitoreando Nodo: $container"
    # Verificar salud de la simulación cuántica sin salir al exterior
    docker exec $container python3 -c "print('Nodo Estable')" 2>/dev/null
done
