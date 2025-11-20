n=int(input())

up,down=[],[]
l3=[]

for _ in range(n):
  t,x=map(int,input().split())
  if t==1:
    up.append(x)
  elif t==2:
    down.append(x)
  else:
    l3.append(x)
    
rdown=list(reversed(down))
rdown.extend(up)

for i in l3:
  print(rdown[-i])