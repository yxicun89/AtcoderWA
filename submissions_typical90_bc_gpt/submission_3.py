
from collections import Counter

from itertools import combinations

import math



N, P, Q = map(int, input().split())



A = list(map(int, input().split()))

A_counter = Counter(map(lambda x: x%P, A))





count = 0

for v in combinations(A, 4):

    A_sub = A_counter - Counter(v)

    mul = v[0] * v[1] * v[2] * v[3]

    if math.gcd(mul, P) != 1:

        continue

    m = A_sub[pow(mul, -1, P) * Q % P]

    count += m



print(count // 5)
