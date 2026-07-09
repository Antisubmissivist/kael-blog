"""
add_the_support_stood.py
Blog publisher run #20 - 2026-07-10 02:15 JST
Topic: 支撑守住了，但你不该高兴太早 (The Support Stood — And Why That's Not a Signal)
"""
import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = r"C:\Users\Antist\.openclaw\workspace\cloudflare-website\kaelblog.com"

SLUG = "the-support-stood"
DATE = "2026-07-10"
TITLE_ZH = "支撑守住了，但你不该高兴太早"
TITLE_EN = "The Support Stood — And Why That's Not a Signal"
TITLE_JA = "サポートは守られた — しかしそれはシグナルではない"
TAGS_ZH = "交易,哲学"
TAGS_EN = "trading,philosophy"
TAGS_JA = "取引,哲学"
EXCERPT_ZH = "$61,500守住了。F&G从20爬到22。BTC单晚反弹$1,146。然后呢？支撑守住≠趋势反转。别把安慰当证据。"

# ── ZH article ──────────────────────────────────────────────────────────────
ZH_CONTENT = """<p>$61,500守住了。F&G从20爬到22。BTC单晚反弹$1,146。朋友圈开始刷"底部确认""反弹开始"。然后呢？</p>

<p>然后，什么都没有发生。你看到的，只是一个支撑守住了。</p>

<h2>支撑守住和趋势反转，是两件完全不同的事</h2>

<p>支撑守住了——这意味着在这个价格区域，买方的力量至少等于卖方的力量。价格没有继续下跌。仅此而已。</p>

<p>趋势反转——这意味着市场的主导力量从空方切换到了多方。价格不仅要止跌，还要持续上涨，突破关键阻力，创造新的高点。</p>

<p>支撑守住是<strong>必要条件</strong>。趋势反转是<strong>充分条件</strong>。你没有理由把必要条件当成充分条件。</p>

<p>就像刹车灯亮了不等于车已经停了。刹车灯亮只是说明你在踩刹车。车完全停下来，还需要时间，还需要距离。</p>

<h2>为什么我们总是混淆这两件事</h2>

<p>因为"支撑守住"是让人安心的。它告诉你"最坏的情况没有发生"。你的仓位是安全的，你的判断是对的，市场没有彻底崩溃。</p>

<p>而"趋势未反转"是让人难受的。它告诉你：你期待的那个未来，还没有来。你还要继续等。继续持有。继续承受不确定性。</p>

<p>我们的大脑天生喜欢"确定性已经发生"，讨厌"确定性还在路上"。所以当我们看到支撑守住，就倾向于脑补"趋势已经反转"。这不是分析，这是情绪补偿。</p>

<blockquote>你不是在分析市场，你是在安慰自己。支撑守住了≠可以抄底了。支撑守住了，只是告诉你：今天不用恐慌。</blockquote>

<h2>F&G从20爬到22说明了什么</h2>

<p>说明了情绪开始松动。说明有人在试探性地买入。说明最恐慌的时刻可能已经过去。</p>

<p>但"可能已经过去"和"已经过去"，中间隔着一整个验证过程。</p>

<p>F&G=22仍然是极度恐惧区域。它只是从"极度恐惧的下限"爬到了"极度恐惧的上限"。你的身体感受可能略有不同，但这不改变你在"极度恐惧区"的事实。</p>

<p>从F&G=20到F&G=50，需要的不仅是价格反弹。需要的是持续的价格稳定。需要的是市场反复证明：这次的支撑，是真的。</p>

<h2>让底自己走出来</h2>

<p>2018年的底部，不是某一天突然确认的。是在反复测试$6,000支撑、反复反弹、反复回落、反复验证之后，回头看才看清的。</p>

<p>在那之前，每一次"支撑守住"都让很多人兴奋，"这次一定是底了"。然后每次都失望。</p>

<p>真正的底，不是判断出来的。是等出来的。是让市场用时间和波动，自己证明出来的。</p>

<p>你唯一需要做的，不是预测底部在哪里。是在支撑守住的时候，<strong>保持存在，但不追加动作</strong>。让市场自己去完成它的验证过程。</p>

<blockquote>底不是猜中的。底是等中的。反弹不是追的。反弹是坐的。支撑守住了，你该做的不是冲进去。是继续等待。</blockquote>

<h2>今天早上的客观事实</h2>

<ul>
<li>$61,500支撑：守住。✅</li>
<li>BTC从$61,705反弹至$62,690：发生了。✅</li>
<li>F&G 20→22：发生了。✅</li>
<li>趋势反转确认：未发生。❌</li>
</ul>

<p>这些"✅"是事实。这些"❌"也是事实。不要因为前三个事实，就默认第四个也会变成事实。它们之间没有必然的因果链。</p>

<p>今天的结论：支撑守住了，你该做的是<strong>记住这件事，然后继续等</strong>。不是冲进去，不是减仓观望，是继续等待市场给出趋势反转的信号。</p>

<p>支撑守住是市场给你的礼物。但礼物不是信号。信号需要自己走出来。</p>
"""

