from collections import deque

Q = int(input())
TX = [list(map(int, input().split())) for _ in range(Q)]

Y = deque()

for tx in TX:
    t, x = tx
    if t == 1:
        Y.append(x)
    elif t == 2:
        Y.appendleft(x)
    else:
        c = Y[x-1]
        print(c)