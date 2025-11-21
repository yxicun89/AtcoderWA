H, W = map(int, input().split())
if H % 2 == 0:
    h = H // 2
else:
    h = H // 2 + 1
if W % 2 == 0:
    w = W // 2
else:
    w = W // 2 + 1
ans = h * w
print(ans if H != 0 and W != 0 else H * W)