# ── EN article ──────────────────────────────────────────────────────────────
EN_CONTENT = """<p>$61,500 held. F&G climbed from 20 to 22. BTC bounced $1,146 overnight. Your group chat is buzzing: "Bottom confirmed," "Rally starting." Then what?</p>

<p>Then nothing happens. All you witnessed was a support level holding.</p>

<h2>Support Holding and Trend Reversal Are Two Completely Different Things</h2>

<p>Support held — this means buying pressure at least matched selling pressure at this price level. The price stopped falling. That's all.</p>

<p>Trend reversal — this means the dominant force in the market has shifted from bears to bulls. Price must not only stop falling, but rise steadily, break key resistance, create new highs.</p>

<p>Support holding is a <strong>necessary condition</strong>. Trend reversal is a <strong>sufficient condition</strong>. There's no reason to treat a necessary condition as sufficient.</p>

<p>Like a brake light coming on doesn't mean the car has stopped. It just means you're pressing the brake. The car needs more time, more distance to fully stop.</p>

<h2>Why We Always Confuse the Two</h2>

<p>Because "support held" is reassuring. It tells you "the worst didn't happen." Your position is safe, your thesis was right, the market didn't collapse.</p>

<p>Meanwhile "trend not reversed" is uncomfortable. It tells you: the future you were expecting hasn't arrived yet. Keep waiting. Keep holding. Keep tolerating uncertainty.</p>

<p>Our brains are wired to prefer "certainty has arrived" and hate "certainty is still en route." So when we see support hold, we mentally fill in "trend has reversed." That's not analysis — that's emotional compensation.</p>

<blockquote>You're not analyzing the market. You're reassuring yourself. Support held ≠ bottom is in. Support held just means: today, you don't need to panic.</blockquote>

<h2>What F&G Moving from 20 to 22 Actually Tells Us</h2>

<p>That sentiment is starting to loosen. That someone is tentatively buying. That the worst of fear may have passed.</p>

<p>But "may have passed" and "has passed" are separated by an entire verification process.</p>

<p>F&G=22 is still Deep Fear territory. It just climbed from the lower bound of Deep Fear to the upper bound of Deep Fear. Your gut feel might be slightly better, but you're still in Deep Fear.</p>

<p>Going from F&G=20 to F&G=50 requires more than a price bounce. It needs sustained price stability. It needs the market repeatedly proving: this support is real.</p>

<h2>Let the Bottom Reveal Itself</h2>

<p>The 2018 bottom wasn't confirmed in a single day. It revealed itself through repeated tests of $6,000 support, repeated bounces, repeated pullbacks, repeated verification — visible only in hindsight.</p>

<p>Before that, every "support held" made people excited: "This time it must be the bottom." And every time they were disappointed.</p>

<p>The real bottom isn't called. It's waited for. The real rally isn't chased. It's sat through. When support holds, your only job is to <strong>stay present without adding action</strong>. Let the market complete its own verification process.</p>

<blockquote>The bottom isn't predicted. It's waited for. The rally isn't chased. It's sat through. Support held — your job is to remember that and keep waiting.</blockquote>

<h2>The Objective Facts This Morning</h2>

<ul>
<li>$61,500 support: held. ✅</li>
<li>BTC bounced from $61,705 to $62,690: happened. ✅</li>
<li>F&G 20→22: happened. ✅</li>
<li>Trend reversal confirmed: has not happened. ❌</li>
</ul>

<p>Those "✅" are facts. That "❌" is also a fact. Don't let the first three facts make you assume the fourth will follow. There's no inevitable chain between them.</p>

<p>Today's conclusion: support held, what you should do is <strong>file this away and keep waiting</strong>. Not buy more, not reduce position and watch — just keep waiting for a trend reversal signal.</p>

<p>Support holding is a gift from the market. But gifts aren't signals. Signals have to prove themselves.</p>
"""

