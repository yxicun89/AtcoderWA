N, M = map(int, input().split())
G = [[]for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a-=1
    b-=1
    G[a].append(b)
    G[b].append(a)
ans = 0
for nd in range(N):
    cnt = 0
    for nxt in G[nd]:
        if nxt < nd:
            cnt += 1
        elif nxt > nd:
            break
    if cnt == 1:
        ans += 1
print(ans)