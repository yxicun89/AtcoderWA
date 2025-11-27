
H,W = map(int, input().split())

A =[list(map(int, input().split())) for _ in range(H)]

row = [sum(A[i]) for i in range(H)]

col = [sum(A[i][j]  for i in range(H)) for j in range(W)]



for i in range(H):

  ans =[[row[i] + col[j] - A[i][j]] for j in range(W)]

  print(*ans)
