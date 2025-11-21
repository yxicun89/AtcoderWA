n,m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
  a,b = map(int, input().split())
  a -= 1
  b -= 1
  g[a].append(b)
  g[b].append(a)

ans = 0
for i,p in enumerate(g):
  if len(p) > 1:
    if p[0] < i and p[1] > i:
      ans += 1
  if len(p) == 1:
    if p[0] < i:
      ans += 1
print(ans)