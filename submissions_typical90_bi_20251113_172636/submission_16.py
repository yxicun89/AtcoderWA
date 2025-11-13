q=int(input())
ls=[]
paper=[]
for i in range(q):
  t,x=map(int,input().split())
  if t==1:
    ls.append(x)
  elif t==2:
    ls.insert(0,x)
  else:
    print(ls[x-1])
    