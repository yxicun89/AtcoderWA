H, W = map(int, input().split())

cols = (H//2) + (H%2)
rows = (W//2) + (W%2)

print(cols*rows)

