H, W = map(int, input().split())
if H % 2 == 0:
    H //= 2
else:
    H = H // 2 + 1
if W % 2 == 0:
    W //= 2
else:
    W = W // 2 + 1
print(H * W)
