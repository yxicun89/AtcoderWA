N,M = map(int,input().split())

d = [[] for _ in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)
ans = 0
for i in range(1,N+1):
    if d[i][0] < i:
        ans += 1

print(ans)