import logging
import pandas as pd
import matplotlib.pyplot as plt
from config import Config
from core.regressao_linear import RegressaoLinear

logging.basicConfig(filename='logs/app.log', level=Config.LOG_LEVEL,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def carregar_dados(caminho):
    try:
        df = pd.read_csv(caminho)
        logging.info(f"Dados carregados: {len(df)} linhas")
        return df
    except Exception as e:
        logging.error(f"Erro ao carregar dados: {e}")
        raise

def main():
    print("🚀 Iniciando treinamento do modelo de previsão de imóveis...")
    
    df = carregar_dados(Config.DATA_PATH)
    X = df['m2'].values
    y = df['preco'].values
    
    modelo = RegressaoLinear()
    modelo.treinar(X, y)
    modelo.salvar(Config.MODEL_PATH)
    
    plt.figure(figsize=(8, 6))
    plt.scatter(X, y, color='blue', label='Real')
    plt.plot(X, modelo.forward(X), color='red', label='Predito')
    plt.xlabel("Área (m²)")
    plt.ylabel("Preço (R$)")
    plt.title("Regressão Linear: Preço de Imóveis")
    plt.legend()
    plt.savefig("output/grafico_previsao.png")
    plt.close()
    
    print("✅ Modelo treinado, salvo e gráfico gerado!")

if __name__ == "__main__":
    main()