
h, w = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(h)]



# 各行と各列の合計を保持

rowsum = [0] * h

colsum = [0] * w



# 行の合計を計算

for i in range(h):

    for j in range(w):

        rowsum[i] += array[i][j]



# 列の合計を計算

for j in range(w):

    for i in range(h):

        colsum[j] += array[i][j]



# 結果配列を計算

res = [[0] * w for _ in range(h)]

for i in range(h):

    for j in range(w):

        res[i][j] = rowsum[i] + colsum[j] - 2 * array[i][j]



# 結果を出力

for row in res:

    print(" ".join(map(str, row)))

