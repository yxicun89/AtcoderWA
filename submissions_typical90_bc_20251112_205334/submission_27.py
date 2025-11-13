# 計算が変

N, P, Q  = map(int, input().split())

A = list(map(int, input().split()))

ans = 0



for i in range(N):

  for j in range(i+1, N):

    for k in range(j+1, N):

      for l in range(k+1, N):

        for m in range(l+1, N):

          res = A[i]*A[j]%P

          res *= A[k]*A[l]*A[m]

          if res == Q:

            ans += 1

print(ans)
