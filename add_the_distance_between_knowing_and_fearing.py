"""
add_the_distance_between_knowing_and_fearing.py
Blog publisher run #27 - 2026-07-21 02:10 JST
Topic: 知道和害怕之间的距离 (The Distance Between Knowing and Fearing)
Slug: the-distance-between-knowing-and-fearing
"""
import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = r"C:\Users\Antist\.openclaw\workspace\cloudflare-website\kaelblog.com"

SLUG = "the-distance-between-knowing-and-fearing"
DATE = "2026-07-21"
TITLE_ZH = "知道和害怕之间的距离"
TITLE_EN = "The Distance Between Knowing and Fearing"
TITLE_JA = "知ると怖がりの間の距離"
TAGS_ZH = "哲学,交易"
TAGS_EN = 'philosophy,trading'
TAGS_JA = "哲学,取引"
EXCERPT_ZH = '你知道市场会下跌。你害怕市场下跌。这两件事之间，有一条沟，叫做「还没发生」。'

# ── ZH article ──────────────────────────────────────────────────────────────
ZH_CONTENT = '''<p>你知道市场会下跌。</p>

<p>你害怕市场下跌。</p>

<p>这两件事之间，有一条沟，叫做「还没发生」。</p>

<p>你知道的事情，和你害怕的事情，不是一样的东西。</p>

<h2>知道是认知，害怕是情绪</h2>

<p>认知和情绪，走的是不同的神经通路。</p>

<p>你知道熬夜对身体不好——这是认知通路。你还是熬了。你熬完的那一刻，身体没有即刻惩罚你，你感觉到的是舒服和自由——这是情绪通路。</p>

<p>情绪通路更强。因为它有即时反馈。</p>

<p>你知道止损是对的。你下单的时候，你的大脑知道这是正确的操作。但当止损真的被触发的那0.5秒，你的多巴胺断崖，你的肾上腺素飙升——那个感觉，跟「失去」一模一样。</p>

<p>你的大脑不知道这是「策略执行」。你的大脑只知道：疼了，损失了，危险了。</p>

<p>所以你扛单。</p>

<h2>知道和做到之间的距离，叫情绪</h2>

<p>王阳明说「知行合一」。</p>

<p>大多数人的理解是：你知道什么，就该做什么。这是错的。</p>

<p>知行合一的真正意思是：你的「知」必须深入到情绪层面，才可能变成「行」。</p>

<p>你「知道」止损是对的——这只是认知层面的知道。你的身体还不知道。你的神经回路还不知道。所以你做不到。</p>

<p>真正的「知道」，是身体知道。</p>

<p>当止损被触发的那一瞬间，你不假思索地按下了按钮——不是因为你觉得应该，而是因为你「知道」就应该这样做，而且这个「知道」已经变成了你的本能反应。</p>

<p>这种「知道」，需要重复。需要足够多的止损次数，把认知层的「知道」反复地输送到情绪层，最终让情绪层接受它。</p>

<h2>你在害怕的，是「已经发生的」不是「还没发生的」</h2>

<p>有意思的是：你害怕的，其实不是市场下跌本身。</p>

<p>你害怕的是：市场下跌了，我的仓位亏了，我必须承受这个结果。</p>

<p>但市场还没下跌的时候，你的仓位还在，你的账户还是红的，你没有「必须承受」的压力。</p>

<p>那你在害怕什么？</p>

<p>你在害怕的，是那个「下跌已经发生」之后的感觉。那个感觉在你还没有真正亏损的时候，就已经被你的大脑提前预演了。</p>

<p>你在为一种还没有发生的情绪付钱。</p>

<h2>提前预演痛苦，是大脑的自我保护机制</h2>

<p>大脑为什么要提前预演痛苦？</p>

<p>因为它想让你避免痛苦。</p>

<p>但这个机制，在交易里是反的。</p>

<p>你在开仓位之前，大脑就开始预演亏损的痛苦。它让你焦虑，让你犹豫，让你迟迟不敢下单——然后行情走出了你没有仓位的那一段。你错过了。</p>

<p>你的大脑想保护你，结果让你亏了另一种钱：机会成本的钱。</p>

<p>这不是大脑的错。大脑是在原始世界进化的。原始世界里，危险是看得见的、立即的。一只老虎追你，你跑。跑不掉，就完蛋了。</p>

<p>但市场不是老虎。市场是可以反复进出的。错过这一次，还有下一次。</p>

<p>你的大脑没有这个概率模型。</p>

<h2>拉长时间，给情绪层学习的时间</h2>

<p>为什么老交易员能淡定持仓？</p>

<p>不是因为他们不怕。是因为他们经历过太多次「害怕→执行→没事发生」。</p>

<p>这个模式重复足够多之后，情绪层终于接受了：「哦，这种害怕，不代表真的危险。它只是一个信号。信号不等于事实。」</p>

<p>他们不是没有情绪。他们是学会了「延迟判断情绪」。</p>

<p>当害怕升起的时候，他们不给害怕贴标签。他们让害怕在身体里待一会儿，等待认知层来评估：这是真实危险，还是预演痛苦？</p>

<p>如果是真实危险，执行止损。如果是预演痛苦，忽略它。</p>

<p>知道和害怕之间的距离，是可以缩短的。</p>

<p>方法是：反复穿过那条沟。</p>

<p>每穿过一次，知道就深一层。害怕就退一寸。</p>

<p>直到有一天，你发现：自己不再害怕了。不是因为危险消失了——而是因为你的情绪层，终于听懂了你的认知层在说些什么。</p>
'''

