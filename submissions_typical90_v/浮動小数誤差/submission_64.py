import math
def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

A,B,C = map(int,input().split())
divisor = gcd(A,gcd(B,C))
print(math.floor((A/divisor-1)+(B/divisor-1)+(C/divisor-1)))