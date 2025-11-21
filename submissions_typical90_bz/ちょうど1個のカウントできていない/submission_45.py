n,m=map(int,input().split())
A=[0]*n
for _ in range(m):
    a,b=map(int,input().split())
    if a>b:
        A[a-1]+=1
    else:
        A[b-1]+=1
ans=0
for i in range(n):
    if A[i]>=2:
        ans+=1
print(ans)