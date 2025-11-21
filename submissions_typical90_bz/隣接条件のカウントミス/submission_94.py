n,m=map(int,input().split())
g=[0]*n
for i in range(m):
  a,b=map(int,input().split())
  g[min(a,b)-1]+=1
ans = 0
print(sum([x==1 for x in g]))