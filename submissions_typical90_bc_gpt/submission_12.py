
import math

from itertools import combinations



N, P, Q = map(int, input().split())

A = list(map(int, input().split()))



count = 0



for combo in combinations(A, 5):

  mod = 1

  for x in combo:

    mod = (mod * x) % P

    if mod > Q:

      break

  else:

    if mod == Q:

      count += 1



print(count)
