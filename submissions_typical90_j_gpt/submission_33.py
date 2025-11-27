n = int(input())
nowa, nowb = 0, 0
s = []
for i in range(n):
    c, p = (list(map(int, input().split())))
    if c == 1:
        nowa += p
    else:
        nowb += p
    s.append([nowa, nowb])

q = int(input())
a, b = [], []
for i in range(q):
    l, r = list(map(int, input().split()))
    a.append(s[r-1][0] - s[l-2][0])
    b.append(s[r-1][1] - s[l-2][1])
for i in range(q):
    print(a[i], b[i])