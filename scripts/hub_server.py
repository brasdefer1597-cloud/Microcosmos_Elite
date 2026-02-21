from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import json
import os

app = FastAPI()
ROOT = "/home/chalamandramagistral/Microcosmos_Elite"

@app.get("/", response_class=HTMLResponse)
async def read_hub():
    with open(f"{ROOT}/sesgo.json", "r") as f:
        data = json.load(f)
    
    # Estética Salamandra: Negro profundo y Verde Neón (#00ff88)
    html_content = f"""
    <html>
        <head>
            <title>SALAMANDRA QUANTUM HUB</title>
            <style>
                body {{ background: #0a0a0a; color: #00ff88; font-family: 'Courier New', monospace; padding: 50px; }}
                .card {{ border: 1px solid #00ff88; padding: 20px; box-shadow: 0 0 15px #00ff8833; border-radius: 10px; }}
                h1 {{ text-shadow: 0 0 10px #00ff88; }}
                .metric {{ font-size: 2em; margin: 10px 0; }}
                .label {{ color: #ffffff; font-size: 0.8em; text-transform: uppercase; }}
            </style>
        </head>
        <body>
            <h1>🦎 CONTROL DE SINGULARIDAD</h1>
            <div class="card">
                <div class="label">Ingresos Totales (Ko-fi)</div>
                <div class="metric">${data.get('ingresos_totales', 0)}</div>
                <hr style="border: 0.5px solid #00ff88">
                <div class="label">POAS Real</div>
                <div class="metric">{data.get('poas_real', 0)}</div>
                <div class="label">Ángulo Cuántico</div>
                <div class="metric">{data.get('vqe_angulo', 0)} rad</div>
                <div class="label">Brillo Cuántico</div>
                <div class="metric">{data.get('brillo_cuantico', 0)}</div>
            </div>
            <p>Satus: <i>SISTEMA EN EQUILIBRIO TÉRMICO</i></p>
        </body>
    </html>
    """
    return html_content

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
