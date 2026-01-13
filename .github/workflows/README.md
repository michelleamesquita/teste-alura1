# GitHub Actions - Security Scan

Este workflow executa análise de segurança automatizada usando Semgrep e SonarCloud.

## 🔧 Configuração Necessária

### 1. Semgrep (Opcional - funciona sem token)

Para usar o Semgrep gratuitamente sem configuração adicional, o workflow já está pronto!

**Opcionalmente**, para recursos avançados do Semgrep Cloud:
1. Acesse https://semgrep.dev/login
2. Crie uma conta
3. Vá em **Settings** → **Tokens**
4. Copie seu token
5. No GitHub: **Settings** → **Secrets and variables** → **Actions** → **New repository secret**
   - Name: `SEMGREP_APP_TOKEN`
   - Value: seu token

### 2. SonarCloud (Requer configuração)

**Passo 1: Criar conta no SonarCloud**
1. Acesse https://sonarcloud.io
2. Faça login com sua conta GitHub
3. Clique em **"+"** → **Analyze new project**
4. Selecione `teste-alura1`
5. Escolha **"With GitHub Actions"**

**Passo 2: Configurar o token**
1. O SonarCloud vai gerar um token
2. Copie o token
3. No GitHub: **Settings** → **Secrets and variables** → **Actions** → **New repository secret**
   - Name: `SONAR_TOKEN`
   - Value: token copiado

**Passo 3: Atualizar `sonar-project.properties`**

Edite o arquivo e atualize:
```properties
sonar.projectKey=SEU_USUARIO_teste-alura1
sonar.organization=SEU_USUARIO
```

Substitua `SEU_USUARIO` pelo seu usuário do GitHub/SonarCloud.

## 🚀 Como Funciona

### Trigger
O workflow é executado quando:
- ✅ Há push nas branches `master` ou `main`
- ✅ Há pull request para `master` ou `main`

### Jobs

#### Job 1: Semgrep
- Faz checkout do código
- Executa Semgrep com regras customizadas (`.semgrep.yml`)
- Detecta vulnerabilidades de segurança
- Faz upload dos resultados como artifact

#### Job 2: SonarCloud
- Faz checkout do código (com histórico completo)
- Executa análise do SonarCloud
- Verifica Quality Gate
- Identifica:
  - 🐛 Bugs
  - 🔒 Vulnerabilidades
  - 💩 Code Smells
  - 📊 Cobertura de código
  - 🔄 Código duplicado

## 📊 Visualizar Resultados

### Semgrep
- No GitHub Actions: aba **Actions** → workflow → **Artifacts** → `semgrep-results`
- Ou no console do workflow

### SonarCloud
- Acesse: https://sonarcloud.io/project/overview?id=michelleamesquita_teste-alura1
- Dashboard completo com métricas de qualidade

## 🎯 Exemplo de Detecção

Este workflow vai detectar a vulnerabilidade XSS em `app.py`:

**Semgrep vai reportar:**
```
flask-xss-user-input-template
Possível vulnerabilidade XSS: dados do usuário usados em 
render_template_string sem sanitização
```

**SonarCloud vai reportar:**
- Security Hotspot para XSS
- Possíveis melhorias de código
- Métricas de manutenibilidade

## ⚡ Execução Local

### Testar Semgrep:
```bash
source venv/bin/activate
semgrep --config .semgrep.yml app.py
```

### Testar SonarCloud (requer Docker):
```bash
docker run --rm \
  -e SONAR_HOST_URL="https://sonarcloud.io" \
  -e SONAR_TOKEN="seu-token" \
  -v "$(pwd):/usr/src" \
  sonarsource/sonar-scanner-cli
```

## 🔐 Segurança dos Secrets

- ✅ NUNCA commite tokens/secrets no código
- ✅ Use apenas GitHub Secrets
- ✅ Tokens são mascarados nos logs
- ✅ Secrets não são expostos em forks

## 📝 Badges (Opcional)

Adicione ao seu README.md:

```markdown
[![Security Scan](https://github.com/michelleamesquita/teste-alura1/actions/workflows/security-scan.yml/badge.svg)](https://github.com/michelleamesquita/teste-alura1/actions/workflows/security-scan.yml)

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=michelleamesquita_teste-alura1&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=michelleamesquita_teste-alura1)
```
