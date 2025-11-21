N, P, Q = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0
res_A = [n % P for n in A]
for i in range(N - 3):
  for j in range(N - 4, N - 2):
    for k in range(N - 3, N - 1):
      for l in range(N - 2, N):
        for m in range(N - 1, N):
          if res_A[i]*res_A[j]*res_A[k]*res_A[l]*res_A[m] % P == Q and P != 0:
            cnt += 1
print(cnt)

