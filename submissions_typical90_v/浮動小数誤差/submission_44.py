import math
A,B,C = map(int,input().split())
GCD = math.gcd(A,B,C)
print(int(A/GCD + B/GCD + C/GCD - 3))