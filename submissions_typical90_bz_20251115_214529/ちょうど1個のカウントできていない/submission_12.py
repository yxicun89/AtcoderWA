N,M=map(int,input().split())
ans=0
li=[True for i in range(N)]
for i in range(M):
  A,B=map(int,input().split())
  if(A<B):
    if(li[B-1]):
      ans+=1
    else:
      ans-=1
    li[B-1]=False
  else:
    if(li[A-1]):
      ans+=1
    else:
      ans-=1
    li[A-1]=False
print(ans)