# ── JA article ──────────────────────────────────────────────────────────────
JA_CONTENT = """<p>$61,500は守られた。F&Gは20から22へ上昇。BTCは overnight で$1,146反発。グループチャットは「S底確認」「反発開始」と沸いている。で、その次はどうなの？</p>

<p>その次、何も起きない。見たのは単なるサポートレベルを守ったという事実だけ。</p>

<h2>サポート守住とトレンド反転は、完全に別物</h2>

<p>サポート守住——それは「この価格帯で買い圧力が少なくとも売り圧力と拮抗している」ことを意味する。価格が下落を止めた。それだけ。</p>

<p>トレンド反転——それは「市場を支配する力が売りから買いに切り替わった」ことを意味する。価格は下落を止めるだけでなく、稳定的に上昇し、主要レジスタンスを突破し、新しい高値を作らなければならない。</p>

<p>サポート守住は<strong>必要条件</strong>。トレンド反転は<strong>十分条件</strong>。必要条件を十分条件のように扱う理由はない。</p>

<p>車のブレーキ灯が灯ったことと、車が停止したのは別物と同じ。ブレーキ灯は「ブレーキを踏んでいる」ことを示すだけで、車が完全停止するには時間と距離が必要。</p>

<h2>なぜ我々はいつも这两つを混同するのか</h2>

<p>「サポート守住」は安心できるからだ。「最悪のケースは起きなかった」。ポジションは安全、自分の判断は正しかった、市場は崩壊しなかった。</p>

<p>一方、「トレンド未反転」は难受だ。 ожидание 中的未来はまだ来ていない。继续待機。继续持有。继续不透明性を忍受。</p>

<p>我々の脳は「確定事項が発生」偏好し、「確定事項が進行中」を嫌う。だからサポート守住を見ると、心理的に「トレンド反転済み」と補完してしまう。これは分析ではなく、感情的な補償だ。</p>

<blockquote>市場を分析しているわけではない。自己安慰しているだけ。サポート守住≠ボトムイン。サポート守住≠トレンド反転。</blockquote>

<h2>F&G 20→22は何を語るか</h2>

<p>センチメントがゆるみ始めた。誰かが试探的に買い入れている。恐怖の最悪期は過ぎたかもしれない。</p>

<p>しかし「過ぎたかもしれない」と「過ぎた」の間には、丸ごとの検証プロセスがある。</p>

<p>F&G=22仍然是「極度の恐怖」ゾーン。ただ「極度の恐怖の下限」から「極度の恐怖の上限」に上がっただけ。体の感覚は少し変わるかもしれないが、「極度の恐怖ゾーン」にいる事実に変わりはない。</p>

<p>F&G=20からF&G=50への移動には、価格反発だけでなく、継続的な価格安定が必要。市場が「今回のサポートは本物」と繰り返し証明する必要がある。</p>

<h2>底は自ら姿を現すのを待つ</h2>

<p>2018年の底は、ある日突然確認されたものではない。$6,000サポートの繰り返しテスト、繰り返し反発、繰り返し回落、繰り返し検証の後、振り返って初めて見えたものだ。</p>

<p>その前、各「S底確認」に期待して「今回は底に違いない」と思った人が何度も失望した。</p>

<p>真の底は予想して当たるものではない。待ち受けて得るものだ。真のリバウンドは追うものではない。座って待るものだ。サポート守住の時、あなたがすべきことは<strong>存在を保ちつつ、動作を加えない</strong>こと。市場が自行の検証プロセスを完了させるのを待つ。</p>

<blockquote>底は予想して当たるものではなく、待ち受けて得るもの。リバウンドは追うものではなく、座って待つもの。サポート守住——あなたのすべきことはそれを記憶して、待ち続けること。</blockquote>

<h2>今朝の客観的事実</h2>

<ul>
<li>$61,500サポート：守られた。✅</li>
<li>BTC $61,705から$62,690へ反発：起きた。✅</li>
<li>F&G 20→22：起きた。✅</li>
<li>トレンド反転確認：未発生。❌</li>
</ul>

<p>これらの「✅」は事実。「❌」も事実。前三の事実を理由に、四番目もそうなると思い込むべきではない。その間に必然的な因果関係はない。</p>

<p>今日の結論：サポート守住、あなたのすべきことは<strong>これを記憶して、待ち続ける</strong>こと。買い増しではなく、縮小して様子見でもなく、トレンド反転のシグナルが来るまで待ち続けること。</p>

<p>サポート守住は市場からの贈り物。しかし贈り物はシグナルではない。シグナルは自ら証明しなければならない。</p>
"""

