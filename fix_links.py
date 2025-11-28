#!/usr/bin/env python3
"""
Script to convert legacy MediaWiki/PHP links to Hugo format.
Converts: index.php%3Ftitle=Article_Name.html to /ejercicios/article-name/
"""

import re
import os
from pathlib import Path
import urllib.parse

def slugify(text):
    """Convert text to URL-friendly slug."""
    # Decode URL encoding
    text = urllib.parse.unquote(text)
    # Remove .html extension
    text = text.replace('.html', '')
    # Convert to lowercase
    text = text.lower()
    # Replace underscores and spaces with hyphens
    text = text.replace('_', '-').replace(' ', '-')
    # Remove special prefixes
    text = re.sub(r'^categoría:', '', text)
    text = re.sub(r'^archivo:', '', text)
    text = re.sub(r'^especial:', '', text)
    # Remove parentheses and other special characters, keep hyphens
    text = re.sub(r'[^\w\s-]', '', text)
    # Replace multiple hyphens with single hyphen
    text = re.sub(r'-+', '-', text)
    # Remove leading/trailing hyphens
    text = text.strip('-')
    return text

def convert_link(match):
    """Convert a single PHP link to Hugo format."""
    full_match = match.group(0)
    title = match.group(1)  # Link text
    url = match.group(2)    # URL
    
    # Extract the article name from the URL
    # Pattern: index.php%3Ftitle=Article_Name.html
    article_match = re.search(r'index\.php%3Ftitle=([^)"\s]+)', url)
    if not article_match:
        return full_match  # Return unchanged if pattern doesn't match
    
    article_name = article_match.group(1)
    
    # Handle special cases
    if 'Especial:' in article_name or 'especial:' in article_name.lower():
        # Skip special pages
        return full_match
    elif 'Archivo:' in article_name or 'archivo:' in article_name.lower():
        # Image/file links - keep as is or handle differently
        return full_match
    elif 'Categoría:' in article_name or 'categoría:' in article_name.lower():
        # Category links
        slug = slugify(article_name)
        return f'[{title}](/ejercicios/{slug}/)'
    else:
        # Regular article links
        slug = slugify(article_name)
        return f'[{title}](/ejercicios/{slug}/)'

def process_file(filepath):
    """Process a single markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Pattern 1: Regular links with index.php
    # Format: [Link Text](index.php%3Ftitle=Article_Name.html "Title")
    pattern1 = r'\[([^\]]+)\]\((index\.php%3Ftitle=[^)]+\.html)\s+"[^"]*"\)'
    content = re.sub(pattern1, convert_link, content)
    
    # Pattern 2: Image links - remove the outer link, keep just the image
    # Format: [![alt](image.jpg)](index.php%3Ftitle=Archivo:image.jpg.html "title")
    # Replace with just: ![alt](image.jpg)
    pattern2 = r'\[!\[([^\]]*)\]\(([^)]+)\)\]\(index\.php%3Ftitle=Archivo:[^)]+\s+"[^"]*"\)'
    content = re.sub(pattern2, r'![\1](\2)', content)
    
    # Pattern 3: Links with escaped characters or any other special formatting
    # Use a more permissive pattern that matches any URL ending in .html
    # Non-greedy match to stop at the first closing paren followed by space and quote
    pattern3 = r'\[([^\]]+)\]\((index\.php%3Ftitle=.+?\.html)\s+"[^"]*"\)'
    content = re.sub(pattern3, convert_link, content)
    
    # Only write if content changed
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    """Process all markdown files in the content directory."""
    content_dir = Path('content/ejercicios')
    
    if not content_dir.exists():
        print(f"Error: {content_dir} does not exist")
        return
    
    files_changed = 0
    files_processed = 0
    
    for md_file in content_dir.glob('**/*.md'):
        files_processed += 1
        if process_file(md_file):
            files_changed += 1
            print(f"✓ Updated: {md_file.name}")
    
    print(f"\nProcessed {files_processed} files, updated {files_changed} files")

if __name__ == '__main__':
    main()
