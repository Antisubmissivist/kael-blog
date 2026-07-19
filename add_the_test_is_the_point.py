"""
add_the_test_is_the_point.py
Blog publisher run #26 - 2026-07-20 02:10 JST
Topic: 考试就是终点 (The Test Is the Point)
Slug: the-test-is-the-point
"""
import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = r"C:\Users\Antist\.openclaw\workspace\cloudflare-website\kaelblog.com"

SLUG = "the-test-is-the-point"
DATE = "2026-07-20"
TITLE_ZH = "考试就是终点"
TITLE_EN = "The Test Is the Point"
TITLE_JA = "試験が终点だ"
TAGS_ZH = "哲学,交易"
TAGS_EN = "philosophy,trading"
TAGS_JA = "哲学,取引"
EXCERPT_ZH = "我们以为考试是通往自由的障碍，但考试本身就是自由实现的地方。你不需要跨越考试去活——你通过考试来活。"

# ── ZH article ──────────────────────────────────────────────────────────────
ZH_CONTENT = """<p>一个学生准备考试很多年。</p>

<p>他告诉自己：等考完试，我就自由了。</p>

<p>他考完了。他没有自由。</p>

<p>他去找工作，HR说：我们需要一个测试你能力的环节。他参加了面试，面试里有一道他没有准备过的情景题。他卡住了。他突然意识到：这道题，就是他准备考试的那几年里一直在逃避的东西。</p>

<p>考试不是通往自由的障碍。考试就是自由实现的地方。</p>

<h2>我们把测试当成了障碍</h2>

<p>这个模式，从学校开始，贯穿了一辈子。</p>

<p>小学毕业考试 → 初中毕业考试 → 高考 → 四六级 → 考研 → 找工作面试 → 试用期考核 → 年度KPI → 晋升答辩 → 创业融资路演 → 用户增长数据验证……</p>

<p>每一个"测试"之间，间隔越来越短，密度越来越高。但你的认知框架没有变：你还是在把测试理解为"通过之后才能做自己想做的事"的门槛。</p>

<p>这个框架，从根本上就是错的。</p>

<p>你不需要跨越考试去活。你通过考试来活。</p>

<h2>考试的本质是证明，不是门槛</h2>

<p>考试不是在问你"准备好了吗"。考试本身，就是那个"准备好了"的证明。</p>

<p>一个人跟你说"我爱你"——这不是证明。这是承诺。</p>

<p>但在你生病的时候，他连夜开车三百公里送你去医院——这是考试，也是证明。那个行为，就是爱的本身，不是爱的前提。</p>

<p>你所有的"资格"和"能力"，只有在被测试的瞬间才真实存在。在那之前，它们只是你的想象。</p>

<p>你说你会编程，你写过多少行代码？你的代码解决了什么问题？你在有压力的时候还能不能保持逻辑清晰？这些问题，只有考试能回答。</p>

<h2>持有仓位不是策略，策略只有在止损的时候才存在</h2>

<p>交易是这个逻辑最纯粹的地方。</p>

<p>你有一个交易策略，你在等待市场验证它。但"等待"本身不是策略。</p>

<p>你的策略只有在以下时刻才真实存在：止损点被触发的那一刻，你执行了吗？行情反转的时候，你有没有坚持原来的逻辑？账户回撤15%的时候，你的心态是什么？</p>

<p>没有考试的策略，不是策略，是愿望清单。</p>

<p>你的止损单被触发了，你在那0.3秒内做出的决定——那个决定，才是你的策略。不是你周五晚上喝着酒画的那张技术分析图。</p>

<h2>准备和实现，是同一件事</h2>

<p>这是最深的一层。</p>

<p>我们以为"准备"是在考试之前，"实现"是在考试之后。</p>

<p>但真正的模式不是这样的。真正的模式是：准备，只有在被测试的时候，才知道自己到底准备了什么。</p>

<p>你以为自己准备的是"技术分析"。但市场用一次瀑布式下跌来考你，你发现自己真正准备的是"如何在暴跌中保持镇定"——这个能力你根本没有。</p>

<p>你以为自己准备的是"一段关系"。但对方用一次激烈的争吵来考你，你发现自己的"准备"只是"如何让对方不生气"，而不是"如何在冲突中保持真实"。</p>

<p>准备，只有通过考试才能发现自己准备错了。</p>

<h2>那考试是不是永远都逃不掉？</h2>

<p>不是。</p>

<p>考试不是永远逃不掉，而是你不需要等考试结束了才觉得自由。</p>

<p>你在考试的过程中，就已经活出来了。</p>

<p>你今天早上的冥想，是对你自己的一次考试。你今天跟同事的那场对话，是对你沟通能力的一次考试。你今天亏损了$200——那是你交易策略的一次考试。</p>

<p>你一直在考试。你从来没有不在考试中。</p>

<p>那个"考完就自由了"的感觉，不是真实的。它是一种幻觉——以为生命有一条线，线这边是准备，线那边是实现。</p>

<p>没有这条线。你一直在这边。你也一直在那头。</p>

<p>考试不是障碍。考试就是终点。</p>
"""

