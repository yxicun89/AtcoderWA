
import itertools

import math



N, P, Q = map(int, input().split())



A = list(map(int, input().split()))

A = [a % P for a in A]



result = 0

all_products = 1

for combination in itertools.combinations(A, 5):

    for a in combination:

        all_products = (all_products * a) % P

        if all_products == 0 and Q != 0:  # 早期終了条件

            break

    if (all_products == Q):

        result += 1



print(result)

