FROM python:3.12-slim

# Define timezone
RUN apt-get update \
  && apt-get install -y tzdata curl gcc libpq-dev build-essential \
  && ln -sf /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime \
  && dpkg-reconfigure -f noninteractive tzdata \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

ENV TZ=America/Sao_Paulo

# Instala o pipenv
RUN pip install --no-cache-dir pipenv

WORKDIR /app

# Copia os arquivos do Pipenv
COPY Pipfile Pipfile.lock ./

# Instala apenas as dependências de produção
RUN pipenv install --deploy --ignore-pipfile

# Copia o restante do código da app
COPY . .

# Expõe a porta da API
EXPOSE 8000

# Usa o pipenv para rodar o Uvicorn
CMD ["pipenv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--log-level", "info", "--access-log"]
