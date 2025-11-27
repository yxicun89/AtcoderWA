h, w = map(int, input().split())
ans = 0
for i in range(h):
    for j in range(w):
        if i % 2 == 0 and j % 2 == 0:
            ans += 1
print(ans)