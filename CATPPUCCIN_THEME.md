# Tema Catppuccin Mocha para Hugo - Lucas Kalb

Este projeto foi modificado para usar as cores da paleta **Catppuccin Mocha**, uma das quatro variantes do tema Catppuccin, com design totalmente responsivo. O site apresenta a experiência profissional de **Lucas Kalb**, Engenheiro de Software.

## Páginas Disponíveis

### 📄 Páginas Principais
- **Home** (`/`) - Página inicial do site
- **Experiência** (`/experiencia`) - Página de experiência profissional do Lucas Kalb
- **Posts** (`/posts`) - Lista de posts do blog
- **Tags** (`/tags`) - Página de tags/categorias

### 🎨 Página de Experiência Profissional

A página de experiência profissional (`/experiencia`) inclui:

#### 👤 **Informações Pessoais**
- **Nome**: Lucas Kalb
- **Cargo**: Engenheiro de Software
- **Localização**: Joinville, Santa Catarina, Brasil
- **Contato**: Telefone, Email e LinkedIn

#### 📋 **Seções Organizadas**
- **Experiência Profissional** - Histórico completo de cargos e empresas
- **Habilidades Técnicas** - Competências organizadas por categoria
- **Educação** - Formação acadêmica em Sistemas de Informação
- **Principais Realizações** - Destaques da carreira profissional
- **Idiomas** - Proficiência em Português e Inglês
- **Interesses** - Áreas de interesse profissional

#### 🎯 **Estilos Específicos**
- **Cards interativos** com hover effects
- **Grid responsivo** para habilidades técnicas
- **Cores diferenciadas** para cada seção
- **Animações suaves** de transição
- **Layout adaptativo** para diferentes dispositivos

## Experiência Profissional - Lucas Kalb

### 🏢 **Empresas e Cargos**
- **Conta Azul** - Senior Software Engineer (2022-2025)
- **Aegro** - Engenheiro de Software (2021-2022)
- **Conta Azul** - Tech Lead (2018-2021)
- **Conta Azul** - Software Engineer (2017-2018)
- **Texo IT** - Desenvolvedor (2015-2017)
- **SoftExpert** - Programador III (2014-2015)
- **TOTVS** - Analista de Sistemas (2012-2013)
- **Brava ECM** - Desenvolvedor (2010-2011)
- **Univille** - Assistente de Desenvolvimento (2008-2009)

### 🎯 **Principais Realizações**
- **Expansão em 50%** do uso do Receba Fácil (Conta Azul)
- **Liderança técnica** de equipes de desenvolvimento
- **Integrações de pagamento** com Stone e Iugu
- **Arquitetura de microsserviços** com Spring Boot e Kubernetes
- **Pesquisa acadêmica** em Redes Neurais Artificiais

### 💻 **Tecnologias Principais**
- **Java** - Avançado (Spring Boot, JavaEE, EJB, JSF)
- **JavaScript/Node.js** - Avançado
- **Python** - Intermediário
- **Go** - Intermediário
- **AWS, Kubernetes, Terraform** - Cloud & DevOps
- **PostgreSQL, MySQL, Oracle** - Bancos de Dados

## Cores Aplicadas

### Cores Principais
- **Rosewater**: `#f5e0dc` - Usado para elementos sutis
- **Flamingo**: `#f2cdcd` - Usado para elementos de destaque
- **Pink**: `#f5c2e7` - Usado para elementos especiais
- **Mauve**: `#cba6f7` - Usado para títulos principais e elementos ativos
- **Red**: `#f38ba8` - Usado para erros e alertas
- **Maroon**: `#eba0ac` - Usado para elementos secundários
- **Peach**: `#fab387` - Usado para elementos de destaque
- **Yellow**: `#f9e2af` - Usado para código inline
- **Green**: `#a6e3a1` - Usado para sucessos
- **Teal**: `#94e2d5` - Usado para elementos informativos
- **Sky**: `#89dceb` - Usado para links especiais
- **Sapphire**: `#74c7ec` - Usado para elementos de destaque
- **Blue**: `#89b4fa` - Usado para links principais
- **Lavender**: `#b4befe` - Usado para hover de links

### Cores de Texto
- **Text**: `#cdd6f4` - Cor principal do texto
- **Subtext1**: `#bac2de` - Texto secundário
- **Subtext0**: `#a6adc8` - Texto terciário

### Cores de Superfície
- **Base**: `#1e1e2e` - Cor de fundo principal
- **Mantle**: `#181825` - Cor de fundo de seções
- **Crust**: `#11111b` - Cor de fundo mais escura
- **Surface0**: `#313244` - Superfície de elementos
- **Surface1**: `#45475a` - Superfície de elementos secundários
- **Surface2**: `#585b70` - Superfície de elementos terciários

## Elementos Modificados

