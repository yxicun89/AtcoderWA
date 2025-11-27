N ,P ,Q = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
for i in range(N):
    for j in range(N):
        for k in range(N):
            for l in range(N):
                for m in range(N):
                    product = 1
                    product = product * A[i] % P
                    product = product * A[j] % P
                    product = product * A[k] % P
                    product = product * A[l] % P
                    product = product * A[m] % P

                    if product == Q:
                        ans +=1

print(ans)