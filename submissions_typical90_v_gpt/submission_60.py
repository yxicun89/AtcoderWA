A,B,C = map(int,input().split())

import math
gcd = math.gcd(A,B,C)

li = [A,B,C]

total = 0
for i in li:
    total += i - gcd

print(total)