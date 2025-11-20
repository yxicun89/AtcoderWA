n, m = map(int, input().split())

cnt = [0] * n
for _ in range(m):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    elif a == b:
        continue
    cnt[a] += 1

ans = 0
for i in range(n):
    if cnt[i] == 1:
        ans += 1
print(ans)