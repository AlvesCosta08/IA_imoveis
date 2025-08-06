FROM python:3.10-slim

LABEL maintainer="voce@email.com"
LABEL version="1.0.0"
LABEL description="API de IA para previsão de imóveis"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Adiciona ao PYTHONPATH
ENV PYTHONPATH=/app

COPY scripts/entrypoint.sh /app/scripts/entrypoint.sh
RUN chmod +x /app/scripts/entrypoint.sh

RUN adduser --disabled-password --gecos '' appuser && \
    chown -R appuser:appuser /app && \
    chmod -R 755 /app

USER appuser

EXPOSE 5000 8501

CMD ["/app/scripts/entrypoint.sh"]