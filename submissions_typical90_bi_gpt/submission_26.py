from collections import deque
q=int(input())
d =deque()
for _ in range(q):
    t, x = map(int, input().split())
    if t==1:
        d.append(x)
    elif t==2:
        d.appendleft(x)
    else:
        for _ in range(x):
            if len(d)==0:
                break
            else:
                print(d.pop())