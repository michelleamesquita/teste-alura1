# App Flask com Vulnerabilidade XSS

Este é um exemplo educacional de uma aplicação Flask com vulnerabilidade XSS detectada por Semgrep.

## Vulnerabilidade

O endpoint `/greet` recebe entrada do usuário via `request.args.get()` e renderiza diretamente em HTML sem sanitização, permitindo ataques XSS.

**Exemplo de exploit:**
```
http://localhost:5000/greet?name=<script>alert('XSS')</script>
```

## Configuração

### 1. Instalar dependências

```bash
pip install -r requirements.txt
```

### 2. Instalar pre-commit e Semgrep

```bash
pip install pre-commit semgrep
```

### 3. Configurar pre-commit hook

```bash
pre-commit install
```

## Executar a aplicação

```bash
python app.py
```

Acesse: http://localhost:5000

## Testar o Semgrep

### Manualmente:
```bash
semgrep --config .semgrep.yml app.py
```

### Via pre-commit:
```bash
# Tente fazer commit do arquivo vulnerável
git add app.py
git commit -m "Add vulnerable code"
```

O pre-commit hook vai bloquear o commit se detectar a vulnerabilidade!

## Como corrigir

Use `escape()` do Jinja2 ou passe variáveis como parâmetros seguros:

```python
from markupsafe import escape

@app.route('/greet')
def greet():
    name = request.args.get('name', 'Visitante')
    safe_name = escape(name)
    html = f'<h1>Olá, {safe_name}!</h1>'
    return render_template_string(html)
```
