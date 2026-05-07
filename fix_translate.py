"""
Fix Google Translate button onclick handlers to use translatePage() with async widget wait.
Works on all HTML files in articles/ and index.html.
"""
import os
import re

BASE = r"C:\Users\Antist\.openclaw\workspace\cloudflare-website\kaelblog.com"

OLD_ONCLICK_RE = re.compile(
    r'<button data-lang="(zh|en|ja)" onclick="\(function\(\)\{var s=document\.querySelector\(\'\.goog-te-combo\'\);if\(s\)\{s\.value=\'(zh-CN|en|ja)\';var e=new Event\(\'change\',\{bubbles:true\}\);s\.dispatchEvent\(e\)\}\}\)\(\)"'
)

NEW_ONCLICK = r'<button data-lang="\1" onclick="translatePage(\'\1\')"'

TRANSLATE_FUNC = """
function translatePage(lang) {
    var gtcFrame = document.querySelector('.goog-te-banner-frame');
    if (gtcFrame) { gtcFrame.style.display = 'none'; }

    function doTranslate() {
        if (lang === 'zh') {
            if (typeof google !== 'undefined' && google.translate) {
                var select = document.querySelector('.goog-te-combo');
                if (select) { select.value = ''; select.dispatchEvent(new Event('change')); }
            }
            applyLang(lang);
            return;
        }

        var langMap = { en: 'en', ja: 'ja' };
        var gLang = langMap[lang] || lang;

        if (typeof google !== 'undefined' && google.translate) {
            var sel = document.querySelector('.goog-te-combo');
            if (sel) { sel.value = gLang; sel.dispatchEvent(new Event('change')); }
        }
        applyLang(lang);
    }

    if (document.querySelector('.goog-te-combo')) {
        doTranslate();
    } else {
        var tryCount = 0;
        var wait = setInterval(function() {
            tryCount++;
            if (document.querySelector('.goog-te-combo')) {
                clearInterval(wait);
                doTranslate();
            } else if (tryCount >= 20) {
                clearInterval(wait);
                applyLang(lang);
            }
        }, 100);
    }
}"""

OLD_FUNC_RE = re.compile(
    r"function translatePage\(lang\)\s*\{.*?applyLang\(lang\);\s*\}",
    re.DOTALL
)

def fix_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = False

    # 1. Fix old inline onclick handlers
    if OLD_ONCLICK_RE.search(content):
        content = OLD_ONCLICK_RE.sub(NEW_ONCLICK, content)
        changed = True

    # 2. Replace translatePage function body with new async-aware version
    if 'function translatePage(lang)' in content:
        # Find the function and replace it block by block
        # We'll do a simpler approach: find start and end
        start = content.find("function translatePage(lang)")
        if start != -1:
            # Find the opening brace
            brace_start = content.find('{', start)
            if brace_start != -1:
                # Find matching closing brace using a simple counter
                depth = 1
                pos = brace_start + 1
                while pos < len(content) and depth > 0:
                    if content[pos] == '{':
                        depth += 1
                    elif content[pos] == '}':
                        depth -= 1
                    pos += 1
                if depth == 0:
                    old_func = content[start:pos]
                    content = content[:start] + TRANSLATE_FUNC.strip() + content[pos:]
                    changed = True

    if changed:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed: {path}")

def main():
    # Fix index.html
    index = os.path.join(BASE, 'index.html')
    if os.path.exists(index):
        fix_file(index)

    # Fix all articles
    articles_dir = os.path.join(BASE, 'articles')
    if os.path.exists(articles_dir):
        for fname in os.listdir(articles_dir):
            if fname.endswith('.html'):
                fix_file(os.path.join(articles_dir, fname))

if __name__ == '__main__':
    main()
