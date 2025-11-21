from collections import defaultdict
import bisect

n,m = map(int, input().split())

g = defaultdict(list)
for i in range(m):
    a,b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

ans = 0
for j,k in g.items():
    if bisect.bisect_right(k,j) == 1:
        ans += 1
print(ans)