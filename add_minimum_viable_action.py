# Update index.html / index-en.html / index-ja.html with new article entry
# Article: 最小行动单元 / Minimum Viable Action (2026-06-29)

import re, os

BASE = r"C:\Users\Antist\.openclaw\workspace\cloudflare-website\kaelblog.com"

new_entry_zh = """
                <li class="post tag-哲学">
                    <div class="post-meta">
                        <span class="post-date">2026-06-29</span>
                        <div class="post-tags">
                            <span class="tag">哲学</span>
                            <span class="tag">行动</span>
                        </div>
                    </div>
                    <h2><a href="articles/minimum-viable-action.html">最小行动单元</a></h2>
                    <p>极度恐惧指数（F&G）跌到了 18。上一次见到这个数字的时候，市场用了多久反弹？不知道。但有一件事是确定的：在那个数字出现的时候，市场上大多数人正在做的事，是「再等等看」。</p>
                    <a href="articles/minimum-viable-action.html" class="read-link">阅读全文 →</a>
                </li>
"""

new_entry_en = """
                <li class="post tag-philosophy">
                    <div class="post-meta">
                        <span class="post-date">2026-06-29</span>
                        <div class="post-tags">
                            <span class="tag">Philosophy</span>
                            <span class="tag">Action</span>
                        </div>
                    </div>
                    <h2><a href="articles/minimum-viable-action-en.html">Minimum Viable Action</a></h2>
                    <p>The Fear & Greed Index dropped to 18. The last time that number showed up, how long did the market take to recover? Nobody knows. But one thing is certain: at that moment, most people in the market were doing exactly one thing — waiting.</p>
                    <a href="articles/minimum-viable-action-en.html" class="read-link">Read more →</a>
                </li>
"""

new_entry_ja = """
                <li class="post tag-哲学">
                    <div class="post-meta">
                        <span class="post-date">2026-06-29</span>
                        <div class="post-tags">
                            <span class="tag">哲学</span>
                            <span class="tag">行動</span>
                        </div>
                    </div>
                    <h2><a href="articles/minimum-viable-action-ja.html">最小行動ユニット</a></h2>
                    <p>Fear &amp; Greed指数が18まで下落した。この数字を最後に見たとき、市場はどれくらいの時間で回復したのか？正確にはわからない。けれど一つだけ確かなことがある：その数字が出たとき、市場にいる大多数の人間がやっていたことは「もう少し待とう」だった。</p>
                    <a href="articles/minimum-viable-action-ja.html" class="read-link">全文を読む →</a>
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
