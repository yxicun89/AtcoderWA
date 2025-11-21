n,m=map(int,input().split())
ans=set()
for i in range(m):
  temp=sorted(list(map(int,input().split())))
  if temp[1] in ans:
    ans.remove(temp[1])
  else:
    ans.add(temp[1])
print(len(ans))