#!/usr/bin/env python3
n, p, q = map(int, input().split())
aa = list(map(int, input().split()))
ans = 0
for i in range(n):
    t = aa[i]
    for j in range(i + 1, n):
        t *= aa[j]
        t %= p
        for k in range(j + 1, n):
            t *= aa[k]
            t %= p
            for l in range(k + 1, n):
                t *= aa[l]
                t %= p
                for m in range(l + 1, n):
                    t *= aa[m]
                    t %= p
                    if t % p == q:
                        ans += 1
print(ans)
