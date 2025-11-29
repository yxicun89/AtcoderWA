---
marp: true
theme: default
paginate: true
backgroundColor: #ffffff
style: |
  /* 全体の設定 */
  section {
    font-family: 'Meiryo', 'メイリオ', sans-serif;
    font-size: 26px;
    font-weight: bold;
    padding: 60px 80px;
    color: #2c3e50;
    line-height: 1.7;
  }

  /* H1: タイトルスライドの大見出し */
  h1 {
    color: #1a5490;
    font-size: 1.95em;
    font-weight: 700;
    border-bottom: none;
    margin-bottom: 0.5em;
  }

  /* H2: 各ページの見出し */
  h2 {
    color: #1a5490;
    border-bottom: 3px solid #3498db;
    border-left: 12px solid #3498db;
    padding-left: 20px;
    padding-bottom: 8px;
    margin-bottom: 35px;
    font-size: 1.8em;
    font-weight: 600;
  }

  /* H3: 小見出し */
  h3 {
    color: #34495e;
    font-size: 1.15em;
    margin-top: 25px;
    margin-bottom: 15px;
    font-weight: 600;
    border-left: 5px solid #95a5a6;
    padding-left: 15px;
  }

  /* リストのスタイル */
  ul {
    margin: 15px 0;
    padding-left: 30px;
  }

  li {
    margin: 10px 0;
    line-height: 1.6;
  }

  /* 表のデザイン */
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 25px 0;
    font-size: 0.9em;
  }

  th {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 15px 12px;
    border: none;
    font-weight: 600;
    text-align: center;
  }

  td {
    padding: 12px;
    border: 1px solid #ddd;
    background-color: #fafafa;
  }

  /* 強調文字を「蛍光ペン風」にする */
  strong {
    color: #2c3e50;
    background: linear-gradient(transparent 65%, #ffeb3b 65%);
    font-weight: 700;
    padding: 2px 4px;
  }

  /* コードブロック */
  code {
    background-color: #f4f4f4;
    padding: 2px 6px;
    border-radius: 3px;
    font-family: 'Consolas', 'Monaco', monospace;
    font-size: 0.9em;
    color: #e74c3c;
  }

  /* 引用ブロック */
  blockquote {
    background: #ecf5ff;
    border-left: 8px solid #3498db;
    padding: 20px 25px;
    margin: 20px 0;
    color: #34495e;
    font-style: italic;
  }

  /* 数式 */
  .katex {
    font-size: 1.1em;
  }

  /* ボックススタイル（重要ポイント用） */
  .box {
    background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%);
    border-left: 6px solid #667eea;
    padding: 20px 25px;
    margin: 20px 0;
    border-radius: 5px;
  }
  .columns {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.5px;
  }
  .col-right {
    border-left: 2px solid #e0e0e0;
    padding-left: 40px;
  }
  .author-name {
    text-align: right;
    /* emではなくpxで指定すると確実です。必要に応じて数字を大きくしてください */
    font-size: 40px;
    margin-top: 80px;
    line-height: 1.5;
    color: #1a5490; /* 文字色を明示したい場合 */
    font-weight: bold; /* 太字にする設定 */
  }
  .margin {
    margin-top: 30px;
  }

  /* タイトルページ用のセンタリングコンテナ */
  .title-center {
    text-align: center;
    padding-top: 60px;
  }

  /* グリッドレイアウト（2カラム） */
  .grid-2col {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 30px;
    margin-top: 25px;
  }

  /* グリッドレイアウト（7:3比率） */
  .grid-7-3 {
    display: grid;
    grid-template-columns: 6fr 4fr;
    gap: 30px;
    margin-top: 25px;
  }

  /* 情報ボックス（黄色） */
  .info-box-yellow {
    padding: 25px;
    background: #fff9e6;
    border-radius: 8px;
    border: 2px solid #ffd700;
  }

  /* 情報ボックス（青） */
  .info-box-blue {
    padding: 25px;
    background: #e6f7ff;
    border-radius: 8px;
    border: 2px solid #3498db;
  }

  /* 警告ボックス（赤） */
  .warning-box {
    padding: 12px;
    background: #f8d7da;
    border-left: 5px solid #dc3545;
    border-radius: 5px;
  }

  /* ヒントボックス */
  .hint-box {
    padding: 15px;
    background: #ecf5ff;
    border-left: 5px solid #3498db;
  }

  /* 小さめのヒントボックス */
  .hint-box-small {
    padding: 12px;
    background: #ecf5ff;
    border-left: 5px solid #3498db;
    font-size: 0.95em;
  }

  /* 比較ボックス（黄色・警告） */
  .compare-box-yellow {
    padding: 15px;
    background: #fff3cd;
    border-left: 5px solid #ffc107;
    border-radius: 5px;
  }

  /* 比較ボックス（青緑・情報） */
  .compare-box-teal {
    padding: 15px;
    background: #d1ecf1;
    border-left: 5px solid #0c5460;
    border-radius: 5px;
  }

  /* エラーボックス（薄い赤） */
  .error-box {
    padding: 12px;
    background: #ffe6e6;
    border-radius: 5px;
  }

  /* 成功ボックス（黄色・大きめ） */
  .success-box-yellow {
    padding: 20px;
    background: #fff3cd;
    border-left: 6px solid #ffc107;
    border-radius: 5px;
  }

  /* 成功ボックス（青緑・大きめ） */
  .success-box-teal {
    padding: 20px;
    background: #d1ecf1;
    border-left: 6px solid #0c5460;
    border-radius: 5px;
  }

  /* フッターノート */
  .footer-note {
    text-align: center;
    margin-top: 20px;
    font-style: italic;
    color: #555;
  }

  /* フッターノート（小さめ） */
  .footer-note-small {
    text-align: center;
    margin-top: 150px;
    color: #555;
    font-size: 0.55em;
    font-family: 'Meiryo', 'メイリオ', sans-serif;
  }

  /* フッターノート（大きめ） */
  .footer-note-large {
    text-align: center;
    margin-top: 30px;
    font-size: 1.1em;
    color: #667eea;
    font-weight: 600;
  }

  /* 固定位置フッター */
  .fixed-footer {
    position: absolute;
    bottom: 50px;
    left: 60px;
    right: 60px;
    padding: 12px;
    background: #ecf5ff;
    border-left: 5px solid #3498db;
  }

  /* 中央メッセージボックス */
  .center-message {
    text-align: center;
    padding: 12px;
    background: #f8f9fa;
    border-radius: 5px;
    font-size: 0.95em;
  }

  /* 終了スライド用 */
  .ending-message {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
    font-size: 2.5em;
    font-weight: 700;
    color: #1a5490;
  }

  /* 分類の仕組み用（小さめテキスト） */
  .classification-section {
    font-size: 0.65em;
  }

  .classification-section h3 {
    font-size: 1.2em;
    margin-top: 0;
    margin-bottom: 8px;
  }

  .classification-section code {
    font-size: 1.06em;
    line-height: 1.3;
  }

  .classification-section .box {
    padding: 10px 12px;
    margin: 8px 0;
  }

  /* 小さい説明文用 */
  .small-text {
    font-size: 0.85em;
    line-height: 1.5;
  }

  /* エラー指数セクション専用 */
  .error-index-section {
    display: flex;
    align-items: center;
    gap: 30px;
    max-width: 85%;
    margin-left: 0;
  }

  .error-index-section .error-index-text {
    flex: 2;
    line-height: 1.5;
  }

  .error-index-section .error-index-formula {
    flex: 1.5;
    flex-shrink: 0;
  }
