N = int(input())
S = [[0]*(N+1) for _ in range(2)]

for i in range(N):
  c,p = map(int,input().split())
  S[c-1][i+1] = p 

for i in range(N):
  for j in range(2):
    S[j][i+1] = S[j][i]

Q = int(input())
LR = [tuple(map(int,input().split())) for _ in range(Q)]

for l, r in LR:
  print(S[0][r]- S[0][l-1], S[1][r]- S[1][l-1])