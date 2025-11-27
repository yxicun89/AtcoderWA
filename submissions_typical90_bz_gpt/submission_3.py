
N, M = map(int, input().split())

graph = [[] for _ in range(N)]

for _ in range(M):

    a, b = map(lambda x: int(x) - 1, input().split())

    graph[a].append(b)

    graph[b].append(a)



ans = 0

for i, j in enumerate(graph):

    cnt = 0

    for v in j:

        if v < i:

            cnt += 1

    ans += cnt



print(ans)
