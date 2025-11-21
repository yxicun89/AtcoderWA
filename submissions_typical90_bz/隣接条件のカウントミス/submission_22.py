N, M = map(int,input().split())

ab = [list(map(int,input().split())) for _ in range(M)]

#print(ab)

def graf(ab):
    
    graph=[[] for _ in range(N)]
    
    for edge in ab:
        a, b = edge 
        a, b = a-1, b-1
        graph[a].append(b+1)
        graph[b].append(a+1)
    return graph

#print(graf(ab))

ans=0
for i in range(1,len(graf(ab))):
    count=0
    for j in graf(ab)[i]:
        if j<i:
            count+=1
    if count==1:
        ans+=1
        
print(ans)