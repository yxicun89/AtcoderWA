n,m=map(int,input().split())
l=[[0] for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    l[a-1].append(b)
    l[b-1].append(a)
ans=0
for j in range(n):
    tmp=0
    for k in l[j]:
        if k<(j+1):
            tmp+=1
    if tmp==1:
        ans+=1
print(ans)