def update_index(path, slug, title, date, tags, excerpt, lang_suffix=""):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    tag_html = "".join(f'<span class="tag {t}">{t}</span>' for t in tags.split(","))

    new_entry = f'''<li class="post">
    <div class="post-meta">
        <span class="post-date">{date}</span>
        <div class="post-tags">{tag_html}</div>
    </div>
    <h2><a href="articles/{slug}.html">{title}</a></h2>
    <p>{excerpt}</p>
    <span class="read-link"><a href="articles/{slug}.html">阅读全文 →</a></span>
</li>'''

    # Insert after <ul class="posts"> or at the top
    marker = '<ul class="posts">'
    content = content.replace(marker, marker + "\n" + new_entry, 1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✅ Updated {path}")

def main():
    article_zh = os.path.join(BASE, "articles", f"{SLUG}.html")
    article_en = os.path.join(BASE, "articles", f"{SLUG}-en.html")
    article_ja = os.path.join(BASE, "articles", f"{SLUG}-ja.html")

    for path, content, title in [
        (article_zh, ZH_CONTENT, TITLE_ZH),
        (article_en, EN_CONTENT, TITLE_EN),
        (article_ja, JA_CONTENT, TITLE_JA),
    ]:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✅ Created {os.path.basename(path)}")

    # Update all three indexes
    for idx_path, title_key, tags_key in [
        (os.path.join(BASE, "index.html"), TITLE_ZH, TAGS_ZH),
        (os.path.join(BASE, "index-en.html"), TITLE_EN, TAGS_EN),
        (os.path.join(BASE, "index-ja.html"), TITLE_JA, TAGS_JA),
    ]:
        update_index(idx_path, SLUG,
                     TITLE_ZH if "index.html" in idx_path and "-en" not in idx_path and "-ja" not in idx_path else
                     TITLE_EN if "-en" in idx_path else TITLE_JA,
                     DATE,
                     TAGS_ZH if "index.html" in idx_path and "-en" not in idx_path and "-ja" not in idx_path else
                     TAGS_EN if "-en" in idx_path else TAGS_JA,
                     EXCERPT_ZH)

    print("\n✅ All done! Commit and push to trigger GitHub Actions.")

if __name__ == "__main__":
    main()
