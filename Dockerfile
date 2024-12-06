# Build stage
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Model download stage
FROM python:3.11-slim AS model
WORKDIR /app

# Install Ollama and download model
RUN apt-get update && apt-get install -y \
    curl \
    procps \
    && rm -rf /var/lib/apt/lists/* \
    && curl -fsSL https://ollama.ai/install.sh | sh

# Start Ollama and download model
RUN ollama serve & \
    sleep 5 && \
    ollama pull tinyllama && \
    mkdir -p /root/.ollama && \
    cd /root/.ollama && \
    tar czf /tmp/model.tar.gz *

# Final stage
FROM python:3.11-slim
WORKDIR /app

# Copy Python packages from builder
COPY --from=builder /root/.local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

# Install runtime dependencies and Ollama
RUN apt-get update && apt-get install -y \
    curl \
    procps \
    && rm -rf /var/lib/apt/lists/* \
    && curl -fsSL https://ollama.ai/install.sh | sh

# Copy the pre-downloaded model
COPY --from=model /tmp/model.tar.gz /tmp/
RUN mkdir -p /root/.ollama && \
    cd /root/.ollama && \
    tar xzf /tmp/model.tar.gz && \
    rm /tmp/model.tar.gz

# Copy application code
COPY . .

# Create startup script
RUN echo '#!/bin/bash\n\
echo "Starting Ollama service..."\n\
ollama serve & \n\
echo "Waiting for Ollama service to be ready..."\n\
sleep 5\n\
echo "Starting Flask application..."\n\
python app.py' > start.sh && chmod +x start.sh

ENV PORT=5001
EXPOSE 5001

CMD ["./start.sh"]