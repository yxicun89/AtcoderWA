n,m=map(int,input().split())
G=[list() for _ in range(n)]
for _ in range(m):
    a,b,=map(int,input().split())
    a-=1
    b-=1
    G[a].append(b)
    G[b].append(a)
    # print(G)
ans=0
for i in range(n):
    cnt=0
    for g in G:
        cnt=sum([i>gg for gg in g])
    if cnt==1:
        ans+=1
print(ans)