# Update index.html / index-en.html / index-ja.html with new article entry
# Article: 等待是最贵的分析 / Waiting Is the Most Expensive Analysis (2026-07-01)

import re, os

BASE = r"C:\Users\Antist\.openclaw\workspace\cloudflare-website\kaelblog.com"

new_entry_zh = """
                <li class="post tag-哲学">
                    <div class="post-meta">
                        <span class="post-date">2026-07-01</span>
                        <div class="post-tags">
                            <span class="tag">哲学</span>
                            <span class="tag">交易</span>
                        </div>
                    </div>
                    <h2><a href="articles/waiting-is-expensive-analysis.html">等待是最贵的分析</a></h2>
                    <p>「再等等看」是市场上最贵的五个字。不是因为它错了，而是因为它是一种伪装成不行动的深度分析。带着条件的等待是策略，没有条件的等待是拖延。</p>
                    <a href="articles/waiting-is-expensive-analysis.html" class="read-link">阅读全文 →</a>
                </li>
"""

new_entry_en = """
                <li class="post tag-philosophy">
                    <div class="post-meta">
                        <span class="post-date">2026-07-01</span>
                        <div class="post-tags">
                            <span class="tag">Philosophy</span>
                            <span class="tag">Trading</span>
                        </div>
                    </div>
                    <h2><a href="articles/waiting-is-expensive-analysis-en.html">Waiting Is the Most Expensive Analysis</a></h2>
                    <p>"I'll wait and see" — the most expensive five words in markets. Conditional waiting is strategy. Unconditional waiting is procrastination. They look identical, but their outcomes are worlds apart.</p>
                    <a href="articles/waiting-is-expensive-analysis-en.html" class="read-link">Read more →</a>
                </li>
"""

new_entry_ja = """
                <li class="post tag-哲学">
                    <div class="post-meta">
                        <span class="post-date">2026-07-01</span>
                        <div class="post-tags">
                            <span class="tag">哲学</span>
                            <span class="tag">取引</span>
                        </div>
                    </div>
                    <h2><a href="articles/waiting-is-expensive-analysis-ja.html">待つことは最も高い分析である</a></h2>
                    <p>「もう少し待ってみよう」——市場においてこれほどコストが掛かる五文字はない。条件付きの待ちは戦略、条件のない待ちは先送り。両者は見かけ上同じで、結末则天壤の別である。</p>
                    <a href="articles/waiting-is-expensive-analysis-ja.html" class="read-link">全文を読む →</a>
                </li>
"""

def insert_entry(path, new_entry, lang):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the ul.posts opening tag and insert after it
    pattern = r'(<ul class="posts">\n)'
    replacement = r'\1' + new_entry + '\n'
    
    new_content, count = re.subn(pattern, replacement, content, count=1)
    
    if count == 0:
        print(f'WARNING: Could not find posts list in {path}')
        return False
    else:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated {path}')
        return True

# Update all three indices
results = []
results.append(insert_entry(os.path.join(BASE, 'index.html'), new_entry_zh, 'ZH'))
results.append(insert_entry(os.path.join(BASE, 'index-en.html'), new_entry_en, 'EN'))
results.append(insert_entry(os.path.join(BASE, 'index-ja.html'), new_entry_ja, 'JA'))

if all(results):
    print('\nAll indices updated successfully.')
else:
    print('\nSome indices may need manual review.')