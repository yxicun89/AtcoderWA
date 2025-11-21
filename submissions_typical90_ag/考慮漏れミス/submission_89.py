h, w = map(int, input().split())
a = 0
if w % 2 == 0:
    a = w // 2
else:
    a = w // 2 + 1
b = 0
if h % 2 == 0:
    b = h // 2
else:
    b = h // 2 + 1
print(a * b)