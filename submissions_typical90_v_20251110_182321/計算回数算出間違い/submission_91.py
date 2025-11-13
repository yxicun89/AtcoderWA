import math

A, B, C = map(int, input().split())
gcd = math.gcd(A, B, C)
print(A + B + C + 3 * (gcd - 1))