H, W = map(int, input().split())
table = [list(map(int, input().split())) for __ in range(H)]
ans = [[0] * W for __ in range(H)]


def sum_func(table, i, j):
    sum_ij = 0
    sum_ij = sum(table[i])
    for k in range(H):
        sum_ij += table[k][j]
    sum_ij -= table[i][j]
    return sum_ij


for i in range(H):
    sum_ij = 0
    for j in range(W):
        ans[i][j] = sum_func(table, i, j)
print(ans)
