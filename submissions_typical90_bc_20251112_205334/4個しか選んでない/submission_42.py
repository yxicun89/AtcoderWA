# 5個なのに4個しか選んでない

import itertools



n,p,q = map(int, input().split())

A = [int(i) for i in input().split()]



count = 0

for a,b,c,d,e in itertools.combinations(A, 5):

  seki_mod = ((((a%p) * (b%p))%p * (c%p))%p * (d%p))%p



  if seki_mod == q:

    count += 1



print(count)
