import re
with open('articles/kael-blog-launch.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The article-body div starts immediately after <main>
# The first </div> after article-body IS the article-body closing div
# Let's use a simpler approach: find article-body open, then grab content until that closing div

ab_start = content.find('<div class="article-body">')
main_start = content.find('<main>')

# Find first </div> after article-body
search_from = ab_start + len('<div class="article-body">')
search_slice = content[search_from:]
first_div = search_slice.find('</div>')

if first_div >= 0:
    actual_end = search_from + first_div
    article_text = content[ab_start + len('<div class="article-body">'):actual_end]
    print('Article content len:', len(article_text))
    print('First 200:', article_text[:200])
    print('Last 200:', article_text[-200:])
else:
    print('Could not find closing div')
