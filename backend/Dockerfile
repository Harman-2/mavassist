FROM python:3.12-slim
ARG INSTALL_AI=true
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 HF_HOME=/opt/models
WORKDIR /app
COPY requirements*.txt ./
RUN pip install --no-cache-dir -r requirements.txt && \
    if [ "$INSTALL_AI" = "true" ]; then \
      pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu && \
      pip install --no-cache-dir -r requirements-ai.txt && \
      python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2', device='cpu')"; \
    fi
COPY . .
RUN useradd -u 10001 -m mavassist && mkdir -p /data /opt/models && chown -R mavassist:mavassist /app /data /opt/models
USER mavassist
EXPOSE 8000
CMD ["sh", "-c", "python -m alembic upgrade head && python -m app.manage seed && exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000} --workers 1 --no-access-log"]
