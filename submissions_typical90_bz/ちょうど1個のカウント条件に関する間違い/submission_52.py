
N,M=map(int,input().split())
seen=[0]*N
connect=[[] for x in range(N)]
for i in range(M):
  a,b=map(int ,input().split())
  connect[a-1].append(b-1)
  connect[b-1].append(a-1)
count=0

#print(connect)
for i in range(N):
  if len(connect[i])==1:
    if connect[i][0]<i:
      count+=1
    
print(count)
  