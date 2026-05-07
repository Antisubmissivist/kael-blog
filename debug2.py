import re
with open(r'C:\Users\Antist\.openclaw\workspace\cloudflare-website\kaelblog.com\articles\kael-blog-launch.html','r',encoding='utf-8') as f:
    c = f.read()

# Check if article-body div exists and what it contains
idx = c.find('article-body')
print('article-body found at index:', idx)

m = re.search(r'<div class="article-body">(.*?)</div>', c, re.DOTALL)
if m:
    body = m.group(1)
    print('Body found, length:', len(body))
    print('First 150 chars:', repr(body[:150]))
else:
    print('No article-body div match')
    # Check what's around main
    m2 = re.search(r'<main>(.*?)<section class="comments">', c, re.DOTALL)
    if m2:
        print('Main->comments block found, length:', len(m2.group(1)))
        print('First 150:', repr(m2.group(1)[:150]))
    else:
        print('Neither pattern found')
        # Show raw structure
        print('Raw excerpt around main:')
        idx2 = c.find('<main>')
        print(repr(c[idx2:idx2+200]))