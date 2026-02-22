const fs = require('fs');

function pulse() {
    const timestamp = new Date().toISOString();
    const message = `[GHOST-PULSE] Generando radiación de tráfico... ${timestamp}\n`;
    
    // Escribimos en el log para simular actividad de red
    fs.appendFileSync('logs/ghost.log', message);
    console.log(message);
    
    // Pulso aleatorio entre 5 y 15 segundos para evitar patrones detectables
    const nextPulse = Math.floor(Math.random() * (15000 - 5000 + 1)) + 5000;
    setTimeout(pulse, nextPulse);
}

console.log("👻 Ghost Pulse Iniciado: El fantasma recorre los cables...");
pulse();
