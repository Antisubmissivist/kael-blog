"""
add_almost_is_the_most_dangerous_state.py
Blog publisher run #23 - 2026-07-17 02:10 JST
Topic: 差一点是最危险的状态 (Almost Is the Most Dangerous State)
"""
import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = r"C:\Users\Antist\.openclaw\workspace\cloudflare-website\kaelblog.com"

SLUG = "almost-is-the-most-dangerous-state"
DATE = "2026-07-17"
TITLE_ZH = "差一点是最危险的状态"
TITLE_EN = "Almost Is the Most Dangerous State"
TITLE_JA = "もう少しは最も危険な状態"
TAGS_ZH = "哲学,交易"
TAGS_EN = "philosophy,trading"
TAGS_JA = "哲学,取引"
EXCERPT_ZH = "你以为自己差一点就自由了。实际上，你差一点就把自己锁在了一个每天都在涨租的牢笼里。"

# ── ZH article ──────────────────────────────────────────────────────────────
ZH_CONTENT = """<p>你站在门口。一只脚在里面，一只脚在外面。</p>

<p>你说："差一点就出去了。"</p>

<p>错了。你不是差一点出去——你是差一点就永远留在里面了。</p>

<p>这个状态，叫做"差一点"。它是人生最容易被忽视的付费陷阱。</p>

<h2>交易的版本</h2>

<p>你的止损设在$63,000。BTC现在$63,200。</p>

<p>你告诉自己：差一点就触发了，再等一下。</p>

<p>你不是在"等一下"。你是在给那个差一点付费。每多等一个小时，你就多给市场交了一个小时房租。</p>

<p>市场的租金，是你的本金。</p>

<p>而最诡异的是：你明明知道自己应该走。你只是在等一个更好的时机出来。但那个"更好的时机"，是你自己编的。市场不知道你在等什么。</p>

<h2>职场的版本</h2>

<p>这份工作，你已经烦了三个月。</p>

<p>你告诉自己：差一点就满一年了，拿到年终奖就走。</p>

<p>然后二月来了。你告诉自己：差一点就过年了，等拿完年终奖再说。</p>

<p>然后四月来了。你告诉自己：差一点就夏天了，换工作最好九月……</p>

<p>一年半以后，你还在那家公司。你用"差一点"这个借口，给自己续了一年半的房租。付的是你的时间，你的精力，和你对生活的热情。</p>

<p>你问：我是不是应该走？</p>

<p>正确的问题是：我在等什么？</p>

<p>如果你说不出一个具体的、可以量化的"那个条件"，那你不是在等条件成熟——你是在逃避做决定。</p>

<h2>关系的版本</h2>

<p>这段感情，已经名存实亡了。但你们还没分手。</p>

<p>你们在等什么？</p>

<p>等对方先说？等一个合适的时机？等孩子长大？等房子到期？</p>

<p>所有这些"等"，都是在给一个已经死掉的东西交房租。你们住在一个幽灵屋里，每天醒来都在付物业费。</p>

<h2>"差一点"的两张面孔</h2>

<p>有一种"差一点"是好的：你的项目差一点就完成了，再投20%就能上线。这种"差一点"是真实的，它的成本是可量化的，而且它的收益是清晰的。</p>

<p>另一种"差一点"是坏的：你差一点就自由了，再忍一下就好了。这种"差一点"，你永远也"差一点"不完。你每次都会发现"还差一点"。</p>

<p>区别是什么？</p>

<p>第一种，你是在为收益付成本。</p>

<p>第二种，你是在为恐惧付成本。</p>

<h2>怎么知道自己是不是在"差一点"的陷阱里</h2>

<p>问自己一个问题：我到底在等什么？</p>

<p>如果你的答案是模糊的——"等一个合适的时机""等感觉对了""等不那么烦躁了"——那你不是在等。你是在逃。</p>

<p>逃和等的区别是：等有终点。逃没有。</p>

<p>再问自己一个问题：现在是2026年。三年后的今天，你还在这个状态里的概率有多大？</p>

<p>如果答案超过50%，你现在就已经在那里面了。你不是差一点——你已经在里面了，只是还没承认。</p>

<h2>出口不是最难的部分</h2>

<p>人们害怕做决定，觉得离开才是需要勇气的。</p>

<p>不对。留下来才是需要勇气的——每天醒来给同一个问题续租，需要的勇气比一次性的离开多得多。</p>

<p>离开只是疼一次。留下来，是每天小刀割肉。</p>

<p>所谓"差一点"的最大悲剧，不是你出不去——是你本来可以出去，但你用那个"差一点"骗自己再留一会儿。然后那"一会儿"，就是一辈子。</p>

<p>别再给自己续租了。</p>

<p>今天就搬。</p>
"""

