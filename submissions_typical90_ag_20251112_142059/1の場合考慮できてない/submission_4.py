# 1の場合考慮できてない

H, W = map(int,input().split())

if H % 2 == 0:

    A = H // 2

else:

    A = H // 2 + 1

if W % 2 == 0:

    B = W // 2

else:

    B = W // 2 + 1

print(A * B)
