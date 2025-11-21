N,M = map(int, input().split())

G = [[] for i in range(N+1)]

for i in range(M):
    u,v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
    
count=0

for i in range(N):
    a=0
    while a != len(G[i]):
        
        if len(G[i]) > G[i][a]:
            count +=1
        a+=1

print(count)
