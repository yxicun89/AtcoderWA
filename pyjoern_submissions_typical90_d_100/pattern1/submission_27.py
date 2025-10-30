# H行W列の数字
# (i,j)マスに、i行の和 + j行の和 - (i,j)の数値

def calc_hvsum(i, j, data):
    hvsum = 0
    # 行の加算
    hvsum += sum(data[i])
    # print(hvsum)
    # 列の加算
    for k in range(0, H):
        hvsum += data[k][j]
    
    hvsum -= data[i][j]
    return hvsum

H, W = map(int, input().split())
# print(H,W)

# 2行目以降で H 行の数字を受け取って2次元リストに格納
data = [list(map(int, input().split())) for _ in range(H)]

# 確認のため出力
for row in data:
    print(row)

# 出力：print(i行目の結果j列目, i行目結果2列目、i行目結果j)

for i in range(H):
    answer_list = []
    for j in range(W):
        answer_list.append(calc_hvsum(i,j,data))
    print(*answer_list)

    
