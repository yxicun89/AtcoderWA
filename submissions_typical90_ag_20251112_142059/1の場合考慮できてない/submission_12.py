H,W = map(int, input().split())

H += 1
W += 1

H //= 2
W //= 2

print(H * W)