---

<!-- _class: lead -->

<div class="title-center">

# プログラミング演習における誤答分類のための<br>構造的アプローチと意味的アプローチの比較評価

<div class="author-name">
山本研究室 2024831008 西村優基
</div>

</div>
</div>

---

## 背景：卒業研究からの継続課題

### 卒業研究

<div class="box">

<!-- **卒業研究のテーマ** -->

ChatGPTが競技プログラミングの誤答に対し、教育的なヒントを提案できるか検証

- **対象問題**: 競プロ典型90問(難易度★2)

</div>

### 検証プロセス

<div class="grid-2col">

<div class="info-box-yellow">

**Step 1: 誤答の収集と分類**

各問題の誤答コードを集計し、どのような誤答があるのか**パターン分け**を実施

</div>

<div class="info-box-blue">

**Step 2: ヒント提案の検証**

各パターンの代表的なコードに対し、LLMが**適切なヒント**を出せるか確認

</div>

</div>

---

## 研究背景：発見した課題

### 卒業研究で直面した問題

<div class="box">

**誤答の収集・仕分け・パターン分類を手作業で実施**

1. 学習者の誤答コードを収集
2. どのような間違いか一つ一つ確認
3. 似た間違いをグループ化してパターンを作成
4. 各パターンに対応したプロンプトを設計
</div>

→ **1問あたり数時間～数日の作業**が必要で指導者の負担が大きい


---

## 本研究の目的

### 提案内容

