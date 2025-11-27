
from itertools import combinations



N, P, Q = map(int, input().split())

A = list(map(int, input().split()))



count = 0

arr = [a % P for a in A]



for comb in combinations(arr, 5):

  product = 1

  for num in comb:

    product = (product * num) % P

    if product == Q:

      count += 1



print(count)

