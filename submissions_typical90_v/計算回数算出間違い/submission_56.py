import math
A,B,C = map(int, input().split())
gcd = math.gcd(A,B,C)
ret = A + B + C - 3 * gcd
print(int(ret/gcd))