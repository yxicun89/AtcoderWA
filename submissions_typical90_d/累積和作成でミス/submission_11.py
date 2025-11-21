# 累積和使用してるけど、二次元配列の初期化方法が誤っているため、すべての行が同じリストを参照されている

H,W=map(int,input().split())

A=[list(map(int,input().split())) for i in range(H)]

"""H=3

W=3

A=[[1,1,1],[1,1,1],[1,1,1]]

"""

B=[]

for i in range(W):

  B.append(0)

result_sum=[B for i in range(H)] # ここで変数名を変更

row_sums = [sum(A[i]) for i in range(H)]

col_sums = []

for i in range(W):

  t=0

  for j in range(H):

    t+=A[j][i]

  col_sums.append(t)

for i in range (H):

  for j in range(W):

    result_sum[i][j]=row_sums[i]+col_sums[j]-A[i][j] # ここでも変数名を使用

for i in range(H):

    print(*result_sum[i])
