n, m = map(int, input().split())
adj_list = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

ans = 0
for i in range(1, n + 1):
    
    if len(adj_list[i]) == 1 and adj_list[i][0] <= i:
        ans += 1

print(ans)