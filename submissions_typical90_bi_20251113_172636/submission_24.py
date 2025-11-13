Q=int(input())
d=[]
for _ in range(Q):
  t,x=map(int,input().split())
  if t==1:
    d=[2]+d
  elif t==2:
    d=d+[x]
  else:
    print(d[x-1])