# 📚 Bookstore API

Uma API RESTful simples para gerenciar livros, construída com FastAPI, SQLAlchemy e Docker. Ideal para estudos e projetos base.

---

## 🚀 Tecnologias Utilizadas

- Python 3.12
- FastAPI
- SQLAlchemy
- PyMySQL
- Docker + Docker Compose
- GitHub Actions (CI)

---

## 🧩 Endpoints Principais

| Método | Endpoint         | Descrição                              |
|--------|------------------|----------------------------------------|
| GET    | /books/          | Lista todos os livros (resumo)         |
| POST   | /books/          | Cria um novo livro                     |
| GET    | /books/{id}      | Retorna os dados completos de um livro|
| PUT    | /books/{id}      | Atualiza um livro                      |
| DELETE | /books/{id}      | Remove um livro e arquiva o registro   |
| GET    | /documentation   | Exibe a documentação HTML personalizada|
| GET    | /docs            | Abre o Swagger UI                      |

---

## 🐳 Como Rodar com Docker

```bash
# Subir os containers
docker-compose up --build

# Acesse:
# API Swagger: http://localhost:8000/docs
# Adminer (banco): http://localhost:8080
```

---

## ⚙️ Variáveis de Ambiente

Crie um arquivo `.env` baseado no exemplo abaixo:

```env
DB_USER=root
DB_PASS=suasenha
DB_HOST=localhost
DB_PORT=3306
DB_NAME=bookstore
```

---

## 🧪 Testes

Há um teste de sanidade em `test_app.py`:

```bash
pytest
```

---

## 📁 Estrutura do Projeto

```
bookstore-api/
├── .env.example
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── database.py
├── models.py
├── schemas.py
├── main.py
├── requirements.txt
├── test_app.py
├── docs/
│   └── index.html
└── .github/
    └── workflows/
        └── python-ci.yml
```

---

## 🛠️ Autor

Projeto desenvolvido por [Paulo Marcelo Cardoso Da Silva].  
Licenciado sob MIT.

---

## ✅ Status

Projeto em desenvolvimento 🚧. PRs e sugestões são bem-vindos!
