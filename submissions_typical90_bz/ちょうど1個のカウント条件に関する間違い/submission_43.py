n,m = map(int,input().split())
#DFS
G = [[] for _ in range(n)]

for i in range(m):
    a,b = map(int,input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

ans = 0
for i in range(0,n):
    l = list(set(G[i]))
    if len(l) == 1:
        if (l[0] < i):
            ans += 1
    elif len(l) > 1:
        if (l[0]< i) and (l[1]>=i):
            ans += 1

print(ans)
