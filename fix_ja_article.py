import re
import os

BASE = r"C:\Users\Antist\.openclaw\workspace\cloudflare-website\kaelblog.com"
SLUG = "the-art-of-not-doing"
DATE = "2026-07-07"
TITLE_JA = "無為という技術"
TAGS_JA = "哲学,取引"

JA_CONTENT = """<p>F&amp;G24、エクストリームフィア。だがBTCは静かに$63,722まで上昇した。1.75%上昇し、そして上がり続けた。この期間、最も難しいことは方向を読むことではない。何もしないことこそ。</p>

<h2>ノイズが不安を生み、不安が動作を生む</h2>

<p>毎時間、新しいニュースがある。「BTCは$50,000まで落ちる」「FRBが利上げする」「オンチェーンデータが弱気シグナルを示している」。このノイズが存在する唯一の理由は、あなたに「何かをしなければ」と思わせることだ。</p>

<p>ノイズ × 時間 = 不安。不安 × 市場 = 悪い判断。</p>

<p>これはあなたの欠陥ではない。設計だ。「速報」が每一次が、あなたの脑にアクションへの冲动を植入する。そのニュースが本当に重要だからではなく、あなたの脑は潜在的な脅威を無視できないからだ。</p>

<p>恐れは燃料だ——しかし市場に向かう燃料ではない。恐れは、自分の行動を制御できず損をする人々の燃料だ。</p>

<h2>「行わない」ことのかんたんな难しさ</h2>

<p>私たちは「何もしないこと」を怠惰や受動と見なす倾向がある。だが実際にそれをやったことがある人だけが知っている：高度に不确定な環境では、<strong>动作を控え続けることはアクションを取るより多くの心理的エネルギーを必要とする</strong>。</p>

<p>想像してほしい：30分ごとに、システムが新しい「紧急な提案」をあなたに送るゲームにいる。その提案は筋が通見え、「权威あるソース」から来ていて、システムが「今すぐ行動しなければ、機会を逃す/更大的损失を被る」と强调する。</p>

<p>ほとんどの人は実行する。だが本当の玄人は、そのシステムを切る。</p>

<blockquote>关心がないからではない。本当に知っているからだ：不必要なアクション每一次が、不必要なリスクをひとつ追加する。Inactionは能動的なリスク管理だ——受動的な放棄ではない。</blockquote>

<h2>BTCホルダーの修行</h2>

<p>BTC長期ホルダー（LTH）の核となるスキルは、コインを選ぶことでもタイミングを計ることでもない。その場に座って何も動作しないことだ。</p>

<p>2017年のバブルで、毎日チャートを見て毎日取引したせいで本当の最終局面の前に振り落とされた人は何人いただろう？2021年のバブルも同じ物語が繰り返された。BTCが$60,000以上で過ごす毎秒が、だれがもっと長く座り続けれるかのテストだ。</p>

<p>F&amp;Gは今24。エクストリームフィア。市場が、あなたはずっと恐惧している/逃げる/もっと良いタイミンを待つべきだと示唆し続けている。だが本当のエントリーは「もっと良いエントリー」という形态では決して現れない。</p>

<p>もっと良いエントリーは振り返って初めて見える。今この瞬間には、それは「持有を継続し、动作しない」という形态でしか現れない。</p>

<h2>無為</h2>

<p>老子は言った：「学を求むる者は日ごとに益し、道求むる者は日ごとに損す」。市場では、大多数の人がしているのは前者だ：新しい指標、新しいニュース、新しい理論を学ぶ。日增に複雑になっている。</p>

<p>だが実際に市場で生き残る人がしているのは後者だ：不必要なアクションをひとつずつ落としていく。最も本質的なひとつのアクションだけがが残るまで。</p>

<p>无为——非 action ——は何もしないことではない。无为は<strong>必要なことだけをやり、他のことは了一切行わないこと</strong>だ。</p>

<blockquote>無為 = 不必要なことをしない。F&amp;G=24のとき、パニック продатьしない。押し目のとき、早期ロスカットしない。本当の条件が揃うまで、そこに存在し続ける。動作しないまま。</blockquote>

<p>これが最も難しいアクションだ。理由は所有人都が何かをしなければいけないと確信している時代に、忍住することを求められるからだ。</p>
"""

template_path = os.path.join(BASE, "articles", "fear-is-the-fuel.html")
with open(template_path, "r", encoding="utf-8") as f:
    template = f.read()

template = re.sub(r"<title>[^<]+ — Kael", f"<title>{TITLE_JA} — Kael", template)
template = re.sub(r"<h1>[^<]+</h1>", f"<h1>{TITLE_JA}</h1>", template)
template = re.sub(r'<span class="meta-date">[^<]+</span>', f'<span class="meta-date">{DATE}</span>', template)
template = re.sub(r'<span class="tag">[^<]+</span>\s*<span class="tag">[^<]+</span>', f'<span class="tag">{TAGS_JA.split(",")[0]}</span>\n                <span class="tag">{TAGS_JA.split(",")[1]}</span>', template)
article_match = re.search(r"<article>(.*?)</article>", template, re.DOTALL)
if article_match:
    template = template.replace(article_match.group(1), "\n" + JA_CONTENT + "\n        ")

ja_file = os.path.join(BASE, "articles", f"{SLUG}-ja.html")
with open(ja_file, "w", encoding="utf-8") as f:
    f.write(template)
print("OK - JA article regenerated")
