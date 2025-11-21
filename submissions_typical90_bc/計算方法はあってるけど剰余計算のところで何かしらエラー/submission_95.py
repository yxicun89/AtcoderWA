n, p, q = map(int, input().split())
a = list(map(int, input().split()))
pq = []
co = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            for l in range(k+1, n):
                for o in range(l+1, n):
                    x = a[i] + a[j] + a[k] + a[l] + a[o]
                    if x % p == q:
                        co += 1
print(co)