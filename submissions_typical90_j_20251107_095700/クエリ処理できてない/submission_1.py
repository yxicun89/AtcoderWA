N = int(input())
c1 = [0]
c2 = [0]
for _ in range(N):
    c, p = map(int, input().split())
    if c == 1:
        c1.append(c1[-1] + p)
        c2.append(c2[-1])
    else:
        c1.append(c1[-1])
        c2.append(c2[-1] + p)

Q = int(input())
l, r = map(int, input().split())
print(c1[r] - c1[l - 1], c2[r] - c2[l - 1])