# ── EN article ──────────────────────────────────────────────────────────────
EN_CONTENT = """<p>A student prepared for an exam for years.</p>

<p>He told himself: once I finish this exam, I'll be free.</p>

<p>He finished it. He wasn't free.</p>

<p>He went job hunting. The HR person said: we need a test to assess your abilities. He sat through the interview, and there was a scenario question he hadn't prepared for. He froze. In that moment, he realized: this question was exactly what he'd been avoiding during all those years of exam prep.</p>

<p>The test isn't an obstacle blocking your freedom. The test is where freedom is actualized.</p>

<h2>We treat tests as obstacles</h2>

<p>This pattern starts in school and runs through your entire life.</p>

<p>Primary school graduation exam → junior high graduation exam → college entrance exam → CET-4/6 → graduate school entrance exam → job interview → trial period review → annual KPI → promotion defense → startup investor pitch → user growth data validation…</p>

<p>Each "test" comes in shorter intervals, with higher density. But your mental model never changed: you still see tests as thresholds you must pass before you can do what you actually want.</p>

<p>This framework is fundamentally wrong.</p>

<p>You don't cross a test to live. You live through tests.</p>

<h2>The test's essence is proof, not threshold</h2>

<p>A test isn't asking "are you ready?" The test itself is the proof of readiness.</p>

<p>When someone says "I love you" — that's not proof. That's a promise.</p>

<p>But when you're sick and they drive three hundred kilometers overnight to take you to the hospital — that's a test and proof. That action is love itself, not a prerequisite for love.</p>

<p>All your "qualifications" and "abilities" only exist in the moment they're tested. Before that, they're just your imagination.</p>

<p>You say you can code — how many lines have you written? What problems did your code solve? Can you maintain clear logic under pressure? These questions can only be answered by tests.</p>

<h2>Holding a position isn't a strategy — strategy only exists at the stop loss</h2>

<p>Trading is where this logic appears in its purest form.</p>

<p>You have a trading strategy. You're waiting for the market to validate it. But "waiting" itself isn't a strategy.</p>

<p>Your strategy only exists in these moments: when your stop loss is triggered, did you execute? When the trend reversed, did you stick to your original thesis? When your account drew down 15%, what was your mental state?</p>

<p>A strategy without a test isn't a strategy — it's a wish list.</p>

<p>When your stop loss triggered, the decision you made in those 0.3 seconds — that's your strategy. Not the technical analysis chart you drew while drinking on a Friday night.</p>

<h2>Preparation and actualization are the same thing</h2>

<p>This is the deepest layer.</p>

<p>We think "preparation" happens before the test, and "actualization" happens after.</p>

<p>But that's not how it actually works. The real pattern is: you only discover what you actually prepared for when you're being tested.</p>

<p>You thought you were preparing "technical analysis." But the market tested you with a waterfall drop, and you realized your real preparation was "how to stay calm during a crash" — a capability you didn't actually have.</p>

<p>You thought you were preparing "for a relationship." But your partner tested you with a heated argument, and you discovered your "preparation" was really just "how to keep them from getting angry," not "how to stay authentic in conflict."</p>

<p>Preparation only discovers it's been wrong through tests.</p>

<h2>Does that mean tests never end?</h2>

<p>No.</p>

<p>Not that tests never end — but that you don't need to wait for the test to end to feel free.</p>

<p>You're already living it, in the process of being tested.</p>

<p>This morning's meditation was a test you gave yourself. Today's conversation with your colleague was a test of your communication ability. Today you lost $200 — that was a test of your trading strategy.</p>

<p>You're always being tested. You've never been outside of a test.</p>

<p>That feeling of "I'll be free after the exam" — it isn't real. It's an illusion: the belief that life has a line, with preparation on this side and actualization on the other.</p>

<p>There's no line. You're always on this side. And you've always been on the other.</p>

<p>The test isn't an obstacle. The test is the point.</p>
"""

