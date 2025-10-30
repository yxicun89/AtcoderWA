H, W = map(int,input().split())
A = [list(map(int,input().split())) for i in range(H)]
B = [[0] * W for i in range(H)]

for i in range(H):
  for j in range(W):
    B[i][j] = 0
    for J in range(W):
      B[i][j] = B[i][j] + A[i][J]
    for I in range(H-1):
      B[i][j] = B[i][j] + A[I+1][j]

for i in range(H):
  print(*B[i])