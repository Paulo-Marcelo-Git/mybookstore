# mybookstore\bookstore-api\Makefile
# 📦 Atalhos para Pipenv
install:
	pipenv install --dev

shell:
	pipenv shell

run:
	PYTHONPATH=$(shell pwd) pipenv run uvicorn main:app --reload

test:
	PYTHONPATH=$(shell pwd) pipenv run pytest

coverage:
	PYTHONPATH=$(shell pwd) pipenv run pytest --cov=. --cov-report=html:htmlcov --cov-report=term --cov-fail-under=90

test-html:
	xdg-open htmlcov/index.html || open htmlcov/index.html || start htmlcov/index.html

lint:
	pipenv run pylint main.py database.py models.py schemas.py

# 🐳 Docker
docker-up:
	docker compose up --build

docker-down:
	docker compose down

# 🧹 Utilitários
clean:
	rm -rf __pycache__ .pytest_cache htmlcov
