# Aula 06 – Entrega atividade

## Passos rápidos
- Criar e ativar venv:
  ```bash
  python -m venv .venv
  source .venv/bin/activate  # Windows: .venv\Scripts\activate
  python -m pip install --upgrade pip
  pip install -r requirements.txt
  pip install -r requirements-dev.txt
  pytest -q
  ```
- Rodar a aplicação local (exemplo):
  ```bash
  python app/main.py
  ```
