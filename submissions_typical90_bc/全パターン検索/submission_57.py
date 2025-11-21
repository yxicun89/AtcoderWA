# 全探索
import sys



def solve():

    # 入力の読み込み

    N, P, Q = map(int, sys.stdin.readline().split())

    A = list(map(int, sys.stdin.readline().split()))



    # DPテーブルの初期化

    # dp[i][r]: i 個選んだときに積の余りが r になる選び方の数

    dp = [[0] * P for _ in range(6)]

    dp[0][0] = 1  # 何も選ばないときの初期状態



    # 数列をループしてDPを更新

    for a in A:

        # 逆順で更新（i=5から0へ）

        for i in range(4, -1, -1):

            for r in range(P):

                if dp[i][r] > 0:  # 有効な状態のみ更新

                    new_r = (r * a) % P

                    dp[i + 1][new_r] += dp[i][r]



    # 答えを出力

    print(dp[5][Q])



