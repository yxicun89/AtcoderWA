Q = int(input())

from collections import deque
q = deque([])

for _ in range(Q):
    t, x = map(int, input().split())
    if t==1:
        q.append(x)
    elif t==2:
        q.appendleft(x)
    else:
        print(q[-x+1])