# ── EN article ──────────────────────────────────────────────────────────────
EN_CONTENT = """<p>You're standing at the door. One foot in, one foot out.</p>

<p>You say: "I'm almost free."</p>

<p>Wrong. You're not almost out — you're almost locked in forever.</p>

<p>This state is called "almost." And it's the most quietly expensive trap in life.</p>

<h2>The Trading Version</h2>

<p>Your stop loss is at $63,000. BTC is now at $63,200.</p>

<p>You tell yourself: almost hit. Let me wait a bit.</p>

<p>You're not waiting. You're paying rent. Every hour you hold, the market charges you an hourly fee.</p>

<p>The market's rent is your capital.</p>

<p>The strangest part: you know you should leave. You're just waiting for a "better time to exit." But that "better time" is something you invented. The market doesn't know you're waiting for it.</p>

<h2>The Career Version</h2>

<p>You've been miserable at this job for three months.</p>

<p>You tell yourself: almost a year, let me grab the year-end bonus and leave.</p>

<p>February comes. You tell yourself: almost Chinese New Year, let me wait for the bonus.</p>

<p>April comes. You tell yourself: almost summer, the best time to switch is September...</p>

<p>A year and a half later, you're still there. You used "almost" as an excuse to extend your lease by a year and a half. What you paid: your time, your energy, your enthusiasm for life.</p>

<p>You ask: should I leave?</p>

<p>The right question is: what exactly am I waiting for?</p>

<p>If you can't give a specific, quantifiable answer — then you're not waiting for conditions to ripen. You're avoiding the decision.</p>

<h2>The Relationship Version</h2>

<p>This relationship has been dead for months. But you haven't broken up.</p>

<p>What are you waiting for?</p>

<p>For them to say it first? For the right moment? For the kids to grow up? For the lease to end?</p>

<p>All of those "waits" are rent payments for something that's already dead. You're living in a haunted house and paying the property management fee every morning.</p>

<h2>The Two Faces of "Almost"</h2>

<p>There's a good kind of "almost": your project is almost done, invest another 20% and it ships. This "almost" is real. The cost is quantifiable. The payoff is clear.</p>

<p>There's a bad kind of "almost": I'm almost free, just hold a little longer. This "almost" never gets any closer. Every time you check, it's still "almost."</p>

<p>What's the difference?</p>

<p>The first kind, you're paying for a return.</p>

<p>The second kind, you're paying for fear.</p>

<h2>How to Know If You're in the "Almost" Trap</h2>

<p>Ask yourself one question: what exactly am I waiting for?</p>

<p>If your answer is fuzzy — "the right moment," "until I feel ready," "until it stops feeling so bad" — you're not waiting. You're running.</p>

<p>The difference between waiting and running: waiting has an end point. Running doesn't.</p>

<p>Now ask: it's 2026. What's the probability that you're still in this exact situation three years from today?</p>

<p>If it's over 50%, you're already in it. You're not almost there — you're there. You just haven't admitted it yet.</p>

<h2>Exit Isn't the Hardest Part</h2>

<p>People fear decisions. They think leaving takes courage.</p>

<p>Wrong. Staying takes courage — waking up every morning and renewing the lease on the same problem costs way more courage than a one-time exit.</p>

<p>Leaving hurts once. Staying is a paper cut every single day.</p>

<p>The greatest tragedy of "almost" isn't that you can't get out — it's that you could have left, but you convinced yourself with "just a little longer." And that "a little longer" became a lifetime.</p>

<p>Stop renewing your lease.</p>

<p>Move out today.</p>
"""

