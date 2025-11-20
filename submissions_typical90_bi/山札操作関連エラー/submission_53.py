# ヒープで順序ミス

import heapq

q = int(input())

c = []

for i in range(q):

  t,x = map(int,input().split())

  if t == 1:

    heapq.heapify(c)

    heapq.heappush(c,x)

  elif t == 2:

    c.append(x)

  else:

    print(c[x-1])

