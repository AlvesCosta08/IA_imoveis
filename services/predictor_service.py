import logging
import time
import pickle
from config import Config
from core.regressao_linear import RegressaoLinear

def carregar_modelo(caminho=None):
    caminho = caminho or Config.MODEL_PATH
    tentativas = 0
    max_tentativas = 15  # até 30 segundos

    while tentativas < max_tentativas:
        try:
            if not caminho:
                raise FileNotFoundError("Caminho do modelo não definido")
                
            with open(caminho, 'rb') as f:
                modelo = pickle.load(f)
            logging.info("Modelo carregado com sucesso para predição.")
            return modelo
            
        except (FileNotFoundError, EOFError, pickle.UnpicklingError) as e:
            tentativas += 1
            logging.warning(f"Falha ao carregar modelo (tentativa {tentativas}): {e}")
            time.sleep(2)

    logging.critical("Falha crítica: modelo não disponível após múltiplas tentativas.")
    raise Exception("Não foi possível carregar o modelo.")