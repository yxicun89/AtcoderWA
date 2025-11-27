n, m = map(int, input().split())

node = [[] for i in range(n+1)]

ans = 0
for i in range(m):
  ai, bi = map(int, input().split())
  node[ai].append(bi)
  node[bi].append(ai)

for i in node:
  if len(i) == 1:
    ans += 1
print(ans)
  