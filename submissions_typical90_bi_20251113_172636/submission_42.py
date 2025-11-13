from collections import deque
q = deque()
for i in range(int(input())):
    (t, x) = map(int, input().split())
    if t == 3:
        print(q[x-1])
    if t == 1:
        q.appendleft(x)
    else:
        q.append(x)