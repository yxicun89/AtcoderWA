N, M = map(int, input().split())

G = [[] for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

ans = 0
for i in range(1, N):
    if len(G[i]) == 1 and G[i][0] < i:
        ans += 1

print(ans)