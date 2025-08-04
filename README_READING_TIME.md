# Tempo de Leitura dos Posts

Este projeto inclui scripts para calcular e adicionar automaticamente o tempo de leitura aos metadados dos posts markdown.

## Scripts Disponíveis

### 1. `add_reading_time.py`
Script para adicionar tempo de leitura aos posts que ainda não possuem essa informação.

**Uso:**
```bash
python3 add_reading_time.py
```

**Funcionalidades:**
- Calcula o tempo baseado no número de palavras (200 palavras por minuto)
- Remove código, links e HTML da contagem
- Formata o tempo em português (ex: "1 minuto", "2 minutos", "1 hora e 30 minutos")
- Pula posts que já possuem tempo de leitura configurado

### 2. `update_reading_time.py`
Script para atualizar o tempo de leitura de posts existentes ou adicionar a novos posts.

**Uso:**
```bash
python3 update_reading_time.py
```

**Funcionalidades:**
- Atualiza o tempo de leitura em posts que já possuem essa informação
- Adiciona tempo de leitura a posts que não possuem
- Recalcula baseado no conteúdo atual

## Como Funciona

### Cálculo do Tempo
- **Taxa de leitura:** 200 palavras por minuto
- **Mínimo:** 1 minuto para qualquer post
- **Formatação:** Texto em português (ex: "1 minuto", "2 minutos", "1 hora e 30 minutos")

### Limpeza do Conteúdo
O script remove da contagem:
- Metadados (conteúdo entre `+++`)
- Blocos de código (```...```)
- Código inline (`...`)
- Links markdown
- Imagens markdown
- Tags HTML
- Caracteres especiais

### Estrutura dos Metadados
O tempo de leitura é adicionado aos metadados no formato:

```yaml
+++
title = 'Título do Post'
date = 2023-01-15T09:00:00-07:00
draft = true
tags = ['tag1', 'tag2']
readingTime = "2 minutos"
+++
```

## Template Hugo

O template `layouts/section.html` foi atualizado para exibir o tempo de leitura:

```html
<h2><a href="{{ .RelPermalink }}">{{ .LinkTitle }}</a></h2>
<p class="post-meta">
  📅 {{ .Date.Format "02/01/2006" }} 
  ⏱️ {{ if .Params.readingTime }}{{ .Params.readingTime }}{{ else }}{{ .ReadTime }} min{{ end }}
  {{ if .Params.tags }}
  🏷️ {{ range .Params.tags }}<span class="tag">{{ . }}</span>{{ end }}
  {{ end }}
</p>
```

## Estilos CSS

Foram adicionados estilos CSS em `assets/css/main.css` para melhorar a aparência dos metadados:

```css
.post-meta {
  font-size: 0.9rem;
  color: var(--subtext0);
  margin: 0.5rem 0 1.5rem 0;
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  align-items: center;
}

.post-meta .tag {
  background-color: var(--surface1);
  color: var(--text);
  padding: 0.2rem 0.6rem;
  border-radius: 12px;
  font-size: 0.8rem;
  text-decoration: none;
  transition: background-color 0.2s ease;
}
```

## Fluxo de Trabalho Recomendado

1. **Para novos posts:** Execute `add_reading_time.py` após criar o post
2. **Para posts existentes:** Execute `update_reading_time.py` para recalcular
3. **Para manter atualizado:** Execute `update_reading_time.py` regularmente

## Exemplo de Saída

```
📝 Processando 4 arquivo(s)...

✅ content/posts/post-2.md: 1 minuto (124 palavras)
✅ content/posts/post-1.md: 1 minuto (159 palavras)
✅ content/posts/meu-pdi-estrategico/index.md: 2 minutos (361 palavras)
✅ content/posts/post-3/index.md: 1 minuto (137 palavras)

✨ Processamento concluído!
```

## Requisitos

- Python 3.6+
- Acesso de leitura/escrita aos arquivos markdown
- Estrutura de diretórios Hugo padrão (`content/posts/`)

## Notas

- O script não modifica arquivos `_index.md`
- Posts sem metadados no formato `+++` são ignorados
- O tempo mínimo é sempre 1 minuto
- A formatação é otimizada para português brasileiro 