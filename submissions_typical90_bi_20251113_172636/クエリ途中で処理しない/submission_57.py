from sys import stdin
nii=lambda:map(int,input().split())
lnii=lambda:list(map(int,input().split()))
from collections import deque

q = int(input())

num = 0
l = []
cnt = []
que = deque()

isThree = False
for i in range(q):
  t, x = nii()
  l.append((t, x))

  if t == 1:
    que.appendleft(x)
    if isThree:
      num += 1
  elif t == 2:
    que.append(x)
  else:
    isThree = True

  cnt.append(num)

cnt = cnt[::-1]

for i in range(q):
  t, x = l[i]
  if t == 3:
    pena = cnt[i]
    inx = x + pena - 1

    ans = que[inx]
    print(ans)