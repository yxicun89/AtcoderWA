N, P, Q = map(int, input().split())

A = list(map(int, input().split()))

modulaA = [0] * N

for i in range(N):
    modulaA[i] = A[i] % P

ans = 0

for i in range(0, N - 4):
    for j in range(i + 1, N - 3):
        for k in range(j + 1, N - 2):
            for l in range(k + 1, N - 1):
                for m in range(l + 1, N):
                    if (
                        modulaA[i] + modulaA[j] + modulaA[k] + modulaA[l] + modulaA[m]
                    ) % P == Q:
                        ans += 1

print(ans)
