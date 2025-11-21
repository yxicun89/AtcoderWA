N, P, Q = map(int,input().split())
A = list(map(int,input().split()))

count = 0
for i in range(N):
  for j in range(N):
    for k in range(N):
      for l in range(N):
        for m in range(N):
          if A[i]%P*A[j]%P*A[k]%P*A[l]%P*A[m]%P == Q:
            count += 1
print(count)