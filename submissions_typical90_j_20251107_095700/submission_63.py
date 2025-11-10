N = int(input())
A = [[0] * (N) for _ in range(2)]
for i in range(N):
  a, b = map(int, input().split())
  if i == 0:
    if a == 1:
      A[0][i] += b
      A[1][i] += 0
    else:
      A[0][i] += 0
      A[1][i] += b
  else:
    if a == 1:
      A[0][i] += A[0][i-1] + b
      A[1][i] += A[0][i-1]
    else:
      A[0][i] += A[0][i-1]
      A[1][i] += A[0][i-1] + b
Q = int(input())
for j in range(Q):
  c, d = map(int,input().split())
  print(A[0][d-1] - A[0][c-1], A[1][d-1]-A[0][c-1])