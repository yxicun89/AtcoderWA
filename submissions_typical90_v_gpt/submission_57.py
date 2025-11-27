import math
A,B,C = map(int,input().split())
print(A * B * C // math.gcd(A,B,C))