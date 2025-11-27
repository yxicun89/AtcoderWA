
# 入力

h, w = map(int, input().split())

a = []

for n in range(h):

  a.append(list(map(int, input().split())))



a_t = [list(x) for x in zip(*a)]



print(a)

print(a_t)

# # 計算

b = [[0 for k in range(w)] for l in range(h)]

# print(b)

for i in range(h):

  for j in range(w):

    # i行j列

    b[i][j] = sum(a[i]) + sum(a_t[j]) -a[i][j]





# # 出力

for m in range(len(b)):

  print(*b[m])
