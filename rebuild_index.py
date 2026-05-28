#!/usr/bin/env python3
"""Update kaelblog index by scanning articles/ directory"""

import os
import re
import glob

BASE = os.path.dirname(os.path.abspath(__file__))
ARTICLES_DIR = os.path.join(BASE, 'articles')
INDEX_HTML = os.path.join(BASE, 'index.html')

def extract_from_article(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Title
    m = re.search(r'<h1>(.*?)</h1>', content)
    title = m.group(1).strip() if m else os.path.basename(path)
    
    # Date
    m = re.search(r'<span class="meta-date">(\d{4}-\d{2}-\d{2})</span>', content)
    date = m.group(1) if m else '2026-01-01'
    
    # Tags
    tags = re.findall(r'<span class="tag">(.*?)</span>', content)
    
    # Excerpt (first paragraph in article body)
    m = re.search(r'<article>(.*?)</article>', content, re.DOTALL)
    excerpt = ''
    if m:
        p_match = re.search(r'<p>(.*?)</p>', m.group(1))
        if p_match:
            excerpt = re.sub(r'<[^>]+>', '', p_match.group(1)).strip()[:120]
    
    slug = os.path.basename(path)
    return {'title': title, 'date': date, 'tags': tags, 'excerpt': excerpt, 'slug': slug}

def build_index():
    articles = []
    for f in sorted(glob.glob(os.path.join(ARTICLES_DIR, '*.html'))):
        slug = os.path.basename(f)
        # Skip translation files for main index
        if '-en.html' in slug or '-ja.html' in slug:
            continue
        articles.append(extract_from_article(f))
    
    # Sort by date descending
    articles.sort(key=lambda x: x['date'], reverse=True)
    
    posts_html = ''
    for a in articles:
        tags_html = ''.join(f'<span class="tag">{t}</span>' for t in a['tags'])
        posts_html += f'''
                <li class="post{' tag-' + a['tags'][0] if a['tags'] else ''}">
                    <div class="post-meta">
                        <span class="post-date">{a['date']}</span>
                        <div class="post-tags">
                            {tags_html}
                        </div>
                    </div>
                    <h2><a href="articles/{a['slug']}">{a['title']}</a></h2>
                    <p>{a['excerpt']}</p>
                    <a href="articles/{a['slug']}" class="read-link">阅读全文 →</a>
                </li>
'''
    return posts_html

def update_html(index_path, posts_html):
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace posts list
    old = re.search(r'<ul class="posts">.*?</ul>', content, re.DOTALL)
    if old:
        new_content = content.replace(old.group(0), f'<ul class="posts">\n{posts_html}\n            </ul>', 1)
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated {index_path}')
    else:
        print(f'Could not find posts list in {index_path}')

posts_html = build_index()
update_html(INDEX_HTML, posts_html)

# Also update index-en.html and index-ja.html
for lang in ['en', 'ja']:
    lang_index = os.path.join(BASE, f'index-{lang}.html')
    if os.path.exists(lang_index):
        update_html(lang_index, posts_html)

print('Done!')