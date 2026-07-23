#!/usr/bin/env python3
"""Add article 'evidence-is-manufactured' to all three index files."""
import re

def make_entry_zh():
    return '''        <article class="post">
          <a href="/articles/evidence-is-manufactured.html" class="post-link">
            <div class="post-meta">
              <time datetime="2026-07-24">2026-07-24</time>
              <span class="post-tags">哲学,交易</span>
            </div>
            <h2 class="post-title">证据是你自己制造的</h2>
            <p class="post-excerpt">市场不给你证据，证据是你自己制造的。你相信某件事是真的，这不是证据；你做了让它变成真的，这才是证据。</p>
          </a>
        </article>
'''

def make_entry_en():
    return '''        <article class="post">
          <a href="/articles/evidence-is-manufactured-en.html" class="post-link">
            <div class="post-meta">
              <time datetime="2026-07-24">2026-07-24</time>
              <span class="post-tags">Philosophy, Trading</span>
            </div>
            <h2 class="post-title">Evidence Is Manufactured</h2>
            <p class="post-excerpt">The market doesn't give you evidence — you manufacture it. Believing something is true isn't proof; doing something that makes it true is.</p>
          </a>
        </article>
'''

def make_entry_ja():
    return '''        <article class="post">
          <a href="/articles/evidence-is-manufactured-ja.html" class="post-link">
            <div class="post-meta">
              <time datetime="2026-07-24">2026-07-24</time>
              <span class="post-tags">哲学、交易</span>
            </div>
            <h2 class="post-title">証拠は自分たちが作るもの</h2>
            <p class="post-excerpt">市場は証拠をくれない。証拠は自分たちが作るものだ。何かを信じていることは証拠ではない。それを本当のものにする行動が証拠だ。</p>
          </a>
        </article>
'''

def insert_before_marker(content, entry, marker):
    idx = content.find(marker)
    if idx == -1:
        print(f"WARNING: marker not found")
        return content
    return content[:idx] + entry + content[idx:]

base = "C:/Users/Antist/.openclaw/workspace/cloudflare-website/kaelblog.com"

configs = [
    ("index.html", make_entry_zh(), "the-market-has-no-memory.html"),
    ("index-en.html", make_entry_en(), "the-market-has-no-memory-en.html"),
    ("index-ja.html", make_entry_ja(), "the-market-has-no-memory-ja.html"),
]

for fname, entry, url in configs:
    path = f"{base}/{fname}"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    marker = f'<article class="post">\n          <a href="/articles/{url}"'
    new_content = insert_before_marker(content, entry, marker)
    if new_content == content:
        print(f"WARNING: No insertion made in {fname}")
    else:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated: {fname}")

print("Done.")
