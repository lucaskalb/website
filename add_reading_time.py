#!/usr/bin/env python3
"""
Script para adicionar tempo de leitura aos metadados dos posts markdown.
Calcula o tempo baseado no número de palavras (aproximadamente 200 palavras por minuto).
"""

import os
import re
import glob
from pathlib import Path

def count_words(text):
    """Conta o número de palavras no texto, excluindo metadados."""
    # Remove os metadados (conteúdo entre +++)
    content = re.sub(r'\+\+\+.*?\+\+\+', '', text, flags=re.DOTALL)
    
    # Remove código em blocos
    content = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
    
    # Remove código inline
    content = re.sub(r'`[^`]+`', '', content)
    
    # Remove links markdown
    content = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', content)
    
    # Remove imagens markdown
    content = re.sub(r'!\[([^\]]*)\]\([^)]+\)', '', content)
    
    # Remove HTML tags
    content = re.sub(r'<[^>]+>', '', content)
    
    # Remove caracteres especiais e quebras de linha
    content = re.sub(r'[^\w\s]', ' ', content)
    content = re.sub(r'\s+', ' ', content)
    
    # Conta palavras
    words = content.strip().split()
    return len(words)

def calculate_reading_time(word_count):
    """Calcula o tempo de leitura em minutos (200 palavras por minuto)."""
    minutes = max(1, round(word_count / 200))
    return minutes

def format_reading_time(minutes):
    """Formata o tempo de leitura em texto."""
    if minutes == 1:
        return "1 minuto"
    elif minutes < 60:
        return f"{minutes} minutos"
    else:
        hours = minutes // 60
        remaining_minutes = minutes % 60
        if remaining_minutes == 0:
            return f"{hours} hora{'s' if hours > 1 else ''}"
        else:
            return f"{hours} hora{'s' if hours > 1 else ''} e {remaining_minutes} minuto{'s' if remaining_minutes > 1 else ''}"

def add_reading_time_to_post(file_path):
    """Adiciona o tempo de leitura aos metadados de um post."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Verifica se já tem tempo de leitura
    if 'readingTime = ' in content:
        print(f"⚠️  {file_path} já possui tempo de leitura configurado")
        return
    
    # Conta palavras
    word_count = count_words(content)
    reading_time_minutes = calculate_reading_time(word_count)
    reading_time_text = format_reading_time(reading_time_minutes)
    
    # Adiciona o tempo de leitura aos metadados
    # Procura pelo padrão de metadados e adiciona antes do fechamento
    if '+++' in content:
        # Encontra o final dos metadados
        metadata_end = content.find('+++', 3)
        if metadata_end != -1:
            # Insere o tempo de leitura antes do fechamento dos metadados
            new_content = (
                content[:metadata_end] + 
                f'readingTime = "{reading_time_text}"\n' +
                content[metadata_end:]
            )
            
            # Salva o arquivo
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✅ {file_path}: {reading_time_text} ({word_count} palavras)")
        else:
            print(f"❌ {file_path}: Não foi possível encontrar o fechamento dos metadados")
    else:
        print(f"❌ {file_path}: Não possui metadados no formato +++")

def main():
    """Função principal."""
    posts_dir = Path("content/posts")
    
    if not posts_dir.exists():
        print("❌ Diretório content/posts não encontrado!")
        return
    
    # Encontra todos os arquivos .md
    md_files = list(posts_dir.glob("**/*.md"))
    
    if not md_files:
        print("❌ Nenhum arquivo .md encontrado em content/posts")
        return
    
    print(f"📝 Processando {len(md_files)} arquivo(s)...\n")
    
    for file_path in md_files:
        if file_path.name == "_index.md":
            continue  # Pula arquivos de índice
        add_reading_time_to_post(file_path)
    
    print(f"\n✨ Processamento concluído!")

if __name__ == "__main__":
    main() 