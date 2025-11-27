
Q = int(input())

TX = [list(map(int, input().split())) for _ in range(Q)]



l = [0]*Q

for i, (t, x) in enumerate(TX):

    if t == 1:

        l.insert(0, x)

    elif t == 2:

        l.append(x)

    else:

        x -= 1  # 0-indexed

        print(l[x])
