import math
A, B, C = map(int, input().split())
print(int((A/math.gcd(A,B,C) - 1) + (B/math.gcd(A,B,C) - 1) + (C/math.gcd(A,B,C) - 1)))