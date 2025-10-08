# Aula Senai - Flask App

Aplicação simples em Flask para gerenciar alunos usando lista e dicionários.

Endpoints:

- POST /adicionar_aluno
  - Body (JSON): { "nome": "Nome do aluno", "idade": 20 }
  - Retorno: objeto do aluno criado com `id`.

- GET /buscar_aluno
  - Parâmetros de query: `id` (ex: /buscar_aluno?id=1) ou `nome` (ex: /buscar_aluno?nome=Maria)
  - Retorno: aluno encontrado ou lista de alunos com o nome.

- GET /listar_aluno
  - Retorno: lista completa de alunos.

Testes com Postman:

1. Rodar a aplicação:

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -r requirements.txt; python app.py
```

2. No Postman faça as requisições:

- POST http://127.0.0.1:5000/adicionar_aluno
  - Body -> raw -> JSON
  - Exemplo: {"nome": "João", "idade": 21}

- GET http://127.0.0.1:5000/listar_aluno

- GET http://127.0.0.1:5000/buscar_aluno?id=1

Observações:
- A aplicação usa armazenamento em memória (lista) - os dados se perdem ao reiniciar o servidor.
