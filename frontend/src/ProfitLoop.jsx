import React from 'react';

const ProfitLoop = ({ biz }) => {
  if (!biz) return null;
  const isProfitable = biz.ltv_cac_ratio > 1;

  return (
    <div className="mt-6 p-4 border-2 border-dashed border-green-900 bg-green-950/10">
      <div className="flex justify-between items-center mb-4">
        <h3 className="text-[10px] font-bold text-green-400 uppercase tracking-widest">Loop de Reinversión</h3>
        <span className={`px-2 py-0.5 text-[8px] font-bold ${isProfitable ? 'bg-green-500 text-black' : 'bg-red-500 text-white'}`}>
          {isProfitable ? 'SOSTENIBLE' : 'CRÍTICO'}
        </span>
      </div>
      
      <div className="grid grid-cols-3 gap-2">
        <div className="text-center">
          <p className="text-[8px] text-zinc-500">POAS</p>
          <p className="text-lg font-black text-yellow-500">{biz.poas}x</p>
        </div>
        <div className="text-center border-x border-green-900/30">
          <p className="text-[8px] text-zinc-500">RATIO LTV:CAC</p>
          <p className={`text-lg font-black ${isProfitable ? 'text-green-400' : 'text-red-500'}`}>{biz.ltv_cac_ratio}</p>
        </div>
        <div className="text-center">
          <p className="text-[8px] text-zinc-500">GROVER BOOST</p>
          <p className="text-[10px] font-bold text-blue-400 mt-2">{biz.grover_boost}</p>
        </div>
      </div>
      
      <div className="mt-4 h-1 bg-zinc-900 w-full overflow-hidden">
        <div 
          className="h-full bg-green-500 transition-all duration-1000" 
          style={{ width: `${Math.min(biz.ltv_cac_ratio * 20, 100)}%` }}
        ></div>
      </div>
    </div>
  );
};

export default ProfitLoop;
