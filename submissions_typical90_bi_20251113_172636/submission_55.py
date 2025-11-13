import sys
input = sys.stdin.readline
q = int(input())
tx = [map(int, input().split()) for _ in range(q)]
t, x = map(list, zip(*tx))


a = []
b = []
for i in range(q):
    if t[i] == 1:
        b.append(x[i])

    elif t[i] == 2:
        a.append(x[i])
    else:
        a = b[::-1] + a
        print(a[x[i]-1])