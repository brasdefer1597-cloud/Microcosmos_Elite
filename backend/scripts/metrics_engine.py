import json

def calcular_metricas_guerrilla():
    # Simulamos datos de entrada (En el futuro leerá de tus CSV/DB)
    ingreso_bruto = 1500.00
    cogs = 600.00  # Costo de bienes
    ads_spend = 300.00
    envios_tarifas = 150.00
    clientes_nuevos = 10
    
    # 1. POAS (Profit On Ad Spend)
    profit = ingreso_bruto - cogs - envios_tarifas
    poas = profit / ads_spend if ads_spend > 0 else 0
    
    # 2. True CAC
    true_cac = ads_spend / clientes_nuevos if clientes_nuevos > 0 else 0
    
    # 3. Ratio CLV Profit : True CAC (Sostenibilidad)
    clv_profit = 45.0  # Ganancia neta estimada por cliente a largo plazo
    ratio_sostenibilidad = clv_profit / true_cac if true_cac > 0 else 0
    
    return {
        "poas": round(poas, 2),
        "true_cac": round(true_cac, 2),
        "ratio": round(ratio_sostenibilidad, 2),
        "status": "SCALABLE" if ratio_sostenibilidad > 1.0 else "DANGER"
    }

if __name__ == "__main__":
    print(json.dumps(calcular_metricas_guerrilla()))
