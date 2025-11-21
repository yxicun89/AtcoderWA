n, m = map(int, input().split())
l = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    l[a-1].append(b)
    l[b-1].append(a)
ans = 0
for i in range(n):
    if sum(i > it for it in l[i]):
        ans += 1
print(ans)
