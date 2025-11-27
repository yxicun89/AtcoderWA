n,m=map(int,input().split())
l=[[] for _ in range(n)]
for _ in range(0,m):
  a,b=map(int,input().split())
  a,b=a-1,b-1
  l[a].append(b)
  l[b].append(a)
ans=0
for i in range(n):
  cnt=0
  for j in range(len(l[i])):
    if(l[i][j]<i):
      if(cnt==0):
        cnt+=1
      else:break
    else:
      if(cnt==1):
        ans+=1
        break
  else:
    if(cnt==1):
      ans+=1
else:print(ans)