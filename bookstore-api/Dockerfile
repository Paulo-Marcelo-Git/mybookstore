# mybookstore\bookstore-api\Dockerfile

FROM python:3.12-slim

RUN apt-get update \
  && apt-get install -y tzdata curl gcc libpq-dev build-essential \
  && ln -sf /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime \
  && dpkg-reconfigure -f noninteractive tzdata \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

ENV TZ=America/Sao_Paulo
WORKDIR /app

# Instala Pipenv
RUN pip install --no-cache-dir pipenv

# Copia Pipfile* e instala **direto no sistema** as deps bloqueadas
COPY Pipfile Pipfile.lock ./
RUN pipenv install --deploy --ignore-pipfile --system

# Copia o restante
COPY . .

EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=5s CMD curl -f http://localhost:8000/ || exit 1

# Inicia Uvicorn **direto**, sem criar venv
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
