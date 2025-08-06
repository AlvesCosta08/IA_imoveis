from flask import Flask, request, jsonify
import logging
from config import Config
from services.predictor_service import carregar_modelo  # ✅ removido 'prever'

app = Flask(__name__)
logging.basicConfig(level=Config.LOG_LEVEL)
logger = logging.getLogger(__name__)

# Carregar modelo ao iniciar
modelo = carregar_modelo()

@app.route("/")
def home():
    return jsonify({
        "mensagem": "API de Previsão de Imóveis v" + Config.MODEL_VERSION,
        "endpoints": ["/prever"]
    })

@app.route("/prever", methods=["POST"])
def previsao():
    try:
        dados = request.get_json()
        if not dados or "m2" not in dados:
            return jsonify({"erro": "Campo 'm2' é obrigatório"}), 400

        m2 = float(dados["m2"])
        if m2 <= 0:
            return jsonify({"erro": "m² deve ser maior que zero"}), 400

        # ✅ Usa diretamente o método forward do modelo
        preco_predito = modelo.forward(m2)

        return jsonify({
            "m2": m2,
            "preco_previsto": round(preco_predito, 2),
            "moeda": "BRL"
        })

    except ValueError:
        return jsonify({"erro": "Valor de m2 deve ser numérico"}), 400
    except Exception as e:
        logger.error(f"Erro na predição: {e}")
        return jsonify({"erro": "Erro interno no servidor"}), 500

if __name__ == "__main__":
    app.run(host=Config.HOST, port=Config.PORT, debug=True)