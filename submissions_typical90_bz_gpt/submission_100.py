N,M=map(int,input().split())
D={i:0 for i in range(1,N+1)}
for i in range(M):
  a,b=map(int,input().split())
  D[a]+=int(a>b)
  D[b]+=int(b<a)
ans=0
for i in range(1,N+1):
  ans+=int(D[i]==1)
print(ans)