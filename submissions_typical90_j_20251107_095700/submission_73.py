from sys import stdin

# 入力
N = int(stdin.readline())
points = [tuple(map(int, stdin.readline().split())) for _ in range(N)]
Q = int(stdin.readline())
queries = [tuple(map(int, stdin.readline().split())) for _ in range(Q)]

sumlist_one, sumlist_two = [0] * N, [0] * N
x, y = 0, 0

for i in range(N):
  if points[i][0] == 1:
    x += points[i][1]
  else:
    y += points[i][1]
  sumlist_one[i], sumlist_two[i] = x, y

for j in range(Q):
  a = sumlist_one[queries[j][1]-1] - sumlist_one[queries[j][0]-1]
  b = sumlist_two[queries[j][1]-1] - sumlist_two[queries[j][0]-1]
  print(' '.join(map(str, (a, b))))