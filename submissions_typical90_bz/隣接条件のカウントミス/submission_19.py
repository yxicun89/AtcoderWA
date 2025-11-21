N, M =map(int,input().split())

link =[[] for _ in range(N)]

for i in range(M):
  a,b = map(int,input().split())
  link[a-1].append(b)
  link[b-1].append(a)

ans=0
for i in range(1,N,1): 
  for j in link[i]:
    count=0
    if j<i+1:
      count+=1
  if count==1:
    ans+=1
  
print(ans)