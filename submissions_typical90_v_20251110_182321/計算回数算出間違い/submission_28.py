import math


A, B, C = map(int, input().split())


d = math.gcd(A, math.gcd(B, C))


x = A // d
y = B // d
z = C // d


total_cubes = x * y * z


print(total_cubes - 1)
