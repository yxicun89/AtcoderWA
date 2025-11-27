n,m = map(int,input().split())
path = [[] for i in range(n)]
for i in range(m):
  a,b = map(int,input().split())
  path[a-1].append(b-1)
  path[b-1].append(a-1)
ans = 0
for i in range(n):
  path[i].sort()
  if len(path[i]) >= 2:
    if path[i][0] < i and i > path[i][1]:
      ans += 1
  elif len(path[i]) == 1:
      if path[i][0] < i:
          ans += 1
print(ans)