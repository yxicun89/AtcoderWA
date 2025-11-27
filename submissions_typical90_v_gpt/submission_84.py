import math

A, B, C = map(int, input().split())

edge = math.gcd(A, B, C)

print(A/edge + B/edge + C/edge)