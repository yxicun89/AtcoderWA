from collections import deque

Q = int(input())
TX = [list(map(int, input().split())) for _ in range(Q)]

dq = deque()

for t, x in TX:
    if t == 1:
        dq.append(x)
    elif t == 2:
        dq.appendleft(x)
    else:
        print(dq[x - 1])
