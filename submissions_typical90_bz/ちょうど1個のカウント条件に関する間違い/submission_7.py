n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

count = 0
for i in range(n):
    if (sum(n < i for n in graph[i])):
        count += 1

print(count)