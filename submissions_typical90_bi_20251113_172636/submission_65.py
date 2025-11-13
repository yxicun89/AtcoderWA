Q = int(input())
l = []
for i in range(Q):
  tx = list(map(int,input().split()))
  t = tx[0]
  x = tx[1]
  if t == 1:
    l.append(x)
  elif t == 2:
    l = l + [x]
  elif t == 3:
    print(l[x-1]) 