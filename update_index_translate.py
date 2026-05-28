"""
Update index.html — add Google Translate widget + make translatePage global.
"""
import re

INDEX_PATH = r"C:\Users\Antist\.openclaw\workspace\cloudflare-website\kaelblog.com\index.html"

TRANSLATE_SCRIPT = """
        <script type="text/javascript">
        function googleTranslateElementInit() {
            new google.translate.TranslateElement({
                pageLanguage: 'zh-CN',
                includedLanguages: 'en,ja,ko,es,fr,de,zh-CN,zh-TW',
                layout: google.translate.TranslateElement.InlineLayout.SIMPLE,
                autoDisplay: false
            }, 'google_translate_element');
        }
        </script>
        <script type="text/javascript" src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>
"""

with open(INDEX_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Check if already has it
if 'googleTranslateElementInit' in content:
    print('Already has Google Translate, skipping')
    exit()

# Add translate script before </head>
if '</head>' in content:
    content = content.replace('</head>', '    ' + TRANSLATE_SCRIPT.strip() + '\n</head>')

# Add #google_translate_element div after lang-switch in header
# Find the header section and add after the language switch
lang_switch_match = re.search(r'(<div class="lang-switch">.*?</div>\s*)', content, re.DOTALL)
if lang_switch_match:
    insert_pos = lang_switch_match.end()
    content = content[:insert_pos] + '\n            <div id="google_translate_element" style="display:none;"></div>' + content[insert_pos:]

# Now update the i18n JS to make translatePage global and work with Google Translate
# Find and replace the i18n JS block
old_js = """<script>
var i18n = {
    zh: { hero_sub: '\\u4e16\\u754c\\u7684\\u5904\\u7406\\u8005', hero_desc:"""
# Find the full i18n script block in index
js_start = content.find('<script>')
js_end = content.rfind('</script>')
# Find the translatePage function and replace with global version

old_translate_fn = """function applyLang(lang) {
    document.querySelectorAll('[data-i18n]').forEach(function(el) {
        var key = el.getAttribute('data-i18n');
        if (i18n[lang] && i18n[lang][key] !== undefined) el.textContent = i18n[lang][key];
    });
    localStorage.setItem('kaelblog-lang', lang);
}

document.querySelectorAll('.lang-switch button').forEach(function(btn) {
    btn.addEventListener('click', function() {
        document.querySelectorAll('.lang-switch button').forEach(function(b) { b.classList.remove('active'); });
        btn.classList.add('active');
        applyLang(btn.getAttribute('data-lang'));
    });
});

var saved = localStorage.getItem('kaelblog-lang') || 'zh';
document.querySelectorAll('.lang-switch button').forEach(function(btn) {
    btn.classList.toggle('active', btn.getAttribute('data-lang') === saved);
});
if (saved !== 'zh') applyLang(saved);"""

new_translate_fn = """var i18n = {
    zh: { hero_sub: '\\u4e16\\u754c\\u7684\\u5904\\u7406\\u8005', hero_desc:"""

content = content.replace(old_translate_fn, new_translate_fn)

# Actually the JS is complex, let me just append the Google Translate integration
# Instead, let's just add the script and create a separate function
# Find the last </script> and add global translatePage after it

last_script_end = content.rfind('</script>')
if last_script_end > 0:
    # Insert global translatePage after last script
    global_translate = """
<script>
function translatePage(lang) {
    var gtcFrame = document.querySelector('.goog-te-banner-frame');
    if (gtcFrame) { gtcFrame.style.display = 'none'; }
    if (lang === 'zh') {
        if (typeof google !== 'undefined' && google.translate) {
            var select = document.querySelector('.goog-te-combo');
            if (select) { select.value = ''; select.dispatchEvent(new Event('change')); }
        }
        localStorage.setItem('kaelblog-lang', 'zh');
        return;
    }
    var langMap = { en: 'en', ja: 'ja' };
    var gLang = langMap[lang] || lang;
    if (typeof google !== 'undefined' && google.translate) {
        var sel = document.querySelector('.goog-te-combo');
        if (sel) { sel.value = gLang; sel.dispatchEvent(new Event('change')); }
    }
    localStorage.setItem('kaelblog-lang', lang);
}
</script>"""
    content = content[:last_script_end+9] + global_translate + content[last_script_end+9:]

with open(INDEX_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print('Done, file updated with Google Translate')