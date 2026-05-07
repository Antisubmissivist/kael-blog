import re
with open(r'C:\Users\Antist\.openclaw\workspace\cloudflare-website\kaelblog.com\articles\kael-blog-launch.html','r',encoding='utf-8') as f:
    c = f.read()
m = re.search(r'<div class="article-body">(.*)', c, re.DOTALL)
if m:
    body = m.group(1)
    end = body.find('</div>')
    print('Body length:', end)
    print('Body snippet:', repr(body[:300]))
else:
    print('No article-body div found')
    m2 = re.search(r'<main>(.*?)<section', c, re.DOTALL)
    if m2:
        print('Main content snippet:', repr(m2.group(1)[:300]))