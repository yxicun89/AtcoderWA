#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
問題タイトルとURL: https://atcoder.jp/contests/typical90/tasks/typical90_ag
問題文: 配点: `2` 点
【問題文】
E869120 くんは、冬に公開するイルミネーションを作成することを計画しています。
E869120 くんが計画しているイルミネーションは、縦 `H` `×` 横 `W` の `HW` 個のLEDで構成されます。
イルミネーションの各 LED は、点灯・消灯の状態を任意に切り替えることができます。
このイルミネーションは、以下の条件を満たすとき 不適切である といいます。
• イルミネーション全体に完全に含まれる 縦 `2` `×` 横 `2` の、`4` つの LED を含む領域であって、点灯している LED が領域内に `2` つ以上あるものが存在する。
適切な（不適切な状態ではない）イルミネーションの点灯パターンのうち、点灯している LED の個数としてありうる最大値を求めてください。
【制約】
• `1 ≦ H, W ≦ 100`
• 入力はすべて整数
【入力】
入力は以下の形式で標準入力から与えられます。  
`H` `W`
【出力】
答えを出力してください。
【入力例 1】2 3
【出力例 1】2
点灯している LED を `'#'`、消灯している LED を `'.'` とすると、たとえば以下の状態が、適切である中で点灯している LED の個数が最大となります。
#.#
...
一方、以下の状態は不適切であるため、条件を満たしません。
上から `1` ～ `2` つ目、左から `1` ～ `2` つ目の LED からなる領域内に点灯している LED が `2` つ存在します。
#.#
.#.
【入力例 2】3 4
【出力例 2】4
たとえば以下の状態が、適切である中で点灯している LED の個数が最大となります。
#..#
....
#..#
【入力例 3】3 6
【出力例 3】6
"""

import sys

# ==================== 高速入力 ====================
from sys import stdin

def I(): return int(stdin.readline())
def MI(): return map(int, stdin.readline().split())
def LI(): return list(map(int, stdin.readline().split()))
def S(): return stdin.readline()[:-1]  # [:-1] が rstrip('\n') より高速

# ==================== 定数 ====================
INF = 10**18
MOD = 10**9 + 7

# ==================== ここから問題を解く ====================
def solve():
    # 入力を読む
    H, W = MI()

    n = m = 0

    if H % 2 == 0:
        n = H //2
    else:
        n = (H+1) //2

    if W % 2 == 0:
        m = W //2
    else:
        m = (W+1) //2

    count = n * m
        
    print(count)

# ==================== 使い方ガイド ====================
"""
【使い方】
# この問題のフォルダに移動してから実行
cd /Users/amatsumto/Desktop/Atcoder_Practice/atcoder/contests/typical90/033

# テスト実行
python3 main.py < tests/sample-1.in

# 全サンプルでテスト（簡単！）
../../../test_here.sh

# または手動で
for f in tests/*.in; do echo "=== $f ==="; python3 main.py < "$f"; done

# 提出
acc submit main.py

【絶対パスで実行する場合】
python3 /Users/amatsumto/Desktop/Atcoder_Practice/atcoder/contests/typical90/033/main.py < /Users/amatsumto/Desktop/Atcoder_Practice/atcoder/contests/typical90/033/tests/sample-1.in

【ヒント】
- サンプル入出力は tests/ フォルダにあります
- 提出前に必ずテストを実行してください
"""

if __name__ == "__main__":
    solve()
