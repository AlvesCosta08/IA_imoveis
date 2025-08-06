#!/bin/bash

echo "🚀 SERVICE_NAME recebido: '$SERVICE_NAME'"

if [ -z "$SERVICE_NAME" ]; then
  echo "❌ Erro: SERVICE_NAME não definido!"
  exit 1
fi

case "$SERVICE_NAME" in
  "train")
    echo "🔧 Executando treinamento..."
    python main.py
    ;;
  "api")
    echo "📡 Iniciando API Flask..."
    python webapp/app.py
    ;;
  "web")
    echo "🌐 Iniciando Streamlit..."
    streamlit run webapp/streamlit_app.py --server.port=8501 --server.address=0.0.0.0
    ;;
  *)
    echo "❌ SERVICE_NAME inválido: '$SERVICE_NAME'"
    echo "Use: train, api ou web"
    exit 1
    ;;
esac