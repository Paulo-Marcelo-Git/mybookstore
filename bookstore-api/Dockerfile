FROM python:3.12-slim

# Evita prompts interativos ao instalar pacotes
ENV DEBIAN_FRONTEND=noninteractive

# Instala o tzdata e configura o fuso de São Paulo
RUN apt-get update \
    && apt-get install -y tzdata \
    && ln -sf /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime \
    && dpkg-reconfigure --frontend noninteractive tzdata \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Define a variável de ambiente de fuso
ENV TZ=America/Sao_Paulo

WORKDIR /app

# Instala dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código
COPY . .

# Comando padrão para iniciar a API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
