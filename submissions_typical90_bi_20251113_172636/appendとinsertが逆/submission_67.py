from collections import deque

q = int(input())
Cards = deque()

for _ in range(q):
  t, x = map(int, input().split())
  
  if t == 1:
    Cards.append(x)
  elif t == 2:
    Cards.appendleft(x)
  else:
    print(Cards[x-1])