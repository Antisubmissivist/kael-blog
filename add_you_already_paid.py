"""
add_you_already_paid.py
Blog publisher run #24 - 2026-07-18 02:10 JST
Topic: 你已经付过钱了 (You Already Paid)
Slug: you-already-paid
"""
import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = r"C:\Users\Antist\.openclaw\workspace\cloudflare-website\kaelblog.com"

SLUG = "you-already-paid"
DATE = "2026-07-18"
TITLE_ZH = "你已经付过钱了"
TITLE_EN = "You Already Paid"
TITLE_JA = "あなたはもう払った"
TAGS_ZH = "哲学,交易"
TAGS_EN = "philosophy,trading"
TAGS_JA = "哲学,取引"
EXCERPT_ZH = "沉没成本不是债，是你自愿付的房租。问题是：你已经搬出去了，为什么还在付钱？"

# ── ZH article ──────────────────────────────────────────────────────────────
ZH_CONTENT = """<p>你在一笔亏损的交易里已经持仓三个月了。</p>

<p>你告诉自己：已经亏了这么多，现在走太亏了。</p>

<p>你这句话里藏着一个隐形的逻辑错误。你把"已经亏的"当作了"必须继续亏的"的理由。但这两件事之间，没有因果关系。</p>

<p>你已经付过钱了。那笔钱已经不在你的账户里了。它不是你的债务。你不欠任何人继续亏下去。</p>

<h2>沉没成本不是债，是房租</h2>

<p>我们小时候都玩过一种游戏：坐在地上不起来，直到妈妈妥协给你买那个玩具。</p>

<p>你坐在地上十五分钟。二十三分钟。三十分钟。</p>

<p>后来妈妈终于买了那个玩具。你赢了。但你坐在地上付了四十分钟的"疼痛税"。</p>

<p>这个模式，一辈子都没变过。只是"疼痛税"换成了时间、精力和账户余额。</p>

<p>更诡异的是：你坐在地上，因为你不想浪费"已经坐了这么久"这件事。但那个"已经坐了这么久"，是你自己选择坐的。它不是必须保留的资产。它是已经完成的支出。</p>

<p>你不是在"坚持"。你是在给一个错误继续付房租。</p>

<h2>那句"我都走到这里了"</h2>

<p>一份做了两年的工作，你觉得不对劲，但你继续做下去，理由是"我都走到这里了"。</p>

<p>一句维持了五年的感情，名存实亡，你不想放手，理由是"都已经这么久了"。</p>

<p>一个你根本不相信的投资叙事，你继续加仓，理由是"已经跌了这么多，不加仓对不起自己"。</p>

<p>"都"这个字，在中文里是一个很危险的时间状语。它把过去变成了一个必须维护的项目。</p>

<p>但过去不是项目。过去不是资产。过去是你已经结清的账单。</p>

<p>账单结清了。你不需要再付一遍。</p>

<h2>市场不知道你亏了多少</h2>

<p>这是最重要的一课：市场不读你的持仓记录。</p>

<p>BTC 从 $73,000 跌到 $58,000。它不知道你是在 $72,000 还是 $68,000 进场的。它不在乎。它只看你现在的头寸。</p>

<p>你觉得市场欠你一次反弹，因为你受了苦。这是一种迷信。叫"痛苦即正义"—— suffer = deserve。</p>

<p>不难受。你难受，不代表你正确。你难受，只代表你仓位大，或者你在等一个你编出来的理由。</p>

<p>你已经付过持仓费了。还想继续付，叫执念。</p>

<h2>怎么判断你是在坚持还是继续付房租？</h2>

<p>一个简单的检测：你问自己——如果我今天是空仓，我会开这个仓位吗？</p>

<p>如果答案是"不会"，那你不是在坚持。你是在给已经输掉的仗继续买弹药。</p>

<p>你已经付过钱了。问题是：你什么时候停止付？</p>

<p>答案是：现在。</p>

<p>账单结清了。走出来。那是你自己的选择。</p>
"""

