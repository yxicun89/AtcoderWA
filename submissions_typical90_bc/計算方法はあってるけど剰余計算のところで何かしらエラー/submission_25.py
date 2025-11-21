from itertools import combinations

N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for i in range(N-4):
    for j in range(i, N-3):
        for k in range(j, N-2):
            for l in range(k, N-1):
                for m in range(l, N):
                    if A[i] * A[j] %P * A[k] % P * A[l] %P * A[m] %P == Q:
                        ans += 1
        
print(ans)