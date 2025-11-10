# 最後のprintがi,jでなくh,w　使ってるインデックス変数間違い

H, W = map(int, input().split())



L = [list(map(int, input().split())) for _ in range(H)]

row = {}

column = {}

for h in range(H):

    row[h] = sum(L[h])

    for w in range(W):

        if w in column:

            column[w] += L[h][w]

        else:

            column[w] = L[h][w]



for i in range(H):

    for j in range(W):

        if j == W - 1:

            print(row[i] + column[j] - L[h][w])

        else:

            print(row[i] + column[j] - L[h][w], end = " ")
