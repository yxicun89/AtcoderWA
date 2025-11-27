N,M = map(int, input().split())

G = [[] for _ in range(N+1)]
for _ in range(M):
  a,b = map(int, input().split())
  G[a].append(b)
  G[b].append(a)

i = 1
ans = 0
for g in G:
  tmp = [g[j] for j in range(len(g)) if g[j] <= i]
  if len(tmp) == 1:
    ans += 1
  i += 1
print(ans)