
n, k = map(int, input().split())

A = list(map(int, input().split()))

B = list(map(int, input().split()))



cnt = 0

for i in range(n):

  cnt += abs(A[i] - B[i])



if abs(cnt % k) == 0 and cnt <= k:

  print('Yes')

else:

  print('No')
