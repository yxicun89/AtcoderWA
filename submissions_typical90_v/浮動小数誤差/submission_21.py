import math

a, b, c = map(int, input().split())
z = math.gcd(a, b, c)

if z >= 2:
  a /= z
  b /= z
  c /= z

print(a + b + c - 3)

