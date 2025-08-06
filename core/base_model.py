from abc import ABC, abstractmethod
import pickle

class BaseModel(ABC):
    @abstractmethod
    def treinar(self, X, y):
        pass

    @abstractmethod
    def forward(self, x):
        pass

    def salvar(self, caminho):
        with open(caminho, 'wb') as f:
            pickle.dump(self, f)
        print(f"[INFO] Modelo salvo em {caminho}")

    @classmethod
    def carregar(cls, caminho):
        with open(caminho, 'rb') as f:
            model = pickle.load(f)
        print(f"[INFO] Modelo carregado de {caminho}")
        return model