#!/usr/bin/env python3
"""
Script para atualizar o tempo de leitura dos posts markdown.
Pode ser usado para posts existentes ou novos.
"""

import os
import re
import glob
from pathlib import Path
from add_reading_time import count_words, calculate_reading_time, format_reading_time

def update_reading_time_in_post(file_path):
    """Atualiza o tempo de leitura nos metadados de um post."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Conta palavras
    word_count = count_words(content)
    reading_time_minutes = calculate_reading_time(word_count)
    reading_time_text = format_reading_time(reading_time_minutes)
    
    # Verifica se já tem tempo de leitura
    if 'readingTime = ' in content:
        # Atualiza o valor existente
        content = re.sub(
            r'readingTime = "[^"]*"',
            f'readingTime = "{reading_time_text}"',
            content
        )
        print(f"🔄 {file_path}: Atualizado para {reading_time_text} ({word_count} palavras)")
    else:
        # Adiciona novo tempo de leitura
        if '+++' in content:
            metadata_end = content.find('+++', 3)
            if metadata_end != -1:
                content = (
                    content[:metadata_end] + 
                    f'readingTime = "{reading_time_text}"\n' +
                    content[metadata_end:]
                )
                print(f"✅ {file_path}: Adicionado {reading_time_text} ({word_count} palavras)")
            else:
                print(f"❌ {file_path}: Não foi possível encontrar o fechamento dos metadados")
                return
        else:
            print(f"❌ {file_path}: Não possui metadados no formato +++")
            return
    
    # Salva o arquivo
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

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
    
    print(f"📝 Atualizando tempo de leitura em {len(md_files)} arquivo(s)...\n")
    
    for file_path in md_files:
        if file_path.name == "_index.md":
            continue  # Pula arquivos de índice
        update_reading_time_in_post(file_path)
    
    print(f"\n✨ Atualização concluída!")

if __name__ == "__main__":
    main() 