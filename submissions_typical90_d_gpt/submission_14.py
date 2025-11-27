
"""

行列内の要素同士の足し算

配列の列の合計値のコードあり

"""



H, W = map(int, input().split())

A = []

for i in range(H):

    tmp = list(map(int, input().split()))

    A.append(tmp)





ans = [["-" for _ in range(W)] for _ in range(H)]

row_sum = []

for i in range(H):

    for j in range(W):



        # 2次元配列の行の合計値を計算

        row_sum.append(sum(A[i][:]))



        # 2次元配列における列の合計を計算

        columns_sum = list(map(sum, zip(*A)))



        ans[i][j] = row_sum[i] + columns_sum[j] - A[i][j]



    print(*ans[i][:])
