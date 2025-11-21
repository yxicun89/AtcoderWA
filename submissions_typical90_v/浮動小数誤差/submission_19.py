import math
A, B, C = map(int, input().split())
s = math.gcd(math.gcd(A, B), C)
a = A/s - 1
b = B/s -1
c = C/s -1
print(a + b+ c)