# 🚀 Setup GitHub Actions - Guia Rápido

## 📁 Arquivos Criados

```
.github/
└── workflows/
    ├── security-scan.yml      # Workflow completo e avançado
    ├── simple-security.yml    # Workflow simples para iniciantes
    └── README.md              # Documentação detalhada
sonar-project.properties        # Configuração do SonarCloud
```

## ⚡ Início Rápido (3 passos)

### 1️⃣ Push para GitHub

```bash
git add .github/ sonar-project.properties GITHUB_ACTIONS_SETUP.md
git commit -m "Add GitHub Actions for security scanning"
git push -u origin master
```

### 2️⃣ Configurar SonarCloud

1. Acesse: https://sonarcloud.io
2. Login com GitHub
3. Clique em **"+"** → **"Analyze new project"**
4. Selecione: `teste-alura1`
5. Escolha: **"With GitHub Actions"**
6. Copie o **SONAR_TOKEN** gerado
7. No GitHub: **Settings** → **Secrets** → **New secret**
   - Name: `SONAR_TOKEN`
   - Value: [cole o token]

### 3️⃣ Atualizar configuração

Edite `sonar-project.properties` e mude:
```properties
sonar.projectKey=SEU_USUARIO_teste-alura1
sonar.organization=SEU_USUARIO
```

## ✅ Pronto!

Faça qualquer commit e o workflow vai executar automaticamente:

```bash
echo "# test" >> README.md
git add README.md
git commit -m "Test workflow"
git push
```

Veja os resultados em: **Actions** tab no GitHub

## 🔍 O que cada ferramenta faz?

### Semgrep
- ✅ Detecta vulnerabilidades de segurança
- ✅ Executa regras customizadas (.semgrep.yml)
- ✅ Rápido e sem configuração necessária
- ✅ Detecta a vulnerabilidade XSS no app.py

### SonarCloud
- ✅ Análise completa de qualidade de código
- ✅ Detecta bugs, vulnerabilidades e code smells
- ✅ Métricas de cobertura e complexidade
- ✅ Dashboard visual completo
- ⚠️ Requer configuração de token

## 🎯 Exemplo de Resultado

Quando você fizer push, os workflows vão:

1. **Semgrep** vai detectar:
```
❌ FAILED
flask-xss-user-input-template
app.py:22 - Vulnerabilidade XSS detectada
```

2. **SonarCloud** vai mostrar:
```
📊 Quality Gate: Failed
🐛 1 Bug
🔒 1 Security Hotspot  
💩 2 Code Smells
```

## 📚 Workflows Disponíveis

### `simple-security.yml` (Recomendado para começar)
- Simples e direto
- 2 jobs: Semgrep + SonarCloud
- Fácil de entender

### `security-scan.yml` (Avançado)
- Mais completo
- Upload de artifacts
- Quality Gate check
- Error handling

## 🔧 Opcional: Semgrep Cloud

Para recursos avançados (opcional):

1. Acesse https://semgrep.dev
2. Crie conta
3. Pegue o token em **Settings**
4. Adicione secret: `SEMGREP_APP_TOKEN`

**Mas funciona sem token também!** 🎉

## 🆘 Troubleshooting

### Semgrep falha
- ✅ Esperado! Tem vulnerabilidade no código
- Use `--error` para falhar no CI
- Ou remova `--error` para apenas avisar

### SonarCloud falha
- ❌ Token não configurado
- ❌ Organization/projectKey incorretos
- ✅ Siga o passo 2️⃣ acima

## 🏆 Badges

Adicione ao README.md para mostrar status:

```markdown
![Security](https://github.com/michelleamesquita/teste-alura1/actions/workflows/simple-security.yml/badge.svg)
```

## 📖 Mais Informações

Veja `.github/workflows/README.md` para documentação completa!