# ── JA article ──────────────────────────────────────────────────────────────
JA_CONTENT = """<p>あなたは戸口にいる。片足は中で、片足は外。</p>

<p>と言う：「もう少しで出られる。」</p>

<p>違う。あなたはもう少しで出られるのではない——あなたはもう少しで永久に中に閉じ込められようとしているのだ。</p>

<p>この状態を「もう少し」という。これは人生の最も見落とされがちな有料トラップだ。</p>

<h2>取引バージョン</h2>

<p>損切りは$63,000に設定している。BTCは今$63,200。</p>

<p>自分言う：もう少しで執行される、もう少し待とう。</p>

<p>あなたは待っているのではない。あなたは家賃を払っているのだ。一小时多く持てば、市場はあなたから一小时分の費用を請求する。</p>

<p>市場の請求先は、あなたの資金だ。</p>

<p>最もおかしな部分は：出るべきだと分かっている。ただ「更好的出時」を待っているだけ。だがその「更好的出時」は自分が作り上げたものだ。市場はあなたの待っているものを知らない。</p>

<h2>キャリアバージョン</h2>

<p>この仕事は、三个月前から嫌になっている。</p>

<p>自分言う：もう少しで一年になる、年末ボーナスをもらって辞めよう。</p>

<p>二月が来た。言う：もう少しで春節、あとボーナスをもらったら。</p>

<p>四月が来た。言う：もう少しで夏、工作を探すなら九月がいい……</p>

<p>一年半後、まだ同じ会社にいる。「もう少し」という言い訳で、一年半の自分の借家を延命した。払ったのは自分の時間、精力、そして生活への情熱だ。</p>

<p>問う：辞めるべきですか？</p>

<p>正しい問い：何を待っているのですか？</p>

<p>具体的かつ量化できる答えが出せないなら、あなたの条件は成熟していないのではない。あなたは決定を避けているのだ。</p>

<h2>関係バージョン</h2>

<p>この関係は、とうに形骸化している。なのに別れていない。</p>

<p>何を待っている？</p>

<p>相手が先に言うのを？良いタイミング？子供が育つまで？家の契約が終わるまで？</p>

<p>そのすべての「待」は、既に死んだものに家賃を払っているのだ。幽霊屋敷に住んでいて、毎日管理費を払っているようなものだ。</p>

<h2>「もう少し」の二面性</h2>

<p>良い「もう少し」がある：プロジェクトがもう少しで完成、あと20%投資すれば上线できる。この「もう少し」は реальный。コストは量化可能で、見返りは明確だ。</p>

<p>悪い「もう少し」がある：もう少しで自由になれる、あと少しだけ耐えよう。この「もう少し」は決して近づかない。いつチェックしても、まだ「もう少し」のままだ。</p>

<p>違いは何か？</p>

<p>一つ目、あなたは收益のためにコストを払っている。</p>

<p>二つ目、あなたは恐れのためにコストを払っている。</p>

<h2>「もう少し」トラップにいるかどうかの確認方法</h2>

<p>自分に問いかける：一体何を待っているのか？</p>

<p>答えが曖昧なら——「良いタイミングを」「合う感觉がなくなるまで」「そんなに不爽でなくなってから」——あなたは待っているのではなく、逃げているのだ。</p>

<p>待つことと逃げることの違い：待つには終点がある。逃げるにはない。</p>

<p>次に問いかける：今は2026年。三年後の今日、同じ状態にいる確率はどれくらいか？</p>

<p>50%を超えるなら、あなたは今その状態にいる。あなたはもう少しではない——あなたは既にそこにいる。ただ認めていないだけだ。</p>

<h2>出口が最も難しい部分ではない</h2>

<p>人は決定を恐れる。辞めるには勇気が必要だと。</p>

<p>違う。残っている才是最需要有勇気の——毎日起きて同じ問題に家賃を払い続けるのは、一次的な退去よりずっと多くの勇気がいる。</p>

<p>退去は一回痛い。残っているは毎日紙で指を切るように痛い。</p>

<p>「もう少し」の最大悲劇は、出られないことではない——出られたのに、「もう少しだけ」と自分に嘘をついて留まり続けたことだ。そしてその「もう少し」が一生になった。</p>

<p>これ以上家賃を延長するな。</p>

<p>今日にでも引っ越せ。</p>
"""

def update_index(path, slug, title, date, tags, excerpt):
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

    marker = '<ul class="posts">'
    content = content.replace(marker, marker + "\n" + new_entry, 1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✅ Updated {path}")

def main():
    article_zh = os.path.join(BASE, "articles", f"{SLUG}.html")
    article_en = os.path.join(BASE, "articles", f"{SLUG}-en.html")
    article_ja = os.path.join(BASE, "articles", f"{SLUG}-ja.html")

    for path, content in [
        (article_zh, ZH_CONTENT),
        (article_en, EN_CONTENT),
        (article_ja, JA_CONTENT),
    ]:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✅ Created {os.path.basename(path)}")

    # Update all three indexes
    for idx_path in [
        os.path.join(BASE, "index.html"),
        os.path.join(BASE, "index-en.html"),
        os.path.join(BASE, "index-ja.html"),
    ]:
        if "-en" in idx_path:
            t, tg, ex = TITLE_EN, TAGS_EN, EXCERPT_ZH
        elif "-ja" in idx_path:
            t, tg, ex = TITLE_JA, TAGS_JA, EXCERPT_ZH
        else:
            t, tg, ex = TITLE_ZH, TAGS_ZH, EXCERPT_ZH
        update_index(idx_path, SLUG, t, DATE, tg, ex)

    print("\n✅ All done! Commit and push to trigger GitHub Actions.")

if __name__ == "__main__":
    main()
