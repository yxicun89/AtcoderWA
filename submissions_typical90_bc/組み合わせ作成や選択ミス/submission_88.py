# ループ範囲が逆

N, P, Q = map(int,input().split())

A = list(map(int, input().split()))



ans = 0

for i in range(N):

  v1 = A[i] % P

  for j in range(i):

    v2 = v1 * A[j] % P

    for k in range(j):

      v3 = v2 * A[k] % P

      for l in range(k):

        v4 = v3 * A[l] % P

        for m in range(l):

          v5 = v3 * A[m] % P

          ans += v5 == Q

print(ans)
