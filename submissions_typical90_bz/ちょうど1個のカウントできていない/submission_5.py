n, m = map(int, input().split())

tmp = {}
ans = 0

for i in range(m):
    a, b = map(int, input().split())
    if a > b:
        if a not in tmp:
            tmp[a] = 1
            ans += 1
        else:
            tmp[a] += 1
            ans -= 1

    else:
        if b not in tmp:
            tmp[b] = 1
            ans += 1
        else:
            tmp[b] += 1
            ans -= 1

if ans < 0:
    ans = 0
    
print(ans)
