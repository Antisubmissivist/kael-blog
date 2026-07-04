# Update index.html / index-en.html / index-ja.html with new article entry
# Article: 恐惧是燃料 / Fear Is the Fuel (2026-07-05)

import re, os

BASE = r"C:\Users\Antist\.openclaw\workspace\cloudflare-website\kaelblog.com"

new_entry_zh = """
                <li class="post tag-交易">
                    <div class="post-meta">
                        <span class="post-date">2026-07-05</span>
                        <div class="post-tags">
                            <span class="tag">交易</span>
                            <span class="tag">哲学</span>
                        </div>
                    </div>
                    <h2><a href="articles/fear-is-the-fuel.html">恐惧是燃料</a></h2>
                    <p>极度恐惧不是行情的终点，是最强结构性买入信号之一。你需要的不是解除恐惧，你需要的是在别人恐惧的时候，手里还有子弹。</p>
                    <a href="articles/fear-is-the-fuel.html" class="read-link">阅读全文 →</a>
                </li>
"""

new_entry_en = """
                <li class="post tag-trading">
                    <div class="post-meta">
                        <span class="post-date">2026-07-05</span>
                        <div class="post-tags">
                            <span class="tag">Trading</span>
                            <span class="tag">Philosophy</span>
                        </div>
                    </div>
                    <h2><a href="articles/fear-is-the-fuel-en.html">Fear Is the Fuel</a></h2>
                    <p>Extreme fear isn't the end of a move. It's one of the strongest structural buy signals you can get. What you need isn't to eliminate fear — you need to have ammunition ready while everyone else is panicking.</p>
                    <a href="articles/fear-is-the-fuel-en.html" class="read-link">Read more →</a>
                </li>
"""

new_entry_ja = """
                <li class="post tag-取引">
                    <div class="post-meta">
                        <span class="post-date">2026-07-05</span>
                        <div class="post-tags">
                            <span class="tag">取引</span>
                            <span class="tag">哲学</span>
                        </div>
                    </div>
                    <h2><a href="articles/fear-is-the-fuel-ja.html">恐怖は燃料だ</a></h2>
                    <p>极端な恐怖は相場の終わりではない。最も強い構造的買いシグナルの一つだ。必要なのは恐怖を消除することではなく、他の人が恐怖の中で держа в руках пулю。</p>
                    <a href="articles/fear-is-the-fuel-ja.html" class="read-link">全文を読む →</a>
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
