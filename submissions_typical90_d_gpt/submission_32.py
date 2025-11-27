
H, W = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(H)]



H_sum = [sum(A[h]) for h in range(H)]

W_sum = [sum(w) for w in zip(*A)]



for i in range(H):

  r = ""

  for j in range(W):

    r += str(H_sum[i] + W_sum[j] - A[i][j] * 2)

    if not j == W - 1:

      r += " "

  print(r)
