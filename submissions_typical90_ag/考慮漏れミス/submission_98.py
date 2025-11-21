H, W = map(int, input().split())
ans = 0
h = 0

if H == 1 or W == 1:
    print(0)
    exit()

while h < H:
    w = 0
    while w < W:
        ans += 1
        w += 2
    h += 2

print(ans)