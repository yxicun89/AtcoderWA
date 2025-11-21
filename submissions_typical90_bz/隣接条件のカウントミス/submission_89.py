import numpy as np
N,M = map(int,input().split())
G = [[None]]*N
for i in range(M):
  a,b = map(int,input().split())
  a -= 1
  b -= 1
  if G[a] == [None]:
    G[a] = [b]
  else:
    G[a].append(b)
  if G[b] == [None]:
    G[b] = [a]
  else:
    G[b].append(a)
ans = 0
for i in range(N):
  if len(G[i]) != 1:
    continue
  c = 0
  for j in range(len(G[i])):
    if i < G[i][j]:
      break
    else:
      c += 1
  if c == 1:
    ans += 1
print(ans)