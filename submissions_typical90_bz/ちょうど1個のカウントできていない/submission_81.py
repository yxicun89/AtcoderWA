N,M = map(int,input().split())
connect = [[] for _ in range(N+1)]
ans = 0

for _ in range(M):
    a,b = map(int,input().split())
    connect[a].append(b)

for i in range(N+1):
    num = 0
    for j in range(len(connect[i])):
        if i > connect[i][j]:
            num += 1
        else:
            continue
    if num == 1:
        ans +=1
    else:
        continue

print(ans)