import React, { useState, useEffect } from 'react';
import ShorHistogram from './ShorHistogram';
import BusinessMetrics from './BusinessMetrics';
import './App.css';

function App() {
  const [metrics, setMetrics] = useState({ ram: "0", status: "Iniciando sensores..." });
  const [bizMetrics, setBizMetrics] = useState({});

  useEffect(() => {
    const interval = setInterval(async () => {
      try {
        const res = await fetch('/data/shor_stats.json');
        const data = await res.json();
        setMetrics(data.metrics || { ram: "0", status: "Sin datos" });
      } catch (e) {
        console.log("Sincronizando con el búnker...");
      }
    }, 5000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="min-h-screen bg-black text-green-400 p-8 font-mono">
      <h1 className="text-2xl font-bold mb-6">🌀 NODO XALAPA - MICROCOSMOS ÉLITE</h1>
      <div className="grid grid-cols-2 gap-8">
        <div>
          <h2 className="text-lg mb-4">🔬 Simulación Shor</h2>
          <ShorHistogram probabilities={[0.2, 0.3, 0.4, 0.1]} />
          <div className="mt-4 p-4 border border-green-900/50">
            <p><span className="text-green-400 font-bold">LOG:</span> {metrics.status}</p>
            <p><span className="text-green-400 font-bold">RAM:</span> {metrics.ram_mb} <span className="text-green-500">MB</span></p>
          </div>
        </div>
        <div>
          <h2 className="text-lg mb-4">📊 Métricas de Negocio</h2>
          <BusinessMetrics data={bizMetrics} />
        </div>
      </div>
    </div>
  );
}

export default App;
