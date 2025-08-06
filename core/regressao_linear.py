import numpy as np
from .base_model import BaseModel

class RegressaoLinear(BaseModel):
    def __init__(self):
        self.a = 0.0
        self.b = 0.0

    def treinar(self, X, y):
        X = np.array(X)
        y = np.array(y)
        n = len(X)
        
        x_mean = np.mean(X)
        y_mean = np.mean(y)
        
        numerador = np.sum((X - x_mean) * (y - y_mean))
        denominador = np.sum((X - x_mean) ** 2)
        
        self.a = numerador / denominador
        self.b = y_mean - self.a * x_mean
        print(f"[INFO] Modelo treinado: y = {self.a:.2f}x + {self.b:.2f}")

    def forward(self, x):
        return self.a * x + self.b