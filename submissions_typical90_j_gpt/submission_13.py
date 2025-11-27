
N = int(input())
C = [0 for i in range(N)]
c = [0 for i in range(N)]
count_C = 0
count_c = 0
for i in range(N):
  A , P = map(int,input().split())
  C[i] = C[i - 1]
  c[i] = c[i - 1]
  if A == 1:
    C[i] += P
  else:
    c[i] += P
Q = int(input())
for i in range(Q):
  L , R = map(int,input().split())
  print(C[R - 1] - C[0],c[R - 1] - c[0])
