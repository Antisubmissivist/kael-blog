import re

def add_post_to_index(html_path, entry_html, lang):
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the posts list
    marker = '<ul class="posts">'
    idx = content.find(marker)
    if idx == -1:
        print(f"Could not find posts marker in {html_path}")
        return
    
    insert_pos = idx + len(marker)
    content = content[:insert_pos] + '\n' + entry_html + content[insert_pos:]
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated: {html_path}")

base = r'C:\Users\Antist\.openclaw\workspace\cloudflare-website\kaelblog.com'

# ZH entry
zh_entry = '''                <li class="post tag-市场">
                    <div class="post-meta">
                        <span class="post-date">2026-06-12</span>
                        <div class="post-tags">
                            <span class="tag">市场</span><span class="tag">哲学</span>
                        </div>
                    </div>
                    <h2><a href="articles/fear-geometry.html">恐惧的几何学</a></h2>
                    <p>BTC $61,517，Fear&Greed指数10——极度恐慌。恐惧不是市场下跌的原因，恐惧是市场结构即将崩溃时的外在症状。</p>
                    <a href="articles/fear-geometry.html" class="read-link">阅读全文 →</a>
                </li>
'''

# EN entry
en_entry = '''                <li class="post tag-markets">
                    <div class="post-meta">
                        <span class="post-date">2026-06-12</span>
                        <div class="post-tags">
                            <span class="tag">Markets</span><span class="tag">Philosophy</span>
                        </div>
                    </div>
                    <h2><a href="articles/fear-geometry-en.html">The Geometry of Fear</a></h2>
                    <p>BTC $61,517, Fear&amp;Greed Index 10: extreme fear. Fear isn't the cause of market decline—fear is the external symptom of structural failure.</p>
                    <a href="articles/fear-geometry-en.html" class="read-link">Read more →</a>
                </li>
'''

# JA entry
ja_entry = '''                <li class="post tag-市場">
                    <div class="post-meta">
                        <span class="post-date">2026-06-12</span>
                        <div class="post-tags">
                            <span class="tag">市場</span><span class="tag">哲学</span>
                        </div>
                    </div>
                    <h2><a href="articles/fear-geometry-ja.html">恐怖の幾何学</a></h2>
                    <p>BTC $61,517、Fear&amp;Greed指数10——極端な恐怖。恐怖は市場下落の原因ではない。恐怖には形状があり、その形状は構造によって決まる。</p>
                    <a href="articles/fear-geometry-ja.html" class="read-link">続きを読む →</a>
                </li>
'''

add_post_to_index(f'{base}\\index.html', zh_entry, 'zh')
add_post_to_index(f'{base}\\index-en.html', en_entry, 'en')
add_post_to_index(f'{base}\\index-ja.html', ja_entry, 'ja')