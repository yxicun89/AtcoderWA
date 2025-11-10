# 入力を受け取る
N = int(input())
C, P, L, R = [], [], [], []
for _ in range(N):
    c, p = map(int, input().split())
    C.append(c)
    P.append(p)
Q = int(input(9))
for _ in range(Q):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

# 累積和のリスト作成
cumulative_sum_list = [[0, 0]]
cumulative_sum = [0, 0]

for c, p in zip(C, P):
    cumulative_sum[c - 1] += p
    cumulative_sum_list.append(cumulative_sum[:])

# 計算して出力
for l, r in zip(L, R):
    a = cumulative_sum_list[r][0] - cumulative_sum_list[l - 1][0]
    b = cumulative_sum_list[r][1] - cumulative_sum_list[l - 1][1]
    print(a, b)