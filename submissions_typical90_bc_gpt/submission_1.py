

import itertools

import math



n, p, q = map(int, input().split())

a = list(map(int, input().split()))



ans = 0

cl = list(itertools.combinations(a, 5))

for i in cl:

    if (i[0]%p)*(i[1]%p)*(i[2]%p)*(i[3]%p)*(i[4]%p) == q:

        ans += 1



print(ans)
