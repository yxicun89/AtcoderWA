N,M=map(int,input().split())

G=[[]for _ in range(N)]

ans=0
for _ in range(M):
    a,b=map(int,input().split())
    if a<b:
        if len(G[b-1])==0:
            ans+=1
            G[b-1].append(a-1)
    else:
        if len(G[a-1])==0:
            ans+=1
            G[a-1].append(b-1)

print(ans)