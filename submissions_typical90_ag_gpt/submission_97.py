H, W = map(int, input().split())

count = 0
for i in range(0, H):
  for j in range(0, W):
    if i % 2 == 0 and j % 2 == 0:
      count += 1

print(count)