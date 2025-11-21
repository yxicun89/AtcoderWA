#インデックスエラー

N = int(input())
pointsum = []
sum_1 = 0
sum_2 = 0
for i in range(N):
  C, P = map(int, input().split())
  if C==1:
    sum_1 += P
  else:
    sum_2 += P
  pointsum.append([sum_1, sum_2])

Q = int(input())
for j in range(Q):
  L, R = map(int, input().split())
  print(pointsum[R-1][0]-pointsum[L-2][0], pointsum[R-1][1]-pointsum[L-2][1])