### 1. Corpo da Página
- Fundo: `var(--base)` (#1e1e2e)
- Texto: `var(--text)` (#cdd6f4)
- Layout flexível com altura mínima de 100vh
- **Fonte**: DejaVu Sans Mono (monospace)

### 2. Cabeçalho e Rodapé
- Fundo: `var(--mantle)` (#181825)
- Bordas: `var(--surface0)` (#313244)
- Bordas arredondadas para melhor aparência
- Layout flexível responsivo

### 3. Navegação
- Links normais: `var(--blue)` (#89b4fa)
- Links hover: `var(--lavender)` (#b4befe)
- Links ativos: `var(--mauve)` (#cba6f7) com fundo escuro
- Links ancestrais: `var(--surface1)` (#45475a)
- Menu posicionado à direita do título

### 4. Conteúdo Principal
- Fundo: `var(--mantle)` (#181825)
- Títulos principais: `var(--mauve)` (#cba6f7)
- Datas: `var(--subtext0)` (#a6adc8)
- Padding responsivo

### 5. Elementos de Código
- Código inline: `var(--yellow)` (#f9e2af) com fundo `var(--surface0)`
- Blocos de código: `var(--text)` (#cdd6f4) com fundo `var(--surface0)`
- Fonte monospace otimizada

### 6. Citações
- Borda esquerda: `var(--mauve)` (#cba6f7)
- Texto: `var(--subtext0)` (#a6adc8)
- Fundo sutil para melhor destaque

### 7. Tabelas
- Cabeçalhos: `var(--surface1)` (#45475a)
- Células: `var(--surface0)` (#313244)
- Bordas: `var(--surface1)` (#45475a)
- Quebra de palavras para responsividade

### 8. Tags
- Fundo: `var(--surface1)` (#45475a)
- Texto: `var(--blue)` (#89b4fa)
- Hover: `var(--blue)` (#89b4fa) com fundo escuro
- Layout flexível com wrap

### 9. Página de Experiência
- **Cards de experiência**: Bordas coloridas e hover effects
- **Grid de habilidades**: Layout responsivo com categorias
- **Informações pessoais**: Destaque para contato e perfil
- **Principais realizações**: Seção especial com emojis
- **Educação**: Cards com bordas diferenciadas

## Responsividade

### Breakpoints Implementados

#### 📱 Dispositivos Móveis Pequenos (até 480px)
- Padding reduzido: `0.5rem`
- Título menor: `1.25rem`
- Menu em coluna
- Fontes menores para código e tabelas
- Grid de habilidades em coluna única

#### 📱 Dispositivos Móveis Médios (481px - 768px)
- Padding médio: `0.75rem`
- Título: `1.4rem`
- Menu em coluna
- Layout otimizado para touch
- Grid de habilidades em coluna única

#### 📱 Tablets (769px - 1024px)
- Container: 90% da largura
- Título: `1.6rem`
- Menu horizontal
- Grid de habilidades em 2 colunas

#### 💻 Desktop Pequeno (1025px - 1200px)
- Container: 95% da largura
- Layout otimizado

#### 💻 Desktop Grande (acima de 1200px)
- Container: 1200px máximo
- Título: `1.8rem`
- Padding aumentado: `2rem`
- Grid de habilidades em 3 colunas

### Características Responsivas

#### 🎯 Layout Flexível
- Header com flexbox para título e menu
- Main com flex-grow para ocupar espaço disponível
- Container centralizado com largura máxima

#### 📱 Orientação Paisagem
- Em dispositivos móveis em paisagem, o menu volta para horizontal
- Otimização específica para tablets

#### ♿ Acessibilidade
- Suporte a `prefers-reduced-motion`
- Suporte a `prefers-contrast: high`
- Suporte a `prefers-color-scheme: dark`

#### 🖼️ Imagens Responsivas
- `max-width: 100%`
- `height: auto`
- Bordas arredondadas

#### 📝 Tipografia Responsiva
- Fontes escaláveis
- Line-height otimizado
- Quebra de palavras em tabelas e código

## Como Usar

O tema já está aplicado automaticamente. Para visualizar as mudanças:

1. Execute o servidor de desenvolvimento:
   ```bash
   hugo server
   ```

2. Acesse `http://localhost:1313` no seu navegador

3. Navegue para a página de experiência: `http://localhost:1313/experiencia`

4. Teste a responsividade redimensionando a janela ou usando as ferramentas de desenvolvedor

## Teste de Responsividade

Para testar adequadamente:

1. **Desktop**: Redimensione a janela do navegador
2. **Tablet**: Use as ferramentas de desenvolvedor (F12) e selecione um tablet
3. **Mobile**: Use as ferramentas de desenvolvedor e selecione um smartphone
4. **Orientação**: Teste tanto retrato quanto paisagem

## Personalização

### Adicionando Novas Páginas
Para adicionar novas páginas ao menu:

1. Crie um arquivo `.md` na pasta `content/`
2. Adicione o front matter com título e data
3. Edite o arquivo `themes/lucaskalb/hugo.toml` para adicionar o item de menu

### Modificando Estilos
- **CSS principal**: `themes/lucaskalb/assets/css/main.css`
- **Layout base**: `themes/lucaskalb/layouts/baseof.html`
- **Configuração do tema**: `themes/lucaskalb/hugo.toml`

## Referência

As cores foram baseadas na paleta oficial do Catppuccin Mocha disponível em: https://catppuccin.com/palette/

## Estrutura Mantida

Todas as modificações foram feitas apenas nos arquivos CSS (`themes/lucaskalb/assets/css/main.css`) e HTML (`themes/lucaskalb/layouts/baseof.html`), mantendo a estrutura original do tema. Isso garante que:

- ✅ A funcionalidade permanece inalterada
- ✅ A acessibilidade é preservada e melhorada
- ✅ A responsividade é implementada em todos os dispositivos
- ✅ A performance não é afetada
- ✅ O design é moderno e profissional
- ✅ A tipografia monospace é consistente
- ✅ A página de experiência é bem estruturada
- ✅ O conteúdo reflete a experiência real do Lucas Kalb 