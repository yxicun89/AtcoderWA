from collections import deque
q=int(input())
d=deque()
for i in range(q):
  t,x=map(int,input().split())
  if t==1:
    d.append(x)
  elif t==2:
    d.appendleft(x)
  else:
    print(d[x-1])