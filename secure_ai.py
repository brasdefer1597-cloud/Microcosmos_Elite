# Fragmento para insertar en app.py para validación
from functools import wraps

# Una llave simple para empezar (Cámbiala por algo complejo)
MASTER_KEY = "CHALAMANDRA_ELITE_2026_SECRET"

def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('X-Chalamandra-Auth')
        if auth_header != MASTER_KEY:
            return jsonify({"error": "No autorizado. Acceso denegado al Nexo."}), 403
        return f(*args, **kwargs)
    return decorated

# Aplicar al endpoint de IA
@app.route('/api/ask-ai', methods=['POST'])
@require_auth
def ask_ai():
    # ... lógica de Gemini aquí ...
