# 条件判定していない

from itertools import combinations



N, P, Q = map(int,input().split())

A = list(map(int,input().split()))



for i in range(N):

  A[i] %= P



ans = 0

for x in combinations(A,5):

  tmp = 1

  for i in range(5):

    tmp *= x[i]

    tmp %= P



print(ans)
