Q = int(input())
cards = []
rev = False
for _ in range(Q):
  t,x = map(int,input().split())
  if t == 3:
    if not rev:
      cards = cards[::-1]
      rev = False
    print(cards[x-1])
  elif t == 1:
    if rev:
      cards = cards[::-1]
      rev = False
    cards.append(x)
  else:
    if not rev:
      cards = cards[::-1]
      rev = True
    cards.append(x)