N,P,Q = map(int,input().split())
A = [int(i)%P for i in input().split()]
ans = 0
for i in range(N):
  for j in range(i+1,N):
    tmp = A[i]*A[j]
    tmp %= P
    for k in range(j+1,N):
      tmp *= A[k]
      tmp %= P
      for l in range(k+1,N):
        tmp *= A[l]
        tmp %= P
        for m in range(l+1,N):
          tmp *= A[m]
          tmp %= P
          if tmp == Q:
            ans += 1
print(ans)