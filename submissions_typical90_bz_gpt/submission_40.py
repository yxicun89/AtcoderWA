import sys
sys.setrecursionlimit(100000)
N , M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    i, j = map(int,input().split())
    graph[i].append(j)
    graph[j].append(i)
ans = [-1] * (N+1)
cnt = 0
# print(graph)

# 深さ優先探索(調べたやつ)
def DFS(i):
    visited[i] = True
    for j in graph[i]:
        if visited[j] == True:
        # このcontinueで1つ上のfor文に戻る
            continue
        if i > j:
            ans[i] += 1
        else:
            pass
        DFS(j)

for i in range(1,N+1):
    visited = [False] * (N+1)
    DFS(i)

# print(ans)
for k in ans:
    if k == 0:
        cnt += 1
print(cnt)