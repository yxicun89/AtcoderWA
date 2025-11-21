n, m = map(int, input().split())

g = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
ans = 0
for i in range(n):
    cnt = 0
    for nt in g[i]:
        if nt < i:
            cnt += 1
    if cnt == 1:
        ans += 1