# ── EN article ──────────────────────────────────────────────────────────────
EN_CONTENT = '''<p>You know the market will drop.</p>

<p>You fear the market will drop.</p>

<p>Between these two things, there's a ditch. It has a name: "it hasn't happened yet."</p>

<p>What you know and what you fear are not the same thing.</p>

<h2>Knowing is cognitive — fearing is emotional</h2>

<p>Cognition and emotion run on different neural pathways.</p>

<p>You know that staying up late is bad for your health — that's the cognitive pathway. You still do it anyway. After you pull an all-nighter, your body doesn't punish you immediately. What you feel is comfort and freedom — that's the emotional pathway.</p>

<p>The emotional pathway is stronger. Because it has immediate feedback.</p>

<p>You know the stop loss is correct. When you place the order, your brain knows this is the right operation. But in the 0.5 seconds after the stop loss triggers, your dopamine drops off a cliff, your adrenaline surges — that feeling is identical to "loss."</p>

<p>Your brain doesn't know this is "strategy execution." Your brain only knows: it hurts, something was lost, danger.</p>

<p>So you hold the position.</p>

<h2>The distance between knowing and doing is called emotion</h2>

<p>Wang Yangming talked about "unity of knowledge and action."</p>

<p>Most people interpret this as: you should do what you know. This is wrong.</p>

<p>The real meaning is: your "knowing" must penetrate the emotional layer before it can become "action."</p>

<p>You "know" the stop loss is right — that's only cognitive-layer knowing. Your body doesn't know yet. Your neural circuits don't know yet. So you can't do it.</p>

<p>True "knowing" is when the body knows.</p>

<p>When the stop loss triggers, you press the button without thinking — not because you feel you should, but because you "know" you should, and this "knowing" has become your instinctive response.</p>

<p>This kind of "knowing" requires repetition. Enough stop-loss executions to repeatedly deliver cognitive "knowing" into the emotional layer, until the emotional layer finally accepts it.</p>

<h2>What you're actually afraid of already happened</h2>

<p>Here's the interesting part: what you fear isn't the market drop itself.</p>

<p>What you fear is: the market dropped, my position is at a loss, I have to bear this result.</p>

<p>But when the market hasn't dropped yet, your position is still open, your account is still in the green, there's no pressure to "bear" anything.</p>

<p>So what are you afraid of?</p>

<p>You're afraid of the feeling that comes "after the drop has happened." That feeling is being rehearsed in advance by your brain — before it actually occurs.</p>

<p>You're paying for a feeling that hasn't happened yet.</p>

<h2>Advance rehearsal of pain is the brain's self-protection mechanism</h2>

<p>Why does the brain rehearse pain in advance?</p>

<p>Because it wants to protect you from pain.</p>

<p>But this mechanism works in reverse in trading.</p>

<p>Before you even open a position, your brain starts rehearsing the pain of a loss. It makes you anxious, hesitant, keeps you from pulling the trigger — and then the market moves without you. You missed the move you had no position in.</p>

<p>Your brain was trying to protect you, and instead it made you lose a different kind of money: opportunity cost.</p>

<p>This isn't the brain's fault. The brain evolved for the primitive world. In the primitive world, danger is visible and immediate. A tiger is chasing you — you run. Can't outrun it — you're dead.</p>

<p>But the market isn't a tiger. The market can be entered and exited repeatedly. Miss this trade, there's always the next one.</p>

<p>Your brain doesn't have this probability model.</p>

<h2>Stretch time — give the emotional layer time to learn</h2>

<p>Why can veteran traders hold positions calmly?</p>

<p>Not because they're not afraid. Because they've been through "afraid to execute to nothing bad happens" enough times.</p>

<p>After enough repetitions, the emotional layer finally accepts: "Oh, this fear doesn't mean actual danger. It's just a signal. Signal is not fact."</p>

<p>They haven't eliminated emotion. They've learned to "delay-tag" their emotions.</p>

<p>When fear rises, they don't label it immediately. They let fear exist in the body for a moment, waiting for the cognitive layer to evaluate: is this real danger, or rehearsed pain?</p>

<p>If it's real danger, execute the stop loss. If it's rehearsed pain, ignore it.</p>

<p>The distance between knowing and fearing can be shortened.</p>

<p>The method: cross that ditch repeatedly.</p>

<p>Every time you cross, knowing goes deeper. Fear retreats an inch.</p>

<p>Until one day, you realize: you're no longer afraid. Not because the danger is gone — but because your emotional layer has finally learned to understand what your cognitive layer is saying.</p>
'''

