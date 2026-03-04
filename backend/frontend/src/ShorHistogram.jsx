import React from 'react';
import { motion } from 'framer-motion';

const ShorHistogram = ({ probabilities = [0.25, 0.25, 0.25, 0.25] }) => {
  const labels = ['0', '4', '8', '12'];

  return (
    <div className="flex flex-col gap-6 p-6 border border-green-900 bg-black font-mono">
      <div className="flex items-center gap-4 border-b border-green-900/30 pb-4">
        <div className="bloch-sphere">
          <div className="inner-qubit"></div>
        </div>
        <div>
          <h4 className="text-[10px] text-green-400 font-bold uppercase">Qubit_Status: Superposición</h4>
          <p className="text-[9px] text-zinc-500">VQC Algorithm Active</p>
        </div>
      </div>

      <div className="h-40 flex items-end justify-around gap-2">
        {probabilities.map((prob, index) => (
          <div key={index} className="flex flex-col items-center flex-1">
            <motion.div
              initial={{ height: 0 }}
              animate={{ height: `${prob * 100}%` }}
              className="w-full bg-green-500/80 shadow-[0_0_15px_rgba(0,255,0,0.3)] border-t border-white/20"
            />
            <span className="text-[9px] text-green-800 mt-2">{labels[index]}</span>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ShorHistogram;
