import React from 'react';

const MetricBox = ({ label, value, sub, color }) => (
  <div className="p-4 border border-green-900/50 bg-black/40 shadow-inner">
    <p className="text-[9px] text-zinc-500 uppercase font-bold tracking-tighter">{label}</p>
    <div className={`text-2xl font-black ${color}`}>{value}</div>
    <p className="text-[8px] text-zinc-600 italic">{sub}</p>
  </div>
);

const BusinessMetrics = ({ data }) => {
  if (!data) return null;
  return (
    <div className="grid grid-cols-2 gap-4 mt-8 border-t border-green-900/30 pt-6">
      <MetricBox 
        label="POAS (Profit On Ad Spend)" 
        value={(data.poas || 0) + "x"} 
        sub="Sustituto real del ROAS" 
        color="text-yellow-500" 
      />
      <MetricBox 
        label="True CAC" 
        value={"$" + (data.true_cac || 0)} 
        sub="Costo Adquisición Real" 
        color="text-red-400" 
      />
      <MetricBox 
        label="Ratio CLV:CAC" 
        value={data.ratio || 0} 
        sub={data.status === 'SCALABLE' ? 'CRECIMIENTO SOSTENIBLE' : 'REVISAR ESTRATEGIA'} 
        color={(data.ratio || 0) > 1 ? "text-green-400" : "text-red-600"} 
      />
      <MetricBox 
        label="Aceleración GPU" 
        value="WEB_GPU" 
        sub="Intel UHD 600 Active" 
        color="text-blue-400" 
      />
    </div>
  );
};

export default BusinessMetrics;
