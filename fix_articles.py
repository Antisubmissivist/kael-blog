import urllib.request
import urllib.error
import json
import re
import os
import time

SLUGS = [
    "agent-invisible-workflow",
    "ambient-presence",
    "breakpoints-are-not-endpoints",
    "failure-as-feedback",
    "guardian-mode-paradox",
    "kael-blog-launch",
    "memory-is-not-a-library",
    "obsidian-second-brain",
    "smallest-unit-of-action",
    "thinking-technology-notes",
    "what-happens-when-ai-agents-debate",
    "when-time-becomes-parameter",
    "why-files-cant-constrain-ai"
]

BASE = r"C:\Users\Antist\.openclaw\workspace\cloudflare-website\kaelblog.com\articles"
API_KEY = "sk-cp-7DTLhuakIKKvo3sd5mVYC3tTKc8WkqV2o-k5-0E1TaCwH4CDZP5paCD4nkvXETkFDxu7_KOlzGFXI117Lj1VkMniKreKikTTyoxxMrBIL2fIbQk0Kx8yv0E"

def extract_article_body(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    m = re.search(r'<article[^>]*>(.*?)</article>', content, re.DOTALL)
    if m:
        return m.group(1).strip()
    return ""

def count_replacement_chars(filepath):
    with open(filepath, 'rb') as f:
        data = f.read()
    return data.count(b'\xef\xbf\xbd')

def translate_via_api(text):
    """Use MiniMax API directly to translate English to Simplified Chinese."""
    url = "https://api.minimax.io/v1/text/chatcompletion_v2"
    
    system_prompt = """You are a professional Chinese translator. Translate the following English article body into Simplified Chinese. 
OUTPUT ONLY the translated Chinese text, no explanations, no quotes, no markdown code fences. Keep all HTML tags as-is.
If there are HTML tags in the text, preserve them exactly as-is."""

    payload = {
        "model": "MiniMax-M2.7",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Translate this to Chinese:\n\n{text}"}
        ],
        "stream": False
    }
    
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        },
        method="POST"
    )
    
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            if "choices" in result and len(result["choices"]) > 0:
                return result["choices"][0]["message"]["content"].strip()
            else:
                print(f"  API response: {result}")
                return None
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        print(f"  HTTP Error {e.code}: {error_body}")
        return None
    except Exception as e:
        print(f"  API exception: {e}")
        return None

def process_article(slug):
    en_path = os.path.join(BASE, f"{slug}-en.html")
    zh_path = os.path.join(BASE, f"{slug}.html")
    
    print(f"\n{'='*60}")
    print(f"Processing: {slug}")
    print(f"{'='*60}")
    
    # Read EN article body
    en_body = extract_article_body(en_path)
    if not en_body:
        print(f"  ERROR: Could not extract article body from {en_path}")
        return False
    
    print(f"  EN body length: {len(en_body)} chars")
    
    # Count before
    before_count = count_replacement_chars(zh_path)
    print(f"  ZH replacement chars BEFORE: {before_count}")
    
    # Translate
    print(f"  Translating via API...")
    zh_body = translate_via_api(en_body)
    
    if zh_body is None:
        print(f"  FAILED to translate {slug}")
        return False
    
    print(f"  Translation length: {len(zh_body)} chars")
    
    # Replace article body in ZH file
    with open(zh_path, 'r', encoding='utf-8', errors='replace') as f:
        zh_content = f.read()
    
    m_zh = re.search(r'<article[^>]*>.*?</article>', zh_content, re.DOTALL)
    if not m_zh:
        print(f"  ERROR: Could not find article tag in {zh_path}")
        return False
    
    # Build new article block - preserve original article tag attributes
    orig_tag_match = re.match(r'<article[^>]*>', m_zh.group(0))
    if orig_tag_match:
        tag = orig_tag_match.group(0)
    else:
        tag = '<article translate="yes">'
    
    new_zh = zh_content.replace(m_zh.group(0), f'{tag}\n{zh_body}\n  </article>')
    
    with open(zh_path, 'w', encoding='utf-8') as f:
        f.write(new_zh)
    
    # Verify
    after_count = count_replacement_chars(zh_path)
    print(f"  ZH replacement chars AFTER: {after_count}")
    
    if after_count == 0:
        print(f"  SUCCESS: {slug} is clean!")
        return True
    else:
        print(f"  WARNING: {slug} still has {after_count} replacement chars")
        return False

def main():
    print("Starting batch translation of 13 articles via MiniMax API...")
    print(f"Base path: {BASE}")
    
    results = {}
    for slug in SLUGS:
        success = process_article(slug)
        results[slug] = success
        # Small delay between articles to avoid rate limiting
        time.sleep(2)
    
    print("\n" + "="*60)
    print("FINAL RESULTS")
    print("="*60)
    
    clean_count = 0
    for slug, success in results.items():
        status = "CLEAN" if success else "HAS ISSUES"
        print(f"  {slug}: {status}")
        if success:
            clean_count += 1
    
    print(f"\nTotal clean (0 replacement chars): {clean_count}/{len(SLUGS)}")

if __name__ == "__main__":
    main()