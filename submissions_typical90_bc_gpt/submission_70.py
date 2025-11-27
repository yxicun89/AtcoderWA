N, P, Q = map(int, input().split())
A = [int(a) & P for a in input().split()]
count = 0
for i in range(N):
    for j in range(i):
        product = A[i]*A[j] % P
        for k in range(j):
            product2 = product*A[k] % P
            for L in range(k):
                product3 = product2*A[L] % P
                for m in range(L):
                    if product3*A[m] % P == Q:
                        count += 1
print(count)