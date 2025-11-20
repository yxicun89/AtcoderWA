n, m = map(int, input().split())
adj_list = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)
c = 0
for i in range(1,n+1):
    if len(adj_list[i][:i]) == 1:
        c += 1
print(c)
