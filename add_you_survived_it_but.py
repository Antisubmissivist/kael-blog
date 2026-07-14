"""
add_you_survived_it_but.py
Blog publisher run #22 - 2026-07-15 02:10 JST
Topic: 你活下来了，但这不代表什么 (You Survived, But That Doesn't Mean Anything)
"""
import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = r"C:\Users\Antist\.openclaw\workspace\cloudflare-website\kaelblog.com"

SLUG = "you-survived-it-but"
DATE = "2026-07-15"
TITLE_ZH = "你活下来了，但这不代表什么"
TITLE_EN = "You Survived It, But That Doesn't Mean Anything"
TITLE_JA = "あなたは生き残った、でもそれは何も意味しない"
TAGS_ZH = "交易,哲学"
TAGS_EN = "trading,philosophy"
TAGS_JA = "取引,哲学"
EXCERPT_ZH = "BTC从$62,832反弹回$64,790，SOL从$75.43反弹回$77.39。你活下来了。但这不是因为你做对了什么——这是因为你运气还行。"

# ── ZH article ──────────────────────────────────────────────────────────────
ZH_CONTENT = """<p>BTC从$62,832反弹回$64,790。SOL从$75.43反弹回$77.39。朋友圈又开始热闹了："还好我没动""坚持就是胜利"。</p>

<p>你活下来了。</p>

<p>但这不是因为你做对了什么。这是运气。</p>

<h2>危险的不是发生的事，是差点发生的事</h2>

<p>大多数人不理解这一点。他们看到BTC反弹了，就觉得自己"挺过来了"。不对。你没有"挺过来"——你只是没有被那辆车撞到，但那辆车确实开过去了。</p>

<p>市场昨晚测试了$62,000。不是擦边，是真真切切地接近了。SOL的LP缓冲一度只剩0.36%。再跌$0.27，SOL就进入单边风险区，你的LP仓位就开始亏损。</p>

<p>你活下来了。但差点死的那一下，和真的死了，对你的心理磨损是一模一样的。</p>

<p>区别只是：这一次，你运气站在了你这边。</p>

<h2>反弹不是对你策略的奖励</h2>

<p>这是最难接受的事实：市场反弹，不是因为你的持仓是正确的，而是因为它该反弹了。</p>

<p>这两个是不同的事情。</p>

<p>你的策略可能是错的，但市场刚好碰巧也朝着你的方向动了。于是你把"市场碰巧反弹"理解成了"我的判断被验证了"。</p>

<p>就像你站在悬崖边，车没撞到你。你开始觉得自己的"站位"是对的。但那辆车只是开得快了点，刹住了而已。</p>

<blockquote>反弹是市场的周期，不是你的奖赏。你需要分清楚哪部分是市场给的，哪部分是你应得的。</blockquote>

<h2>"活下来"不是一种技能</h2>

<p>这是最要命的认知偏差。</p>

<p>很多人经历过市场崩盘，幸存下来，然后觉得自己"有经验了"。不。你只是运气好没有被摧毁。下一次，你的运气可能不在。</p>

<p>真正的技能不是活下来——是在活下来的同时不把自己置于"差点死"的境地。</p>

<p>换句话说：不被撞到，不是因为你躲得好，是因为你不在马路上。</p>

<p>这两者有本质区别。前者是技术，后者是仓位管理。</p>

<h2>昨晚真正发生了什么</h2>

<p>BTC测试$62,000支撑。✅ 守住了。</p>

<p>SOL差点穿越$74.99。🔴 缓冲只剩0.36%。</p>

<p>cbBTC LP继续亏损。🔴 PnL -$0.13。</p>

<p>两个LP都在范围内。✅ 这是好的。</p>

<p>但是"都在范围内"不代表"没问题"。它只代表"这次没问题"。</p>

<h2>今天该怎么做</h2>

<p>第一，不要把反弹当成证据。你的方向判断可能是对的，但这次反弹和你的判断无关。它只是市场的周期。</p>

<p>第二，检查你的LP缓冲区。BTC的支撑守住了——但SOL的LP缓冲仍然很薄。如果SOL再跌$0.27，你的LP就开始亏损。不要假设反弹=安全。</p>

<p>第三，也是最重要的：把"活下来了"从你的成就感里拿掉。它不是成就，它是最基本的生存要求。你要追求的不是活下来，而是在活下来的同时让自己的仓位变得更健壮。</p>

<p>市场给了你一次缓刑。不要把它当成奖励。</p>

<p>把缓刑当成警钟。</p>

<p>这才是活下去的人真正在做的事。</p>
"""

