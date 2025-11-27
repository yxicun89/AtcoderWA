n, k = input().split()
k = int(k)
for _ in range(k):
    v = 0
    d = 1
    for i in range(len(n) - 1, -1, -1):
        v += int(n[i]) * d
        d *= 8
    n = ''
    while v:
        v, r = divmod(v, 9)
        n = str(r) + n
    n = n.replace('8', '5')
print(n)