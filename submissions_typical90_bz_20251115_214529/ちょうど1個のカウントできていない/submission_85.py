# 078 - Easy Graph Problem（★2）
n,m = map(int,input().split())
g = [[] for i in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)
# print(g)

from collections import deque
que = deque([1])
visited = [-1]*(n+1)
visited[1]  = False

while que:
    now = que.popleft()
    for to in g[now]:
        if visited[to] == -1:
            que.append(to)
            if to > now:
                visited[to] = now
        else:
            if visited[to] != False:
                if to > now:
                    visited[to] = False
# print(visited)
ans = 0
for i in range(1,n+1):
    if visited[i] != -1 and visited[i] != False:
        ans += 1
print(ans)