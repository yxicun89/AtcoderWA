n, m = map(int, input().split())
a = []
b = []
ans = 0

for _ in range(m):
    tmp1, tmp2 = map(int, input().split())
    a.append(tmp1)
    b.append(tmp2)

for i in range(n):
    tmp = 0
    for j in range(m):
        if i + 1 == a[j] and b[j] < i + 1:
            tmp += 1

    if tmp == 1:
        ans += 1
print(ans)
