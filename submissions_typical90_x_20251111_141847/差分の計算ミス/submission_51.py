# 絶対値で2重for文になっている

import math



N, K = list(map(int, input().split()))

A = list(map(int, input().split()))

B = list(map(int, input().split()))





n = (K - sum([ abs(a - b) for a in A for b in B]))

c1 = n % 2 == 0

c2 = n >= 0





print( "Yes" if c1 and c2 else "No")
