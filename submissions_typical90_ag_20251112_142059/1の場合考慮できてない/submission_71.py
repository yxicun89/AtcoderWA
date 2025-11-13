H, W = map(int, input().split())

row_cnt = W // 2 if W % 2 == 0 else W // 2 + 1
col_cnt = H // 2 if H % 2 == 0 else H // 2 + 1

print(row_cnt * col_cnt)