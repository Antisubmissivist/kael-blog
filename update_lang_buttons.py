import os
import re

articles_dir = r"C:\Users\Antist\.openclaw\workspace\cloudflare-website\kaelblog.com\articles"

lang_map = {
    "zh": "zh-CN",
    "en": "en",
    "ja": "ja"
}

# Pattern to replace: <button data-lang="LANG" class="active">TEXT</button>
# or: <button data-lang="LANG">TEXT</button>
# with onclick to trigger google translate combo
pattern = r'<button data-lang="(zh|en|ja)"(?: class="active")?>(ZH|EN|JA)</button>'

def replace_button(match):
    lang = match.group(1)
    text = match.group(2)
    gt_value = lang_map[lang]
    onclick = f'onclick="(function(){{var s=document.querySelector(\'.goog-te-combo\');if(s){{s.value=\'{gt_value}\';var e=new Event(\'change\',{{bubbles:true}});s.dispatchEvent(e)}}}})()"' 
    return f'<button data-lang="{lang}" {onclick}>{text}</button>'

for filename in os.listdir(articles_dir):
    if not filename.endswith('.html'):
        continue
    filepath = os.path.join(articles_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = re.sub(pattern, replace_button, content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {filename}")
    else:
        print(f"No change: {filename}")