N, M = map(int, input().split())

graph = [[0]*N for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1


ans_cnt = 0
for i in range(N):
    cnt = 0
    if len(list(filter(lambda x: x == 1, graph[i]))) == 1:
        ans_cnt += 1

print(ans_cnt)