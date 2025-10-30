H,W = map(int,input().split())

A_array = [list(map(int,input().split())) for _ in range(H)]

row_sums = []
col_sums = []

ans = []

for i in range(H):
    row_sum = 0
    # col_sum = 0
    for j in range(W):
        row_sum += A_array[i][j]
        # if i < W and j < H:
        #     col_sum += A_array[j][i]
    row_sums.append(row_sum)
    # col_sums.append(col_sum)

for i in range(W):
    col_sum = 0
    for j in range(H):
        col_sum += A_array[j][i]
    col_sums.append(col_sum)


# for i,col_sum in enumerate(col_sums):
#     col_ans = []
#     for row_sum in row_sums:
#         col_ans.append(col_sum+row_sum)
#     ans.append(col_ans)

for i,col_sum in enumerate(row_sums):
    row_ans = []
    for row_sum in col_sums:
        row_ans.append(col_sum+row_sum)
    ans.append(row_ans)

for i in range(H):
    print(*ans[i])