収集したソースコードをもとに、誤答を**機械的に分類する手法**を検討する

### 期待される効果
<div class = "box">

-  パターン分類にかかる時間を**大幅削減**
-  教員やTAなど指導者の**作業時間を効率化**

</div>

→ 手作業の自動化により、教育支援の質と量を向上

---

## 先行研究：コードクラスタリングのアプローチ

既存のソースコードクラスタリングには主に**3つのアプローチ**が存在

| アプローチ | 特徴 | 主な課題 |
|:---:|:-----|:--------|
| **構造的** | トークン、AST、CFGなどの構文的特徴を抽出<br>→ コードの構造解析に強い | ・フォーマット変更に敏感<br>・動作や意味の考慮が不足<br>・クラスタ数が増加しやすい |
| **意味的** | 意味や機能に基づくベクトル表現<br>→ データフローを考慮し変数の使われ方を捉える | ・階層作成の距離計算コストが高い |
| **行動的** | 実行時動作やDeep Learningによる埋め込み学習<br>→記述形式に依存せず、動作に基づき同一視| ・大量データセットが必要<br>・データ選別・前処理の労力が高い |

---

## 先行研究：Asanas Cluster

先行研究では 意味的かつ構造的アプローチ **Asanas Cluster** という<br>ソースコード自動分類ツールを紹介している [1]

### 概要

<div class="box">

ソースコードから **制御フローグラフ(CFG)** と<br> **データフローグラフ(DFG)** を作成し、特徴量を抽出

→抽出した特徴量をもとにクラスタリングを実施する自動分類ツール

</div>

<div class="footer-note-small">
[1] Rivers, K., & Koedinger, K. R. (2017). Data-Driven Hint Generation in Vast Solution Spaces: a Self-Improving Python Programming Tutor. International Journal of Artificial Intelligence in Education, 27(1), 37-64.
</div>

---

## 制御フローグラフ (CFG) とは

**Control Flow Graph (CFG)**

プログラム内の **「処理の流れ」** を表現したグラフ

<div class="box">

- **ノード**: 基本ブロック（命令のまとまり）
- **エッジ**: 制御の移動（if文の分岐、ループなど）

</div>

### 用途

コードの**論理構造を可視化**するために用いられる

---

## データフローグラフ (DFG) とは

**Data Flow Graph (DFG)**

プログラム内の **「データの依存関係」** を表現したグラフ

<div class="box">

ある変数が**どこで定義**され、**どこで参照（使用）**されるかを追跡する

</div>

### 用途

変数の値が**どのように計算・伝播されるか**を解析するために用いられる

---

## 抽出する特徴量（1/2）

ソースコードからCFGとDFGを作成し、計**11個の数値的特徴**を抽出

### CFGから抽出する特徴量

| 特徴量 | 意味| 重み |
|:---|:---|:---|
| 連結成分の数 | 独立した処理ブロックの数（通常は1） | 1.0 |
| ループ文の数 | `for`,`while`,`再帰`が何個あるか | 1.0 |
| 条件分岐文の数 | `if`,`for`,`while`文が何個あるか | 1.0 |
| 閉路の数 | 繰り返し構造がいくつあるか | 1.0 |
| パスの数 | プログラムの実行経路が何通りあるか(分岐や閉路を一度のみ考慮する) | 1.0 |
| 複雑度 | プログラムの複雑さを示す指標<br>（複雑度 = エッジの数 - ノードの数 + 2*連結成分の数） | 1.0 |

---

## 抽出する特徴量（2/2）

### DFGから抽出する特徴

| 特徴量 | 意味| 重み |
|:---|:---|:---|
| 変数の数 | プログラムで使っている変数が何個あるか | 0.6 |
| 参照の総数 | 変数を読み取る操作が全体で何回あるか | 0.1 |
| 代入の総数 | 変数に値を書き込む操作が全体で何回あるか | 0.1 |
| 最大参照回数 | 最もよく読まれる変数は何回読まれているか | 0.1 |
| 最大代入回数 | 最もよく書き込まれる変数は何回書き込まれているか | 0.1 |

<div class="hint-box">

💡 **具体例**: `x = a + b` → `a`と`b`を読み取り（参照）、`x`に書き込み（代入）

</div>

---

## 分類の仕組み
抽出した特徴量をもとに以下疑似コードをもとにクラスタリングを実行
<div class="grid-7-3 classification-section">

<div>

### 疑似コード

