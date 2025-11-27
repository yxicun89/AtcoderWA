from collections import deque
def main():
    N,M = map(int,input().split())
    ab = [list(map(int,input().split())) for i in range(M)]

    edge = [[] for _ in range(N)]
    for i in range(M):
        edge[ab[i][0]-1].append(ab[i][1]-1)
        edge[ab[i][1]-1].append(ab[i][0]-1)

    visit = [0]*N    
    q = deque()
    q.append(0)

    ans = 0
    while len(q) > 0:
        now = q.popleft()
        visit[now] = 1
        cnt = 0
        for nxt in edge[now]:
            if nxt < now:
                cnt += 1
            if visit[nxt] == 0:
                q.append(nxt)
        if cnt == 1:
            ans += 1

    print(ans)

main()