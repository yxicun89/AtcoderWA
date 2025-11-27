n, m = map(int, input().split())
adj_list = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    adj_list[a-1].append(b-1)
    adj_list[b-1].append(a-1)

count = 0
for i in range(n):
    if all(j >= i for j in adj_list[i]) and len(adj_list[i]) == 1:
        count += 1

print(count)
