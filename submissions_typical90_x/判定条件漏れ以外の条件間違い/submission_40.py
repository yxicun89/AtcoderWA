def abs(a):
  if a>= 0:
    return a
  else:
    return -a


N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

s = 0
for i in range(N):
  s+= abs(A[i]-B[i])

if s>=K and (s-K)%2 == 0:
  print("Yes")
else:
  print("No")