import sys
import itertools

n, p, q = map(int, input().split())
a = list(map(int, input().split()))
count = 0

combs = itertools.combinations(a, 5)
for a, b, c, d, e in combs:
  if a* b * c * d * e == q:
    count += 1

print(count)