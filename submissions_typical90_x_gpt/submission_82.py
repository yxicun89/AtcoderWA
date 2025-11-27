N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

m = 0

for i in range(N):
  d = abs(A[i] - B[i])
  m += d

l = K-m

if (l>0 and l%2==0):
  print('Yes')
else:
  print('No')