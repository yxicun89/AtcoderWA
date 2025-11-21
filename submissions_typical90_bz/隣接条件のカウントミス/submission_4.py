import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())

G = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)        
    
visited = [False]*(N+1)

q = deque([1])

ans = 0
while len(q) > 0:
    pos = q.popleft()
    visited[pos] = True
    cnt = 0
    for next_pos in G[pos]:
        if next_pos<pos:
            cnt += 1
        if visited[next_pos] == False:
            q.append(next_pos)
    if cnt == 1:
        ans += 1
print(ans)
    