import re
with open(r'C:\Users\Antist\.openclaw\workspace\cloudflare-website\kaelblog.com\articles\kael-blog-launch.html','r',encoding='utf-8') as f:
    c = f.read()
print('File size:', len(c))
# Find <article> tag
idx = c.find('<article>')
print('<article> index:', idx)
if idx > 0:
    print('First 300 chars after <article>:', repr(c[idx:idx+300]))
# Find </article>
idx2 = c.find('</article>')
print('</article> index:', idx2)
if idx2 > 0:
    print('Last 100 chars before </article>:', repr(c[idx2-100:idx2+10]))
# Check for section or main
print('Has <main>:', '<main>' in c)
print('Has <section: comments>:', '<section' in c and 'comments' in c)