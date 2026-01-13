# Como Testar o Pre-Commit Hook

Este repositório demonstra como o Semgrep pode detectar e bloquear vulnerabilidades XSS automaticamente durante commits.

## 🔴 Vulnerabilidade Presente

O arquivo `app.py` contém uma vulnerabilidade XSS intencional na linha 22-33:

```python
name = request.args.get('name', 'Visitante')  # Entrada do usuário
html = f'<h1>Olá, {name}!</h1>'               # Inserido diretamente
return render_template_string(html)            # VULNERÁVEL!
```

## 🛡️ Pre-Commit Hook Configurado

O hook foi instalado e está ativo. Para testar:

### Teste 1: Semgrep Manual
```bash
source venv/bin/activate
semgrep --config .semgrep.yml app.py
```

**Resultado:** Deve detectar 1 vulnerabilidade

### Teste 2: Tentar Fazer Commit (SERÁ BLOQUEADO)
```bash
# Modifique algo no app.py
echo "# comentário teste" >> app.py

# Tente commitar
git add app.py
git commit -m "Tentando commitar código vulnerável"
```

**Resultado:** ❌ Commit será BLOQUEADO pelo Semgrep!

```
Semgrep Security Check...................................................Failed
- hook id: semgrep
- exit code: 1

    app.py 
       flask-xss-user-input-template                                            
          Possível vulnerabilidade XSS: dados do usuário usados em              
          render_template_string sem sanitização
```

### Teste 3: Bypass do Hook (para demonstração)
```bash
git commit -m "Commit com bypass" --no-verify
```

**Resultado:** ✅ Commit será permitido (não recomendado em produção!)

## ✅ Como Corrigir a Vulnerabilidade

Substitua o código vulnerável por:

```python
from markupsafe import escape

@app.route('/greet')
def greet():
    name = request.args.get('name', 'Visitante')
    safe_name = escape(name)  # Sanitiza entrada
    html = f'<h1>Olá, {safe_name}!</h1>'
    return render_template_string(html)
```

Ou use templates Jinja2 com autoescaping ativo:

```python
@app.route('/greet')
def greet():
    name = request.args.get('name', 'Visitante')
    return render_template_string(
        '<h1>Olá, {{ name }}!</h1>',
        name=name
    )
```

Após corrigir, o Semgrep permitirá o commit! ✅

## 🔥 Explorar a Vulnerabilidade

```bash
# Execute o app
python app.py

# Acesse no navegador:
http://localhost:5000/greet?name=<script>alert('XSS')</script>
```

O JavaScript será executado, demonstrando a vulnerabilidade!

## 📋 Resumo

- ✅ Vulnerabilidade XSS criada intencionalmente
- ✅ Semgrep configurado com regras customizadas
- ✅ Pre-commit hook instalado e funcional
- ✅ Hook detecta e bloqueia commits vulneráveis
- ✅ Documentação completa fornecida

**Objetivo educacional alcançado!** 🎓
