import sys
sys.setrecursionlimit(10000000)

N, M = map(int, input().split())

G = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

global_counter = 1
for i in range(N):
    counter = 0
    for j in G[i]:
        if (j < i):
            counter += 1
    if counter == 1:
        global_counter += 1

print(global_counter)