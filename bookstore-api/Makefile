# mybookstore\bookstore-api\Makefile/

# 📦 Pipenv
install:
	pipenv install --dev

shell:
	pipenv shell

run:
	PYTHONPATH=$(shell pwd) pipenv run uvicorn main:app --reload --host=0.0.0.0 --port=8000

test:
	PYTHONPATH=$(shell pwd) pipenv run pytest --cov=. --cov-report=term --cov-fail-under=90

docker-test:
	docker compose exec backend pipenv run pytest --cov=. --cov-report=term

coverage:
	PYTHONPATH=$(shell pwd) pipenv run pytest --cov=. --cov-report=html:htmlcov --cov-report=term --cov-fail-under=90

test-html:
	xdg-open htmlcov/index.html || open htmlcov/index.html || start htmlcov/index.html

lint:
	pipenv run pylint main.py database.py models.py schemas.py tests/

format:
	pipenv run black .
	pipenv run isort .

check:
	pipenv run black --check .
	pipenv run isort --check-only .
	pipenv run pylint main.py database.py models.py schemas.py tests/
	pipenv run mypy main.py database.py models.py schemas.py

typecheck:
	pipenv run mypy .

# 🐳 Docker
docker-up:
	docker compose up --build

docker-down:
	docker compose down

# 🧹 Limpeza
clean:
	rm -rf __pycache__ .pytest_cache htmlcov

# Início rápido
start:
	./start.sh
