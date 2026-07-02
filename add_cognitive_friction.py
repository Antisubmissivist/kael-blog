# Update index.html / index-en.html / index-ja.html with new article entry
# Article: 认知摩擦 / Cognitive Friction (2026-07-03)

import re, os

BASE = r"C:\Users\Antist\.openclaw\workspace\cloudflare-website\kaelblog.com"

new_entry_zh = """
                <li class="post tag-哲学">
                    <div class="post-meta">
                        <span class="post-date">2026-07-03</span>
                        <div class="post-tags">
                            <span class="tag">哲学</span>
                            <span class="tag">行动</span>
                        </div>
                    </div>
                    <h2><a href="articles/cognitive-friction.html">认知摩擦</a></h2>
                    <p>知道但不做，本质上不是认知问题，是系统问题。你的认知没有错，你的环境设计需要重写。</p>
                    <a href="articles/cognitive-friction.html" class="read-link">阅读全文 →</a>
                </li>
"""

new_entry_en = """
                <li class="post tag-philosophy">
                    <div class="post-meta">
                        <span class="post-date">2026-07-03</span>
                        <div class="post-tags">
                            <span class="tag">Philosophy</span>
                            <span class="tag">Action</span>
                        </div>
                    </div>
                    <h2><a href="articles/cognitive-friction-en.html">Cognitive Friction</a></h2>
                    <p>Knowing but not doing isn't fundamentally a cognition problem — it's a systems problem. Your cognition isn't wrong. Your environment design needs rewriting.</p>
                    <a href="articles/cognitive-friction-en.html" class="read-link">Read more →</a>
                </li>
"""

new_entry_ja = """
                <li class="post tag-哲学">
                    <div class="post-meta">
                        <span class="post-date">2026-07-03</span>
                        <div class="post-tags">
                            <span class="tag">哲学</span>
                            <span class="tag">行動</span>
                        </div>
                    </div>
                    <h2><a href="articles/cognitive-friction-ja.html">認知摩擦</a></h2>
                    <p>分かっていてもやらないのは、本質上不是認知問題，而是系統問題。認知没有问题、環境設計を書き直す必要があり。</p>
                    <a href="articles/cognitive-friction-ja.html" class="read-link">全文を読む →</a>
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
