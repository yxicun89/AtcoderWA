from itertools import combinations
N, P, Q = map(int, input().split())
a = list(map(int, input().split()))

cnt = 0
for a, b, c, d, e in combinations(a, 5):
  if a % P * b % P * c % P * d % P * e * P == Q:
    cnt += 1

print(cnt)