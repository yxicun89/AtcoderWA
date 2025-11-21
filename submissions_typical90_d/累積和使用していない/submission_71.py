import numpy as np

# N: 行数, W: 列数を取得
N, W = map(int, input().split())

# A を2次元配列として初期化
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

# Aをnumpy配列に変換
A = np.array(A)

# Bを初期化（全てゼロ）
B = np.zeros((N, W))

# 各要素の計算
for i in range(N):
    for j in range(W):
        B[i][j] = int(A.sum(axis=0)[j] + A.sum(axis=1)[i] - A[i][j])

# Bを出力
for i in range(N):
    print(*B[i])
