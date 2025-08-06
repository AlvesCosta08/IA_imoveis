# 🏠 Sistema de Previsão de Preço de Imóveis com IA

Um sistema completo de **inteligência artificial** para prever o preço de imóveis com base na área (m²), usando **regressão linear**, **API Flask**, **Streamlit**, **Docker** e arquitetura modular.

> ✅ Treinamento automático  
> ✅ API REST para predições  
> ✅ Interface web interativa  
> ✅ Containerizado com Docker  
> ✅ Pronto para evoluir para produção

---

## 🚀 Demonstração

| Interface Web | API REST |
|--------------|----------|
| ![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-blue?logo=streamlit) | ![Flask](https://img.shields.io/badge/Flask-API%20REST-green?logo=flask) |
| Acesse: `http://localhost:8501` | Acesse: `http://localhost:5000` |

---

## 📦 Funcionalidades

- ✅ **Regressão Linear** do zero (sem scikit-learn)
- ✅ Treinamento com dados reais (CSV)
- ✅ Persistência do modelo com `pickle`
- ✅ API REST com **Flask**
- ✅ Interface web com **Streamlit**
- ✅ Orquestração com **Docker Compose**
- ✅ Logging, configuração com `.env`
- ✅ Arquitetura modular e escalável

---

## 🧱 Arquitetura




---

## 🛠️ Pré-requisitos

- [Docker](https://www.docker.com/get-started) instalado
- [Docker Compose](https://docs.docker.com/compose/install/) (geralmente incluso)

---

## ▶️ Como rodar o projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/ia-previsao-imoveis.git
   cd ia-previsao-imoveis


   Acesse:
🔧 API Flask: http://localhost:5000
🌐 Interface Web: http://localhost:8501


curl -X POST http://localhost:5000/prever \
  -H "Content-Type: application/json" \
  -d '{"m2": 90}'


  {
  "m2": 90,
  "preco_previsto": 293333.33,
  "moeda": "BRL"
}