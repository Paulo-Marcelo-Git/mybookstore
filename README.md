# 📚 Bookstore API

Uma API RESTful moderna para gerenciamento de livros, construída com **FastAPI**, **SQLAlchemy** e **Docker**. Ideal para aprendizado prático, testes e projetos base de backend.

---

## 🚀 Tecnologias Utilizadas

- **Python 3.12**
- **FastAPI**
- **SQLAlchemy**
- **PyMySQL**
- **Docker + Docker Compose**
- **GitHub Actions (CI/CD)**
- **Pytest + Coverage**

---

## 🔌 Endpoints Disponíveis

| Método | Endpoint         | Descrição                                 |
|--------|------------------|-------------------------------------------|
| GET    | `/books/`        | Lista todos os livros (ID + título)       |
| POST   | `/books/`        | Cria um novo livro                        |
| GET    | `/books/{id}`    | Retorna dados completos de um livro       |
| PUT    | `/books/{id}`    | Atualiza dados de um livro existente      |
| DELETE | `/books/{id}`    | Remove (arquiva) o livro                  |
| GET    | `/documentation` | Abre a documentação HTML personalizada    |
| GET    | `/docs`          | Acessa o Swagger UI gerado automaticamente|

---

## 🐳 Executando com Docker

```bash
# Suba os containers com:
docker-compose up --build

# Acesse:
# Swagger UI: http://localhost:8000/docs
# Documentação HTML: http://localhost:8000/documentation
# Adminer (gerenciador de banco): http://localhost:8080
```

---

## ⚙️ Variáveis de Ambiente

Crie um arquivo `.env` com as seguintes chaves:

```env
DB_USER=root
DB_PASS=suasenha
DB_HOST=localhost
DB_PORT=3306
DB_NAME=bookstore
```

---

## 🧪 Rodando os Testes

Utilize `make` ou `pytest` para executar os testes:

```bash
# Executar testes com cobertura
make coverage

# Visualizar relatório de cobertura
make test-html
```

---

## 📁 Estrutura do Projeto

```
bookstore-api/
├── main.py                  # Entrypoint da API
├── database.py              # Configuração do banco
├── models.py                # Models SQLAlchemy
├── schemas.py               # Schemas Pydantic
├── tests/                   # Testes automatizados
├── docs/index.html          # Documentação personalizada
├── Pipfile / Pipfile.lock   # Dependências do projeto
├── Dockerfile               # Build da imagem
├── Makefile                 # Atalhos úteis
└── .github/workflows/       # CI com GitHub Actions
```

---

## 👨‍💻 Autor

Desenvolvido por **Paulo Marcelo Cardoso Da Silva**  
Licença MIT – contribuições são bem-vindas!

---

## ✅ Status do Projeto

🚧 Em desenvolvimento – PRs e melhorias são encorajados!