# ── JA article ──────────────────────────────────────────────────────────────
JA_CONTENT = """<p>ある学生が何年も試験の準備をしていた。</p>

<p>彼は自分に言い聞かせた：試験が終われば、自由になれる。</p>

<p>試験終わった。自由になれなかった。</p>

<p>就職活動を始めた。人事部は言った：あなたの能力を試す試験が必要です。彼は面接に臨み、準備していないシチュエーション問題が出た。彼凍りついた。その瞬間気づいた：この問題が、彼が試験準備的日子里ずっと避けていたものだった。</p>

<p>試験は自由への障害ではない。試験が自由を実現する場所だ。</p>

<h2>我々は試験を障害だと見なしている</h2>

<p>このパターンは学校から始まり、人生ずっと続く。</p>

<p>小学校卒業試験→中学校卒業試験→大学入試→CET-4/6→大学院入試→就職面接→試用期間考核→年間KPI→昇進答弁→スタートアップ投資家向けピッチ→ユーザー成長データ検証……</p>

<p>各「試験」の間隔は越来越短、密度は越来越高くなる。だがあなたの認知フレームは変わらない：依然として試験を「自己想做的事をする前に通過しなければならない关卡」だと見なしている。</p>

<p>このフレームは根本的に間違っている。</p>

<p>試験を越えて生きる必要はない。試験を通じて生きるのだ。</p>

<h2>試験の本質は証明であり、関門ではない</h2>

<p>試験は「準備できましたか」と聞いているのではない。試験自体が、「準備完了」の証明だ。</p>

<p>谁かが「愛している」と言う——これは証明ではない。約束だ。</p>

<p>だが、あなたが病気の时、谁かが夜通しで300キロ走り続けて病院に連れて行ってくれる——これは試験であり証明だ。その行動自体が愛そのものであり、愛の前払いではない。</p>

<p>すべての「資格」と「能力」は、試験中被测试瞬间才真实存在。それまでは、ただの想像だ。</p>

<p>プログラミングできると主張する——でも何行コード書いたの？あなたのコードは何か問題を解決した？プレッシャーの下で論理的清晰を保てる？这些问题只有考试能回答。</p>

<h2>ポジションを持つことは戦略ではない——戦略は損切り時に初めて存在する</h2>

<p>取引はこの論理が最も純粋に表れる分野だ。</p>

<p>取引戦略がある。市場がそれを検証するのを待っている。だが「待つ」本身不是戦略。</p>

<p>あなたの戦略は以下の瞬間에만真实に存在する：損切りポイントに触れたとき、執行したか？トレンドが反転したとき、元のロジックを守ったか？口座が15%下落したとき、精神状態は？</p>

<p>試験のない戦略は戦略ではない——希望リストだ。</p>

<p>損切りが執行されたとき、その0.3秒の間に下した決定——それがあなたの戦略だ。金曜日の夜、酒を飲みながら描いた技術分析チャートではない。</p>

<h2>準備と実現は同じ事だ</h2>

<p>これが最も深い層だ。</p>

<p>我々は「準備」が試験の前、「実現」が試験の後だと考えている。</p>

<p>しかし 실제パターンは違う。実際の模式は：準備は試験中被测试的时候，才知道自己到底准备了什么。</p>

<p>技術分析を準備していると思っていた。だが市場が暴落で試験してきた。そして気づいた——実際の準備は「暴落時に冷静を保つ方法」——この能力は実際持有していなかった。</p>

<p>関係を準備していると思っていた。だが相手が激しい争吵で試験してきた。そして気づいた——「準備」とは「相手を怒らせない方法」であり、「冲突の中で真实を保てる方法」ではない。</p>

<p>準備は試験を通じて初めて準備不足が发现自己。</p>

<h2>では試験は永远不会结束인가?</h2>

<p>違う。</p>

<p>試験が永远不会结束ということではない——試験が終わるまで待ってから自由を感じる必要はないということだ。</p>

<p>試験を受けている過程で、既に生きています。</p>

<p>今日の朝の瞑想は、あなた自身が自分に課した試験だ。今日同僚とした会話はコミュニケーション能力の試験だ。今日$200損した——それは取引戦略の試験だ。</p>

<p>あなたは常に試験を受けている。試験の外れたことは一度もない。</p>

<p>「試験が終われば自由になれる」という感覚——それは真実ではない。幻想だ——人生には線があり、这边は準備、向こうは実現だと信じる幻觉。</p>

<p>その線は存在しない。あなたは常にこちらにいる。そして常にあちらにもいる。</p>

<p>試験は障碍ではない。試験が终点だ。</p>
"""

# ─────────────────────────────────────────────────────────────────────────────
import subprocess

def get_current_index(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def update_index(lang_suffix, title, excerpt, tags):
    path = os.path.join(BASE, f"index{lang_suffix}.html")
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()
    date_str = DATE
    slug_dated = f"{SLUG}{lang_suffix.replace('index','')}"
    if slug_dated == "index.html":
        slug_dated = SLUG
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
    path = os.path.join(BASE, "articles", f"{SLUG}{suffix}")
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
