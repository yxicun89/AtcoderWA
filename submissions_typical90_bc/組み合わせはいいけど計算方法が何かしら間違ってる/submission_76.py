N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    for j in range(i+1,N):
        t = (A[i] * A[j]) % P
        for k in range(j+1,N):
            t = (t * A[k]) % P
            for l in range(k+1,N):
                t = (t * A[l]) % P
                for m in range(l+1,N):
                    if (t * A[m]) % P == Q:
                        ans += 1

print(ans)


