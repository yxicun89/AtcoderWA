h, w = map(int, input().split())
a = [[] for _ in range(h)]
result = [[0 for _ in range(w)] for _ in range(h)]

for i in range(h):
  a[i] = list(map(int,input().split()))
  
for i in range(h):
  for j in range(w):
    result[i][j] = sum(a[i])
    for s in range(h):
      result[i][j] += a[s][j]
    result[i][j] -= a[i][j]
      
print(result)
    