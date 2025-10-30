H, W = map(int, input().split())
A = []
B = []
for i in range(H):
  B.append([0]*W)
  
for i in range(H):
  a = list(map(int, input().split()))
  A.append(a)
  for j in range(W):
    B[i][j] += a[j] + sum(a)

for i in range(H):
  for j in range(W):
    B[i][j] -= A[i][j]
    
for i in range(H):
  print(*B[i])