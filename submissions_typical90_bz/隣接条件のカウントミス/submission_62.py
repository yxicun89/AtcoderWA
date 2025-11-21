import bisect
ans = 0
n,m = map(int,input().split())
l = [[] for i in range(n+1)]

for i in range(m):
  a,b = map(int,input().split())
  l[a].append(b)
  l[b].append(a)
for i in range(1,n+1):
  if bisect.bisect_left(l[i],i) == 1:
    ans += 1
print(ans)
  
  