N, P, Q = [int(x) for x in input().split(" ")]
A = list(map(lambda x : int(x) % P, input().split(" ")))
#print(A)
c = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            for l in range(k+1,N):
                for m in range(l+1,N):
                    if (A[i]+A[j]+A[k]+A[l]+A[m])%P == Q:
                        c += 1
print(c)