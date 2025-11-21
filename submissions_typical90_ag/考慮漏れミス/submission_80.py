h, w = map(int, input().split())

ah = max(1, (h + 1) // 2)
aw = max(1, (w + 1) // 2)
print(ah * aw)