```
Require: 2 <= k <= 16
Ensure: dist(c, S) は距離関数
Ensure: C は k-means++ で初期化
Ensure: N はゼロ初期化配列

repeat
    Let S be the new solution
    min, min_c ← ∞, 0
    for c ∈ C do
        d ← dist(c, S)
        if d <= min then
            min ← d
            min_c ← c
        end if
    end for
    N[min_c] ← N[min_c] + 1
    if S is correct then
        min_c ← min_c +
          (1/N[min_c]) × (S - min_c)
    end if
until no more submissions
```

</div>

<div>

### ポイント

<div class="box">
<!-- <div class = "margin"></div> -->

- クラスタ数: 2~16個

- 初期配置をkmeans++にし、局所解防止

- ユークリッド距離を用いて最も近いセントロイドを発見

- 正解セントロイドを与え、正しい解の場合のみ
セントロイドを移動

- データが一つ増えるたび重心を更新

</div>

</div>

</div>

---

## 手法

今回の実験では**2つの手法**でどちらの方がうまく仕分けられるか確認する

<div class="grid-2col">

<div class="info-box-yellow">

### 手法1：Asanas Cluster

構造的・意味的アプローチ

CFGとDFGから特徴量を抽出し、<br>k-meansアルゴリズムでクラスタリング

</div>

<div class="info-box-blue">

### 手法2：LLM
意味的・行動的アプローチ

GPT-4oを用いた自然言語による誤答分類

</div>

</div>

---

## 手法2：LLMによる誤答分類

### 概要

<div class="box">

コードの**意味理解に長けたGPT-4o (OpenAI API)** に、問題文・コード・分類カテゴリを与えて分類させる

</div>

<div class="grid-2col">

<div>

### 採用理由

- **システム化の容易さ**: API経由で利用可能
- **性能の高さ**
- **将来性**: モデルの進化により、<br>コストパフォーマンスの向上が期待

</div>

<div>

### プロンプト設計の工夫

1. **コスト削減**:　　 問題文は必要最低限
2. **出力の制限**: 　　間違いの説明と
　　　　　　　　カテゴリ番号のみ出力
3. **カテゴリの明示**: 事前に人間が分類した
　　　　　　　　カテゴリ名を与える

</div>

</div>

---

## 手法2：プロンプト例

```
このコードの間違いを教えてください。
最後に以下のカテゴリのどれに当たるか数字のみ出力してください。
間違いの説明とカテゴリの出力のみ出力してください。

【問題文（要約したもの）】
...

【カテゴリ】
1. [カテゴリ1]
2. [カテゴリ2]
...
n. [カテゴリn]

【コード】
...
```

<div class="footer-note">
→ シンプルで明確な指示により、精度の高い分類を目指す
</div>


---

## 実験設定

### データセット

- **対象**: 競プロ典型90問（★2）の誤答(WA)コード
- **正解ラベル**: 手作業で問題ごとにカテゴリ分類
  - 例：「条件考慮漏れ」「全探索することでTLE」「浮動小数点誤差による計算誤差」

### 評価方法

<!-- <div class="grid-2col"> -->

<div>

**エラー指数**

<div class="error-index-section">

<div class="error-index-text">

1つのグループに異なる種類の誤答が<br>どれだけ混ざっているかを測定
（**0に近いほど良い**）

</div>

<div class="error-index-formula">

$$
\text{Error Index} = \frac{n_{\text{total}} - n_{\text{max}}}{n_{\text{total}}}
$$

</div>

</div>

</div>

<div>

<!-- **一致率**
<div class = "small-text">
正解との一致度を測定

自動分類の結果が、人間が分類した<br>正解とどれだけ一致しているか

→ 高いほど精度が良い -->

</div>

</div>

---

## 実験結果：手法1（Asanas Cluster）

### 問題例：典型90問-問題AA

全体的に同じような結果が見られたが、**特に顕著な例**を示す

<div class="grid-2col">

<div>

**PCA可視化：クラスタリング前**

（各点が1つの誤答コードを表す）

[ここにPCAグラフ画像を配置]

</div>

<div>

**PCA可視化：クラスタリング後**

（色分けされたクラスタ）

[ここにPCAグラフ画像を配置]

**エラー指数: 0.XX**

</div>

</div>

<div class="warning-box">

**問題点**: 色がきれいに分かれていない → 異なる意味の誤答が同じクラスタに混在し、**意味的な分類ができていない**

</div>

---

## 考察：手法1（静的解析）

### なぜうまくいかなかったのか

静的解析は **コードの見た目（構造）** だけを見る → **間違いの本質（意味）** は分からない

### 具体例：構造が似ているが意味が異なる誤答

<div class="grid-2col">

<div class="error-box">

