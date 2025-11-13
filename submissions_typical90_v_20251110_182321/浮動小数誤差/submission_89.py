import math
A, B, C = map(int, input().split())
D = math.lcm(A, B, C)
print((A/D)+(B/D)+(C/D)-3)