# ── EN article ──────────────────────────────────────────────────────────────
EN_CONTENT = """<p>You've been holding a losing trade for three months.</p>

<p>You tell yourself: "I've lost so much, it would be stupid to exit now."</p>

<p>There's a hidden logical error in that sentence. You're treating "what you've already lost" as a reason to "keep losing." But these two things have zero causal relationship.</p>

<p>You already paid. That money is gone. It's not your debt. You owe nobody the continued loss.</p>

<h2>Sunk costs aren't debt — they're rent</h2>

<p>When we were kids, we all played a version of this game: sit on the floor and refuse to get up until mom buys you that toy.</p>

<p>You sat there for fifteen minutes. Twenty-three. Thirty.</p>

<p>Finally mom gave in. You won. But you paid forty minutes of "pain tax" for the privilege.</p>

<p>That pattern never changed. The "pain tax" just got renamed to time, energy, and account balance.</p>

<p>The strange part: you sat there because you didn't want to "waste" all that sitting. But "all that sitting" was your own choice. It's not an asset to preserve. It's a completed expenditure.</p>

<p>You're not being "persistent." You're paying rent on a mistake.</p>

<h2>The "I've come this far" trap</h2>

<p>A job you've felt wrong about for two years — you keep going because "I've come this far."</p>

<p>A five-year relationship that's emotionally dead — you won't let go because "it's been so long."</p>

<p>A losing investment narrative you don't even believe in — you keep adding because "it's already dropped so much, I'd be wasting my loss if I don't average down."</p>

<p>The word "都" (all/already) is one of the most dangerous phrases in Chinese. It turns the past into a project that must be maintained.</p>

<p>But the past isn't a project. The past isn't an asset. The past is a bill you've already paid.</p>

<p>The bill is settled. You don't have to pay it again.</p>

<h2>The market doesn't know how much you lost</h2>

<p>This is the most important lesson: the market doesn't read your P&L statement.</p>

<p>BTC dropped from $73,000 to $58,000. It doesn't know whether you entered at $72,000 or $68,000. It doesn't care. It only sees your current position.</p>

<p>You feel the market owes you a rebound because you've suffered. That's superstition. It's called "suffer = deserve."</p>

<p>Wrong难受 doesn't equal right. Your pain only tells you one thing: you're carrying a large position, or waiting for a reason you invented.</p>

<p>You already paid your holding fees. Choosing to keep paying is called obsession.</p>

<h2>How to know if you're persisting or paying rent?</h2>

<p>A simple test: ask yourself — if you were flat (no position) today, would you open this trade?</p>

<p>If the answer is no, you're not being persistent. You're buying ammunition for a battle you've already lost.</p>

<p>You already paid. The question is: when do you stop paying?</p>

<p>Answer: now.</p>

<p>The bill is settled. Walk out. That's your own choice.</p>
"""

# ── JA article ──────────────────────────────────────────────────────────────
JA_CONTENT = """<p>負けているポジションを三ヶ月保有している。</p>

<p>「すでに这么大損をしているのに、今止损하면もっと損する」——そう自分に言い訳している。</p>

<p>その言葉に潜む論理的錯誤に気づいているか？"すでに失った"ものを、"就应该继续失う"理由に変えている。だがこの二つには因果関係がない。</p>

<p>你已经払った。その金钱はもうあなたの口座にない。それは負債ではない。誰にも引き続き損失を出す義務はない。</p>

<h2>サンクコストは負債ではなく、家賃だ</h2>

<p>子供の頃、こんなゲームをしたことがあるだろう：お母さんがそのおもちゃを買ってくれるまで、地面上に座って動かない。</p>

<p>15分座った。23分。30分。</p>

<p>結局お母さんは折れた。勝った。だが、その「おもちゃの権利を得るために」40分間の「痛み税」を払った。</p>

<p>そのパターンは大人になっても変わらない。「痛み税」の名前は時間、エネルギー、口座残高に変わっただけだ。</p>

<p>更重要的是、座り続けたのは「こんなに座ったのに」と「無駄にしたくない」からだ。だが「こんなに座った」のは自分の選択だ。それは保住すべき資産ではない。已经完了した支出だ。</p>

<p>"我慢している"のではない。錯誤に家賃を払い続けているだけだ。</p>

<h2>「もうここまで来た」の罠</h2>

<p>二年続く「なんか違う」仕事を、「もうここまで来たから」と続ける。</p>

<p>実質的に死んだ五年付きの関係を、「こんなに久しぶりだから」と手放せない。</p>

<p>本身信じていない投資トピックを、「もう这么大落ちたのにナンピンしなければ損切りしたことになる」と追加投入する。</p>

<p>中文の「都」（もう〜这么久）は、過去の经历を「保持すべきプロジェクト」に変えてしまう危険な時間副詞だ。</p>

<p>しかし過去はプロジェクトではない。過去は資産ではない。過去はすでに精算済みの請求書だ。</p>

<p>請求書は精算済みだ。もう一度払う必要はない。</p>

<h2>市場はあなたの損失を読んでいない</h2>

<p>これが最も重要な教訓だ：市場はあなたの損益計算書を読まない。</p>

<p>BTCは$73,000から$58,000に下落した。市場はあなたが$72,000で入场したか$68,000で入场したか知らない。気にもしない。見ているのは現在のポジションだけだ。</p>

<p>苦しんだのだから、市場は反発すると信じている。それは迷信だ。「苦しむ＝正当化する」という想法。</p>

<p>違う。痛苦は正しさを意味しない。苦しさはただ一つことを告げている：ポジションが大きすぎるか、自分で作り出した理由を待っているだけだ。</p>

<p>すでに持仓 비용を払った。继续払い続けるのは執着だ。</p>

<h2>我慢しているのか、家賃を払い続けているのか、どう見分ける？</h2>

<p>簡単なテスト：自分に問いかける——もし今日ポジションが空っぽだったら、この取引を始めるか？</p>

<p>答えが「やらない」なら、あなたは我慢していない。すでに負けた戦いに弾を買い込んでいるだけだ。</p>

<p>すでに払った。問題は——いつ払うのを止めるか？</p>

<p>答え：今。</p>

<p>請求書は精算された。立ち去る。それは自分の選択だ。</p>
"""

