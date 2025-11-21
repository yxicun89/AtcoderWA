import heapq
N,M = map(int,input().split())
#Q = int(input())

p = [[] for _ in range(N)]
for i in range(M):
    A,B = map(int,input().split())
    p[A-1].append(B-1)
    p[B-1].append(A-1)

def dfs(s):
    visited = [False]*N
    q = []
    heapq.heappush(q,s)
    ans = 0
    while q:
        a = 0
        node = heapq.heappop(q)
        visited[node]= True
        for n in p[node]:
            if n < node:
                a += 1
            if visited[n]:
                continue
            heapq.heappush(q,n)
        if a == 1:
            ans += 1
    return ans
print(dfs(0))