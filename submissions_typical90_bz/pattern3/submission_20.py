N, M = map(int, input().split())
L = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    L[a - 1].append(b - 1)
    L[b - 1].append(a - 1)

for v in L:
    v.sort()

ans = 0
for i, v in enumerate(L):
    if len(v) == 1:
        if i > v[0]:
            ans += 1
    elif len(v) > 2:
        if i > v[0] and i <= v[1]:
            ans += 1

print(ans)