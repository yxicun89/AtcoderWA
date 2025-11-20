N, M = map(int, input().split())

connect = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    connect[a].append(b)
    connect[b].append(a)

cnt = 0
for i in range(N):
    if len(connect[i]) == 1:
        if connect[i][0] < i:
            cnt += 1
    if len(connect[i]) > 1:
        if connect[i][0] < i < connect[i][1]:
            cnt += 1

print(cnt)