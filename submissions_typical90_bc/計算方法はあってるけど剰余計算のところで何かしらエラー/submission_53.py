n, p, q = map(int, input().split())
l = list(map(int, input().split()))
ans = 0

for i in range(n-4):
    for j in range(i+1, n-3):
        for k in range(j+1, n-2):
            for ll in range(k+1, n-1):
                for m in range(ll + 1, n):
                    t = l[i] * l[j] % p * l[k] % p * l[ll] % p * l[m] % p
                    if t == q:
                        ans += 1