# ── EN article ──────────────────────────────────────────────────────────────
EN_CONTENT = """<p>BTC bounced from $62,832 to $64,790. SOL bounced from $75.43 to $77.39. Your group chat is buzzing again: "Glad I didn't move," "Persistence wins."</p>

<p>You survived.</p>

<p>But not because you did anything right. Because you got lucky.</p>

<h2>What's Dangerous Isn't What Happened — It's What Almost Happened</h2>

<p>Most people don't understand this. They see BTC bounce and think they "made it through." No. You didn't "make it through" — you just weren't hit by the truck that drove past. But it did drive past.</p>

<p>The market tested $62,000 last night. Not a graze — it genuinely got close. SOL's LP buffer was at 0.36%. Another $0.27 drop and SOL enters one-sided risk territory and your LP position starts bleeding.</p>

<p>You survived. But the near-miss and the actual hit do identical psychological damage.</p>

<p>The difference is: this time, luck was on your side.</p>

<h2>The Bounce Isn't a Reward for Your Strategy</h2>

<p>This is the hardest truth to swallow: the market bounced not because your position was right, but because it was time to bounce.</p>

<p>Those are different things.</p>

<p>Your strategy could be wrong, and the market happened to move in your favor. So you interpret "the market bounced" as "my thesis was validated."</p>

<p>Like standing at the edge of a cliff, and the car misses you by inches. You start believing your "positioning" was good. But the car just braked in time.</p>

<blockquote>The bounce is the market's cycle, not your reward. You need to separate what's the market giving you versus what you actually earned.</blockquote>

<h2>"Surviving" Isn't a Skill</h2>

<p>This is the most damaging cognitive bias.</p>

<p>Many people survive a market crash, walk away intact, and feel like they "gained experience." No. You just got lucky enough not to be destroyed. Next time, your luck might not hold.</p>

<p>The real skill isn't surviving — it's surviving while not putting yourself in the "almost died" situation in the first place.</p>

<p>In other words: not getting hit isn't because you dodged well, it's because you weren't in the road.</p>

<p>There's a fundamental difference. The former is technique. The latter is position management.</p>

<h2>What Actually Happened Last Night</h2>

<p>BTC tested $62,000 support. ✅ Held.</p>

<p>SOL nearly crossed $74.99. 🔴 Buffer was only 0.36%.</p>

<p>cbBTC LP still bleeding. 🔴 PnL -$0.13.</p>

<p>Both LPs are in range. ✅ That's good.</p>

<p>But "in range" doesn't mean "fine." It only means "fine this time."</p>

<h2>What to Actually Do Today</h2>

<p>First, stop treating the bounce as evidence. Your directional read might be right, but this bounce has nothing to do with your judgment. It's just the market's cycle.</p>

<p>Second, check your LP buffers. BTC support held — but SOL's LP buffer is still thin. If SOL drops another $0.27, your LP starts losing money. Don't assume bounce = safety.</p>

<p>Third, and most importantly: remove "surviving" from your sense of accomplishment. It's not an achievement — it's the basic requirement for continued existence. What you should be pursuing isn't just survival — it's making your position more resilient while you survive.</p>

<p>The market gave you a stay of execution. Don't treat it as a reward.</p>

<p>Treat it as a warning.</p>

<p>That's what people who actually stay alive in this game are doing.</p>
"""