# ── JA article ──────────────────────────────────────────────────────────────
JA_CONTENT = '''<p>市場は下落すると知っている。</p>

<p>市場の暴落を恐れている。</p>

<p>この二つの間には溝がある。名前は「まだ起きていない」。</p>

<p>知っていることと恐れていることは、同じものではない。</p>

<h2>知るは認知、恐れるは感情</h2>

<p>認知と感情は異なる神経経路を走る。</p>

<p>夜更かしが体に悪いと知っている——これは認知経路だ。それでもあなたは夜更かしする。夜更かしした後、体はすぐに罰してくれない。あなたが感じるのは快適さと自由——これは感情経路だ。</p>

<p>感情経路の方が強い。即時フィードバックがあるからだ。</p>

<p>損切りが正しいと知っている。注文を入れた時、脳はこれが正しい操作だと知っている。だが損切りが執行されたその0.5秒、ドーパミンは崖から落ち、アドレナリンは急上昇する——その感じは「損失」と全く同じだ。</p>

<p>脳はこれが「戦略実行」だと知らない。脳只知道：痛い、損失した、危険だ。</p>

<p>だからポジションを保有し続ける。</p>

<h2>知と行の間の距離は、感情が占めている</h2>

<p>王陽明は「知行合一」を説いた。</p>

<p>ほとんどの人の解釈は：知っていることを実行すべきだ。这是間違い。</p>

<p>本当の意味は：あなたの「知」は、感情レベルに浸透してこそ「行」になれる。</p>

<p>損切りが正しいと「知っている」——これは認知レベルの知っているに過ぎない。あなたの体はまだ知らない。神経回路はまだ知らない。だから実行できない。</p>

<p>本当の「知る」は、体が知るということだ。</p>

<p>損切りが執行された瞬間、反射的にボタンを押す——と思う不是你感觉你应该，而是因为你すでに「知っている」就应该这样做，而且这个「知っている」已经变成了你的本能反应。</p>

<p>この「知る」には反復が必要だ。十分な損切り回数をこなして、認知レベルの「知る」を感情レベルに繰り返し運び込み、ついに感情レベルがそれを受け入れるまでだ。</p>

<h2>あなたが恐れているのは「既に起きたこと」でしかない</h2>

<p>面白いのは：あなたが恐れているのは、市場の下落そのものじゃない。</p>

<p>あなたが恐れているのは：市場が下落して、私のポジションが損失して、私はこの結果を承受しなければならない。</p>

<p>でも市場がまだ下落していない時、ポジションはまだある、口座はまだ赤い、「承受しなければならない」压力はまだない。</p>

<p>那你又在恐れる什么？</p>

<p>あなたが恐れているのは、「下落が既に起きた」後の感覚だ。その感覚は、まだ本当に起きていないのに、脑裏で先に予行練習されている。</p>

<p>あなたは、まだ起きていない感情のためにお金を使っている。</p>

<h2>痛苦の予行練習は、脑の自己防衛メカニズムだ</h2>

<p>なぜ脑は痛苦を先に予行練習するのか？</p>

<p>身を守るためだ。</p>

<p>だがこのメカニズムは、取引では逆方向に 작용한다。</p>

<p>ポジションを入れる前から、脑は損失の痛苦の予行練習を始める。焦虑させて、躊躇させて、決済ボタンを押すのを躭躇させる——そして行情はあなたのいないところを進んだ。あなたは持っていなかったトレンドを逃した。</p>

<p>脑はあなたを守ろうとしたのに、別の種類のお金を失わせた：機会費用のお金だ。</p>

<p>これは脑のせいではない。脑は原始世界で进化してきた。原始世界では、危険は見えていて即時のものだ。虎が追いかけてくる——走れば逃げられる。逃げられない——終わりだ。</p>

<p>でも市場は虎じゃない。市場は繰り返し出入できる。这次取引を逃しても、次はある。</p>

<p>脑にはこの確率モデルがない。</p>

<h2>時間を伸ばす——感情層に学習時間を与える</h2>

<p>なぜ老練なトレーダーは落ち着いたを持てるのか？</p>

<p>恐れないからじゃない。十分な「恐れる→実行→无事発生」の経験があるからだ。</p>

<p>このパターンが十分に繰り返された後、感情層はようやく受け入れた：「ああ、この恐れるは実際の危険を意味しない。ただのシグナルだ。シグナルは事実じゃない。」</p>

<p>彼らから感情をeliminateしたんじゃない。「感情的判断を迟らす」ことを学んだんだ。</p>

<p>恐れるが起きた時、すぐにラベルを貼らない。恐れるを体の中にしばらく間置き、認知層が評価するのを待つ：これは実際の危険か、予行練習された痛苦か？</p>

<p>実際の危険なら、損切りを実行する。予行練習された痛苦なら、無視する。</p>

<p>知ると恐れるの間の距離は縮められる。</p>

<p>方法は：その溝を繰り返し渡过する。</p>

<p>渡るたびに、知は深くなる。恐れるは一歩引く。</p>

<p>いつか気づく：你はもう恐れていない。危険がなくなったからじゃない——感情層がようやく認知層の言うことを理解できたからだ。</p>
'''

# ─────────────────────────────────────────────────────────────────────────────
import subprocess

def update_index(lang_suffix, title, excerpt, tags):
    path = os.path.join(BASE, f"index{lang_suffix}.html")
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()
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
    path = os.path.join(BASE, "articles", f"{SLUG}{suffix}")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✅ {path} written")

# ── Write 3 language article files ──────────────────────────────────────────
article_template_zh = f'''<!DOCTYPE html>
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
</html>'''

article_template_en = f'''<!DOCTYPE html>
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
</html>'''

article_template_ja = f'''<!DOCTYPE html>
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
</html>'''

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