**誤答A**
```
for i in range(n-1):  # 範囲不足
    if a[i] > max:
        max = a[i]
```
→ **ループ範囲のミス**

</div>

<div class="error-box">

**誤答B**
```
for i in range(n):
    if a[i] >= max:  # 等号ミス
        max = a[i]
```
→ **条件判定のミス**

</div>

</div>

どちらも「for文1つ + if文1つ」→ **同じグループに分類**
構造は似ているが、**間違いの種類は全く違う** → 意味的な分類には**別のアプローチが必要**

---

## 実験結果：手法2（LLM）- 成功例

<!-- ### コードの意味を理解した適切な分類 -->

LLMでは**コードの間違い箇所と意味合いを理解**し、カテゴリ分けに成功

<div class="grid-2col">

<div class="success-box-yellow">

**誤答A**
```python
for i in range(n-1):  # 範囲不足
    if a[i] > max:
        max = a[i]
```

**LLMの分類結果**
→ カテゴリ: **ループ範囲のミス**
</div>

<div class="success-box-teal">

**誤答B**
```python
for i in range(n):
    if a[i] >= max:  # 等号誤り
        max = a[i]
```

**LLMの分類結果**
→ カテゴリ: **条件判定のミス**
</div>

</div>

<div class="box">

✅ 構造は似ているが、**誤りの意味が異なる**コードを正しく別カテゴリに分類
✅ 文法的には正しいが**ロジックが誤っている**コードも適切に分類

</div>

---

## 実験結果：手法2（LLM）- 失敗例

<!-- ### ハルシネーションによる誤分類 -->

Pythonライブラリを使用したコードに対して、**もっともらしい嘘**をつくケースが見られた

<div class="error-box">

**誤答コード例**
```python
import heapq
q = []
heapq.heappush(q, (cost, node))
# 実際の誤り: グラフ構造の定義ミス
```

**LLMの誤った分析**
「`heapq.heappush`の使い方が誤っています。第一引数は...」
→ **誤ったカテゴリ「ライブラリ使用ミス」へ分類**
</div>

<div class="warning-box">

**課題**: 特定のライブラリ関数や仕様に関する知識が不正確な場合、**ハルシネーション**により誤分類が発生する

</div>

---

## 考察

### 静的解析の限界

<div class="compare-box-yellow">

・静的解析アプローチは、コードの **「構造」を捉える**のには適している
・教育的指導に必要な **「誤りの意味」を分類する**には情報が不足
・**特に初学者のコードは構造が多様**であり、構造的特徴だけで意味を同一視するのは困難

</div>

### LLMの優位性と課題

<div class="grid-2col">

<div class="compare-box-teal">

**優位性**

LLMは**コードのセマンティクスを理解**できるため、「誤答パターンの分類」において静的解析より遥かに高い適性を持つ

</div>

<div class="warning-box">

**課題**

**ハルシネーション**による誤った指摘のリスクが存在

→信頼性の担保には注意が必要

</div>

</div>

---

## 結論

### 本研究の成果
<!--
競プロの誤答コード自動分類について、**2つのアプローチ**を比較検討

1. **静的解析アプローチ**（Asanas Cluster）
2. **LLMアプローチ**（GPT-4o） -->

<div class="box">

**誤答分類の自動化**を目指す上では、
従来のような**特徴量ベースの静的解析手法**よりも、<br>**LLMを用いた意味的アプローチ**の方が有効である可能性が高い
</div>

<div class="grid-2col">

<div class="success-box-yellow">

**静的解析**

構文的特徴に基づくため、<br>**意味的な誤り分類には限界**がある

</div>

<div class="success-box-teal">

**LLM**

コードの意味を理解し、<br>**より正確な分類が可能**

</div>

</div>

---

## 今後の展望

### 短期的な取り組み

- **プロンプトの改良**: より正確な分類のための指示設計
- **多様な問題での検証**: 異なる難易度・問題タイプでの評価
- **ハルシネーション対策**: ライブラリ関連の誤分類を減らす工夫

### 長期的な目標

<div class="box">

- **実用化に向けた精度向上**: モデルの進化による性能改善
- **教育支援システムへの実装**: 誤答収集から分類までの完全自動化
- **教員・TAの作業時間を大幅削減**: より多くの問題に対応可能なシステム構築

</div>

<!-- <div class="footer-note-large">
→ 競技プログラミング教育の質と効率を向上させる基盤技術へ
</div> -->

---

<!-- _class: lead -->
<!-- _paginate: false -->

<div class="ending-message">

ご清聴ありがとうございました

</div>
