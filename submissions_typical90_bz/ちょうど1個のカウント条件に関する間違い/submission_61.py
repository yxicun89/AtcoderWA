N, M = map(int, input().split())
a = []
b = []
for _ in range(M):
    aa, bb = map(int, input().split())
    a.append(aa)
    b.append(bb)

ans = 0
for n in range(N, 1, -1):
    if a.count(n) == 1:
        i = a.index(n)
        if b[i] < n:
            ans += 1
    elif a.count(n) == 0:
        if b.count(n) == 1:
            i = b.index(n)
            if a[i] < n:
                ans += 1
    else:
        continue

print(ans)