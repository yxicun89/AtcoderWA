N,M=map(int, input().split())
G=[[] for i in range(N)]
num=0
for i in range(M):
  a,b=map(int, input().split())
  a-=1
  b-=1
  G[a].append(b)
  G[b].append(a)
for x in range(N):
    c=0
    for y in G[x]:
       if x>y:
          c+=1
          if c==1:
             num+=1
                
print(num)