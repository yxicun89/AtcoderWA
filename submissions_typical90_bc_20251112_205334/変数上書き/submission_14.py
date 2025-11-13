# sekiの上書き

import sys



n, p, q = list(map(int, sys.stdin.readline().split()))

a = list(map(int, sys.stdin.readline().split()))

ans = 0

for i in range(0, n - 4):

    for j in range(i + 1, n - 3):

        seki = a[i] * a[j] % p

        for k in range(j + 1, n - 2):

            seki = seki * a[k] % p

            for l in range(k + 1, n - 1):

                seki = seki * a[l] % p

                for m in range(l + 1, n):

                    seki = seki * a[m] % p

                    if seki == q:

                        ans += 1

print(ans)
