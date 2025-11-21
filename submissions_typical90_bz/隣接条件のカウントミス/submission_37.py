from collections import deque

N,M=map(int,input().split())
G=[[] for _ in range(N+1)]
for _ in range(M):
  a,b=map(int,input().split())
  G[a].append(b)
  G[b].append(a)

memo=deque([1])
seen=[False]*(N+1)
ans=0
while memo:
  v=memo.popleft()
  seen[v]=True
  count=0
  
  for v2 in G[v]:
    if v2<v : count+=1
    if not seen[v2] : memo.append(v2)
  ans+=(count==1)

print(ans)