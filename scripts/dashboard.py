import json, matplotlib.pyplot as plt, os

root = "/home/chalamandramagistral/Microcosmos_Elite"
data_path = f"{root}/data/telemetry.jsonl"
output_path = f"{root}/data/evolucion_total.png"

nodes, entropy, traffic = [], [], []

if os.path.exists(data_path):
    with open(data_path, "r") as f:
        for line in f:
            d = json.loads(line)
            if 'node' in d:
                nodes.append(f"{d['node']}\n{round(d['ts'] % 100,0)}")
                entropy.append(d.get('entropy', 0) or 0)
            if d.get('event') == 'clic_refineria':
                traffic.append(1) # Contador de clics

    plt.figure(figsize=(12, 6))
    plt.style.use('dark_background')
    
    plt.plot(entropy, marker='o', color='magenta', label='Entropía (Creatividad)')
    plt.bar(range(len(nodes)), [e*0.5 for e in entropy], alpha=0.3, color='cyan', label='Esfuerzo Cuántico')
    
    plt.title("MICROCOSMOS ELITE: Evolución de la Conciencia Adaptativa", color='yellow')
    plt.legend()
    plt.savefig(output_path)
    print(f"✅ Dashboard V6 generado en: {output_path}")
