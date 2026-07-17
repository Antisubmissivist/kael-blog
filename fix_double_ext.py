import sys
sys.stdout.reconfigure(encoding='utf-8')
content = open('add_you_already_paid.py', 'r', encoding='utf-8').read()
fixed = content.replace(
    'path = os.path.join(BASE, "articles", f"{SLUG}{suffix}.html")',
    'path = os.path.join(BASE, "articles", f"{SLUG}{suffix}")'
)
open('add_you_already_paid.py', 'w', encoding='utf-8').write(fixed)
print('Fixed write_article path - now re-run add_you_already_paid.py')