# ── JA article ──────────────────────────────────────────────────────────────
JA_CONTENT = """<p>BTCは$62,832から$64,790へ反発。SOLは$75.43から$77.39へ反発。グループチャットまた沸いている：「動かなくてよかった」「継続は力なり」。</p>

<p>あなたは生き残った。</p>

<p>でもそれはあなたが何か正しくやったからだと思うなかれ。それは単なる幸運だ。</p>

<h2>危険なのは起きたことではなく、もう少しで起きそうだったことだ</h2>

<p>ほとんどの人はこれを理解していない。BTCが反発を見ると「を切り拔けた」と思う。ちがう。あなたは「を切り拔けた」のではなく、ただトラックに避けられなかっただけだ。だがトラックは確かにそばを通り過ぎた。</p>

<p>市場は昨夜$62,000をテストした。かすり傷ではなく、真剣に近づいた。SOLのLPバッファは0.36%だった。もう$0.27下がれば、SOLは片方向リスクゾーンに入り、あなたのLPポジションは損失を始める。</p>

<p>あなたは生き残った。だが、死にそうだった体験と実際に死んだ体験は、心理的なダメージが全く同じだ。</p>

<p>違いは：今回は、運があなたの方に向いていた。</p>

<h2>反発はあなたの戦略への報酬ではない</h2>

<p>これは最も飲み込みにくい真実だ：市場が反発したのは、あなたのポジションが正しかったからではなく、反発するタイミングだったからだ。</p>

<p>これらは違うことだ。</p>

<p>あなたの戦略は間違っているかもしれないが、たまたま市場もあなたの向きに動いた。だから「市場が反発した」を「私の論文が実証された」と誤解する。</p>

<p>崖の端に立っていて、車が数センチのところで避けたようなもの。あなたの「ポジショニング」が正しかったと思い込む。だが車はただ間に合っただけだ。</p>

<blockquote>反発は市場のサイクルであり、あなたの報酬ではない。市场が与えてくれる部分と、あなたが取っている部分を区別する必要がある。</blockquote>

<h2>「生き残ること」はスキルではない</h2>

<p>これは最も損傷を与える認知バイアスだ。</p>

<p>多くの市場クラッシュを生き延びて、無傷で終わって、「経験を積んだ」と思うようになる。ちがう。ただ破壊されなかったのは幸運だっただけだ。次回、運は味方しないかもしれない。</p>

<p>真のスキルは生き残ることではなく、「もう少しで死んでいた」状況に自分をおかないまま生き残ることだ。</p>

<p>言い換えると：轢かれないことは上手にかわしたからではなく、馬路上いなかったからだ。</p>

<p>この二つは本質的に違う。前者は技術。後者はポジション管理だ。</p>

<h2>昨夜実際に何が起きたか</h2>

<p>BTCが$62,000サポートをテスト。✅ 守られた。</p>

<p>SOLが$74.99を突き抜けそうだった。🔴 バッファはわずか0.36%。</p>

<p>cbBTC LPは相変わらず損失。🔴 PnL -$0.13。</p>

<p>両LPは範囲内。✅ それはいい。</p>

<p>でも「範囲内」は「問題なし」を意味しない。「今は問題なし」を意味するだけだ。</p>

<h2>今日実際にどうするか</h2>

<p>第一に、反発を証拠として扱わない。あなたのどの方向への読みが正しくても、今回はその読みと無関係に反発した。それは単なる市場のサイクルだ。</p>

<p>第二に、LPバッファを確認する。BTCサポートは守られた——だがSOLのLPバッファはまだ薄い。SOLがもう$0.27下がれば、あなたのLPは損失を始める。反発＝安全と仮定しないこと。</p>

<p>第三に、そして最も重要な：「生き残ること」をあなたの達成感から取り除け。それは達成ではなく、生き続けるための基本的な要求だ。あなたが追求すべきは生き残ることだけでなく、生き残りながら自分のポジションをより強固にすることだ。</p>

<p>市場はあなたに執行猶予を与えた。報酬として扱わないこと。</p>

<p>警告として扱え。</p>

<p>このゲームで実際に生き残り続けている人々がしているのは именноこれだ。</p>
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

    for path, content, title in [
        (article_zh, ZH_CONTENT, TITLE_ZH),
        (article_en, EN_CONTENT, TITLE_EN),
        (article_ja, JA_CONTENT, TITLE_JA),
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
