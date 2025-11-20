n,q=map(int,input().split())
ls=[[0 for _ in range(n)] for _ in range(n)]

for i in range(q):
  x,y=map(int,input().split())
  if x<y:
    ls[x-1][y-1]=1
  else:
    ls[y-1][x-1]=1

count=0  

for i in range(n):
  if sum(ls[i][:i])==1:
    count+=1
print(count)
