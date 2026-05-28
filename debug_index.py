import re
with open(r'C:\Users\Antist\.openclaw\workspace\cloudflare-website\kaelblog.com\index.html','r',encoding='utf-8') as f:
    c = f.read()
print('File size:', len(c))
# Check if already has Google Translate
print('Has google translate:', 'googleTranslateElementInit' in c)
# Check for lang-switch div
idx = c.find('lang-switch')
print('lang-switch index:', idx)
if idx > 0:
    print(repr(c[idx-100:idx+200]))