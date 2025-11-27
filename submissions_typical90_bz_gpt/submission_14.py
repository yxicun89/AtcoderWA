import bisect



n, m = map(int, input().split())

d = {}

for _ in range(m):

    a, b = map(int, input().split())

    if a not in d:

        d[a] = []

    d[a].append(b)



    if b not in d:

        d[b] = []

    d[b].append(a)



ans = 0

for i, j in d.items():

    k = sorted(j)

    ans += bisect.bisect(k, i)

print(ans)


