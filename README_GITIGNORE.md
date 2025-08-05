# Gitignore do Projeto Hugo

Este projeto possui um arquivo `.gitignore` configurado para projetos Hugo, incluindo suporte para ferramentas de desenvolvimento modernas.

## 📁 Arquivos Ignorados

### 🎯 **Hugo Específicos**
```
.hugo_build.lock    # Lock file do Hugo
public/             # Pasta de build do Hugo
resources/_gen/     # Recursos gerados pelo Hugo
assets/jsconfig.json # Configuração JS do Hugo
hugo_stats.json     # Estatísticas do Hugo
```

### 🏗️ **Build e Deploy**
```
build/              # Pasta de build alternativa
dist/               # Pasta de distribuição
.hugo/              # Cache do Hugo
.vercel             # Deploy Vercel
.netlify            # Deploy Netlify
```

### 💻 **IDEs e Editores**
```
.vscode/            # Configurações do VS Code
.idea/              # Configurações do IntelliJ
*.swp               # Arquivos temporários do Vim
*.swo               # Arquivos temporários do Vim
*~                  # Arquivos de backup
```

### 🖥️ **Sistemas Operacionais**
```
.DS_Store           # macOS
.DS_Store?          # macOS
._*                 # macOS
.Spotlight-V100     # macOS
.Trashes            # macOS
ehthumbs.db         # Windows
Thumbs.db           # Windows
```

### 📦 **Node.js (se usar)**
```
node_modules/       # Dependências
npm-debug.log*      # Logs do npm
yarn-debug.log*     # Logs do yarn
yarn-error.log*     # Logs do yarn
package-lock.json   # Lock file do npm
yarn.lock           # Lock file do yarn
```

### 🐍 **Python (para scripts)**
```
__pycache__/        # Cache Python
*.py[cod]           # Arquivos compilados Python
*.so                # Extensões Python
venv/               # Ambiente virtual
env/                # Ambiente virtual
```

### 🔧 **Configurações Locais**
```
config.local.toml   # Configuração local Hugo
config.local.yaml   # Configuração local Hugo
.env                # Variáveis de ambiente
.env.local          # Variáveis de ambiente local
```

## 🎯 **Por que Ignorar Esses Arquivos?**

### ✅ **Performance**
- Arquivos de build são grandes e desnecessários no repositório
- Cache pode ser regenerado localmente
- Reduz o tamanho do repositório

### ✅ **Segurança**
- Arquivos de configuração local podem conter senhas
- Variáveis de ambiente não devem ser versionadas
- Evita exposição de dados sensíveis

### ✅ **Colaboração**
- Cada desenvolvedor pode ter configurações locais diferentes
- Evita conflitos de merge desnecessários
- Mantém o repositório limpo

### ✅ **Deploy**
- Arquivos de build são gerados automaticamente
- Diferentes ambientes podem ter configurações diferentes
- Facilita o processo de CI/CD

## 🔧 **Como Usar**

### 📝 **Verificar Arquivos Ignorados**
```bash
# Ver quais arquivos estão sendo ignorados
git status --ignored

# Ver arquivos ignorados em uma pasta específica
git status --ignored content/
```

### 🆕 **Adicionar Novos Padrões**
Se precisar adicionar novos padrões ao `.gitignore`:

1. **Edite o arquivo `.gitignore`**
2. **Adicione o padrão na seção apropriada**
3. **Comente o motivo se necessário**

### 🗑️ **Remover Arquivos Já Versionados**
Se um arquivo já foi commitado e agora deve ser ignorado:

```bash
# Remove do repositório mas mantém localmente
git rm --cached arquivo.txt

# Remove pasta do repositório mas mantém localmente
git rm -r --cached pasta/
```

## 📋 **Exemplos de Uso**

### 🎨 **Desenvolvimento Frontend**
```bash
# Instalar dependências (se usar npm/yarn)
npm install

# Os arquivos node_modules/ serão ignorados automaticamente
```

### 🐍 **Scripts Python**
```bash
# Criar ambiente virtual
python -m venv venv

# O ambiente virtual será ignorado automaticamente
```

### 🚀 **Deploy**
```bash
# Build do Hugo
hugo

# A pasta public/ será ignorada automaticamente
```

## 🔍 **Verificação**

### ✅ **Verificar se está funcionando**
```bash
# Adicionar arquivo que deveria ser ignorado
touch .DS_Store

# Verificar status
git status

# O arquivo .DS_Store não deve aparecer
```

### 🛠️ **Solução de Problemas**

#### **Arquivo não está sendo ignorado:**
1. Verifique se o padrão está correto no `.gitignore`
2. Verifique se o arquivo já foi commitado anteriormente
3. Use `git rm --cached` se necessário

#### **Padrão muito amplo:**
1. Torne o padrão mais específico
2. Use `!` para exceções
3. Teste com `git status --ignored`

## 📚 **Recursos Adicionais**

- [Documentação oficial do Git](https://git-scm.com/docs/gitignore)
- [Gitignore.io](https://www.gitignore.io/) - Gerador de .gitignore
- [GitHub .gitignore templates](https://github.com/github/gitignore)

## 🎯 **Conclusão**

O `.gitignore` configurado garante que apenas os arquivos necessários sejam versionados, mantendo o repositório limpo e seguro. Isso facilita a colaboração e o deploy do projeto. 