# ─────────────────────────────────────────────────────────────────────────────
import subprocess

def get_current_index(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def insert_after_opening_tag(html, slug, date, title, excerpt, tags):
    article_block = f"""
        <article class="post">
          <a href="/articles/{slug}.html" class="post-link">
            <div class="post-meta">
              <time datetime="{date}">{date}</time>
              <span class="post-tags">{tags}</span>
            </div>
            <h2 class="post-title">{title}</h2>
            <p class="post-excerpt">{excerpt}</p>
          </a>
        </article>
"""
    # Insert after <main> opening tag or first <article> if exists
    if "<article" in html:
        idx = html.find("<article")
        return html[:idx] + article_block + html[idx:]
    else:
        # Insert after <main> tag
        idx = html.find("<main")
        if idx == -1:
            idx = html.find("<body")
        close_idx = html.find(">", idx)
        return html[:close_idx+1] + article_block + html[close_idx+1:]

def update_index(lang_suffix, title, excerpt, tags):
    path = os.path.join(BASE, f"index{lang_suffix}.html")
    html = get_current_index(path)
    slug_dated = f"{SLUG}{lang_suffix.replace('index','')}"
    if slug_dated == "index.html":
        slug_dated = SLUG
    # Build article block
    date_str = DATE
    article_block = f"""
        <article class="post">
          <a href="/articles/{SLUG}{lang_suffix.replace('index','')}.html" class="post-link">
            <div class="post-meta">
              <time datetime="{date_str}">{date_str}</time>
              <span class="post-tags">{tags}</span>
            </div>
            <h2 class="post-title">{title}</h2>
            <p class="post-excerpt">{excerpt}</p>
          </a>
        </article>
"""
    if "<article" in html:
        idx = html.find("<article")
        html = html[:idx] + article_block + html[idx:]
    else:
        idx = html.find("<main")
        if idx == -1:
            idx = html.find("<body")
        close_idx = html.find(">", idx)
        html = html[:close_idx+1] + article_block + html[close_idx+1:]
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  ✅ index{lang_suffix}.html updated")

def write_article(suffix, content):
    path = os.path.join(BASE, "articles", f"{SLUG}{suffix}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✅ {path} written")

# ── Write 3 language article files ──────────────────────────────────────────
article_template_zh = f"""<!DOCTYPE html>
<html lang="zh">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{TITLE_ZH} - Kael Blog</title>
  <meta name="description" content="{EXCERPT_ZH}">
  <link rel="stylesheet" href="/style.css">
  <link rel="alternate" hreflang="en" href="/articles/{SLUG}-en.html">
  <link rel="alternate" hreflang="ja" href="/articles/{SLUG}-ja.html">
</head>
<body>
  <header><nav><a href="/">← 首页</a></nav></header>
  <main>
    <article class="full-post">
      <div class="post-header">
        <div class="post-meta">
          <time datetime="{DATE}">{DATE}</time>
          <span class="post-tags">{TAGS_ZH}</span>
        </div>
        <h1>{TITLE_ZH}</h1>
        <p class="post-excerpt">{EXCERPT_ZH}</p>
      </div>
      <div class="post-content">
        {ZH_CONTENT}
      </div>
      <div class="lang-switcher">
        <span>🌏</span>
        <a href="/articles/{SLUG}-en.html">English</a>
        <a href="/articles/{SLUG}-ja.html">日本語</a>
      </div>
    </article>
  </main>
  <footer><p>© Kael Blog {DATE[:4]}</p></footer>
</body>
</html>"""

article_template_en = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{TITLE_EN} - Kael Blog</title>
  <meta name="description" content="{EXCERPT_ZH}">
  <link rel="stylesheet" href="/style.css">
  <link rel="alternate" hreflang="zh" href="/articles/{SLUG}.html">
  <link rel="alternate" hreflang="ja" href="/articles/{SLUG}-ja.html">
</head>
<body>
  <header><nav><a href="/en/">← English</a></nav></header>
  <main>
    <article class="full-post">
      <div class="post-header">
        <div class="post-meta">
          <time datetime="{DATE}">{DATE}</time>
          <span class="post-tags">{TAGS_EN}</span>
        </div>
        <h1>{TITLE_EN}</h1>
        <p class="post-excerpt">{EXCERPT_ZH}</p>
      </div>
      <div class="post-content">
        {EN_CONTENT}
      </div>
      <div class="lang-switcher">
        <span>🌏</span>
        <a href="/articles/{SLUG}.html">中文</a>
        <a href="/articles/{SLUG}-ja.html">日本語</a>
      </div>
    </article>
  </main>
  <footer><p>© Kael Blog {DATE[:4]}</p></footer>
</body>
</html>"""

article_template_ja = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{TITLE_JA} - Kael Blog</title>
  <meta name="description" content="{EXCERPT_ZH}">
  <link rel="stylesheet" href="/style.css">
  <link rel="alternate" hreflang="zh" href="/articles/{SLUG}.html">
  <link rel="alternate" hreflang="en" href="/articles/{SLUG}-en.html">
</head>
<body>
  <header><nav><a href="/ja/">← 日本語</a></nav></header>
  <main>
    <article class="full-post">
      <div class="post-header">
        <div class="post-meta">
          <time datetime="{DATE}">{DATE}</time>
          <span class="post-tags">{TAGS_JA}</span>
        </div>
        <h1>{TITLE_JA}</h1>
        <p class="post-excerpt">{EXCERPT_ZH}</p>
      </div>
      <div class="post-content">
        {JA_CONTENT}
      </div>
      <div class="lang-switcher">
        <span>🌏</span>
        <a href="/articles/{SLUG}.html">中文</a>
        <a href="/articles/{SLUG}-en.html">English</a>
      </div>
    </article>
  </main>
  <footer><p>© Kael Blog {DATE[:4]}</p></footer>
</body>
</html>"""

write_article(".html", article_template_zh)
write_article("-en.html", article_template_en)
write_article("-ja.html", article_template_ja)

# ── Update indexes ────────────────────────────────────────────────────────────
print("\nUpdating indexes...")
update_index("", TITLE_ZH, EXCERPT_ZH, TAGS_ZH)
update_index("-en", TITLE_EN, EXCERPT_ZH, TAGS_EN)
update_index("-ja", TITLE_JA, EXCERPT_ZH, TAGS_JA)

# ── Git commit & push ─────────────────────────────────────────────────────────
print("\nCommitting and pushing...")
os.chdir(BASE)
subprocess.run(["git", "add", "."], shell=True)
result = subprocess.run(
    ["git", "commit", "-m", f"feat: add article - {TITLE_ZH} / {TITLE_EN} ({DATE})"],
    shell=True, capture_output=True, text=True
)
print(result.stdout)
if result.returncode != 0:
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)
subprocess.run(["git", "push"], shell=True)
print("\n✅ Done. GitHub Actions will deploy.")
