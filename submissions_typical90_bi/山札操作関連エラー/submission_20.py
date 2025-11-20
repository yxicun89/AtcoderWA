from collections import deque

Q = int(input())
d = deque()

for _ in range(Q):
  t, x = map(int, input().split())
  if t == 1:
    d.append(x)
  elif t == 2:
    d.appendleft(x)
  else:
    print(d[x-1])