n, m = map(int, input().split())

ans = 0
graph = [[] * n for _ in range(n)]
for i in range(m):
  a, b = map(int, input().split())
  a -= 1
  b -= 1
  graph[a].append(b)
  graph[b].append(a)
  


for i,num in enumerate(graph):
  c = 0
  

  for j,n in enumerate(num):
    if n == 1 and j < i:
      c += 1
  
  if c == 1:
    ans += 1

  
print(ans)