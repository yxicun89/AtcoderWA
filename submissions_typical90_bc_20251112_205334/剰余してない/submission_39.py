import itertools
import math
N, P , Q = map(int, input().split())
A = [a % P for a in map(int, input().split())]

B = itertools.combinations(A, 5)


answer = 0

for b in B:
  if math.prod(b) == Q:
    answer += 1

print(answer)