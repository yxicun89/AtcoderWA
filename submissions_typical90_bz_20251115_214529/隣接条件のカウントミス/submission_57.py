N, M = map(int,input().split())
Edges = [[] for _ in range(N)]
ans = 0

for _ in range(M):
    a, b = map(int,input().split())
    Edges[a-1].append(b)
    Edges[b-1].append(a)
    
for i in range(N):
    Edges[i].sort()
    
#print(Edges)
    
for j in range(N):
    num = j + 1
    
    if num - Edges[j][0] == 1:
        ans += 1
        
    elif len(Edges[j]) == 1 and Edges[j][0] < num:
        ans += 1
        
print(ans)