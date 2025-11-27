
import sys

N = int(input())

sum1 = [0] * (N+1)
sum2 = [0] * (N+1)

for i in range(1,N+1):
  C,P = map(int,input().split())

  sum1[i] = sum1[i-1]

  if C == 1:
    sum1[i] += P
  else:
    sum2[i] += P

Q = int(input())

for _ in range(Q):
  L,R = map(int,input().split())

  ans1 = sum1[R] - sum1[L-1]
  ans2 = sum2[R] - sum2[L-1]
  print(ans1, ans2)
