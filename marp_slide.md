---
marp: true
theme: default
paginate: true
backgroundColor: #ffffff
style: |
  /* 全体の設定 */
  section {
    font-family: 'Helvetica Neue', Arial, 'Hiragino Kaku Gothic ProN', 'Meiryo', sans-serif;
    font-size: 26px;
    padding: 60px 80px;
    color: #2c3e50;
    line-height: 1.7;
  }

  /* H1: タイトルスライドの大見出し */
  h1 {
    color: #1a5490;
    font-size: 2.0em;
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
    font-size: 1.5em;
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
---

<!-- _class: lead -->

<div style="text-align: center; padding-top: 60px;">

# 競技プログラミングにおける<br>誤答コードの自動分類手法の検討

<div style="font-size: 0.85em; color: #555; margin-top: 30px; font-weight: 500;">
LLMによる教育的ヒント生成の効率化に向けて
</div>

<div style="text-align: right; font-size: 0.95em; margin-top: 80px; line-height: 2.0;">

**発表者**: [あなたの名前]

**指導教員**: [先生の名前]

**所属**: [大学・研究室名]

</div>
</div>

---

## 研究背景：卒業研究での取り組み

### 競技プログラミング（競プロ）とは？

- アルゴリズムやデータ構造の知識を問うプログラミングコンテスト
- 問題に対して正しく動作するコードを制限時間内に作成

### 卒業研究での取り組み

- **目的**: ChatGPT（LLM）が学習者に教育的なヒントを提案できるか検証
- **対象**: 競プロ典型90問の★2難易度（基礎～中級レベル）
- **手法**: 誤答パターンごとにプロンプトを作成し、適切なヒントが出せるか評価

---

## 研究背景：発見した課題

### 卒業研究で直面した問題

<div class="box">

**誤答の収集・仕分け・パターン分類を手作業で実施**

1. 学習者の誤答コードを収集
2. どのような間違いか一つ一つ確認
3. 似た間違いをグループ化してパターンを作成
4. 各パターンに対応したプロンプトを設計

→ **1問あたり数時間～数日の作業**が必要

</div>

### 問題点

- 膨大な時間がかかり、多くの問題に展開できない
- 教員やTAの負担が大きすぎる

---

## 本研究の目的

### 提案内容

収集したソースコードをもとに、誤答を**機械的に仕分ける手法**を検討する

### 期待される効果

- ✅ パターン分類にかかる時間を**大幅削減**
- ✅ 教員やTAなど指導者の**作業時間を効率化**
- ✅ より多くの問題に対してヒント提案システムを展開可能に

<div style="text-align: center; margin-top: 30px; font-size: 1.1em; color: #667eea; font-weight: 600;">
→ 手作業の自動化により、教育支援の質と量を向上
</div>

---

## 先行研究：コードクラスタリングのアプローチ

既存のソースコードクラスタリングには主に**3つのアプローチ**が存在

| アプローチ | 特徴 | 主な課題 |
|:---:|:---|:---|
| **構造的** | AST（抽象構文木）などの構文的特徴を抽出 | 構文変更に敏感で、クラスタ数が増加しやすい |
| **意味的** | コードの意味や機能に基づく分類<br>（例：SemCluster） | 階層的クラスタリングでの編集距離計算コストが高い |
| **行動的** | プログラムの実行時動作を基準<br>ディープラーニング活用 | 大量データセットと慎重なデータ選別が必要 |

---

## 先行研究：Asanas Cluster

### 特徴

- **構造的アプローチ**に基づく自動分類ツール
- CFG（制御フローグラフ）とDFG（データフローグラフ）から特徴量を抽出
- **処理速度を重視**した設計

### 課題

<div class="box">

- 精度よりも速度を優先しているため、分類精度に限界がある
- 構文的な類似性に依存し、**意味的な誤りの違い**を捉えにくい

</div>

---

## 提案手法の概要

本研究では**2つの異なるアプローチ**で誤答の自動分類を試みる

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 25px; margin-top: 20px;">

<div>

### 手法1：静的解析

- Asanas Clusterベース
- 構造的特徴を数値化
- 機械学習で分類
- 処理が高速

</div>

<div>

### 手法2：LLM

- GPT-4oを使用
- 意味を理解して分類
- 人間に近い判断
- 柔軟性が高い

</div>

</div>

<div style="text-align: center; margin-top: 25px; padding: 12px; background: #f8f9fa; border-radius: 5px; font-size: 0.95em;">
両手法の性能を比較し、実用的な誤答分類システムの実現可能性を検討
</div>

---

## 手法1の基本概念：プログラムをグラフで表現

<div style="font-size: 0.9em;">

プログラムの構造を**視覚的・数学的に分析**するため、2種類のグラフを使用

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 15px;">

<div>

### CFG（制御フローグラフ）

プログラムの**実行の流れ**を表現

- 条件分岐（if文）
- ループ（for/while文）
- 処理の順序

→ **「どう動くか」を表す**

</div>

<div>

### DFG（データフローグラフ）

変数の**使われ方**を表現

- 変数への代入
- 変数の参照
- データの流れ

→ **「データがどう扱われるか」を表す**

</div>

</div>

<div style="margin-top: 15px; padding: 10px; background: #ecf5ff; border-left: 5px solid #3498db;">

💡 これらのグラフから数値的な特徴を抽出し、コードを比較・分類する

</div>

</div>

---

## 手法1：抽出する特徴量（1/3）

ソースコードからCFGとDFGを作成し、計**11個の数値的特徴**を抽出

### CFGから抽出する特徴（プログラムの構造）

| 特徴量 | 意味（わかりやすく） |
|:---|:---|
| ループ文の数 | `for`や`while`が何個あるか |
| 条件分岐文の数 | `if`文が何個あるか |
| 閉路の数 | 繰り返し構造がいくつあるか |
| パスの数 | プログラムの実行経路が何通りあるか |
| 複雑度 | プログラムの複雑さを示す指標<br>（数式: $M = E - N + 2P$） |
| 連結成分の数 | 独立した処理ブロックの数（通常は1） |

---

## 手法1：抽出する特徴量（2/3）

### DFGから抽出する特徴（変数の使われ方）

| 特徴量 | 意味（わかりやすく） |
|:---|:---|
| 変数の数 | プログラムで使っている変数が何個あるか |
| 参照の総数 | 変数を読み取る操作が全体で何回あるか |
| 代入の総数 | 変数に値を書き込む操作が全体で何回あるか |
| 最大参照回数 | 最もよく読まれる変数は何回読まれているか |
| 最大代入回数 | 最もよく書き込まれる変数は何回書き込まれているか |

<div style="margin-top: 25px; padding: 15px; background: #ecf5ff; border-left: 5px solid #3498db;">

💡 **具体例**: `x = a + b` → `a`と`b`を読み取り（参照）、`x`に書き込み（代入）

</div>

---

## 手法1：分類の仕組み（3/3）

### 機械学習による自動分類

**k-means++アルゴリズム**で似た特徴を持つコードをグループ化

- **クラスタ数**: 16個（先行研究より設定）
- **類似度**: ユークリッド距離を使用

### 重要度の調整（重み付け）

| 何を見るか | 重要度 | 理由 |
|:---|:---:|:---|
| プログラムの構造 | **高（1.0）** | 本質的な違いが現れる |
| 変数の数 | **中（0.6）** | ある程度重要 |
| 変数の読み書き回数 | **低（0.1）** | 補助的な情報 |

---

## 手法2：LLMアプローチとは？

**ChatGPT**などのAIを使って、コードの意味を理解させる

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 20px;">

<div style="padding: 15px; background: #fff3cd; border-left: 5px solid #ffc107; border-radius: 5px;">

**手法1（静的解析）**

「if文が3個、ループが2個」<br>という**数値**で判断

→ 構造は分かるが<br>**意味は分からない**

</div>

<div style="padding: 15px; background: #d1ecf1; border-left: 5px solid #0c5460; border-radius: 5px;">

**手法2（LLM）**

「このコードは条件判定を<br>間違えている」と**意味を理解**

→ 人間に近い判断が可能

</div>

</div>

---

## 手法2：使用するモデルと設計

### 使用モデル

**GPT-4o** (OpenAI API)

- API経由で利用可能な高性能モデル
- 今後のモデル改善で精度・コスパ向上が期待

### プロンプト設計の工夫

1. **コスト削減**: 問題文は要約版のみ提供
2. **出力の制限**: 間違いの説明とカテゴリ番号のみ
3. **カテゴリの明示**: 事前に人間が分類したカテゴリ名を与える

<div style="margin-top: 15px; padding: 12px; background: #ecf5ff; border-left: 5px solid #3498db; font-size: 0.95em;">

💡 LLMに「この誤答はどのカテゴリに属するか」を判定してもらう

</div>

---

## 手法2：プロンプト例

```
このコードの間違いを教えてください。
最後に以下のカテゴリのどれに当たるか数字のみ出力してください。
間違いの説明とカテゴリの出力のみ出力してください。

【問題文（要約版）】
...

【カテゴリ】
1. [カテゴリ1の説明]
2. [カテゴリ2の説明]
...
n. [カテゴリnの説明]

【コード】
...
```

<div style="text-align: center; margin-top: 20px; font-style: italic; color: #555;">
→ シンプルで明確な指示により、精度の高い分類を目指す
</div>


---

## 実験設定

### データセット

- **対象**: 競プロ典型90問（★2難易度）の誤答コード
- **正解ラベル**: 著者が手作業で分類
  - 例：「ループ範囲ミス」「計算式の誤り」「境界条件の誤り」

### 評価方法

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 15px;">

<div>

**エラー指数**

グループの「純粋さ」を測定<br>（**0に近いほど良い**）

$$
\text{Error Index} = \frac{n_{\text{total}} - n_{\text{max}}}{n_{\text{total}}}
$$

1つのグループに異なる種類の<br>誤答がどれだけ混ざっているか

</div>

<div>

**一致率**

正解との一致度を測定

自動分類の結果が、人間が分類した<br>正解とどれだけ一致しているか

→ 高いほど精度が良い

</div>

</div>

---

## 実験結果：手法1（静的解析）

多くの問題で**期待した精度が得られなかった**

### 典型的な失敗パターン

<div class="box">

**問題点**: 論理的な間違いが異なるコードでも、構造（if文やループの数など）が似ていると**同じクラスタに分類**されてしまう

</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 20px;">

<div style="padding: 12px; background: #fff3cd; border-left: 5px solid #ffc107; border-radius: 5px;">

**理想的な分類**<br>
エラーの意味合いごとに<br>きれいに色分け

</div>

<div style="padding: 12px; background: #f8d7da; border-left: 5px solid #dc3545; border-radius: 5px;">

**実際の分類結果**<br>
異なる意味の誤答が<br>同じクラスタに混在

</div>

</div>

---

## 考察：手法1（静的解析）

### なぜうまくいかなかったのか

静的解析は**コードの見た目（構造）**だけを見る → **間違いの本質（意味）**は分からない

### 具体例：構造が似ているが意味が異なる誤答

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 15px;">

<div style="padding: 12px; background: #ffe6e6; border-radius: 5px;">

**誤答A**
```
for i in range(n-1):  # 範囲不足
    if a[i] > max:
        max = a[i]
```
→ **ループ範囲のミス**

</div>

<div style="padding: 12px; background: #ffe6e6; border-radius: 5px;">

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

## 実験結果：手法2（LLM）

静的解析と比較して**良好な結果**が得られた

### 成功例

✅ 文法的には正しいがロジックが誤っているコード<br>
✅ 構造は似ているが意味が異なる誤答<br>
✅ 細かいアルゴリズムの違い

これらを**正しく別のカテゴリに分類**することができた

### 問題による違い

- **うまくいった問題**: 論理的な誤りの種類が明確な問題
- **課題が残る問題**: 誤答の境界が曖昧な問題

<div style="text-align: center; margin-top: 20px; font-style: italic; color: #555; font-size: 0.95em;">
現在、より多くのデータで詳細な評価を実施中
</div>

---

## 考察：手法2（LLM）

### なぜLLMの方が有効だったのか

<div class="box">

LLMは**コードの意味合い**を汲み取ることができる

- 単なる構文の違いではなく、**論理的な誤りの本質**を理解
- 人間が分類した際の**意図**に近い分類が可能
- 自然言語による説明も生成できるため、教育的価値が高い

</div>

### 今後の展望

- **プロンプトエンジニアリング**のさらなる改善
- **モデルの進化**により、精度とコストパフォーマンスが向上する見込み
- 実用的な教育支援システムとしての実装可能性が高い

---

## まとめと結論

### 本研究の成果

競プロの誤答コード自動分類について、**2つのアプローチ**を比較検討

1. **静的解析アプローチ**（Asanas Cluster）
2. **LLMアプローチ**（GPT-4o）

### 結論

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 25px; margin-top: 20px;">

<div style="padding: 20px; background: #fff3cd; border-left: 6px solid #ffc107; border-radius: 5px;">

**静的解析**

構文的特徴に基づくため、<br>**意味的な誤り分類には限界**がある

</div>

<div style="padding: 20px; background: #d1ecf1; border-left: 6px solid #0c5460; border-radius: 5px;">

**LLM**

コードの意味を理解し、<br>**より正確な分類が可能**

</div>

</div>

---

## 今後の展望

### 短期的な目標

- 📊 **データセット拡充**: より多くの問題と誤答パターンで検証
- 📈 **定量的評価**: エラー指数、一致率の詳細な分析
- 🔧 **プロンプト最適化**: より高精度な分類のための改良

### 長期的な目標

<div class="box">

✨ **自動分類システムの実装**

- 誤答収集から分類までの完全自動化
- 教員・TAの作業時間を大幅削減
- より多くの問題に対応可能な教育支援システムの構築

</div>

<div style="text-align: center; margin-top: 30px; font-size: 1.1em; color: #667eea; font-weight: 600;">
→ 競技プログラミング教育の質と効率を向上させる基盤技術へ
</div>

---

<!-- _class: lead -->
<!-- _paginate: false -->

<div style="display: flex; justify-content: center; align-items: center; height: 100%; font-size: 2.5em; font-weight: 700; color: #1a5490;">

ご清聴ありがとうございました

</div>