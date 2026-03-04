import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Activity, Zap, Radio, Database, ShieldAlert } from 'lucide-react';

const StatCard = ({ label, value, color, suffix = "", icon }) => (
  <div className="p-4 border border-green-900 bg-zinc-950/50 relative group">
    <div className="absolute top-2 right-2 opacity-20 group-hover:opacity-100 transition-opacity">{icon}</div>
    <p className="text-[10px] text-zinc-500 mb-1">{label}</p>
    <div className={`text-2xl font-black ${color}`}>{value}<span className="text-xs ml-1">{suffix}</span></div>
  </div>
);

const SingularityPanel = () => {
  const [data, setData] = useState({ entropy: 0, redshift: 0, mass: 0 });
  const [alert, setAlert] = useState(false);

  useEffect(() => {
    const fetchData = () => {
      const newMass = (Math.random() * 2000).toFixed(2);
      if (parseFloat(newMass) > parseFloat(data.mass)) {
        setAlert(true);
        setTimeout(() => setAlert(false), 2000);
      }
      setData({
        entropy: Math.floor(Math.random() * 5000),
        redshift: (Math.random() * 0.08).toFixed(4),
        mass: newMass
      });
    };
    const interval = setInterval(fetchData, 4000);
    return () => clearInterval(interval);
  }, [data.mass]);

  return (
    <div className="bg-black text-green-500 font-mono scanline-effect min-h-screen flex items-center justify-center p-4 overflow-hidden">
      <AnimatePresence>
        {alert && (
          <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}
            className="fixed inset-0 bg-red-600/10 z-50 pointer-events-none flex items-center justify-center">
            <div className="text-red-600 text-6xl font-black animate-pulse italic">MATERIA_DETECTADA</div>
          </motion.div>
        )}
      </AnimatePresence>

      <div className="w-full max-w-4xl border border-green-900 p-6 bg-black/90 shadow-[0_0_40px_rgba(0,50,0,0.5)]">
        <header className="flex justify-between border-b border-green-900 pb-4 mb-6">
          <div>
            <h1 className="text-2xl font-black italic glitch-text">NODO_XALAPA_SINGULARITY</h1>
            <p className="text-[9px] text-green-800 uppercase">brasdefer1597-cloud // Celeron_N4020</p>
          </div>
          <div className="text-right">
            <div className="flex items-center gap-2 text-red-500 text-[10px] animate-pulse">
              <ShieldAlert size={12} /> STATUS: RADIATING
            </div>
          </div>
        </header>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <StatCard label="ENTROPÍA (S)" value={data.entropy} color="text-green-400" icon={<Database size={14}/>} />
          <StatCard label="REDSHIFT (z) (z)" value={data.redshift} suffix="ly" color="text-blue-400" icon={<Radio size={14}/>} />
          <StatCard label="MASA DEVORADA" value={`$${data.mass}`} color="text-yellow-500" icon={<Zap size={14}/>} />
        </div>

        <div className="mt-6 p-3 border border-green-900/30 bg-zinc-950/80 text-[10px] text-green-900">
          <p className="mb-1 opacity-50 uppercase tracking-tighter italic font-bold text-zinc-500">Live Terminal Output:</p>
          <p>> SHOR_FACTOR_STABLE: OK</p>
          <p>> MEM_PURGE_SUCCESSFUL: 200MB_THRESHOLD</p>
          <p>> SINC_BY: brasdefer1597-cloud</p>
        </div>
      </div>
    </div>
  );
};

export default SingularityPanel;
